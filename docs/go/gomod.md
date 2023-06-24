# go mod版本管理

## 操作过程

1. 新建git源码分支
```
git branch v2
git checkout v2
git branch
```

2. 修改gomod版本号

假设当前模块名称为github.com/ascode/common-sdk
```
go mod edit --module=github.com/ascode/common-sdk/v2 go.mod
```
该命令后会修改go.mod文件第一行为
```
module github.com/ascode/common-sdk/v2
```

2. 推送新分支到服务器
```
git push -u origin v2
```

3. 给当前新分支代码打一个tag，并推送tag到服务器
```
git tag v2.0.0
git push origin v2.0.0
```

5. go get模块

经过如上的步骤后，在其他项目中go get github.com/ascode/common-sdk/v2，则go.mod中的引用会变成
```
require (
	github.com/ascode/common-sdk/v2 v2.0.0
)
```

6. 如何变成github.com/ascode/common-sdk/v2 v2.0.1

修改代码之后有如下操作：
```
git add .
git commit -m ""
git push origin v2
git tag v2.0.1
git push origin v2.0.1
```

然后再次go get github.com/ascode/common-sdk/v2，则go.mod中的引用就会变成
```
require (
	github.com/ascode/common-sdk/v2 v2.0.1
)
```

## 相关原理说明

### 介绍

go mod 是go对包管理支持，在go1.11版本添加的，在go1.13版本默认开启GO111MODULE="on"，且不会受到GOPATH影响。在项目下通常会生成一个go.mod文件。

go mod文件内容如下：
```
module github.com/ascode/common-sdk/v2
 
go 1.20
```

### 模块路径

我们在应用中通常引用第三方库包时需要使用go get {项目地址}，这里的{项目地址}称为模块路径，模块的路径是包内的公共前缀，它由存储库根路径、存储库目录和主要版本后缀构成。其中存储库根路径是开发中版本控制存储库的根目录。存储库目录是模块下包含的子包，该包提供独立功能。主要版本后缀则是Go modules中对于v2及以上版本需要在模块名中申明。

举个例子：在github.com中我创建了一个common-sdk库，该库也称为模块，模块的版本为v2。而common-sdk库下的一个目录例如http则称为包，而github.com/ascode/common-sdk/v2是common-sdk模块路径，github.com/ascode/common-sdk也叫做存储库根路径，v2是版本后缀（非必须），http是存储库目录（也是个目录）。

引入github.com/ascode/common-sdk/v2模块路径下的http包如下：
```
import (
 "github.com/ascode/common-sdk/v2/http"
)
```

### 版本类别

* 通用版本

对于打了版本tag的会在末尾追加最新版本例如v2.0.1
```
require (
	github.com/ascode/common-sdk/v2 v2.0.1
)
```

对于在代码中没被引用的会在 后面加indirect。
```
require (
	github.com/ascode/common-sdk/v2 v2.0.1 // indirect
)
```

* 伪版本

对于没有打tag的版本返回类似下面形式v0.0.0-20220708160210-fc5e318e30f7，v0.0.0是最近提交的版本号，20220708160210时间戳，fc5e318e30f7随机字符串。

```
module github.com/ascode/horde
 
go 1.20
 
require github.com/ascode/common-sdk/v2 v0.0.0-20220708160210-fc5e318e30f7
```

* 主版本后缀

对于2.0及以上的版本需要在mod文件中的module后加上v2。

```
module github.com/ascode/common-sdk/v2
 
go 1.20
```

使用时go.mod文件中添加
```
github.com/ascode/common-sdk/v2 v2.0.1
```

* 兼容版本

对于在以前没有go.mod时（例如：旧版本go1.9），却使用了v2.0.0及以上版本表示，在下载包时会出现v2.0.0+incompatible类型如下所示。

```
github.com/seanshenhy/go-mod-demo v2.0.0+incompatible
```

### 模块路径后面为什么会有v2

go mod 要求每个module从大版本2开始，模块路径必须有类似 /v2 版本号的后缀，假如module example.com/mod 从 v1.0.0发展到v2.0.0，这时它的go.mod中的模块路径应该修改为 example.com/mod/v2。go mod 认为如果一个module的两个不同版本之间引入路径相同，则它们必须是相互兼容的，而不同的大版本通常意味着是不兼容的，所以引入路径也不该相同，通过在模块路径上加上大版本后缀，这样就可以同时使用同一个模块的多个不同大版本。

