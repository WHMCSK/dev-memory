# Python版本管理工具

如果你使用Python开发，对于不同的开发框架或应用肯定会有Python多版本共存的情况，此时Python多环境管理工具就可以帮你快速解决此问题，以便将精力专注开发。下面介绍常用的多版本管理工具：

1. Anaconda
2. Virtualenv
3. pyenv
4. pythonbrew
5. 使用Docker容器管理Python版本

## 1.Anaconda

Anaconda多应用在科学计算中，但是它可以很方便的对各个Python环境进行切换；而且自动包管理器conda可以安装软件包的多个版本和依赖。从官网下载安装包自行安装即可。用法如下：

```
#创建Python虚拟环境
conda create -n py36 python=3.6
 
#激活Python虚拟环境
source activate py36
 
#安装相关依赖，并正常使用此环境下的python版本。
pip install tensorflow
 
#退出虚拟环境
source deactivate
```

## 2.Virtualenv
Virtaulenv的原理是把系统Python复制一份到Virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令Python和pip均指向当前的virtualenv环境。Virtaulenv相较于Anaconda，更多应用在开发环境。以下是virtualenv的安装和使用步骤。

```
#安装virtualenv
pip install virtualenv
 
#创建Python虚拟环境
virtualenv -p /usr/bin/python2.7 py27env
# 或者
virtualenv venv --python=python3.11
 
#指定虚拟环境的路径，成功创建Python虚拟环境
source py27env/bin/activate
 
#安装相关依赖
pip install -r requirements.txt
 
#退出虚拟环境
deactivate
```

## 3.Pyenv
pyenv是一个forked自ruby社区的简单、低调、遵循UNIX哲学的Python环境管理工具, 它可以轻松切换全局解释器版本, 同时结合vitualenv插件可以方便的管理对应的包源。

pipenv是requests 作者 Kenneth Reitz大神写的一个python虚拟环境管理工具, 结合了pip和virtualenv的功能, 侧重点还是在包环境管理上, 使用思路是先创建一个指定python版本的环境, 然后在此环境上安装相应的包。

```
# 查看当前版本
pyenv version
 
# 查看所有版本
pyenv versions
 
# 查看所有可安装的版本
pyenv install --list
 
# 安装指定版本
pyenv install 3.6.5
# 安装新版本后rehash一下
pyenv rehash
 
# 删除指定版本
pyenv uninstall 3.5.2
 
# 指定全局版本
pyenv global 3.6.5
 
# 指定多个全局版本, 3版本优先
pyenv global 3.6.5 2.7.14
 
# 实际上当你切换版本后, 相应的pip和包仓库都是会自动切换过去的
```

## 4.pythonbrew

pythonbrew是受 perlbrew 和 rvm 启发，在用户的$HOME目录中进行python构建和安装自动化的项目。另一衍生版本 ： pythonz 。

## 5.使用Docker容器管理Python版本

我们还可以使用Docker容器管理Python版本。Docker是一种可移植的容器化应用程序，可以将应用程序与其所有的依赖性（库、环境变量等）打包在一起，形成一个独立的应用程序实体，以便在任何Docker支持的平台上运行。以下是使用Docker容器管理Python版本的步骤。

```
#在Docker中安装Python镜像，创建Python的容器。
docker run -it python:3.6 /bin/bash
 
#安装相关依赖
pip install tensorflow
 
#退出Docker容器
exit
```