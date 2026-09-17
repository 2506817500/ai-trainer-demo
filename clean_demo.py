import re

# AI训练师：模拟真实脏数据清洗
raw_text = "  今天   学习AI训练师  , 目标城市：深圳  "
print("原始脏数据：", repr(raw_text))

# 1. replace 删除【普通空格】，无法处理\xa0不间断空格
no_space = raw_text.replace(" ","")
print("replace删除普通空格：", no_space)

# 2. strip()：只删除字符串两头空格，保留文本中间空白
trim_text = raw_text.strip()
print("仅去掉首尾空格：", trim_text)

# ==========新增：正则一次性删除所有空白（普通空格 + \xa0 +换行）==========
no_space_all = re.sub(r'\s+','',raw_text)
print("正则删除全部空白（包含\\xa0）：", no_space_all)


# ========== 清洗函数：正则清洗 + 全角转半角 + 清除\xa0不间断空格 ==========
def full2half(s):
    """全角标点 转为 半角标点"""
    result = ""
    for char in s:
        code = ord(char)
        # 全角字符范围：65281 ~ 65374
        if 65281 <= code <= 65374:
            char = chr(code - 65248)
        result += char
    return result

def clean_text(text):
    # 重点：处理网页数据里的不间断空格 \xa0
    text = text.replace("\xa0"," ")
    # 去掉首尾空白
    text = text.strip()
    # 多个连续空格，统一变成单个空格
    text = re.sub(r'\s+', ' ', text)
    # 全角符号转半角
    text = full2half(text)
    # 过滤异常乱码符号，只保留中文、英文、数字、常用标点
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9,.?!：；]', '', text)
    return text


# 测试1：普通脏样本（没有\xa0，新旧代码看不出区别）
dirty_sample_1 = "　这　是【测　试】，全角逗号，！"
clean_result_1 = clean_text(dirty_sample_1)
print("\n=====测试1：普通脏样本=====")
print("原始脏样本：", dirty_sample_1)
print("清洗之后：", clean_result_1)

# 测试2：带\xa0不间断空格（这里就能看出新加代码的作用）
dirty_sample_2 = "这\xa0是【测\xa0试】，全角逗号，！"
clean_result_2 = clean_text(dirty_sample_2)
print("\n=====测试2：包含\xa0不间断空格=====")
print("原始脏样本：", repr(dirty_sample_2))
print("清洗之后：", clean_result_2)
