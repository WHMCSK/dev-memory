# Docker Desktop 4.18 发布，带来了大量新特性

最新版 Docker Desktop 4.18 带来了大量的新功能，包括漏洞快速查看、漏洞修复建议和 Docker Scout 的镜像比较、稳定的 Container File Explorer、快速将 Docker 添加到项目中的 init 命令，以及实验性的用于监控项目内部变化的 Compose File Watch。

在 4.17 版中引入的 Docker Scout 目前仅对 Docker Pro、Team 或 Business 订阅版本可用，通过分析镜像内容并使用 docker scout cves 命令列出所有已知的 CVE 来了解容器镜像的安全性。

Docker Desktop 4.18 现在能够提供关于如何修复已知 CVE 的建议。这可以通过运行 docker scout recommendations 命令来实现，这个命令将提示新的基础镜像的可用性，并列出它将带来哪些好处。此外，Scout 还提供了一个新的 docker scout quickview 命令，它可以列出镜像中发现的所有问题，包括其基础镜像，并按严重程度进行分组。

Docker Scout 还带来了一个新的实验性功能，让镜像的比较和记录为了解决镜像的漏洞而做出了哪些变更变得更加容易。使用 docker scout compare 命令生成的报告中包含了在基础镜像中找到的 CVE 的摘要，以及所有添加、删除或更新的包的清单。

Docker Desktop 4.18 还提供了一个新的 CLI 命令 docker init（处于 Beta 测试阶段），用它可以方便地创建将 Docker 添加到现有项目中所需的所有文件，包括 Dockerfiles、Compose files 和.dockerignore。目前，docker init 支持 Go 语言项目，但 Docker 开发团队也正在努力增加对 Node.js、Python、Rust 和其他语言的支持。

除了命令行，Docker Desktop 还提供了一个新的 GUI 工具 Container File Explorer 来简化容器文件的检查或删除任务。开发人员可以用它检查容器文件系统，拖放文件和文件夹，编辑和删除文件。对于没有提供 shell 的运行中的容器，这个新工具就特别有用。

关于 Docker Desktop 4.18 最后值得一提的是，它提供了一个新的 Compose 配置选项，可以在修改服务的同时保持服务的最新状态。还处于实验阶段的 Compose File Watch 提供了一个新的监视服务，可以通过 docker compose alpha watch 命令来运行。

服务的行为可以通过 compose.yaml 中的 x-develop 部分来控制。这部分内容指定了在给定目标发生变更时需要执行的动作。例如：



x-develop:watch:- action: syncpath: ./webtarget: /app/web- action: rebuildpath: .package.json
上面的代码片段将使 Compose 自动同步./web 目录下的任何变更，并基于 package.json 的变更重新构建镜像。

要了解 Docker Desktop 4.18 所有的变更，请查看官方的发布说明。

https://www.infoq.com/news/2023/04/docker-4-18-released/

如何检查 Docker 镜像是否存在漏洞 (https://www.infoq.cn/article/Z8128Ope7MVzfAgLNH9F )

Docker+Wasm 第 2 个技术预览版发布，新增 3 个运行时引擎支持 (https://www.infoq.cn/article/1WdmawdEDTcLLLdwq7tg )