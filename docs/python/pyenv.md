# Python版本管理神器-pyenv

## 一、问题情景:

1. Python解释器版本混乱, 2和3差别巨大, 而且细分版本也不尽相同, 难以选择和管理.
2. 不同Linux发行版自带Python不同, 如ubuntu16自带2.7和3.5版本, 其中系统许多组件依赖于自带解释器, 一旦删除或者更改都可能会造成系统出问题.
3. 不同的Python解释器软件包管理也是问题, 如pip和ipython等必备包组件, 而且在项目开发中如何保证不同的包环境互不干扰也是一个问题.

那么有没有一个终极的解决办法能在管理不同解释器版本的同时控制不同的包环境呢? 有的, 就是pyenv.

## 二、pyenv是什么? 能干什么?

pyenv是一个forked自ruby社区的简单、低调、遵循UNIX哲学的Python环境管理工具, 它可以轻松切换全局解释器版本, 同时结合vitualenv插件可以方便的管理对应的包源.
我们知道, 在terminal中输入一个命令比如‘ls’时, shell会从当前环境的PATH中的各个目录里看是不是有ls这个可执行文件, 如果找到就执行, 否则就会报‘command no found’ 的错误, 同理, 只要控制PATH变量就能够做到python版本的切换, pyenv通过在PATH头部插入shims路径来实现对python版本的控制.


### pyenv和流行的pipenv、virtualenv的关系

pipenv是requests 作者 Kenneth Reitz大神写的一个python虚拟环境管理工具, 结合了pip和virtualenv的功能, 侧重点还是在包环境管理上, 使用思路是先创建一个指定python版本的环境, 然后在此环境上安装相应的包, 好评不错, 看到很多大牛都在推荐.

virtualenv是一个比较传统成熟的虚拟环境管理工具了, 用的人也比较多, 思路也是创建虚拟环境, 然后安装相应的包, 要进入环境就source一下activate脚本激活一下, 尽管成熟, 但是我个人不太喜欢用, 在部署项目的时候老是容易出现一些环境问题.


pyenv相对来说知名度就差很多了, 不过也很稳定, 这三个环境管理工具我都用过, 我个人更喜欢pyenv, 理由如下:

相对于其他两个工具, pyenv更侧重在python 解释器版本管理上, 比包管理更大一个层级, 使用pyenv我可以方便的下载指定版本的python解释器, pypy, anaconda等, 可以随时自由的在shell环境中本地、全局切换python解释器
开发的时候不需要限定某个版本的虚拟环境, 只需要在部署的时候用pyenv指定某个版本就好了
pyenv切换解释器版本的时候, pip和ipython以及对应的包环境都是一起切换的, 所以如果你要同时运行ipython2.x和ipython3.x多个解释器验证一些代码时就很方便
pyenv也可以创建好指定的虚拟环境, 但不需要指定具体目录, 自由度更高, 使用也简单
## 三、安装pyenv

1. 在家目录里clone项目:

```
 $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# MacOS的话可以直接用homebrew安装
$ brew update
$ brew install pyenv 
```

2. 添加shell配置文件中追加如下: (如zshrc)

```
export PYENV_ROOR="$HOME/.pyenv"
export PATH=$PYENV_ROOT/shims:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

3. source一下配置文件, 输入pyenv --version测试一下

## 四、简单使用

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

## 五、包管理插件pyenv-virtualenv

首先下载:
```
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $.pyenv/plugins/pyenv-virtualenv
```
克隆完成后添加如下到shell配置文件(mac的话是.zshrc)

```
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

实际上mac用户直接brew安装就可以了...
```
$ brew install pyenv-virtualenv
$ eval "$(pyenv init -)"
$ eval "$(pyenv virtualenv-init -)"
```
使用:
```
# 创建一个3.6.5版本的虚拟环境, 命名为v365env, 然后激活虚拟环境
$ pyenv virtualenv 3.6.5 v365env
$ pyenv activate v365env
# 关闭虚拟环境
$ pyenv deactivate v365env
```

当切换python解释器的时候对应的pip和包库也会一并切换过去, 而且可以为指定版本的解释器创建项目所需的虚拟环境, 切换的时候也异常简单, 个人常用的做法是为每个项目创建不同的虚拟环境, 当进入该环境的时候就可以随便浪而不用担心影响到其它项目, 搭配Pycharm使用效果更佳.

## 六、了解更多使用姿势

pyenv项目地址:

pyenv/pyenv
​github.com/pyenv/pyenv.git

pyenv-vitualenv插件地址:

pyenv/pyenv-virtualenv
​github.com/pyenv/pyenv-virtualenv.git
