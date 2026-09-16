import json

# 标注好的问答数据
label_data = [
    {
        "instruction": "Python里字符串的strip()函数作用是什么？",
        "input": "",
        "output": "strip()用来去掉字符串首尾的空格、换行符等空白符号，不会修改字符串中间内容。"
    },
    {
        "instruction": "Git的commit是干什么的？",
        "input": "",
        "output": "commit是把当前改动，在本地仓库保存一个版本快照，方便后续回溯代码。"
    }
]

# 写入jsonl文件，一行一条
with open("label_data.jsonl", "w", encoding="utf-8") as f:
    for item in label_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("标注样本文件生成完成！")