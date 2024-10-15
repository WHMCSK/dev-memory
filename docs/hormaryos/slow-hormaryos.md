# 鸿蒙开发进程跟不上，导致一些问题，例如新发布的api9，开发的程序在很多机型上卡到无法使用

## 槽点

* arkui开发的鸿蒙app为什么真机调试点不动？


网友支招：

1. 可以用 scrcpy 投屏操作,官方地址：https://github.com/Genymobile/scrcpy
2. 或者启用开发人员选项中的”显示面（surface）更新“，但容易闪花了老眼


* 解决使用真机开发Harmony OS 4.0版本运行 ArkUI demo运行非常卡顿，黑屏

网友支招：

解决办法

1. 购买真机Mate60 ,Mate50,Mate40 Pro，这些已知机型不卡
2. 用DevEco Studio里自带云真机，选择API9空闲的真机调试
3. 还有一种临时解决办法：打开开发者

```
1.停用HW叠加层 – 打开
2.设置GPU渲染程序 – 选择OpenGL(Skia)
3.显示面（surface）更新（注意：会闪瞎钛合金狗眼，打开这个非常流畅，可以不打开）
设置后可以正常打开，虽然卡顿和黑屏没了，但是还是不流畅。
```

## 推荐解决办法

使用真机投屏工具进行交互操作

这里，我们可以使用scrcpy这个工具，投屏之后在电脑上进行操作。

安装ADB工具

```
brew install android-platform-tools
```

安装

```
brew install scrcpy
```

启动scrcpy

```
scrcpy
scrcpy --no-audio --record=file.mkv
scrcpy --help
man scrcpy
```