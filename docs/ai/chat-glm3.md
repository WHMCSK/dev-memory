# ChatGLM3

## conda

升级Conda到最新版本，是为了我们后面安装依赖包的时候不会出现其他的兼容的问题
```
conda update conda
```

更新完成后，再次检查 Conda的版本来确认更新是否成功。

```
conda --version
```

更新完 Conda后，需要更新环境中的所有包，以确保所有软件包都是最新的。避免产生未知的依赖问题，使用以下命令来更新所有安装的包

```
conda update --all
```

使用Conda创建独立的隔离环境

创建一个新环境用于多卡部署启动ChatGLM3-6B，避免与现有环境中的包发生冲突。使用以下命令创建一个新环境（我这里设置的环境名为 chatglm3_multi，大家根据需要更改虚拟环境的名称）：

```
conda create --name chatglm3_multi python=3.11
```

进入隔离环境

创建完成后，使用 conda activate 进入该虚拟环境。

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
 pip install sqlparse python-multipart fschat gitpython auto_gpt_plugin_template langchain sentence-transformers alembic accelerate protobuf==4.25.1 duckdb chardet pymysql peft jieba ruamel_yaml datasets rouge_chinese mpi4py
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

注：需要开科学上网才能进入Hugging Face官网执行下载，如果没有，可以选择进入 ModelScope 魔搭社区，按照教程执行下载。

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

## 单机多卡启动ChatGLM3-6B模型

单机多卡（多个 GPU）环境相较于单机单卡（一个GPU），可以提供更高的计算能力，但同时也会存在更复杂的资源管理和更复杂的程序代码。比如我们需要考虑如何使所有的GPU 的负载均衡，如果某个 GPU 负载过重，而其他GPU 空闲，这会导致资源浪费和性能瓶颈，除此之外，还要考虑每个 GPU 的内存不会被过度使用及模型训练过程中GPU 之间的同步和通信。

尽管如此，单机多卡或者多机多卡往往才是工业界实际使用的方式，单机单卡的瓶颈非常有限，所以这方面的内容还是非常有必要掌握的。而如果初次接触，我们需要做的就是：学会有效的使用简单的GPU监控工具来帮助配置一些重要的超参数，例如批大小（batch size），像出现 GPU 内存溢出（即显存不足）等情况，去考虑减小批大小等等。

### 查看GPU状态信息

* 查看当前机器的GPU数量

方式一：Ispci 命令。这是最常用的方法之一，这个命令会显示与图形相关的设备信息，列出所有PCI设备，包括GPU，其执行命令如下：

```
lspci | grep VGA
```

方式二：Nvidia-smi 命令。如果系统中安装的是 NVIDIA GPU 和驱动程序，最熟知且最直观的 nvidia-smi命令。这个命令可以查看当前机器上所有GPU的使用情况，包括显存占用情况，执行命令如下：

```
nvidia-smi
```

* GPU性能参数

持续模式：耗能大，但是在新的GPU应用启动时，花费的时间更少，这里显示的是off的状态。

性能状态：从PO到P12，PO表示最大性能，P12表示状态最小性能。

除了直接运行 nvidia-smi 命令之外，还可以加一些参数，来查看一些本机GPU 使用的实时情况，这种方式也是在执行训练过程中最简单直观且比较常用的一种监测方式，执行命令如下：

```
watch -n 1 nvidia-smi
```

### 单机多卡启动ChatGLM3-6B模型服务

在 Linux 系统中想要在多GPU环境下启动一个应用服务，并且指定使用某些特定的GPU，主要有两种方式：

1. CUDA_VISIBLE_DEVICES环境变量
使用 CUDA_VISIBLE_DEVICES 环境变量是最常用的方法之一。这个环境变量可以控制哪些GPU对CUDA程序可见。例如，如果系统有4个GPU（编号为0，1.2,3），而你只想使用编号为1和2的GPU，那么可以在命令行中这样设置：

```
CUDA_VISIBLE_DEVICES=1,2 python your_script.py
```

这会让 your_script.py 只看到并使用编号为1和2的GPU。

2. 修改程序代码

这种方式需要直接在代码中设置CUDA设备。例如，在PyTorch中，可以使用torch.cuda.set_device()函数来指定使用哪个GPU，除此之外，某些框架或工具提供也可能提供相关的参数或环境变量来控制GPU的使用，但都需要修改相关的启动代码。

