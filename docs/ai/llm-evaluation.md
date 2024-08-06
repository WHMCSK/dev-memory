# 大模型评估

## 评估行情的了解

1. LLM 实时排行，来自 UC伯克利：https://lmsys.org/blog/2023-06-22-leaderboard/


2. 选择中文模型：中文语言理解测评基准（CLUE）：https://www.cluebenchmarks.com/index.html 和SuperCLUE琅琊榜: https://www.superclueai.com/

开源领域 ChatGLM, LLAMA, RWKV 主要就是这3种模型，中文好一点就是 ChatGLM，潜力最好的就是LLAMA，RNN架构决定RWKV有很好的推理效率（随输入长度内存占比线性自增，而LLAMA则是指数增加）和 Length Extrapolation（关于长度外推性，可以参考苏神的文章）。当然 MPT-7B-StoryWriter-65k+模型也有较长的外推能力。

自ChatGPT为代表的大语言模型（Large Language Model, LLM）出现以后，由于其惊人的类通用人工智能（AGI）的能力，掀起了新一轮自然语言处理领域的研究和应用的浪潮。尤其是以ChatGLM、LLaMA等平民玩家都能跑起来的较小规模的LLM开源之后，业界涌现了非常多基于LLM的二次微调或应用的案例。下面这个项目在收集和梳理中文LLM相关的开源模型、应用、数据集及教程等资料，目前收录的资源已达100+个！

Awesome Chinese LLM，主要是整理开源的中文大语言模型，以规模较小、可私有化部署、训练成本较低的模型为主，包括底座模型，垂直领域微调及应用，数据集与教程等。

```
Awesome Chinese LLM #JGitHubitft: https://github.com/HqWu-HITCS/Awesome-Chinese-LLM
```


## 大模型评测数据集

### 中文大模型评测数据集

| 名称 | 网址 | 介绍 |
| --- | --- | --- |
| C-Eval | 源码：https://github.com/hkust-nlp/ceval  官网：https://cevalbenchmark.com/#home  使用教程：https://github.com/hkust-nlp/ceval/blob/main/README_zh.md | C-Eval是全面的中文基础模型评估套件，涵盖了52个不同学科的13948个多项选择题，分为四个难度级别 \n通常你可以直接从模型的生成中使用正则表达式提取出答案选项（A,B,C,D)。在少样本测试中，模型通常会遵循少样本给出的固定格式，所以提取答案很简单。然而有时候，特别是零样本测试和面对没有做过指令微调的模型时，模型可能无法很好的理解指令，甚至有时不会回答问题。这种情况下我们推荐直接计算下一个预测token等于"A", "B", "C", "D"的概率，然后以概率最大的选项作为答案 -- 这是一种受限解码生成的方法，MMLU的官方测试代码中是使用了这种方法进行测试。注意这种概率方法对思维链的测试不适用。[更加详细的评测教程](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fgithub.com%2Fhkust-nlp%2Fceval%2Fblob%2Fmain%2Fresources%2Ftutorial.md&source=article&objectId=2379575)。 |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |
|  | 源码：  官网：  使用教程： |  |


.C-Eval：构造中文大模型的知识评估基准，其榜单是一个全面的中文基础 模型评估 套件（多层次、多学科的语文评价基础模型套件）。它由13948个选择题组成 问题跨越52个不同的学科和四个难度级 别，测试集用于模型评估（简单来说就是针对中文模型的综合测试机），目的是C-Eval能够帮助开发人员跟踪模型开发的进展，以及分析开发中模型的优点和弱
点。

C-Eval #GitHubttht: https://github.com/hkust-n|p/ceval,

论文地址：https://arxiv.org/pdf/2305.08322v1.pdf

