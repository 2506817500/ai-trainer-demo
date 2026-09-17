# ai-trainer-demo
AI训练师入门练习项目，Python实现SFT数据集处理、RLHF偏好样本构建、数据内容审核。

## 项目简介
本项目模拟AI训练师完整工作流：SFT指令标注、RLHF偏好样本构建、文本清洗、脏数据过滤、数据集内容审核，输出标准jsonl格式训练样本。
在数据处理过程中，解决标注时全角/半角符号混用、JSONL单行格式报错等真实业务问题。

## 实现功能
1. 文本清洗：去除多余空格、无效特殊字符，统一标点符号（修正全角/半角标点错误）
2. 样本过滤：过滤空文本、过短、无效问答脏样本
3. jsonl读写：读取原始标注数据，输出符合SFT微调规范的jsonl训练集
4. RLHF偏好数据集构建：生成一对优劣回答样本，用于偏好训练
5. 数据集内容审核：对生成样本做合规筛查
6. 数据集格式校验：保证输出文件格式合法，可直接用于大模型微调
7. Git版本管理：项目全程使用Git做版本快照，代码托管GitHub

## 文件说明
### 脚本文件
- hello_ai.py：入门测试脚本
- clean_demo.py：文本清洗示例脚本
- filter_demo.py：脏样本过滤逻辑脚本
- json_demo.py：基础jsonl读写，生成SFT标注数据集
- label_demo.py：模拟人工标注生成指令样本
- rlhf_demo.py：RLHF偏好对比数据集生成脚本
- audit_demo.py：数据内容审核脚本
- read_jsonl.py：读取并校验jsonl数据集文件
- test.py：代码调试测试文件

### 生成的数据集文件
- train_data.jsonl：SFT训练数据集
- label_data.jsonl：标注原始样本
- filtered_data.jsonl：过滤清洗后的数据集
- rlhf.jsonl：RLHF偏好成对样本
- audit.jsonl：内容审核样本

## 使用环境
Python3.x，Windows
Git（版本控制）

## 运行步骤
1. 克隆仓库到本地
```bash
git clone https://github.com/2506817500/ai-trainer-demo.git
cd ai-trainer-demo