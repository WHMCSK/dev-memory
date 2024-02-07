# ChatGLM3

重要网站：

- Github仓库: https://github.com/THUDM/ChatGLM3
- Github仓库: https://github.com/THUDM
- API开放平台：https://open.bigmodel.cn
- 官方网站：https://www.zhipuai.cn
- 智谱清言：https://chatglm.cn
- 论文：https://arxiv.org/abs/2203.08674
- 说明文档：https://zhipu-ai.feishu.cn/wiki/HIj5wVxGqiUg3rkbQ1OcVEe5n9g

## 安装说明

1. 安装包

为了保证 torch 的版本正确，请严格按照 [官方文档](https://pytorch.org/get-started/locally/) 的说明安装。

为了安装过程顺畅，建议先安装以下依赖包：
```
 pip install sqlparse python-multipart fschat gitpython auto_gpt_plugin_template langchain sentence-transformers alembic accelerate protobuf==4.25.1 duckdb chardet pymysql
```

2. 克隆代码

```
git clone https://github.com/THUDM/ChatGLM3.git
```

3. 下载模型

```
cd ChatGLM3
git lfs install
git clone https://huggingface.co/THUDM/chatglm3-6b.git
sha256 checksums for chatglm3-6b
```

4. 安装依赖

```
pip install -r requirements.txt
```

5. 运行demo

使用本地模型加载并使用命令行来问答

```
python basic_demo/cli_demo.py
```

