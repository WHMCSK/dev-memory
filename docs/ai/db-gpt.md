# 

传统的数据库交互需要用户掌握复杂的SQL语言，或者使用有限的图形界面，这些方式都不够直观和灵活。DB-GPT则允许用户通过自然语言来查询和更新数据库，无需编写任何代码，让更多的人可以快捷方便的去使用数据库。

DB-GPT项目主页：https://github.com/csunny/DB-GPT/blob/main/README.zh.md

视频中的安装文档链接：

DB-GPT部署视频：https://www.bilibili.com/video/BV1mu411Y7ve/vd_source=4fed55ef30f958576f5d0334c74bd1e8

DB-GPT支持大部分LLM在本地环境(6-24GB显存)部署，包含vicuna、chatglm、guanaco、gorilla、falcon和GPT4ALL等系列大模型。同时为降低部署成本，也提供了提供openai key直连GPT的方式，具体教程为https://db-gpt.readthedocs.io/projects/db-gpt-docs-zh-cn/zh_CN/latest/index.html 

 项目地址在：https://github.com/csunny/DB-GPT/blob/main/README.zh.md
 
 conda activate dbgpt_env

 pip install sqlparse python-multipart fschat gitpython auto_gpt_plugin_template langchain sentence-transformers alembic accelerate protobuf==3.19.0 duckdb chardet pymysql

 python dbgpt/app/dbgpt_server.py --port 6006


git lfs install


# 中途的错误

Exception: model vicuna-13b-v1.5@huggingface(172.17.0.5:6006) start failed, Error parsing message with type 'sentencepiece.ModelProto'


积卷神经网络（CNN）
循环神经网络（RNN）
自注意力机制Transformer（的方法）解决了自然语言特征提取的问题