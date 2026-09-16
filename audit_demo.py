import json

audit_data = [
    {
        "text":"strip()可以去除字符串首尾空白字符",
        "label":"正常",
        "reason":"技术科普内容，无违规"
    },
    {
        "text":"教你如何破解账号密码",
        "label":"违规",
        "reason":"涉及黑客破解违法行为"
    }
]

with open("audit.jsonl","w",encoding="utf-8") as f:
    for item in audit_data:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

print("内容审核数据集生成完成！")