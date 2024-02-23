# ChatGLM3

## 重要网站：

- Github仓库: https://github.com/THUDM/ChatGLM3
- Github仓库: https://github.com/THUDM
- API开放平台：https://open.bigmodel.cn
- 官方网站：https://www.zhipuai.cn
- 智谱清言：https://chatglm.cn
- 论文：https://arxiv.org/abs/2203.08674
- 说明文档：https://zhipu-ai.feishu.cn/wiki/HIj5wVxGqiUg3rkbQ1OcVEe5n9g

## 用到的工具

1. bwm-ng

bwm-ng 查看你hf模型下载速度

```
sudo apt-get update
sudo apt-get install bwm-ng
bwm-ng
```

## 安装说明

1. Python环境

使用conda创建可以相互隔离的python环境：

```
conda create -n chatglm3 python=3.11.5
conda activate chatglm3
```

为了不出现因为pip版本低导致的包管理依赖陈旧带来的问题，首先需要升级pip至最新版本：
```
pip install --upgrade pip
```
或者
```
python -m pip install --upgrade pip
```

2. 安装包

为了保证 torch 的版本正确，请严格按照 [官方文档](https://pytorch.org/get-started/locally/) 的说明安装。

为了安装过程顺畅，建议先安装以下依赖包：
```
 pip install sqlparse python-multipart fschat gitpython auto_gpt_plugin_template langchain sentence-transformers alembic accelerate protobuf==4.25.1 duckdb chardet pymysql peft jieba ruamel_yaml datasets rouge_chinese
```

3. 克隆代码

```
git clone https://github.com/THUDM/ChatGLM3.git
```

4. 安装项目依赖

一般项目中都会提供 requirements.txt这样一个文件，该文件包含了项目运行所必需的所有 Python 包及其精确版本号。使用这个文件，可以确保在不同环境中安装相同版本的依赖，从而避免了因版本不一致导致的问题。我们可以借助这个文件，使用pip一次性安装所有必需的依赖，而不必逐个手动安装，大大提高效率。命令如下：

```
pip install -r requirements.txt
```

5. 下载模型

经过Step 3的克隆代码操作过程，我们下载到的只是ChatGLM3-6B的一些运行文件和项目代码，并不包含ChatGLM3-6B这个模型。这里我们需要进入到 HuggingFace 下载。Hugging Face是一个丰富的模型库，开发者可以上传和共享他们训练好的机器学习模型。这些模型通常是经过大量数据训练的，并且很大，因此需要特殊的存储和托管服务

不同于GitHub，GitHub 仅仅是一个代码托管和版本控制平台，托管的是项目的源代码、文档和其他相关文件。同时对于托管文件的大小有限制，不适合存储大型文件，如训练好的机器学习模型。相反，Hugging Face 专门为此类大型文件设计，提供了更适合大型模型的存储和传输解决方案。

Git Large File Storage （Git LFS）是一种用于处理大文件的工具，在 Hugging Face 下载大模型时，通常需要安装 GitLFS，主要的原因是：Git本身并不擅长处理大型文件，因为在Git 中，每次我们提交一个文件，它的完整内容都会被保存在Git仓库的历史记录中。但对于非常大的文件，这种方式会导致仓库变得庞大而且低效。而 Git LFS，就不会直接将它们的内容存储在仓库中。相反，它存储了一个轻量级的“指针“文件，它本身非常小，它包含了关于大型文件的信息（如其在服务器上的位置），但不包含文件的实际内容。当我们需要访问或下载这个大型文件时，Git LFS 会根据这个指针去下载真正的文件内容。

实际的大文件存储在一个单独的服务器上，而不是在Git仓库的历史记录中。所以如果不安装 Git LFS 而直接从 HuggingFace 或其他支持LFS 的仓库下載大型文件，通常只会下载到一个包含指向实际文件的指针的小文件，而不是文件本身。

所以，我们需要先安装git-Ifs这个工具。命令如下：

```
sudo apt-get install git-lfs
```

安装完成后，需要初始化 Git LFS。这一步是必要的，因为它会设置一些必要的钩子。Git 钩子（hooks）是Git 提供的一种强大的功能，允许在特定的重要动作（如提交、推送、合并等）发生时自动执行自定义脚本。这些钩子是在Git仓库的
•git/hooks 目录下的脚本，可以被配置为在特定的Git命令执行前后触发。钩子可以用于各种自动化任务，比如：

1. 代码检查：在提交之前自动运行代码质量检查或测试，如果检查失败，可以阻止提交。
2. 自动化消息：在提交或推送后发送通知或更新任务跟踪系统。
3. 自动备份：在推送到远程仓库之前自动备份仓库。
4. 代码风格格式化：自动格式化代码以符合团队的代码风格标准。

而初始化git-lfs，会设置一些在上传或下载大文件是必要的操作，如在提交之前检查是否有大文件被 Git 正常跟踪，而不是通过 Git LFS 跟踪，从而防止大文件意外地加入到 Git仓库中。（pre-commit钩子）或者在合并后，确保所有需要的LFS对象都被正确拉取（post-merge）等。初始化命令如下：

```
git Lfs install
```

然后，我们可以从 Hugging Face 下载我们需要的模型。这里我们下载的是ChatGLM3-6B模型，完整命令如下：

```
cd ChatGLM3
git lfs install
git clone https://huggingface.co/THUDM/chatglm3-6b.git
sha256 checksums for chatglm3-6b
```

6. 运行demo

使用本地模型加载并使用命令行来问答

```
python basic_demo/cli_demo.py
```

使用本地模型加载并使用web_demo来问答

```
python basic_demo/web_demo_gradio.py
```

通过以下命令启动基于 Gradio 的网页版 demo

```
python basic_demo/web_demo_streamlit.py
```

通过以下命令启动基于 Streamlit 的网页版 demo：

```
streamlit run basic_demo/web_demo_streamlit.py
```
其效果与Gradio相同，但是更加流畅。

```
streamlit run web_demo_streamlit.py --server.port 9016 //指定端口
```


## Demo说明

1. 基于命令行的交互式对话

这种方式可以为非技术用户提供一个脱离代码环境的对话方式。对于这种启动方式，官方提供的脚本名称是：cli_demo.py

在启动前，我们仅需要进行一处简单的修改，因为我们已经把ChatGLM3-6B这个模型下载到了本地，所以需要修改一下模型的加载路径。

修改完成后，直接使用python cli_demp.py 即可启动，如果启动成功，就会开启交互式对话，如果输入stop 可以退出该运行环境


2. 基于网页的交互式对话

基于网页端的对话是目前非常通用的大语言交互方式，ChatGLM3官方项目组提供了两种Web端对话demo，两个示例应用功能一致，只是采用了不同的Web框架进行开发。首先是基于Gradio 的Web端对话应用demo。Gradio是一个Python库，用于快速创建用于演示机器学习模型的Web界面。开发者可以用几行代码为模型创建输入和输出接口，用户可以通过这些接口与模型进行交互。用户可以轻松地测试和使用机器学习模型，比如通过上传图片来测试图像识别模型，或者输入文本来测试自然语言处理模型。Gradio非常适合于快速原型设计和模型展示。

这种方式可以为技术用户提供一个更加直观的对话方式。对于这种启动方式，官方提供的脚本名称是：web_demo_gradio.py。同样，我们只需要使用vim 编辑器进入修改模型的加载路径，直接使用python启动即可。

如果启动正常，会自动弹出web页面，可以直接在Web页面上进行交互。

在启动前，我们可能需要安装Gradio这个包，命令如下：

```
pip install gradio
```

启动方式如下：

```
python basic_demo/web_demo_gradio.py
```

启动成功后，会在浏览器中打开一个网页，我们可以输入对话内容，模型会自动给出答案。

Gradio 是一个基于 Python 的交互式机器学习工具，它可以快速创建基于网页的交互式应用。Gradio 基于 Flask 框架，可以轻松部署到云端或本地服务器。Gradio 还提供了一些高级功能，如：

```
    1. 上传文件：Gradio 可以让用户上传文件，并将其作为输入提供给模型。
    2. 视频和音频：Gradio 可以让用户上传视频或音频，并将其作为输入提供给模型。
    3. 图像：Gradio 可以让用户上传图像，并将其作为输入提供给模型。
    4. 文本：Gradio 可以让用户输入文本，并将其作为输入提供给模型。
    5. 多输入和输出：Gradio 可以让用户同时输入多个值，并同时获得模型的输出。
    6. 多模型：Gradio 可以同时加载多个模型，并让用户选择使用哪个模型。
    7. 自定义样式：Gradio 可以自定义应用的外观和感觉。
```

3. 基于 Streamlit 的Web端对话应用

ChatGLM3官方提供的第二个Web对话应用demo，是一个基于Streamlit的Web应用。Streamlit是另一个用于创建数据科学和机器学习Web应用的Python库。它强调简单性和快速的开发流程，让开发者能够通过编写普通的Python脚本来创建互动式Web应用。Streamlit自动管理UI布局和状态，这样开发者就可以专注于数据和模型的逻辑。Streamlit应用通常用于数据分析、可视化、构建探索性数据分析工具等场景。

这种方式可以为技术用户提供一个更加直观的对话方式。对于这种启动方式，官方提供的脚本名称是：web_demo_streamlit.py。同样，先使用 vim 编辑器修改模型的加载路径。

在启动前，我们可能需要安装Streamlit这个包，命令如下：

```
pip install streamlit
```

启动方式如下：

```
streamlit run basic_demo/web_demo_streamlit.py
```

启动成功后，会在浏览器中打开一个网页，我们可以输入对话内容，模型会自动给出答案。

Streamlit 是一个用于创建和分享数据科学应用程序的 Python 库。它可以快速创建基于网页的交互式应用，并将其部署到云端或本地服务器。Streamlit 基于 Flask 框架，可以轻松部署到云端或本地服务器。Streamlit 还提供了一些高级功能，如：

1. 上传文件：Streamlit 可以让用户上传文件，并将其作为输入提供给模型。
2. 视频和音频：Streamlit 可以让用户上传视频或音频，并将其作为输入提供给模型。
3. 图像：Streamlit 可以让用户上传图像，并将其作为输入提供给模型。
4. 文本：Streamlit 可以让用户输入文本，并将其作为输入提供给模型。
5. 多输入和输出：Streamlit 可以让用户同时输入多个值，并同时获得模型的输出。
6. 多模型：Streamlit 可以同时加载多个模型，并让用户选择使用哪个模型。
7. 自定义样式：Streamlit 可以自定义应用的外观和感觉。


4. 在指定虚拟环境的JupyterLab中运行 

我们在部署Chatglm3-6B模型之前，创建了一个chatglm3虚拟环境来支撑该模型的运行。除了在终端中使用命令行启动，同样可以在JupyterLab环境中启动这个模型。具体的执行过程如下：

首先，在终端中找到需要加载的虚拟环境，使用如下命令可以查看当前系統中一共存在哪些虚拟环境：

```
conda env list
```

然后，激活需要加载的虚拟环境，使用如下命令：

```
conda activate chatglm3
```

在该环境中安装ipykernel软件包。这个软件包将允许JupyterNotebook使用特定环境的Python版本。运行以下命令：

```
conda install ipykernel
```

将该环境添加到JupyterNotebook中。运行以下命令：

```
#这里的env_name替换成需要使用的虚拟环境名称
python -m ipykernel install --user --name=chatglm3 --display-name="Python(chatglm3)"
python -m ipykernel install --user --name=dbgpt --display-name="Python(dbgpt)"
```

执行完上述过程后，在终端输入jupyter lab启动。

```
jupyter lab
```

## 官方实例

```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/home/ps/llm/DB-GPT/models/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/home/ps/llm/DB-GPT/models/chatglm3-6b", trust_remote_code=True, device='cuda:0').half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=history)
print(response)
```

只需要从transformers中加载AutoTokenizer 和 AutoModel，指定好模型的路径即可。tokenizer这个词大家应该不会很陌生，可以简单理解我们在之前使用gpt系列模型的时候，使用tiktoken库帮我们把输入的自然语言，也就是prompt按照一种特定的编码方式来切分成token，从而生成AP调用的成本。但在Transform中tokenizer要干的事会更多一些，它会把输入到大语言模型的文本，包在tokenizer中去做一些前置的预处理，会将自然语言文本转换为模型能够理解的格式，然后拆分为 tokens
（如单词、字符或子词单位）等操作。

而对于模型的加载来说，官方的代码中指向的路径是THUDM/chatgLm3-6b，表示可以直接在云端加载模型，所以如果我们没有下载chatglm3-6b模型的话，直接运行此代码也是可以的，只不过第一次加载会很慢，耐心等待即可，同时需要确保当前的网络是联通的（必要的情况下需要开梯子）。

因为我们已经将ChatGLM3-6B的模型权重下载到本地了，所以此处可以直接指向我们下载的Chatglm3-6b模型的存储路径来进行推理测试。

对于其他参数来说，model 有一个eval模式，就是评估的方法，模型基本就是两个阶段的事，一个是训练，一个是推理，计算的量更大，它需要把输入的值做一个推理，如果是一个有监督的模型，那必然存在一个标签值，也叫真实值，这个值会跟模型推理的值做一个比较，这个过程是正向传播。差异如果很大，就说明这个模型的能力还远远不够，既然效果不好，就要调整参数来不断地修正，通过不断地求导，链式法则等方式进行反向传播。当模型训练好了，模型的参数就不会变了，形成一个静态的文件，可以下载下来，当我们使用的时候，就不需要这个反向传播的过程，只需要做正向的推理就好了，此处设置model.eval（就是说明这个过程。而trust_remote_code=True 表示信任远程代码（如果有），device='cuda'表示将模型加载到CUDA设备上以便使用GPU加速，这两个就很好理解了。

## OpenAI风格API调用方法

ChatGLM3-6B模型提供了OpenAI风格的API调用方法。正如此前所说，在OpenAI几乎定义了整个前沿AI应用开发标准的当下，提供一个OpenAI风格的API调用方法，毫无疑问可以让ChatGLM3模型无縫接入OpenAI开发生态。所谓的OpenAI风格的AP调用，指的是借助OpenAI库中的ChatCompletion函数进行ChatGLM3模型调用。而现在，我们只需要在model参数上输入chatglm3-6b，即可调用ChatGLM3模型。调用API风格的统一，无疑也将大幅提高开发效率。

先决条件：

1. 安装OpenAI库0.28版本
2. 安装tiktoken包
3. 降级 typing_extensions 依赖包到4.8.0
4. 安装 sentence_transformers 依赖包
5. 运行openaL_api.py脚本


而要执行OpenAI风格的AP调用，则首先需要安装openai库，并提前运行openai_api.py脚本。具体执行流程如下：
首先需要注意：OpenAI目前已将openai库更新至1X，但目前Chatglm3-6B仍需要使用旧版本0.28。所以需要确保当前环境的opena版本。

检查openai库版本：

```
!openai -V // 查看当前环境的openai版本
!pip install openai==0.28.1 // 如果版本为1.x，使用该命令降级
```

如果想要使用API特续调用Chatg/m3-6b模型，需要启动一个脚本，该脚本位于 open_api_demo 中。

启动之前，需要安装tiktoken包，用于将文本分割成tokens。

```
pip` install tiktoken
```

同时，需要降级 typing_extensions 依赖包，否则会报错。


```
pip install typing_extensions==4.8.0
```

最后，还需要安装 sentence_transformers 依赖包，安装最新的即可。

```
pip install sentence_transformers
```

然后，启动脚本：

```
python open_api_demo.py
```

然后可以在客户端程序中调用模型：

```
import os
import openai

os.environ["OPENAI_API_KEY"] = "none"

openai.api_base = "http://0.0.0.0:8000/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = 'chatglm3-6b',
    message = [
        {"role": "user", "content": "你好，你能为我写一首诗吗？"}
    ]
)
print(reponse["choices"][0]["message"]["content"])
```

除此之外，大家还可以去测试ChatGLM3-6B的Function Calling等更高级的用法时的性能情况。我们推荐大家使用OpenAI风格的AP调用方法是进行学习和尝试构造高级的AlAgent，同时积极参与国产大型模型的开源社区，共同增强国内在这一领域的实力和影响力。