对于 v0 和 v1 两个大版本，go mod不允许存在版本后缀，这是因为 v0 版本通常是不稳定版本，不提供兼容性保证，并且通常 v1 版本兼容最新的 v0 版本，所以从 v0 版本迭代到 v1 版本，不需要修改module 路径 。

作为特殊情况，以 gopkg.in 打头的module 不管是 v0、v1 还是其他大版本都必须存在版本后缀，且它的的版本后缀是用 ‘.’ 而不是 ‘/’，比如：

```
require (
    get gopkg.in/yaml.v1 v1.0.0-20140924161607-99df34309c0
    get gopkg.in/yaml.v2 v2.4.0
    get gopkg.in/yaml.v3 v3.0.1
)
```

对于一些比较老的项目可能当时go mod还没出现，但版本早已经迭代到v2 以上，或者有些项目没有遵循以上的原则，go mod为了能够正常使用它们，会在引入 v2 以上的版本后加上 +incompatible 以示提醒，比如 github.com/docker/docker

```
require github.com/docker/docker v20.10.17+incompatible
```
且这样的项目根目录下不允许存在 go.mod 文件，如果项目添加了go.mod且又不遵循module path后缀原则，则将无法拉取到 v2 以上版本，如果手动指定v2 以上版本强制拉取则会报错：
```
192:incomptible zy$ go get github.com/zhyee/Ranking-of-Internet-Corp-By-Go@v2.1.1 go: github.com/zhyee/Ranking-of-Internet-Corp-By-Go@v2.1.1: invalid version: module contains a go
mod file, so module path must match major version ("github.com/zhyee/Ranking-of-Internet-Corp-By
- Go/v2")
```

对于那些比较老的go 模块，如果大版本已经达到 v2 以上，但不存在向后兼容问题，这时不建议添加 go.mod 文件，以便使用该模块的人能正常更新到最新版本，如果后续迭代出现大的变动已经无法向后兼容，这时应该升级一个大版本，并添加 go.mod 文件，同时模块path也要加上新的大版本后缀，使用者要使用该新版本则需要像引入一个新的模块一样使用带有后缀的module path。

### 语义化版本规范 2.0.0

