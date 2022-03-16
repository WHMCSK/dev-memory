# windows下git的使用

首先介绍一下如何配置git的ssh key，以便我们可以用git方式下载源码

首先打开gitbash，如下都是在gitbash里面完成

首先用如下命令（如未特别说明，所有命令均默认在Git Bash工具下执行）检查一下用户名和邮箱是否配置（github支持我们用用户名或邮箱登录）：

```
git config --global  --list 
```

如未配置，则执行以下命令进行配置：

```
git config --global  user.name "这里换上你的用户名"
git config --global user.email "这里换上你的邮箱"
```

然后执行以下命令生成秘钥：

```
ssh-keygen -t rsa -C "这里换上你的邮箱"
```

执行命令后需要进行3次或4次确认：

1. 确认秘钥的保存路径（如果不需要改路径则直接回车）；
2. 如果上一步置顶的保存路径下已经有秘钥文件，则需要确认是否覆盖（如果之前的秘钥不再需要则直接回车覆盖，如需要则手动拷贝到其他目录后再覆盖）；
3. 创建密码（如果不需要密码则直接回车）；
4. 确认密码；

在指定的保存路径下会生成2个名为id_rsa和id_rsa.pub的文件，到此git就可以使用ssh连接了


## 问题一：Unable to negotiate with 47.98.**.** port 22: no matching host key type found. Their offer: ssh-rsa

环境 window10 + GIT  
用Git远程拉去项目  
报错Unable to negotiate with xx.xx.xx.xx port 22: no matching key exchange method found.  
Their offer:diffie-hellman-group1-sha1  

解决办法：  
在生成公钥的~/.ssh文件夹下，新建一个config文件（config文件没有后缀），文件中添加如下内容：  
Host *  
HostkeyAlgorithms +ssh-rsa  
PubkeyAcceptedKeyTypes +ssh-rsa  

然后保存即可。  
注意：xx.xx.xx.xx为服务器ip；+前面有一个空格！  
