# DB-GPT试用笔记

传统的数据库交互需要用户掌握复杂的SQL语言，或者使用有限的图形界面，这些方式都不够直观和灵活。DB-GPT则允许用户通过自然语言来查询和更新数据库，无需编写任何代码，让更多的人可以快捷方便的去使用数据库。

DB-GPT项目主页：https://github.com/csunny/DB-GPT/blob/main/README.zh.md

DB-GPT使用文档：https://www.yuque.com/eosphoros/dbgpt-docs/kwg1ed88lu5fgawb

视频中的安装文档链接：

[使用AutoDL云服务器搭建DB-GPT的教程](https://r.mckt3.fashiontech.top/AI/DB-GPT/DB-GPT用私有化LLM技术定义数据库下一代交互方式/DB-GPT云服务器安装文档.pdf?OSSAccessKeyId=LTAI4Fy7h96gJaRHCAqzUkJN&Expires=1705379711&Signature=ACI8XdxR%2BkjcSLhYkIP95TxHevE%3D)

DB-GPT部署视频：https://www.bilibili.com/video/BV1mu411Y7ve/vd_source=4fed55ef30f958576f5d0334c74bd1e8

DB-GPT支持大部分LLM在本地环境(6-24GB显存)部署，包含vicuna、chatglm、guanaco、gorilla、falcon和GPT4ALL等系列大模型。同时为降低部署成本，也提供了提供openai key直连GPT的方式，具体教程为https://db-gpt.readthedocs.io/projects/db-gpt-docs-zh-cn/zh_CN/latest/index.html 

 项目地址在：https://github.com/csunny/DB-GPT/blob/main/README.zh.md
 
## 创建Python虚拟环境

```
conda create -n dbgpt_env python=3.10
conda activate dbgpt_env
```

## 先决条件
```
 pip install sqlparse python-multipart fschat gitpython auto_gpt_plugin_template langchain sentence-transformers alembic accelerate protobuf==3.19.0 duckdb chardet pymysql chromadb openai

 pip install -U langchain-community
```

## 安装Torch

到官网，根据选择提示进行安装：https://pytorch.org

## 安装完Torch之后，需要检查一下cuda是否可用

```
python
import torch
torch.cuda.is_available()

返回False，说明是cuda和pytorch的冲突问题，cuda不可用。
返回Trues，说明cuda可用。
```

解决方案：

nvidia-smi获得机器支持最高cuda版本信息，nvcc -V获得当前安装cuda版本信息，到pytorch官网看下cuda和pytorch的版本对应。然后把自己机器上已有的cuda、pytorch删除干净，重装即可。

## cuda安装 （windows版）

windows10 版本安装 CUDA ，首先需要下载两个安装包

* CUDA toolkit（toolkit就是指工具包）
* cuDNN

注：cuDNN 是用于配置深度学习使用

官方教程：

CUDA [https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

cuDNN [https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows)

安装工具的准备:

1. CUDA toolkit Download

https://developer.nvidia.com/cuda-toolkit-archive

官网安装：

https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64

选择版本：

GA = General Availability,通用版本,指软件的通用版本。  
RC=Release Candidate,含义 是"发布候选版",它不是最终的版本,而是最终版(RTM=Release To Manufacture)之前的最后一个版本  

官网说明文档，
https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

CUDA的版本是跟显卡型号有关还是驱动有关？

一般是驱动版本决定了能用的CUDA版本的上限，比如新版的显卡驱动可以支持老的CUDA runtime。但是老的显卡可能无法更新到最新的显卡驱动，比如Fermi显卡只能装到391驱动，因此只能用到CUDA9.1。除此之外，显卡硬件与CUDA compute capability相关，当然编译时也可以指定streaming multiprocessor。新的架构支持更多特性就是了。

2. cuDNN Download

cuDNN地址如下，不过要注意的是，我们需要注册一个账号，才可以进入到下载界面。大家可以放心注册的。

https://developer.nvidia.com/rdp/cudnn-download

可以使用下面网址，查看适配的 cuDNN

https://developer.nvidia.com/rdp/cudnn-archive

CUDA 安装与配置过程

1. 双击“exe文件”，选择下载路径（推荐默认路径）

2. 安装选项

如果你是第一次安装，尽量全选  
如果你是第n次安装，尽量只选择第一个，不然会出现错误  

不要选Visual Studio Integration，即使选了也不能成功安装

如果本机的驱动版本(当前版本)小于cuda对应的版本（新版本），则选择，否则不选。如果当前版本小于新版本，并且不覆盖安装，之后电脑会频繁蓝屏或死机

3. 记住安装位置，tensorflow要求配置环境

重点提醒：一定要记住这个路径，把这个路径保留下来，后面我们还会用到！！！




## 运行
```
 python dbgpt/app/dbgpt_server.py --port 6006
```
或者
```
dbgpt start webserver --port 6006
```


git lfs install


# 中途的错误

### 错误1:
Exception: model vicuna-13b-v1.5@huggingface(172.17.0.5:6006) start failed, Error parsing message with type 'sentencepiece.ModelProto'

这个好像是模型没有下载好

### 错误2:
安装完成后，回答速度较慢。运行大模型框架提示：Current platform is windows, use avx2 as default cpu architecture

cuda没有用上，需要检查cuda框架版本，torch框架版本是否对应

### 错误3:

提问报错：RuntimeError: "addmm_impl_cpu_" not implemented for 'Half'

提问报这个错误，可能是cuda没有用上，需要检查cuda框架版本，torch框架版本是否对应


积卷神经网络（CNN）
循环神经网络（RNN）
自注意力机制Transformer（的方法）解决了自然语言特征提取的问题