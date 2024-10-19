# Consul Introduction

## consul的启动与关闭

前台启动命令如下：（前台运行）

```
consul agent -dev
```

浏览器访问：http://localhost:8500。  
如上这种方式是以前台进行的启动，那么相应的只需要 ctrl + c 即可关闭 consul。  

后台启动命令如下，部分参数根据自己情况修改：(后台运行)

```
consul agent -server -ui -bootstrap-expect=1 -client=0.0.0.0 -bind 你的ip地址 -data-dir=/状态数据存储文件夹/data >> /日志记录文件夹/logs/consul.log &
```

* bind：绑定的内部通讯地址，默认0.0.0.0，即所有的本地地址，也可以改为自己的ip地址。
* data-dir：状态数据存储用的文件目录。
简单说一下这两条命令，其他参数参考后面标题3给出的解释。
命令执行参考：

```
consul agent -server -ui -bootstrap-expect=1 -client=0.0.0.0 -bind 192.168.0.174 -data-dir=/Users/jiajunguo/data/consul >> /Users/jiajunguo/logs/consul/consul.log &
```

关闭命令：如图所示，一般执行完就给出 PID 了，直接 kill 掉就可以了。

```
kill -9 21314
```

如果没有给出怎么办？

```
查看端口占用情况：lsof -i :8500
```

搜出来的 PID 结果直接 kill 即可。