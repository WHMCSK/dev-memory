# 安装jupyter notebook

### 安装notebook
```
conda install notebook
```

### 安装扩展包
```
conda install -c conda-forge jupyter_contrib_nbextensions jupyterlab
```

安装进度条扩展ipywidgets
```
conda install ipywidgets
```

### 启动jupyter

```
jupyter notebook
```

### 常规操作

配置jupyter notebook密码：

```
jupyter notebook password
```

启动jupyterlab：

```
jupyter lab
```

打开浏览器，输入`http://localhost:8888`访问jupyterlab。

### 配置文件

配置文件路径：
```
~/.jupyter/jupyter_notebook_config.py
```

如果没有找到该文件，或者之前没有进行配置，可通过jupyter notebook --generate-config命令创建配置文件。

```
jupyter notebook --generate-config
```

### 常见问题

- NotebookApp] Blocking Cross Origin API request for /api/contents. Origin: http://xx/xx/xx/xx:123546, Host: 172.20.25.164

解决方法：

打开jupyter_notebook_config.py文件

找到c.NotebookApp.allow_origin = ' '将' '改为‘*’

保存退出 重新启动jupyter 成功