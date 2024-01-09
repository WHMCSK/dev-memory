# Python包和模块

## 内建包和模块

```
import builtins
print(dir(builtins)) # 查看所有内建包和模块
```

## 导入多个模块

```
import os, os.path, matplotlib.pyplot as plt
```


## 别名

还可以这么玩

```
if file_extension = 'txt':
    import txt_parse as p
elif file _extension == "doc" 
    import doc_parse as p
p.open()
p.read()
p.close()
```

## 导入包

如果没有在包里面的“__init__.py“文件导入模块，那么在包外面直接使用"import 包"，则不会导入包里面的任何模块，尝试"包.模块"的用法会报错，找不到模块。应该怎么做呢？

假设包名为a,里面有模块tools

a包里面的__init__.py

```
import a.tools # 注意，这里必须是import a.tools，而不能是import tools，某则会报错找不到tools。
```

然后在包外面的模块b，使用"import a"导入包，才能使用“a.tools.成员”的方式来引用。

当然，还可以用另外一种方式，就是在包外面的模块不仅仅导入包，直接导入到模块“import a.tools”，那么就可以直接使用a.tools.成员了。

## import导入包和from import导入模块

使用import导入包，会导入包里面的所有模块和对象，而使用from import则只导入指定包里面的指定模块或者只导入指定模块六面的指定对象.

from import后面的必须最简化

```
from p1 import subp.sub_xxx # 会报语法错误
from p1.subp import sub_xxx # from import后面的必须最简化，这个才是对的
```
可以这么理解，在p1里面能看到subp，但是看不到subp里面的东西，只有在subp里面才能看到subp里面这些模块。


## Python模块打包发布

文档网址：

https://python-packaging.readthedocs.io/en/latest/

1. 在https://pypi.org注册账号
2. 环境准备

    * setuptools安装
    * pip安装
    * wheel安装
    * twine安装

```
pip install wheel # 使用pip安装
python3 -m pip install wheel # 使用python3使用-m参数指定后面的pip install wheel是以脚本的形式执行
```

3. 发布前的准备

项目结构

```
项目名称
    包名称
        __init__.py
        模块
    模块
    setup.py
    README.rst
    LICENSE.txt
    MANIFEST.in
```
注意：
在包中__init__.py中使用"from . import szlibon"导入包里面的其他模块.

4. 发布

4.1 安装twine

```
pip install twine
```

4.2 配置twine使用的pypi账户

在自己的用户目录下新建一个空白文件命名为.pypirc，内容如下：
```
[distutils]
  index-servers =
    pypi

[pypi]
  repository: <repository-url> # 这个行前面貌似得有两个空格
  username: <username>
  password: <password>
```

4.3 进入到要发布的包目录，输入：

```
python setup.py sdist   # 打包
twine upload dist/*     # 上传
```

如上三步即可发布成功。