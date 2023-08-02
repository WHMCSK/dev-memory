# java tools

### jps 命令
一、概述

jps 是 Java Process Status Tool 的简称,它的作用是为了列出所有正在运行中的 Java 虚拟机进程

每一个 Java 程序在启动的时候都会为之创建一个 Jvm 实例,通过 jps 可以查看这些进程的相关信息

jps 是 Jdk 提供的一个工具,它安装在 JAVA_HOME/bin  下


二、常用 jps 命令参数

语法格式

jps [ options ] [ hostid ]

实际生产应用中不会去连接远程主机,hostid 这个一般不用

options 是对应的参数

| options 参数选项 |	作用 |
| --- | --- |
| -q | 只输出进程ID,省略主类的名称 |
| -m | 输出虚拟机进程启动时传递给主类 main() 方法的参数 | 
| -l | 输出主类的名称,如果进程执行的是 JAR 包,则输出 JAR 文件的路径 |
| -v | 输出虚拟机进程启动时的 JVM 参数 |