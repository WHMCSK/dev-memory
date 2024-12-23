# 论文

## 读哪些论文？

1. 分类角度

论文类型角度:

- 综述
- 理论
- 实验
- 系统
- 其他

论文主题角度:

- 计算机视觉
- 自然语言处理
- 机器学习
- 强化学习
- 其他

论文评价角度:

- 新颖性
- 有效性
- 实用性
- 重要性
- 其他

论文评价标准:

- 引用次数
- 被引次数
- 被评价次数
- 被引用率
- 被评价率

以上是从不同角度看待论文，但是我们出于实用和学习路径角度来看，论文分为两类：

- 综述论文
- 专题论文

1. 综述论文： 快速熟悉某领域发展历程、 现状及子方向，了解领域内基础概念及关键词
2. 专题论文： 除了综述论文，剩下的都可以称之为专题论文，介绍具体算法，可学习 其设计思路，实验技巧，代码实现等具体技术

通常我们进入一个新的领域，首先找高质量综述论文，入门了解。在了解了领域之后，就针对性的找专题论文进行深入学习。

2. 质量角度

* 高质量期刊会议：CVPR、ECCV.ICCV、AAAI、NIPS, ICLR, ICML
* 高引论文：同行间普遍认可，参考，借鉴的论文
* 知名团队：Yoshua Bengio、Yann LeCun、Geoffrey Hinton, Andrew Ng等
* 有代码的论文： “Talk is cheap, show me the code.”
* 推荐网站： https://paperswithcode.com

## 怎么找论文

1. 未知论文题目：依关键词搜索相关领域论

1.知网：寻找优质综述，快入入门
2.百度学术、google scholar
3.arXiv: https://arxiv.org 论文预印本（preprint）平台
4.顶会：CVPR、ECCV、ICCV、AAAI、NIPS、ICLR、ICML等

论文发表前，一般都会在arXiv网站上先发出，占个坑，代表这个论文、观点、方法是这个作者提出的，主要是因为论文正式发表需要经过一个漫长的评审过程。

通过以上途径，我们可以找到成千上万论文，但是如何筛选优质论文呢？要看论文所在的期刊是否优质，看IF：
IF（Impact Factor， 影响因子）：期刊前N年发表的论文被引数除以前N年发表的论文数，通常N=2或N=5
JCR （Journal Citation Reports，期刊引证报告）：统计SCI期刊的论文引用数据，给出各期刊IF 

还有个更加直接的方式，就是看SCI期刊分区：
• JCR方式，一、二、三、四区各占25％
• 中科院方式，一区为前5%，二区为5%-20%，三区为20%-50%，四区为50%-100%

2. 如果指导论文题目，没有下载途径

2.1 sci-hub：一个能绕过科研论文收费的神奇网站
• https://sci-hub.tw
• https://sci-hub.si
• https://sci-hub.se

搜索论文的时候可能遇到的专业名词：

* PMID（PubMed Unique Identifier,PubMed唯一标识码）：PubMed搜索引擎中收录的生命科学和医学等领域的文献编号
* DOI （Digital Object Unique Identifier，数字对象唯一标识符），相当于文献的数字身

例如通过DOI搜索名为Going Deeper with Convolutions的论文：10.1109/CVPR.2015.7298594

2.2 百度学术 文献互助：http://xueshu.baidu.com

## 怎么整理论文

1. 手动管理：

统一命名格式：时间-作者-题名；时间-关键词-题名

按类别归入文件夹

检索：电脑自带搜索工具，搜索关键词

2. 论文管理软件

endnote,Mendeley, Zotero, Citavi等

免费的首选Mendeley

## 如何读论文

1. 泛读
2. 精读
3. 总结

* 泛读：快速浏览，把握概要 重点读标题、摘要、结论、所有小标题
* 精读：选出精华，仔细阅读 找出问中关键内容，进行仔细阅读
* 总结：总览全文，归纳总结 总结文中创新点，关键点，启发点等重要信息

