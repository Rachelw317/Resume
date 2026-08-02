# Resume Assistant

一个基于 LangGraph 的简历优化流水线Demo。读取简历文件（docx, pdf）和职位描述(txt)，提取结构化信息，分析匹配度，生成优化后的简历内容，写入 Markdown 输出。

## 项目结构

- `agents/`：Agent 相关逻辑
- `core/`：核心解析、分析和优化逻辑
- `graph/`：LangGraph 工作流定义
- `loaders/`：文件加载器
- `nodes/`：工作流节点
- `schemas/`：数据模型定义
- `tools/`：工具函数
- `tests/`：测试样例与测试代码

## 环境要求

- Python 3.11+
- 可访问的 DeepSeek API

## 安装依赖

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 配置环境变量

在项目根目录下创建 `.env` 文件，并加入你的 DeepSeek API Key：

```bash
DEEPSEEK_API_KEY=你的密钥
```

## 运行项目

默认入口脚本为：

```bash
python main.py
```

当前示例会使用项目中的测试文件进行一次完整流程运行，结果会输出到 `outputs/optimized_resume.md`。