选择哪种方法取决于具体需求和使用的框架或工具。通常，CUDA_VISIBLE_DEVICES 是最简单和最直接的方式，而且它不需要修改代码，这使得它在不同环境和不同应用程序之间非常灵活。如果有控制多个服务并且每个服务需要使用不同GPU的需求，那么需要根据具体情况结合使用。

接下来我们依次尝试上述两种方式来启动ChatGLM3-6B模型服务。

* 根据GPU数量自动进行分布式启动

这里我们以命令行的交互方式来进行多卡启动测试。官方提供的脚本名称是：cli_demo.py。

在启动前，仅需要进行一处简单的修改，因为我们已经把ChatGLM3-6B这个模型下载到了本地，所以需要修改一下模型的加载路径。

如果仅修改模型权重就执行启动，该过程会自动检测可用的 GPU 并将模型的不同部分映射到这些 GPU上

模型服务运行后输入 Stop 退出启动程序，GPU资源就会立即被释放。

默认启动会自动使用多块GPU的资源的原因，在于cli_demo.py 这个.py文件中的这行代码：

```
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()
```

参数 device_map="auto"， 这个参数指示 transformers 库自动检测可用的 GPU 并将模型的不同部分映射到这些GPU上。如果机器上有多个 GPU，模型会尝试在这些GPU 上进行分布式处理。其通过分析各个GPU 的当前负载和能力来完成。负载均衡的目标是最大化所有GPU的利用率，避免任何一个GPU过载。

可以通过如下代码，查看当前环境下的GPU情况：

```
import torch

# 检查 CUDA 是否可用
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

# 列出所有可用的 GPU
if cuda_available:
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")

    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        # 获取当前默认 GPU
    print(f"Current CUDA device: {torch.cuda.current_device()}")
else:
    print("No GPUs available.")
```

可以把上述代码写在一个py文件中，执行该文件后会输出当前机器上的GPU资源情况，方便我们对当前的资源情况有一个比较清晰的认知。

* 如果想要指定使用某一块GPU，那么需要这样修改代码 cli_demo.py 中的代码：

```
import torch

# 设置 GPU 设备
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

#model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto"). eval ()
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).eval()

# 将模型移到指定的 GPU
model = model.to(device)
```

* 在代码程序中指定某几块GPU加载服务

更多数人的情况是：比如当前机器中有4块GPU，我们只想使用前两块GPU做此次任务的加载，该如何选择呢？这很常见，其问题主要在于：如果某块GPU已经处于满载运行当中，这时我们再使用四块默认同时运行的话大概率会提示out ofmemory报错，或者提示显卡不平衡imblance的warning警告。

如果是想在代码中指定多块卡运行该服务，需要在代码中添加这两行代码：

```
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ','.join(map(str, [0,1]))
```

## ChatGLM3-6B高效微调实践
在大模型掀起新一轮的Al热潮以来，目前的形式就是大语言模型（LLM）百花齐放，工业界用于生产的算法模型由原来是几万，几十万的参数，到现在上升到上十亿，上百亿的情况。在这种情况下，因为显卡资源的因素，预训练大模型基本是大公司或者高校才可以做的事情，小公司或个人只能对大模型进行微调后使用。

以前我们比较熟悉的都是全量微调，这个微调过程是对原始模型的所有参数全部做一个调整。但对于LLM，在消费级显卡上就做根本没有办法实现。所以目前对于大模型来说，主流的微调技术叫做高效微调，这种方式是通过微调大模型少量或者额外的一些参数，固定预训练模型（LLM）参数，以此来降低计算和存储成本，同时，还可以在一定程度上实现与全量参数微调相当的性能。

### 主流的高效微调方法介绍

* Freeze

Freeze是冻结的意思，Freeze方法指的是参数冻结，对原始模型的大部分参数进行冻结，仅训练少部分的参数，这样就可以大大减少显存的占用，从而完成对大模型的微调。特别是在Bert模型出来的时候，比较会常用到Freeze的这样一个微调方法，比如Bert有12层，我们把前10层冻结了，只训练后两层。这是一种比较简单微调方法，由于冻结的参数是大部分，微调的参数是少部分，因此在代码中只需要设置需要微调的层的参数即可，把不需要参加训练的层数 requires_grad 设置为False，不让其进行更新，从而达到冻结的这样一个效果。

### 官方案例

更多请参考：  [ChatGLM3-6B 微调](./chat-glm3-funetune.md)

