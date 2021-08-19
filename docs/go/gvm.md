# GoLang语言多版本管理工具--GVM

GVM由Josh Bussdieker（jbuss，jaja，jbussdieker）在Moovweb工作期间

GVM提供了一个管理Go版本的界面。

开源项目：https://github.com/moovweb/gvm

特征
* 安装/卸载Go gvm install [tag]标签为“60.3”，“go1”，“weekly.2011-11-08”或“tip”的版本
* 列出GOROOT中添加/删除的文件 gvm diff
* 使用管理GOPATH gvm pkgset [create/use/delete] [name]。使用--local如name在本地路径管理信息库（/path/to/repo/.gvm_local）。
* 列出最新发布标签gvm listall。使用--all列出每周为好。
* 为多个版本安装缓存最新Go源的干净副本。
* 将项目目录链接到GOPATH

背景

当我们开始使用Go不匹配的依赖项开发时，API的变化会影响我们的构建过程，并且很难与其他人的变化合并。

经过几次整理GOROOT并重建后，我决定拿出一个工具来监督这个过程。它最终演变成今天的gvm。

安装
```
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)

```
Or if you are using zsh just change bash with zsh

Installing Go

```
gvm install go1.4
gvm use go1.4 [--default]
```

一旦完成，Go将在路径中并准备使用。$ GOROOT和$ GOPATH自动设置。

安装Go时可以指定其他选项

```
Usage: gvm install [version] [options]
    -s,  --source=SOURCE      Install Go from specified source.
    -n,  --name=NAME          Override the default name for this version.
    -pb, --with-protobuf      Install Go protocol buffers.
    -b,  --with-build-tools   Install package build tools.
    -B,  --binary             Only install from binary.
         --prefer-binary      Attempt a binary install, falling back to source.
    -h,  --help               Display this message.
```

关于编译Go 1.5+的注意事项

Go 1.5+从工具链中删除了C编译器，并将其替换为Go中编写的编译器。显然，如果您还没有可用的Go安装，这会产生引导问题。为了编译Go 1.5+，请确保首先安装Go 1.4。

```
gvm install go1.4 -B
gvm use go1.4
export GOROOT_BOOTSTRAP=$GOROOT
gvm install go1.5
```

列出所有已安装的Go版本（当前版本的前缀为“=>”）：

```
gvm list
```

列出可供下载的所有Go版本：

```
gvm listall
```

卸载

要完全删除gvm和所有已安装的Go版本和包：
```
gvm implode
```
如果不起作用，请参阅本页底部的故障排除步骤。


故障排除

有时特别是在升级期间，gvm文件的状态可能会混淆。对于从旧版本升级到0.0.8以上的情况，这种情况最为正确。变化正在放缓，LTR迫在眉睫。但是现在rm -rf ~/.gvm将永远删除gvm。敬请关注！