# AI训练师：模拟真实脏数据清洗
raw_text = "  今天   学习AI训练师  , 目标城市：深圳  "
print("原始脏数据：", repr(raw_text))

# 1. 删除全部空格
no_space = raw_text.replace(" ","")
print("删掉所有空格：", no_space)

# 2. strip()：只删除字符串两头空格（保留中间）
trim_text = raw_text.strip()
print("仅去掉首尾空格：", trim_text)