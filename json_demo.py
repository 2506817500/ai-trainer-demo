import json

# AI训练的一条样本：问答对，大模型微调最常见格式
sample = {
    "instruction": "解释什么是AI训练师",
    "input": "",
    "output": "AI训练师负责制作、清洗标注数据集，调教大模型，提升模型回答质量。"
}

# Python字典转为JSON字符串（保存到文件要用）
json_str = json.dumps(sample, ensure_ascii=False)
print(json_str)

# 把这条训练样本写入本地数据集文件
with open("train_data.jsonl","a",encoding="utf-8") as f:
    f.write(json_str + "\n")

print("✅已经把训练样本写入 train_data.jsonl")