import json

# 模拟一批原始问答样本，里面混有无效脏数据
data_list = [
    {"instruction":"解释什么是AI训练师","output":"AI训练师负责制作清洗数据集，调教大模型。"},
    {"instruction":"你好","output":"嗯"}, # 回答太短，无效样本
    {"instruction":"Python怎么学","output":"多写代码练习，从小案例入手。"},
    {"instruction":"hi","output":""} # 回答为空，无效样本
]

valid_samples = []
for item in data_list:
    ans = item["output"]
    # 过滤：输出不为空，并且回答长度大于等于8个字
    if ans and len(ans) >= 8:
        valid_samples.append(item)

print(f"原始样本数：{len(data_list)}")
print(f"过滤后有效样本数：{len(valid_samples)}")

# 将清洗后的有效样本保存jsonl
with open("filtered_data.jsonl","w",encoding="utf‑8") as f:
    for s in valid_samples:
        f.write(json.dumps(s,ensure_ascii=False)+"\n")

print("✅过滤完成，保存 filtered_data.jsonl")