目录： ChatGLM3/finetune_demo/

本目录提供 ChatGLM3-6B 模型的微调示例，包括全量微调和 P-Tuning v2。格式上，提供多轮对话微调样例和输入输出格式微调样例。

如果将模型下载到了本地，本文和代码中的 THUDM/chatglm3-6b 字段均应替换为相应地址以从本地加载模型。

运行示例需要 python>=3.10，除基础的 torch 依赖外，示例代码运行还需要依赖。

我们提供了 示例notebook 用于演示如何使用我们的微调代码。

```
pip install -r requirements.txt
```

测试硬件标准

我们仅提供了单机多卡/多机多卡的运行示例，因此您需要至少一台具有多个 GPU 的机器。本仓库中的默认配置文件中，我们记录了显存的占用情况：

* SFT 全量微调: 4张显卡平均分配，每张显卡占用 48346MiB 显存。
* P-TuningV2 微调: 1张显卡，占用 18426MiB 显存。
* LORA 微调: 1张显卡，占用 14082MiB 显存。

```
请注意，该结果仅供参考，对于不同的参数，显存占用可能会有所不同。请结合你的硬件情况进行调整。
请注意，我们仅仅使用英伟达 Hopper(代表显卡：H100) 和 Ampère(代表显卡:A100) 架构和系列显卡做过测试。如果您使用其他架构的显卡，可能会出现

未知的训练问题 / 显存占用与上述有误差。
架构过低而不支持某些特性。
推理效果问题。 > 以上三种情况为社区曾经遇到过的问题，虽然概率极地，如果您遇到了以上问题，可以尝试在社区中解决。
```

#### 多轮对话格式

多轮对话微调示例采用 ChatGLM3 对话格式约定，对不同角色添加不同 loss_mask 从而在一遍计算中为多轮回复计算 loss。

对于数据文件，样例采用如下格式

如果您仅希望微调模型的对话能力，而非工具能力，您应该按照以下格式整理数据。

```
[
  {
    "conversations": [
      {
        "role": "system",
        "content": "<system prompt text>"
      },
      {
        "role": "user",
        "content": "<user prompt text>"
      },
      {
        "role": "assistant",
        "content": "<assistant response text>"
      },
      // ... Muti Turn
      {
        "role": "user",
        "content": "<user prompt text>"
      },
      {
        "role": "assistant",
        "content": "<assistant response text>"
      }
    ]
  }
  // ...
]
```

请注意，这种方法在微调的step较多的情况下会影响到模型的工具调用功能

如果您希望微调模型的对话和工具能力，您应该按照以下格式整理数据。

```
[
  {
    "tools": [
      // available tools, format is not restricted
    ],
    "conversations": [
      {
        "role": "system",
        "content": "<system prompt text>"
      },
      {
        "role": "user",
        "content": "<user prompt text>"
      },
      {
        "role": "assistant",
        "content": "<assistant thought to text>"
      },
      {
        "role": "tool",
        "name": "<name of the tool to be called",
        "parameters": {
          "<parameter_name>": "<parameter_value>"
        },
        "observation": "<observation>"
        // don't have to be string
      },
      {
        "role": "assistant",
        "content": "<assistant response to observation>"
      },
      // ... Muti Turn
      {
        "role": "user",
        "content": "<user prompt text>"
      },
      {
        "role": "assistant",
        "content": "<assistant response text>"
      }
    ]
  }
  // ...
]
```

* 关于工具描述的 system prompt 无需手动插入，预处理时会将 tools 字段使用 json.dumps(..., ensure_ascii=False) 格式化后插入为首条 system prompt。

* 每种角色可以附带一个 bool 类型的 loss 字段，表示该字段所预测的内容是否参与 loss 计算。若没有该字段，样例实现中默认对 system, user 不计算 loss，其余角色则计算 loss。

* tool 并不是 ChatGLM3 中的原生角色，这里的 tool 在预处理阶段将被自动转化为一个具有工具调用 metadata 的 assistant 角色（默认计算 loss）和一个表示工具返回值的 observation 角色（不计算 loss）。

* 目前暂未实现 Code interpreter 的微调任务。

* system 角色为可选角色，但若存在 system 角色，其必须出现在 user 角色之前，且一个完整的对话数据（无论单轮或者多轮对话）只能出现一次 system 角色。



## 大模型并行训练框架-DeepSpeed

