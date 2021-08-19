# java环境管理工具jenv和sdk

重要提示：Mac下查看已安装的jdk版本及其安装目录,打开终端，输入：/usr/libexec/java_home -V

sdk工具可用，但是没怎么用，最常用的方式是在官网下载需要版本的jdk安装包，安装一次jdk，然后加入到jenv管理，然后就可以使用jenv进行全局java版本的随意切换了。

安装jenv

Linux / OS X
```
$ git clone https://github.com/gcuisinier/jenv.git ~/.jenv
```

Mac OS X via Homebrew
```
brew install jenv
```

jenv的不同shell配置：
Bash
```
$ echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(jenv init -)"' >> ~/.bash_profile
```
Zsh
```
$ echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(jenv init -)"' >> ~/.zshrc
```

注意 jenv 不能自动的安装不同版本jdk ，需要你 自行下载 不同版本jdk 安装

然后 把路径 添加到jenv

命令如下：
```
$ jenv add /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
  oracle64-1.6.0.39 added
$ jenv add /Library/Java/JavaVirtualMachines/jdk17011.jdk/Contents/Home
  oracle64-1.7.0.11 added
```

不想自己下载jdk 可以 使用sdkman 下载不同版本jdk 
方法 参考 sdkman 官网：http://sdkman.io/

常用命令
```
$ jenv versions
  system
  oracle64-1.6.0.39
* oracle64-1.7.0.11 (set by /Users/hikage/.jenv/version)
```

把jdk加入到jenv
```
$ jenv add /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
  oracle64-1.6.0.39 added
```

Configure global version
```
$ jenv global oracle64-1.6.0.39
```

Configure local version (per directory)
```
$ jenv local oracle64-1.6.0.39
```

Configure shell instance version
```
$ jenv shell oracle64-1.6.0.39
```

其中
优先级 jenv shell > jenv local > jenv global

