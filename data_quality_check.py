import json
import re

def check_jsonl_quality(file_path, min_len=5, max_len=1000):
    """
    JSONL数据集质量质检
    :param file_path: jsonl文件路径
    :param min_len: 文本最小长度阈值
    :param max_len: 文本最大长度阈值
    :return: 质检结果报告
    """
    report = {
        "total": 0,
        "valid": 0,
        "bad_json": 0,
        "empty_field": 0,
        "text_too_short": 0,
        "text_too_long": 0,
        "special_char": 0,
        "bad_samples": []
    }
    # 匹配不可见特殊控制字符
    special_pattern = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            report["total"] += 1
            if not line:
                report["bad_json"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "空行"})
                continue
            # 校验JSON格式
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                report["bad_json"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "JSON解析失败"})
                continue

            # 检测空字段，适配SFT/RLHF两种样本结构
            text_content = ""
            if "instruction" in data and "output" in data:
                if not data["instruction"] or not data["output"]:
                    report["empty_field"] += 1
                    report["bad_samples"].append({"line": line_num, "reason": "指令或回答为空"})
                    continue
                text_content = data["instruction"] + data["output"]
            elif "text" in data:
                text_content = data["text"]
            else:
                report["empty_field"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "缺少必要字段"})
                continue

            # 文本长度校验
            if len(text_content) < min_len:
                report["text_too_short"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "文本过短"})
                continue
            if len(text_content) > max_len:
                report["text_too_long"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "文本过长"})
                continue

            # 特殊不可见字符检测
            if special_pattern.search(text_content):
                report["special_char"] += 1
                report["bad_samples"].append({"line": line_num, "reason": "存在不可见特殊字符"})
                continue

            # 全部校验通过
            report["valid"] += 1
    return report

if __name__ == "__main__":
    # 可以替换成你项目里任意jsonl文件
    target_file = "train_data.jsonl"
    result = check_jsonl_quality(target_file)
    print("=" * 50)
    print(f"【数据集质检报告】文件：{target_file}")
    print(f"总样本数：{result['total']}")
    print(f"合格样本：{result['valid']}")
    print(f"合格率：{result['valid']/result['total']*100:.2f}%")
    print(f"JSON格式错误：{result['bad_json']}")
    print(f"空字段样本：{result['empty_field']}")
    print(f"文本过短：{result['text_too_short']}")
    print(f"文本过长：{result['text_too_long']}")
    print(f"含特殊控制字符：{result['special_char']}")
    print("=" * 50)
    if len(result["bad_samples"]) > 0:
        print("坏样本清单（前10条）：")
        for item in result["bad_samples"][:10]:
            print(f"行号:{item['line']}, 问题:{item['reason']}")