训练像ChatGL.M3-6B这种大的模型往往需要配备高价的多GPU、多节点的集群，但是，即便拥有了这些先进的硬件资源，实际的机器利用率往往只能达到其最大效率的一半左右。这意味着，仅仅拥有更加强大的硬件资源并不能保证更高的模型训练吞吐量。同样，即使系统具有更高的吞吐量，也并不能保证所训练出的模型具有更高的精度或更快的收敛速度。更重要的是，当前的开源软件的易用性也常常被用户诟病。

DeepSpeed是一个开源深度学习优化库，专门设计来提高大型模型训练的效率和扩展性。这个库采用了一系列先进技术，如模型并行化、梯度累积、动态精度缩放和混合精度训练等，来实现快速训练。除此之外，DeepSpeed还搭载了一套强大的辅助工具集，涵盖分布式训练管理、内存优化以及模型压缩等功能，帮助开发者更有效地处理和优化大规模的深度学习任务。值得一提的是，DeepSpeed是基于PyTorch构建的，因此对于现有的PyTorch项目，开发者可以轻松地实施迁移。
此库已在众多大规模深度学习应用中得到验证，涉及领域包括但不限于语言模型、图像分类和目标检测。

其使用非常简单，其较强的易用性源于把该软件的构造难度交给开发者而不是用户，所以我们用起来是非常简单的，就是一个configs文件，然后在训练代码中反向传播后执行参数更新的时候加一两行代码就可以了。对于ChatGLM3-6B模型的微调，默认只是在全量微调的脚本中加入了deepspeed的代码，因硬件配置相差太大，即使是使用deepspeed也无法运行。但我们可以将其应用到高效微调的P-Turning v2中，只需要添加一行代码，其他的全部使用默认的即可。

DeepSpeed已经在Github上开源，地址：https://github.com/microsoft/DeepSpeed

这里在fineturn_pt.sh 中加入这样一行代码：


Issues：

* lora_finetune.ipynb，报错：

```
Traceback (most recent call last):
  File "/home/ps/llm/ChatGLM3/finetune_demo/finetune_hf.py", line 148, in <module>
    @dc.dataclass
     ^^^^^^^^^^^^
  File "/home/ps/anaconda3/envs/chatglm3/lib/python3.11/dataclasses.py", line 1230, in dataclass
    return wrap(cls)
           ^^^^^^^^^
  File "/home/ps/anaconda3/envs/chatglm3/lib/python3.11/dataclasses.py", line 1220, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ps/anaconda3/envs/chatglm3/lib/python3.11/dataclasses.py", line 958, in _process_class
    cls_fields.append(_get_field(cls, name, type, kw_only))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ps/anaconda3/envs/chatglm3/lib/python3.11/dataclasses.py", line 815, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'transformers.training_args_seq2seq.Seq2SeqTrainingArguments'> for field training_args is not allowed: use default_factory
```

解决方法：

找到代码中的@dc.dataclass, 和里面定义的dc.field()，将其中的default=xxx改为default_factory=xxx即可。

```
training_args: Seq2SeqTrainingArguments = dc.field(
        default_factory=Seq2SeqTrainingArguments(output_dir='./output')
    )
```



## 低成本部署

### 模型量化

默认情况下，模型以 FP16 精度加载，运行上述代码需要大概 13GB 显存。如果你的 GPU 显存有限，可以尝试以量化方式加载模型，使用方法如下：

```python
model = AutoModel.from_pretrained("THUDM/chatglm3-6b",trust_remote_code=True).quantize(4).cuda()
```

模型量化会带来一定的性能损失，经过测试，ChatGLM3-6B 在 4-bit 量化下仍然能够进行自然流畅的生成。

### CPU 部署

如果你没有 GPU 硬件的话，也可以在 CPU 上进行推理，但是推理速度会更慢。使用方法如下（需要大概 32GB 内存）
```python
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).float()
```

### Mac 部署

