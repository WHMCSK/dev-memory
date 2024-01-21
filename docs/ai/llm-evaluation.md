# 大模型评估


1. LLM 实时排行，来自 UC伯克利：https://lmsys.org/blog/2023-06-22-leaderboard/


2. 选择中文模型：中文语言理解测评基准（CLUE）：https://www.cluebenchmarks.com/index.html 和SuperCLUE琅琊榜: https://www.superclueai.com/

开源领域 ChatGLM, LLAMA, RWKV 主要就是这3种模型，中文好一点就是 ChatGLM，潜力最好的就是LLAMA，RNN架构决定RWKV有很好的推理效率（随输入长度内存占比线性自增，而LLAMA则是指数增加）和 Length Extrapolation（关于长度外推性，可以参考苏神的文章）。当然 MPT-7B-StoryWriter-65k+模型也有较长的外推能力。

自ChatGPT为代表的大语言模型（Large Language Model, LLM）出现以后，由于其惊人的类通用人工智能（AGI）的能力，掀起了新一轮自然语言处理领域的研究和应用的浪潮。尤其是以ChatGLM、LLaMA等平民玩家都能跑起来的较小规模的LLM开源之后，业界涌现了非常多基于LLM的二次微调或应用的案例。下面这个项目在收集和梳理中文LLM相关的开源模型、应用、数据集及教程等资料，目前收录的资源已达100+个！

Awesome Chinese LLM，主要是整理开源的中文大语言模型，以规模较小、可私有化部署、训练成本较低的模型为主，包括底座模型，垂直领域微调及应用，数据集与教程等。

```
Awesome Chinese LLM #JGitHubitft: https://github.com/HqWu-HITCS/Awesome-Chinese-LLM
```



## 中文大模型评估标准

| 名称 | 网址 | 介绍 |
| --- | --- | --- |
| C-Eval | 源码：https://github.com/hkust-nlp/ceval  官网：https://cevalbenchmark.com/#home | C-Eval是全面的中文基础模型评估套件，涵盖了52个不同学科的13948个多项选择题，分为四个难度级别 |