论文阅读效果自测

回答三个的终极问题

•你是谁：论文提出/采用什么方法，细节是什么  
•从哪里来：论文要解决什么问题/任务，其启发点或借鉴之处在哪  
•到哪里去：论文方法达到什么效果  

论文中可借鉴地方总结

## 论文结构

1. Abstruct  
论文简介，阐述工作内容，创新点，效果

2. Introduction   
介绍研究背景，研究意义，发展历程，提出问题

3. Related Work   
相关研究算法简介，分析存在的缺点

4. Our Work  
论文主要方法，实现

5. Experiments  
实现步骤及结果分析

6. Discussion  
论文结论及未来可研究方向

## 论文代码学习方法

1. 任务定义  
•搞清楚程序的目的   
•为了实现什么任务   

2. 数据来源   
•源码获取渠道   
•数据集类型   
•数据集的来源    

3. 运行环境  
•运行环境    
•实验工具    
•第三方库    

4. 运行结果  
•能否运行成功     
•运行代码后出现什么样的结果    

4. 如何实现  
•代码整体架构    
•每部分实现细节    

## 基础知识

### Python 基础  

1.编程基础  
2.机器学习库  

### 神经网络基础知识  

一、神经网络与多层感知器  
1.1 人工神经元：MP模型  
1.2 多层感知机  
1.3 激活函数(sigmoid/tanh/relu)  
1.4 反向传播(BP):梯度下降，学习率  
1.5损失函数：MSE/CE；Softmax函数  
1.6 权值初始化  
1.7正则化：L1、L2和Dropout；提及BN/GN/IN/LN  

二、卷积神经网络基础  
2.1 卷积神经网络简介  
2.2卷积层  
2.3池化层  
2.4 Lenet5  

三、循环神经网络  
3.1 rnn循环神经网络  
3.2 lstm 长短记忆循环神经网络  
3.3 gru 门控循环单元  

### 数学基础  

1.矩阵计算  
2.概率论、信息论  

### PyTorch 入门  

1.PyTorch简介及安  
2.PyTorch人名币分类  
3.PyTorch数据读取模块  
4.PyTorch数据增强   
5.PyTorch Module模块  
6.PyTorch 常用网络层  
7.PyTorch 损失函数  
8.PyTorch 优化器Optimizer  
9.PyTorch可视化TensorBoard  
10.PyTorch实用技巧GPU/Finetune/保存加载  

### CV图像基础  

一、图像基础知识  
1.1 数字图像  
1.2 图像的属性    

二、常见图像处理  
2.1 绘图、添加文字  
2.2 图像几何变换  
2.2 图像滤波与增强  
2.2形态学变化  

三、图像分割  
3.1 阈值分割  
3.2 边缘检测  
3.3 连通域分析  
3.4 图像轮廓  
3.5 区域生长  
3.6 分水岭  

四、图像特征与目标检测  
4.1 图像特征理解  
4.2 形状特征  
4.3 纹理特征  
4.4 模板匹配  
4.5 人脸检测  
4.6 行人检测  

五、运动目标识别  
5.1 摄像头调用  
5.2 视频的读取与保存  
5.3 帧差法  
5.4 光流法  
5.5 背景减除法  

### NLP 基础知识  

一、文本特征  
1.1 词袋 bag of words BOW  
1.2 分布特征 （distributional）  
1.3 tfidf权重  
1.4 n元语言模型  
1.5 语言学特征：句法树  

二、Nlp相关任务  
2.1 文本分类  
2.2 序列标注  
2.3 翻译、摘要生成、信息抽取等  
2.4 文本生成NLG  


## 最近看的论文

### AutoGen

code:

https://github.com/microsoft/autogen

cite paper:

* [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
* [Cost-Effective Hyperparameter Optimization for Large Language Model Generation Inference](https://arxiv.org/abs/2303.04673)
* [An Empirical Study on Challenging Math Problem Solving with GPT-4](https://arxiv.org/abs/2306.01337)

