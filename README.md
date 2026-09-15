# ai‑trainer‑demo
> AI训练师入门练习项目，Python实现SFT数据集处理。

## 项目简介
本项目模拟AI训练师日常SFT数据集处理工作，完成大模型监督微调数据集处理，输出标准jsonl格式训练样本。

## 实现功能
1. 文本清洗：去除空格、无效内容
2. 样本过滤：过滤过短、无效问答样本
3. jsonl读写：读取原始数据，输出符合SFT微调规范的jsonl训练集
4. 数据集格式校验，生成可直接用于微调的样本文件

## 文件说明
- hello_ai.py：入门测试脚本
- clean_demo.py：文本清洗示例
- filter_demo.py：无效样本过滤逻辑
- json_demo.py：jsonl读写示例
- read_jsonl.py：读取jsonl数据集
- *.jsonl：生成的SFT训练数据集

## 使用环境
Python3.x，Windows。

## 仓库地址
https://github.com/2506817500/ai-trainer-demo