[语义化版本 2.0.0](https://semver.org/lang/zh-CN/)摘要
```
版本格式：主版本号.次版本号.修订号，版本号递增规则如下：

主版本号：当你做了不兼容的 API 修改，
次版本号：当你做了向下兼容的功能性新增，
修订号：当你做了向下兼容的问题修正。
先行版本号及版本编译信息可以加到“主版本号.次版本号.修订号”的后面，作为延伸。
```

Go module不但遵循语义化版本规范 2.0.0,而且还更进一步，对语义化版本中的major还还赋予了更深的意义。
* v0.X.X: 对于主版本号(major)是0的情况，隐含你当前的API还处于不稳定的状态，新的小版本可能不向下兼容
* v1.X.X: 当前的API处于稳定状态，minor的增加只意味着新的feature的增加，API还是向下兼容的
* v2.X.X: major的增加意味着API已经不向下兼容了

你知道在go module中，哪些版本号隐含当前API是不稳定的？

但是go module与众不同鹤立鸡群卓然不群的是，一旦你的major大于等于2, 你的module path必须加上v2后缀(如果tag是v3.X.X,那就是v3后缀，以此类推)。

而且，包引用路径也要加上v2，比如 go.etcd.io/etcd/client/v3。

这是一个怪异的写法，相当于在正常的易于理解的module path上加了一个狗屁膏药，以提示这个引入的库是哪个版本的？

为什么要加上这个v2、v2后缀的，肯定有一定的考虑。

最主要的，Go的开发者(这里指Russ Cox)在import compatibility rule指出:

```
If an old package and a new package have the same import path,
the new package must be backwards compatible with the old package.
```

也就是相同module path应该保证新的版本向下兼容。

这种想法是好的。比如你在你的项目中可以使用同一个库的多个版本， v1版本处理以前遗留的逻辑，v2版本处理新的逻辑，v3版本试验未来的版本，同一套库的不同版本可以共存，并不会出现版本冲突的地方。

而且程序员看到这些module path,也很清楚的知道版本不兼容了，谁是更新的版本。

但是这种方式也是很有争议的，在实践中中也带来了很多问题，我在开发某模块深受其害,你可以看它的v3.4.X的版本，就是因为没有加上v3的后缀，导致go命令下载或者导入(get)这些package的时候根本就下载不了。

### 摘自某博客

* vX后缀污染了package path
本来正常的package path一般是仓库路径+package name,或者go module下 module path + package的方式，可是一旦版本大于等于2,就不得不加上一个后缀v2,v3等，将package path的含义改变了。

当然忍一忍我们还能接受，大不了闭着眼睛用呗，最痛苦的很多Go的初学者并不了解这种设置，不知道导入新的库的版本要加v2后缀，一脸茫然。

* v0, v1和v2数据类型不兼容

在module path中增加了v2,v3等后缀后，也就以为着这些package都是不同的package，虽然它们中大部分的数据类型并没有做改变，还是向下兼容的，也不能直接赋值，还是需要强转一下。

比如你的项目依赖Auth 1.0.0, 也依赖Auth 2.0.0,那么即使A.Config在两个版本中没做任何改变，你也不能把Auth.Config赋值给Auth/v2.Config,而是需要在代码中加上强转的逻辑，两两互转。一旦发布了v3,那就得三三互转，很长的一个switch分支处理这种情况，如果发布v4，那么逻辑更复杂了。

* 给第三方库的开发者带来了很大的负担

虽然你觉得我也就发布v2,v3,v4等几个版本，版本路线很清晰，管理起来也不复杂，没什么大不了的。

但是，如果你的库是一个非常流行的库，很多开发者基于你的库开发了第三方的库的话，就非常痛苦了。

这意味着一旦你发布了一个新的版本，这些第三方的开发者就必须及时的更新他们的库，基于你的新的版本发布他们新的v2，v3版本。这就像病毒一样，初步扩展开来。给广大的开发者带来的很大的负担。

当然，见仁见智，这些情况可能你不会遇到，或者也不会给你带来困扰，所以它不是一个问题。而我，在开发rpcx，或者解答一些网友的问题的时候，深深被v2伤害到了,小小的心灵无法承受v2之重。

一些开源项目，为了避免版本号跳到v2,采用了其它的一些办法，比如protobuf-go, 正在做新的版本的重构，改动非常大，不和以前的版本兼容了，可以以前的版本都v1.X.X了，那怎么办呢？换module path名称。

github.com/golang/protobuf: 支持先前的protobuf go,目前最高版本v1.5.2   
google.golang.org/protobuf: 新版本的module path,目前最高版本v1.27.0，初始版本v1.20.0   

[官方的说法](https://github.com/protocolbuffers/protobuf-go)是：
```
This project is the second major revision of the Go protocol buffer API implemented by the google.golang.org/protobuf module. The first major version is implemented by the github.com/golang/protobuf module.
```

对于我开发的rpcx项目，因为在go module出来之前版本号已经发布到了v6.X.X。 我想回到从前，貌似回不去了。所以我采用了一个极端的做法，把tag重建，所有的版本号都定义在v1.X.X内。还好影响的用户比较少，所以也没有用户抱怨。

我这种做法比较极端，没造成用户抱怨的原因是我一直坚持go module和GOPATH并存的方式。发版的时候采用go module发版，master开发分支上采用GOPATH方式，绝大部分用户都使用master分支，或者自己fork了一个新的版本，所以造成的影响很小。

## 总结
对于go modules我们在开发中只需要知道两点即可，一是go.mod文件引用库包的含义（v0.x.x和v1.x.x区别，版本后带// indirect的含义，版本类型为v0.0.0-20220708160210-fc5e318e30f7含义， 版本类型为v2.0.0+incompatible含义），二 v2以下与v2及以上版本库模块名称定义和引用区别，库包定义时，v2以前的版本在go.mod文件中modules后没有/vx，v2及以上则必须带上/vx；使用时，v2以前版本 直接go get {库包}即可，v2及以上则需要使用go get {库包/vx}方式。

## Tips
若库包包含多版本，则最好使用vx方式单独维护分支，这是常见的一种方式，例如：github.com/go-redis/redis库维护了多个分支。
