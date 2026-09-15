import json

# 读取本地AI数据集jsonl文件
with open("train_data.jsonl","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        item = json.loads(line)
        print("📝指令：", item["instruction"])
        print("📖回答：", item["output"])
        print("-"*40)