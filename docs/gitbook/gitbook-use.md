# gitbook的使用

gitbook-cli是一个在同一系统上安装和使用多个版本的GitBook的实用程序。它将自动安装所需版本的GitBook来构建一本书。

打开终端输入npm install gitbook-cli -g命令进行全局安装：
```
npm install gitbook-cli -g

npm http fetch GET 304 https://registry.npm.taobao.org/os-tmpdir 100ms (from cache)
npm http fetch GET 304 https://registry.npm.taobao.org/os-homedir 113ms (from cache)
/usr/local/bin/gitbook -> /usr/local/lib/node_modules/gitbook-cli/bin/gitbook.js
+ gitbook-cli@2.3.2
added 578 packages from 672 contributors in 17.806s
```

安装成功后可使用gitbook --version来查看是否安装成功：
```
gitbook --version
CLI version: 2.3.2
GitBook version: 3.2.3
```

注意：终端第一次运行gitbook命令，可能会自动安装gitbook，因为刚才安装的是CLI，此时CLI会自动安装gitbook。

如果想卸载CLI，可使用npm uninstall gitbook-cli -g来删除。

### 初始化一本书

初始化一本书的命令是gitbook init,

首先在终端创建一个项目目录，并进入这个目录：
```
mkdir book
cd book
```

然后使用gitbook init来初始化一本书：
```
~ gitbook init

warn: no summary file in this book 
info: create README.md 
info: create SUMMARY.md 
info: initialization is finished
```

gitbook init会在空项目中创建README.md和SUMMARY.md两个文件：  
README.md文件是项目的介绍文件。  
SUMMARY.md是gitbook书籍的目录。  

如果SUMMARY.md文件里面有如下内容：
```
* [项目介绍](README.md)
* http
    * [http说明](doc/http/http解析.md)
        * [tcp说明](doc/http/tcp/tcp说明.md)
            * [udp说明](doc/http/tcp/udp/udp说明.md)
* HTML
    * [HTML5-特性说明](doc/html/HTML5-特性说明.md)
```

那么在使用gitbook init时，如果目录里面的文件不存在，则会创建目录中的文件：
```
~ gitbook init

info: create doc/http/http解析.md 
info: create doc/http/tcp/tcp说明.md 
info: create doc/http/tcp/udp/udp说明.md 
info: create doc/html/HTML5-特性说明.md 
info: create SUMMARY.md 
info: initialization is finished 
```

### 本地启动服务编写书籍

终端打开项目目录，使用gitbook serve启动服务：
```
~ gitbook serve

Live reload server started on port: 35729
Press CTRL+C to quit ...

info: 7 plugins are installed 
info: loading plugin "livereload"... OK 
……
info: loading plugin "theme-default"... OK 
info: found 5 pages 
info: found 0 asset files 
info: >> generation finished with success in 2.1s ! 

Starting server ...
Serving book on http://localhost:4000
```

然后根据终端的提示，在浏览器中打开http://localhost:4000查看书籍

### 文档打包

可使用gitbook build命令来生成最终的项目：

```
~ gitbook build

info: 7 plugins are installed 
info: 6 explicitly listed 
info: loading plugin "highlight"... OK 
info: loading plugin "search"... OK 
info: loading plugin "lunr"... OK 
info: loading plugin "sharing"... OK 
info: loading plugin "fontsettings"... OK 
info: loading plugin "theme-default"... OK 
info: found 5 pages 
info: found 0 asset files 
info: >> generation finished with success in 1.0s !
```

命令执行结束后，会在项目下生成_book的文件夹,此文件夹就是最终生成的项目。  

在_book文件夹里有一个index.html文件，这个文件就是文档网站的HTM入口，把_book文件夹复制到服务器，然后把web服务的入口引向index.html即可完成文档网站的部署。

如果你想查看输出目录详细的记录，可使用gitbook build ./ --log=debug --debug来构建查看。

### 生成电子书

这里本人试了，没有成功，你可以尝试一下

GitBook 可以生成一个网站，但也可以输出内容作为电子书（ePub，Mobi，PDF）。

```
# Generate a PDF file
$ gitbook pdf ./ ./mybook.pdf

# Generate an ePub file
$ gitbook epub ./ ./mybook.epub

# Generate a Mobi file
$ gitbook mobi ./ ./mybook.mobi
```

我还在网上找了一个包：[https://link.segmentfault.com/?enc=qz2PfAT36FMlnqn4qNJ63w%3D%3D.JsJCeUdls%2BuMW9HX%2F3OggufHaQFzJAipr17P6Mg99IezALbTYbKDr0MlP%2Bj%2FkZg6](https://link.segmentfault.com/?enc=qz2PfAT36FMlnqn4qNJ63w%3D%3D.JsJCeUdls%2BuMW9HX%2F3OggufHaQFzJAipr17P6Mg99IezALbTYbKDr0MlP%2Bj%2FkZg6)，可以试一下

