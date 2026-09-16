import json

# RLHF偏好标注样本：同一个问题，两个回答，标注哪个更好
rlhf_data = [
    {
        "instruction": "strip()函数是干什么的？",
        "response_a": "删空格。",
        "response_b": "strip()可以删除字符串开头和结尾的空格、换行符，不会改动文字中间的空格。",
        "better_response": "b"
    },
    {
        "instruction": "git commit作用是什么？",
        "response_a": "commit保存本地代码版本快照，可以回退到之前的代码状态。",
        "response_b": "git就是玩代码的。",
        "better_response": "a"
    }
]

# 保存为rlhf.jsonl，一行一条样本
with open("rlhf.jsonl", "w", encoding="utf-8") as f:
    for item in rlhf_data:
        f.write(json.dumps(item, ensure_ascii=False)+"\n")

print("RLHF偏好标注样本生成完成！")