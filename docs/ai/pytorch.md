# PyTorch

## 安装

我的苹果电脑是Intel版本，无法使用cuda

```
pip3 install torch torchvision torchaudio
```

做张量变换的时候，有时候用到的参数“-1”，是什么意思？

例如：

```
    t = torch.randperm(8)
    t_reshape = torch.reshape(t, (-1, 2, 2))    # -1
    print("t:{}\nt_reshape:\n{}".format(t, t_reshape))
```

这里用-1代表任意长度，其值等于总长度除以其他维度上的长度。这里-1等同于2.

