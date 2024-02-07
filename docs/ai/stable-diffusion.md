# Stable Diffusion

## 安全

1. sd自带的登陆界面

使用参数，sd启动之后就会首先访问登陆界面，输入用户名和密码，才能进入到sd的主界面。
```
nohup ./webui.sh --gradio-auth username:password
```

2. 也可以使用nginx进行访问控制

配置nginx，设置访问密码

安装htpasswd

```
yum install -y httpd-tools
```

创建密码文件

```
htpasswd -c /etc/nginx/.htpasswd username
```

配置nginx

```
server {
    listen 80;
    server_name yourdomain.com;
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        auth_basic "Restricted Content";    # 提示信息
        auth_basic_user_file /etc/nginx/.htpasswd; # 存放密码文件的路径
    }
}
```

重启nginx

```
systemctl restart nginx
```

## 启动

1. 启动stable diffusion

```
nohup ./webui.sh -listen --enable-insecure-extension-access -xformers -no-half-vae &
```

-listen：是启动参数，用于指定stable diffusion的监听地址，默认是0.0.0.0。

-enable-insecure-extension-access：是启动参数，用于允许不安全的扩展（extension）的访问。

-xformers：是启动参数，用于启用transformer模型。

-no-half-vae：是启动参数，用于禁用半精度VAE模型。

2. 后台运行

nohup ./webui.sh -listen --enable-insecure-extension-access -xformers -no-half-vae &

&：是一个命令，用于将命令放入后台运行，即使终端关闭或断开连接，命令也会继续运行。
nohup：是一个命令，用于在运行命令时忽略 Hangup（挂起）信号，即使终端关闭或断开连接，也能保持命令继续运行。

webui.sh： 是stable diflusion的启动脚本。

tail -f nohup.out

tall： 用于显示文件的末尾内容。f：是"Yollw”的缩写，用于实时追踪文件的变化。

## 玩耍

1. 参数和对比

fp16（半精计算模式）、fp32（单精计算模式）
fp16 model（半精模型）、fp32 model（单精模型）
Pruned model(裁剪模型) 、 Full model (完整模型)

![](./assets/sd-parameter.jpg)

![](./assets/sd-parameter-compare.jpg)

## 插件

1. 修复脸崩手崩：

https://github.com/Bing-su/adetailer.git

2. 提示词自动翻译插件：

https://github.com/Physton/sd-webui-prompt-all-in-one

3. 汉化插件

双语插件
https://github.com/journey-ad/sd-webui-bilingual-Localization

中文语言包
https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN

## 源码和社区

1. Civitia源码：

https://github.com/civitai/civitai

How to use models：

https://github.com/civitai/civitai/wiki/How-to-use-models#lora

## 高级设置

1. 禁用GPU

```
./launch.py --disable-gpu
```

2. 禁用WebGL

```
./launch.py --disable-webgl
```

3. 禁用WebAssembly

```
./launch.py --disable-webassembly
```

4. 禁用WebGL2

```
./launch.py --disable-webgl2
```

5. 禁用WebAudio

```
./launch.py --disable-webaudio
```

6. 指定显卡

Stable Diffusion是一款强大的绘图工具，但在处理复杂的任务时，单张显卡可能会显得有些力不从心。通过利用多显卡，您可以轻松提高程序的加速性能，让您的创作更加高效。

```
export CUDA_VISIBLE_DEVICES=0,1  // 这将使Stable Diffusion使用编号为0和1的两张显卡来共同完成任务，从而加速处理过程。
export CUDA_VISIBLE_DEVICES=0,1,3,4,5,6,7  // 如果您想要排除一些显卡，只使用剩余的显卡设备，也是可行的。例如，如果您想排除第2号显卡，使用其他所有可用显卡
export CUDA_VISIBLE_DEVICES=0  // 这将使Stable Diffusion仅使用编号为0的显卡进行计算。这对于较小的任务可能足够了
```

设置CUDA_VISIBLE_DEVICES环境变量后，您只需运行Stable Diffusion的launch.py脚本，程序将会自动检测并使用您指定的显卡设备进行计算。这样，您就能够更充分地利用多显卡堆积的性能，加速绘图和其他计算任务。

通过利用多显卡堆积，您可以显著提高Stable Diffusion的性能，加速绘图和其他计算任务。这个简单的设置可以让您更高效地进行创作和实验，将Stable Diffusion的潜力充分发挥出来。


