# HTTP 请求及 API 调用教程
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

本项目整理了 HTTP 请求、API 调用和大模型 API 调用相关的课程材料，适合用于课堂演示、自学练习和 Jupyter Notebook 交互式实验。课程从 API 的基本概念和天气接口调用入手，逐步讲解 HTTP 请求结构、响应解析、文件与图片传输、本地 Flask API 服务，以及通过百度千帆平台调用大模型对话接口。

## 项目结构

```text
.
├── README.md
├── requirements.txt
├── .env.example
├── notebooks/
│   ├── 01_api调用引入.ipynb
│   ├── 02_http请求详解.ipynb
│   └── 03_大模型api调用.ipynb
├── examples/
│   └── service.py
└── assets/
    ├── docs/
    │   └── 中华人民共和国民法.txt
    └── images/
        └── 905504.png
```

- `notebooks/`：课程主体内容，按学习顺序拆分为三节 Notebook。
- `examples/service.py`：本地 Flask API 示例，提供图片 base64 传输和尺寸识别接口。
- `assets/images/`：Notebook 中使用的示例图片素材。
- `assets/docs/`：课程练习中使用的文本素材。
- `.env.example`：API Key 配置模板。
- `requirements.txt`：运行课程代码需要安装的 Python 依赖。

## 课程内容

1. `notebooks/01_api调用引入.ipynb`
   - API 基本概念
   - 天气 API 调用示例
   - API Key 的安全配置方式
   - curl 工具入门
   - Python `json` 库的序列化、反序列化和文件读写

2. `notebooks/02_http请求详解.ipynb`
   - URL、请求方法、请求结构和响应结构
   - HTTP 状态码和关键特性
   - 不同 `Content-Type` 的请求体传递方式
   - 图片、文本、二进制数据等响应内容解析
   - base64 图片传输
   - 本地 Flask API 服务调用

3. `notebooks/03_大模型api调用.ipynb`
   - Chat Completions 接口请求与响应结构
   - 单轮对话和多轮对话
   - 流式输出
   - 常见对话参数：`temperature`、`top_p`、`max_tokens`、`thinking`、`reasoning_effort`、`presence_penalty`、`frequency_penalty`

## 环境准备

建议使用 Python 3.10 或更新版本。

安装依赖：

```bash
pip install -r requirements.txt
```

启动 Jupyter Notebook：

```bash
jupyter notebook
```

## API Key 配置

课程示例会用到以下环境变量：

- `QWEATHER_API_KEY`：和风天气 API Key，用于天气接口调用示例。
- `QIANFAN_API_KEY`：百度千帆 API Key，用于大模型对话接口调用示例。

请不要把真实 API Key 直接写进 Notebook，也不要提交到 Git 仓库。

复制 `.env.example` 为 `.env`：

```bash
cp .env.example .env
```

然后在 `.env` 中填入自己的 Key：

```env
QIANFAN_API_KEY=your_qianfan_api_key_here
QWEATHER_API_KEY=your_qweather_api_key_here
```

Notebook 中通过 `python-dotenv` 读取配置：

```python
from dotenv import load_dotenv
import os

load_dotenv()
qianfan_api_key = os.environ.get("QIANFAN_API_KEY")
qweather_api_key = os.environ.get("QWEATHER_API_KEY")
```

## 许可协议

© 2026 asunhw | 原创教程

本作品采用 [CC BY-NC 4.0 协议](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)：

- 可以免费学习和分享
- 可以修改内容或二次创作
- 不可用于任何商业用途
- 转载请注明出处