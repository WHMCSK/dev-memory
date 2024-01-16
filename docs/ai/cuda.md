# CUDA安装 （windows版）

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