对于搭载了 Apple Silicon 或者 AMD GPU 的 Mac，可以使用 MPS 后端来在 GPU 上运行 ChatGLM3-6B。需要参考 Apple 的 [官方说明](https://developer.apple.com/metal/pytorch) 安装 PyTorch-Nightly（正确的版本号应该是2.x.x.dev2023xxxx，而不是 2.x.x）。

目前在 MacOS 上只支持[从本地加载模型](README.md#从本地加载模型)。将代码中的模型加载改为从本地加载，并使用 mps 后端：
```python
model = AutoModel.from_pretrained("your local path", trust_remote_code=True).to('mps')
```

加载半精度的 ChatGLM3-6B 模型需要大概 13GB 内存。内存较小的机器（比如 16GB 内存的 MacBook Pro），在空余内存不足的情况下会使用硬盘上的虚拟内存，导致推理速度严重变慢。

### 多卡部署
如果你有多张 GPU，但是每张 GPU 的显存大小都不足以容纳完整的模型，那么可以将模型切分在多张GPU上。首先安装 accelerate: `pip install accelerate`，然后通过如下方法加载模型：

```python
from utils import load_model_on_gpus

model = load_model_on_gpus("THUDM/chatglm3-6b", num_gpus=2)
```
即可将模型部署到两张 GPU 上进行推理。你可以将 `num_gpus` 改为你希望使用的 GPU 数。默认是均匀切分的，你也可以传入 `device_map` 参数来自己指定。 


## ChatGLM3 对话格式
为了避免用户输入的注入攻击，以及统一 Code Interpreter，Tool & Agent 等任务的输入，ChatGLM3 采用了全新的对话格式。

### 规定
#### 整体结构
ChatGLM3 对话的格式由若干对话组成，其中每个对话包含对话头和内容，一个典型的多轮对话结构如下
```text
<|system|>
You are ChatGLM3, a large language model trained by Zhipu.AI. Follow the user's instructions carefully. Respond using markdown.
<|user|>
Hello
<|assistant|>
Hello, I'm ChatGLM3. What can I assist you today?
```
**实际中每轮对话内容并不一定以换行符结尾，这里只是为了美观，下同**

#### 对话头
对话头占完整的一行，格式为
```text
<|role|>{metadata}
```
其中 `<|role|>` 部分使用 special token 表示，无法从文本形式被 tokenizer 编码以防止注入。metadata 部分采用纯文本表示，为可选内容。
* `<|system|>`：系统信息，设计上可穿插于对话中，**但目前规定仅可以出现在开头**
* `<|user|>`：用户
  - 不会连续出现多个来自 `<|user|>` 的信息
* `<|assistant|>`：AI 助手
  - 在出现之前必须有一个来自 `<|user|>` 的信息
* `<|observation|>`：外部的返回结果
  - 必须在 `<|assistant|>` 的信息之后

### 样例场景

为提升可读性，下列样例场景中表示角色的 special token 前均额外添加了一个换行符。实际使用及 tokenizer 实现中均无需额外添加这一换行。

#### 多轮对话
* 有且仅有 `<|user|>`、`<|assistant|>`、`<|system|>` 三种 role
```text
<|system|>
You are ChatGLM3, a large language model trained by Zhipu.AI. Follow the user's instructions carefully. Respond using markdown.
<|user|>
Hello
<|assistant|>
Hello, I'm ChatGLM3. What can I assist you today?
```

#### 工具调用
````
<|system|>
Answer the following questions as best as you can. You have access to the following tools:
[
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string"},
            },
            "required": ["location"],
        },
    }
]
<|user|>
今天北京的天气怎么样？
<|assistant|>
好的，让我们来查看今天的天气
<|assistant|>get_current_weather
```python
tool_call(location="beijing", unit="celsius")
```
<|observation|>
{"temperature": 22}
<|assistant|>
根据查询结果，今天北京的气温为 22 摄氏度。
````

#### 代码执行
* 有 `<|user|>`、`<|assistant|>`、`<|system|>`、`<|observation|>` 四种 role。其中 `<|assistant|>` 的 metadata 只有 interpreter。

````text
<|system|>
你是一位智能AI助手，你叫ChatGLM3，你连接着一台电脑，但请注意不能联网。在使用Python解决任务时，你可以运行代码并得到结果，如果运行结果有错误，你需要尽可能对代码进行改进。你可以处理用户上传到电脑上的文件，文件默认存储路径是/mnt/data/。
<|user|>
#File: /mnt/data/metadata.jsonl
#Size: 35380
#File uploaded
文件中是否存在缺失值或异常值？
<|assistant|>
首先，我将读取您提供的文件，并查看其内容以确定是否存在缺失值或异常值。

