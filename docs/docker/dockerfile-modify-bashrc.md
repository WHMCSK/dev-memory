# 如何在dockerfile加载修改的.bashrc

我在 Dockerfile 中的 .bashrc 中添加了很多东西，这是执行一些我想稍后在 Dockerfile 中运行的命令所必需的，
我厌倦了source .bashrc它不起作用。

我尝试使用，RUN /bin/bash -c --login ...但出现错误：mesg: ttyname failed: inappropriate ioctl for device

Dockerfile 中的每个命令都会创建一个新的临时容器，但没有 tty（issue 1870，在PR 4955 中讨论，但已关闭以支持PR 4882）。

在 docker 构建期间缺少 tty 会触发ttyname failed: inappropriate ioctl for device错误消息。

您可以尝试运行一个包装脚本，该脚本将在其中获取.bashrc.

Dockerfile：
```
COPY myscript /path/to/myscript
RUN /path/to/myscript
```

myscript：

```
#!/bin/bash
source /path/to/.bashrc
# rest of the commands  
```

直接RUN或者使用/bin/bash命令执行source，只能保证当前这条bash进程内有效，当bash进程销毁，source的命令无效

#RUN echo "source /etc/profile" >> ~/.bashrc   （使用这个命令只能保证，通过执行shell命令的程序才生效）

在Dockerfile文件使用ENV命令声明成全局环境变量

ENV JAVA_HOME="/data/jdk1.8.0_221"

在Dockerfile的entrypoint.sh中执行source ~/.bashrc的目的是为了使容器内的环境变量能够被正确设置和加载。

在Linux系统中，当用户登录时，系统会自动读取用户主目录下的.bashrc文件，该文件包含了一些常用的环境变量和别名等配置信息，例如PATH变量等。然而，在容器内运行时，由于用户没有进行登录操作，因此系统不会自动加载.bashrc文件。如果在容器内执行某些需要使用环境变量的操作时，这些变量可能未被正确设置，导致出现错误。

为了解决这个问题，可以在entrypoint.sh中执行source ~/.bashrc命令，以加载.bashrc文件中的环境变量和别名等配置信息。这样，容器内的操作就能够正确地使用这些环境变量了。

需要注意的是，如果您在构建镜像时没有安装bash或.bashrc文件不存在，那么执行source ~/.bashrc命令将会失败。在这种情况下，您可以考虑在entrypoint.sh文件中手动设置需要的环境变量，而不是依赖于.bashrc文件。
