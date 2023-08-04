# MdBook

### mdBook简介

mdBook是一个Rust语言编写，Markdown创建书籍的命令行工具。它非常适合创建产品或API 文档、教程、课程材料或任何需要简洁、易于导航和可定制的演示文稿。功能和Gitbook类似，最大优势是速度快。

* 轻量级，Markdown语法
* 搜索，集成搜索功能
* 语法高亮，syntax highlighting
* 多个主题，Theme自定义输出的格式
* 预先处理器，支持preprocessor预处理器支持，markdown渲染器之前对其进行修改的扩展
* 后端，Backends支持多种输出格式
* 速度，Rust开发，速度没得说
* 甚至，Rust代码自动化测试。

### 安装mdBook

由于mdBook使用Rust语言开发，我们需要提前安装Rust

安装Rust

```
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
......
Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, run:
source "$HOME/.cargo/env"
# cargo version
cargo 1.65.0 (4bc8f24d3 2022-10-20)
```

应用cargo环境：
```
source "$HOME/.cargo/env"
```

安装Rust后，命令行构建和安装mdBook，安装完成后：

```
# cargo install mdbook
    Updating crates.io index
  Installing mdbook v0.4.21
  Downloaded os_str_bytes v6.4.0
  Downloaded chrono v0.4.23
  Downloaded 2 crates (210.4 KB) in 1.30s
  ......
   Compiling libc v0.2.137
   Compiling mdbook v0.4.21
    Finished release [optimized] target(s) in 1m 12s
  Installing /Users/wanzi/.cargo/bin/mdbook
   Installed package `mdbook v0.4.21` (executable `mdbook`) #这里说明已经安装成功
# mdbook  --version
mdbook v0.4.21
# tree -L 2 ~/.cargo
/Users/wanzi/.cargo
├── bin
│   ├── cargo
│   ├── cargo-clippy
│   ├── cargo-fmt
│   ├── cargo-miri
│   ├── clippy-driver
│   ├── mdbook #这里说明已经安装完成
│   ├── rls
│   ├── rust-gdb
│   ├── rust-gdbgui
│   ├── rust-lldb
│   ├── rustc
│   ├── rustdoc
│   ├── rustfmt
│   └── rustup
├── env
└── registry
    ├── CACHEDIR.TAG
    ├── cache
    ├── index
    └── src
```

当然，如果你需要最新版本可以使用如下方法：

```
cargo install --git https://github.com/rust-lang/mdBook.git mdbook
```

### 使用MdBook写一本电子书

初始化生成一本书名为devops-manual的书籍：

```
# mdbook init devops-manual
Do you want a .gitignore to be created? (y/n)
y
What title would you like to give the book?
devops-manual
2022-10-06 13:59:33 [INFO] (mdbook:📖:init): Creating a new book with stub content

All done, no errors...
# tree devops-manual
devops-manual
├── book
├── book.toml
└── src
    ├── SUMMARY.md
    └── chapter_1.md

2 directories, 3 files
```

启动mdbook，测试本地预览：

```
# mdbook serve --open
2022-10-06 14:04:05 [INFO] (mdbook::book): Book building has started
2022-10-06 14:04:05 [INFO] (mdbook::book): Running the html backend
2022-10-06 14:04:05 [INFO] (mdbook::cmd::serve): Serving on: http://localhost:3000
2022-10-06 14:04:05 [INFO] (mdbook): Opening web browser
2022-10-06 14:04:05 [INFO] (warp::server): Server::run; addr=127.0.0.1:3000
2022-10-06 14:04:05 [INFO] (warp::server): listening on http://127.0.0.1:3000
2022-10-06 14:04:05 [INFO] (mdbook::cmd::watch): Listening for changes...
```

–open选项将打开默认网络浏览器以查看新书

对于生成的mdBook新书目录结构：