我们从加载文件开始：
<|assistant|>interpreter
```python
import json

# Load the uploaded file
data = []
with open("/mnt/data/metadata.jsonl", 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Display the first few records to get a sense of the data
data[:5]
```
<|observation|>
```result
[{'file_name': 'aceinthehole.png',
  'name': 'Ace in the Hole',
  'type': 'survivor',
  'description': 'Lady Luck always seems to be throwing something good your way.'},
 {'file_name': 'adrenaline.png',
  'name': 'Adrenaline',
  'type': 'survivor',
  'description': 'You are fuelled by unexpected energy when on the verge of escape.'},
 {'file_name': 'aftercare.png',
  'name': 'Aftercare',
  'type': 'survivor',
  'description': "Unlocks potential in one's aura reading ability."},
 {'file_name': 'agitation.png',
  'name': 'Agitation',
  'type': 'killer',
  'description': 'You get excited in anticipation of hooking your prey.'},
 {'file_name': 'alert.png',
  'name': 'Alert',
  'type': 'survivor',
  'description': 'Your acute senses are on high alert.'}]
```
<|assistant|>
该文件看起来包含有关某些条目的元数据，每个条目有以下字段：


- `file_name`: 文件名称
- `name`: 名称
- `type`: 类型（例如 "survivor" 或 "killer"）
- `description`: 描述

接下来，我将检查这些字段是否存在缺失值。
<|assistant|>interpreter
```python
# Check for missing values in each column
missing_values = {key: sum(1 for item in data if key not in item) for key in data[0].keys()}

missing_values
```
<|observation|>
```result
{'file_name': 0, 'name': 0, 'type': 0, 'description': 0}
```
<|assistant|>
每个字段都没有缺失值。这意味着每个条目都完整。

接下来，我们可以检查是否存在任何潜在的异常值。这通常需要更深入的分析和对数据的了解，但我可以从一些基本的统计和分布开始进行检查。为了这样做，我们可以查看“type”字段的值分布，看看是否有任何意外的类别。
<|assistant|>interpreter
```python
# Check the distribution of values in the 'type' column
type_distribution = {key: sum(1 for item in data if item['type'] == key) for key in set(item['type'] for item in data)}

type_distribution
```
<|observation|>
```result
{'survivor': 116, 'killer': 103}
```
<|assistant|>
“type”字段有两个值：“survivor”和“killer”。其中，“survivor”有116个条目，而“killer”有103个条目。

从这个初步的检查中，我们没有发现任何明显的异常值。

如果您有任何特定的标准或其他字段需要检查，我可以为您提供更详细的分析。您还希望我检查什么呢？
<|user|>
帮我画一个爱心
<|assistant|>interpreter
```python
import numpy as np
import matplotlib.pyplot as plt

# 爱心形状的参数方程
def heart(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart(t)

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.axis('equal')
plt.axis('off')
plt.show()
```
<|observation|>
```result
[Image]
```
<|assistant|>
这是一个爱心形状。我使用了参数方程来描述这个形状，并使用matplotlib进行了绘制。如果您有任何其他需求或问题，请随时告诉我。
<|user|>  # End
````

## 报错

### pip install mpi4py报错：ERROR: Could not build wheels for mpi4py, which is required to install pyprojec

情况一：

在 conda 环境下 pip install mpi4py 安装 mpi4py 库时出现编译报错，报错信息为：

```
line 301: x86_64-conda_cos6-linux-gnu-cc: command not found
      failure.
      removing: _configtest.c _configtest.o
      error: Cannot compile MPI programs. Check your configuration!!!
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for mpi4py
Failed to build mpi4py
ERROR: Could not build wheels for mpi4py, which is required to install pyproject.toml-based projects
```

所以导致该错误的原因是

```
x86_64-conda_cos6-linux-gnu-cc: command not found
```

解决方法：

即没有找到 x86_64-conda_cos6-linux-gnu-cc。只需执行以下命令安装即可：
```
conda install gcc_linux-64
```

安装完成后重新执行 pip install mpi4py 即可完成安装。

情况二： 

在 pip 环境下 pip install mpi4py 安装 mpi4py 库时出现编译报错，报错信息为：

```
      _configtest.c:2:10: fatal error: mpi.h: No such file or directory
          2 | #include <mpi.h>
            |          ^~~~~~~
      compilation terminated.
      failure.
      removing: _configtest.c _configtest.o
      error: Cannot compile MPI programs. Check your configuration!!!
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for mpi4py
Failed to build mpi4py
ERROR: Could not build wheels for mpi4py, which is required to install pyproject.toml-based projects
```

解决方法：

```
sudo apt install libopenmpi-dev
pip install mpi4py
```