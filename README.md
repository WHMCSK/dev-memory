# 开发者笔记

## 踩坑记

* [Windows中使用C#写打印程序踩坑记](./docs/windows/print.md)
* [go-face人脸识别踩坑记](./docs/face/go-face-tour.md)  

## 日常
* [Macbook日常管理](./docs/macbook/daily-maintain.md)

## 工具 

* [npm淘宝镜像与官方源切换](./docs/npm/npm-registry.md)
* [java环境管理工具jenv和sdk](./docs/java/java-env.md)
* [GoLang语言多版本管理工具--GVM](./docs/go/gvm.md)
* [文字角标](./docs/text/text-corner-mark.md)
* [go-frp内网穿透](./docs/frp/frp-common-use.md)
* [Centos下源码安装git](./docs/git/centos源码安装git.md)
* [git push 到Total 2406 (delta 379), reused 0 (delta 0)就不动了](./docs/git/git_use_issue.md)
* [windows下git的使用](./docs/git/win-git-use.md)
* [git常用命令](./docs/git/dailygit.md)
* [Python版本管理神器-pyenv](./docs/python/pyenv.md)
* [Windows命令行乱码问题解决](./docs/windows/cmd.md)
* [go mod版本管理](./docs/go/gomod.md)
* [gitbook的使用](./docs/gitbook/gitbook-use.md)
* [mdBook](./docs/mdbook/mdbook-use.md)
* [Makefile编写规则](./docs/makefile/makefile.md)
* [Prometheus应用监控](./docs/prometheus/prometheus.md)

## Markdown

* [Markdown特殊字符](./docs/markdown/markdown-special-character.md)
* [Markdown表格](./docs/markdown/markdown-table.md)

## grpc

* [go grpc](./docs/grpc/grpc-go.md)

## MYSql

* [mysql临时关闭安全更新](./docs/mysql/mysql_common_use.md)
* [Mysql管理](./docs/mysql/mysql_mgmt.md)

## Redis

* [Redis从小白到大白笔记](./docs/redis/Redis.md)

## java
* [java tools](./docs/java/tools.md)

## Python
* [Python版本管理工具](./docs/python/env-mgmt.md)
* [Python版本管理神器-pyenv](./docs/python/pyenv.md)
* [conda](./docs/python/conda.md)
* [Python面向对象](./docs/python/python-oo.md)
* [Python常用命令](./docs/python/common-use-command.md)
* [Python微服务框架比较](./docs/python/python-microservice.md)
* [Python包和模块](./docs/python/package-module.md)

## 加密解密

* [go语言和java语言加密解密对比](./docs/encrypt/go-java-encrypt.md)  

## 系统设计  

* [设备管控中间件设计](./docs//device-check/device-check.md)  

## 系统配置

* [Mac 中显示资源库（Library）文件夹目录的几种方法](./docs/sys-settings/mac-library.md)


## 安卓

* [安卓中一个进程如何在转入后台后不被系统杀死](./docs/android/android-service-forever.md)  

## 大数据
* [常用命令](./docs/bigdata/common-use-command.md)
* [大数据组件自带管理界面](./docs/bigdata/mgmt-pages.md)
* [熟悉spark](./docs/spark/spark.md)

## docker
* [docker使用手册](./docs/docker/docker.md)
* [Docker Desktop 4.18 发布，带来了大量新特性](./docs/docker/Docker%20Desktop%204.18新特性.md)
* [如何在dockerfile加载修改的.bashrc](./docs/docker/dockerfile-modify-bashrc.md)

## 识别
* [车牌识别](./docs/licence-plate/licence-plate.md)

## opencv
* [opencv2](./docs/opencv/opencv.md)

## ros
* [ros](./docs/ros/ros.md)

## 数据可视化
* [Python数据可视化](./docs/datavisualize/python.md)
* [Dash](./docs/datavisualize/dash.md)
* [数据可视化框架比较](./docs/datavisualize/data-visualize-framework.md)
* [Pandas](./docs/datavisualize/pandas.md)

## GIS
* [qgis](./docs/qgis/qgis.md)

## 机器学习
* [机器学习十大算法](./docs/ml/ml.md)

## AI
* [CUDA安装](./docs/ai/cuda.md)
* [DB-GPT试用笔记](./docs/ai/db-gpt.md)
* [人工智能算力和硬件](./docs/ai/compute-capability.md)
* [人工智能自研以及用于项目的可行性研究](./docs/ai/how-could-we-use-llm-reach.md)
* [LLM QA](./docs/ai/llm-qa.md)
* [大模型训练特点数据](./docs/ai/training-feature-data.md)
* [向量数据库](./docs/ai/voctor-db.md)
* [ChatGLM3](./docs/ai/chat-glm3.md)



软件需求：
1. Ubuntu由于Windows
2. 安装Ubuntu或者Ubuntu和windows双系统
3. 编程语言建议Python为主
4. 使用DeepSpeed等优化工具提升大模型的运行效率

硬件需求：
预训练：

算力最密集，消耗的算力通常是推理过程的至少三个数量级以上；
Gpt3.5，据相关人士统计，我们可以按照175B参数规模计算，训练它需要1千块80G的A100训练一个月时间
据某机构的报告，Gpt3的单次训练成本约140万美元，由此，根据模型的参数量级不同，基本上一次模型全新训练要花费200到1200万美元之间。最重要的是你一次训练并不能保证你得到的模型是效果好的，可能涉及到多次训练，这样的成本不是一般个人和企业能够承担的。所以我们普通人，普通企业更应该关注在推理和微调上面。

微调：

算力需求低于训练，但高于推理；
ChatGLM3-6B这种模型，如果做全量微调，至少需要4张80G的A100

推理：

算力消耗最低
Gpt3.5只需要9块80G的A100


ChatGLM-6B为例：
| 量化等级 | 最低 GPU 显存（推理） | 最低 GPU 显存（高效参数微调） |
| --- | --- | --- |
| 单精度 |  20G | 22G |
| 半精度 | 13G | 14G |
| INT8 | 8G | 9G |
| INT4 | 6G | 7G |

主流的显卡显存容量：超算级别显卡A100、H100、A800、H800为80G显
存；其中A100也有40G显存；消费级显卡4090和3090显存为24GB



为什么不能用4090训练大模型
我们要考虑到训练过程，首先几个T的数据，我们要把它分发到不同的Gpu上，这个叫数据并行; 一个大模型的参数很难在一个Gpu上保存下来所以我们需要把大模型的不同层分发到不同的Gpu上做一个串联，这叫做流水线并行; 大模型的训练Transformer一般都是多头（多头注意力机制Multi-head Attention）的，这就涉及到一些张量并行(Tensor并行)。 数据并行，流水线并行，张量并行整体形成了大模型数据层、模型层内、模型层间的关系，这种关系通常涉及到参数的存储、GPU之间的通信计算，在这种情况下，内存带宽、通信延迟、通信带宽就显得尤为重要。

Transformer为何使用多头注意力机制？（为什么不使用一个头）
[](https://www.zhihu.com/question/341222779)
 注解：简单回答就是，多头保证了transformer可以关注到不同子空间的信息，捕捉到更加丰富的特征信息。  

## ESP8266
* [深入理解Arduino下的ESP8266_Non-OS_SDK API⑥ Sniffer(混杂模式) 相关接口](./docs/esp/esp8266-wifi-sniffer.md)
* [深入理解Arduino下的ESP8266_Non-OS_SDK API⑤ Wi-Fi接口](./docs/esp/esp8266-wifi.md)
* [深入理解Arduino下的ESP8266_Non-OS_SDK API⑤ Wi-Fi接口.pdf](./docs/esp/深入理解Arduino下的ESP8266_Non-OS_SDK%20API⑤%20Wi-Fi接口_51CTO博客_arduino+esp8266.pdf)

## ESP-Drone
* [ESP-Drone笔记](./docs/esp/esp-drone.md)
* [ESP-Drone官方文档](https://docs.espressif.com/projects/espressif-esp-drone/zh_CN/latest/gettingstarted.html)



## 各类awesome

* [awesome-python-cn](https://github.com/jobbole/awesome-python-cn)
* [awesome-python](https://github.com/vinta/awesome-python)
* [awesome-go](https://github.com/avelino/awesome-go)
* [awesome-go-cn](https://github.com/jobbole/awesome-go-cn)
* [go-awesome](https://github.com/shockerli/go-awesome)
* [awesome-go-cn](https://github.com/yinggaozhen/awesome-go-cn)
* [awesome-go-storage](https://github.com/gostor/awesome-go-storage)
* [awesome-golang-algorithm](https://github.com/6boris/awesome-golang-algorithm)