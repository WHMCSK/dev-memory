# 安装jupyter notebook

### 安装notebook
```
conda install notebook
```

### 安装扩展包
```
conda install -c conda-forge jupyter_contrib_nbextensions jupyterlab ipywidgets ipykernel
```

 * ipywidgets：进度条扩展ipywidgets
 * ipykernel：这个软件包将允许JupyterNotebook使用特定环境的Python版本

### 安装ipykernel

在该环境中安装ipykernel软件包。这个软件包将允许JupyterNotebook使用特定环境的Python版本。运行以下命令：

```
conda install ipykernel
```

将该环境添加到JupyterNotebook中。运行以下命令：

```
#这里的env_name替换成需要使用的虚拟环境名称
python -m ipykernel install --user --name=chatglm3 --display-name="Python(chatglm3)"
python -m ipykernel install --user --name=dbgpt --display-name="Python(dbgpt)"
```

另外删除kernel环境：

```
jupyter kernelspec remove 环境名称
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

### Jupyterlab4.0来了

Jupyter 贡献者社区自豪地宣布 JupyterLab 4.0，这是我们功能齐全的开发环境的下一个主要版本。该软件包现在可在 PyPI 和 conda-forge 上使用。您可以通过运行

```
pip install --upgrade jupyterlab
```

或升级

```
conda install -c conda-forge jupyterlab
```

[JupyterLab 文档](https://jupyterlab.readthedocs.io/en/latest/index.html)已经更新了。

### 常见问题

- NotebookApp] Blocking Cross Origin API request for /api/contents. Origin: http://xx/xx/xx/xx:123546, Host: 172.20.25.164

解决方法：

打开jupyter_notebook_config.py文件

找到c.NotebookApp.allow_origin = ' '将' '改为‘*’

保存退出 重新启动jupyter 成功