* book.toml：描述如何构建电子书的设置，使用TOML语法编写
* SUMMARY.md：位于src/SUMMARY.md，该文件包含本书所有章节的列表，在查看章节之前，必须将其添加到此列表中。
* src：该目录存放书籍的源文件，每章都有一个单独的Markdown文件
* book：存放电子书html文件,当你构建完成一本书(mdbook build)后，会在该目录下生成电子书静态文件，用于托管到其他web服务上，例如Github Pages等。

到这里，想写一本关于Devops的电子书，我们只需要写好目录，然后将各个章节逐一编写即可。

比如我这里的：devops-manual/SUMMARY.md

```
# Summary

[介绍](README.md)

# DevOps工程

- [DevOps](xops/devops.md)

# DevOps工具链

- [基础工具](base/readme.md)
  - [Git](base/git.md)
  - [Docker](base/docker.md)
  - [Makefile](base/makefile.md)

- [产品需求](project/readme.md)
  - [Jira](project/jira.md)
  - [PingCode](project/jira.md)

- [代码管理](code/readme.md)
  - [Gitlab](code/gitlab.md)
  - [Github](code/github.md)
  - [Gerrit](code/Gerrit.md)

- [测试安全扫描](test/readme.md)
  - [Jmeter](test/jmeter.md)
  - [SnoarQube](test/snoarqube.md)
  - [BlackDuck](test/blackduck.md)
  - [Fortify](test/fortify.md)

- [编译构建](makebuild/readme.md)
  - [Maven](makebuild/maven.md)
  - [Gradle](makebuild/gradle.md)
  - [Node](makebuild/node.md)
  - [Npm](makebuild/npm.md)
  - [Cargo](makebuild/cargo.md)

- [制品仓库](hub/readme.md)
  - [Harbor](hub/harbor.md)
  - [Nexus](hub/nexus.md)
  - [Jfrog artifactory](hub/jfrog.md)

- [自动化部署](autodeploy/readme.md)
  - [Ansible](autodeploy/ansible.md)
  - [ArgoCD](autodeploy/argocd.md)
  - [Helm](autodeploy/helm.md)
  - [Kustomize](autodeploy/kustomize.md)

- [日志监控链路](logmonitor/readme.md)
  - [EFK](logmonitor/efk.md)
  - [Prometheus](logmonitor/prometheus.md)
  - [Grafana](logmonitor/grafana.md)
  - [Loki](logmonitor/loki.md)
  - [Skywalking](logmonitor/skywalking.md)
  - [Jaeger](logmonitor/jadger.md)
  - [Pinpoint](logmonitor/pinpoint.md)

- [其他工具](others/readme.md)
  - [Rancher](others/rancher.md)
  - [Jumpserver](others/jumpserver.md)
  - [Nacos](others/nacos.md)
  - [Consul](others/consul.md)
  - [Trafik](others/apisix.md)
  - [Apisix](others/apisix.md)
  - [Terraform](others/terraform.md)
  - [Pulumi](others/pulumi.md)
  - [Valut](others/valut.md)

- [开发语言](language/readme.md)
  - [Shell](language/shell.md)
  - [Python](language/python.md)
  - [Golang](language/golang.md)

- [框架模块](framework/readme.md)
  - [Gin](framework/gin.md)
  - [Vue](framework/vue.md)
  - [React-antd](framework/antd.md)
  - [Django](framework/django.md)
  - [Bootstrap](framework/bootstrap.md)
  - [Swagger](framework/swagger.md)
  - [Postman](framework/postman.md)
  - [ApiPost7](framework/apipost7.md)
  - [RBAC](framework/rbac.md)
  - [JWT](framework/jwt.md)

- [XOPS](xops/xops.md)
  - [GitOps](xops/gitops.md)
  - [AiOps](xops/aiops.md)
  - [MLOps](xops/mlops.md)
  - [FinOps](xops/finops.md)
  - [DevSecOps](xops/devsecopsmd)
  - [DevDBOps](xops/devdbops.md)
  - [混沌工程](xops/hundun.md)
```

完成以上编写工作，只需要mdbook build,然后将book目录映射到nginx目录下，并配置虚拟主机即可，是不是很简单？

