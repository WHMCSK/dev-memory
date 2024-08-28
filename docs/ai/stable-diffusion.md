# Stable Diffusion

## 安装环境依赖

```
sudo apt-get install google-perftools
pip install modelscope xformers insightface 
```

## 安全

1. sd自带的登陆界面

使用参数，sd启动之后就会首先访问登陆界面，输入用户名和密码，才能进入到sd的主界面。

```
nohup ./webui.sh --enable-insecure-extension-access --xformers --gradio-auth username:password
nohup ./webui.sh --enable-insecure-extension-access --gradio-auth username:password
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

* 双语插件
https://github.com/journey-ad/sd-webui-bilingual-Localization

* 中文语言包
https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN

4. 图片裁剪插件：

https://github.com/Physton/sd-webui-image-cropper

5. 图片旋转插件：

https://github.com/Physton/sd-webui-image-rotate

6. 图片缩放插件：

https://github.com/Physton/sd-webui-image-zoom

7. 图片翻转插件：

https://github.com/Physton/sd-webui-image-flip

8. 图片滤镜插件：

https://github.com/Physton/sd-webui-image-filter

9. 图片美化插件：

https://github.com/Physton/sd-webui-image-beautify

10. 图片背景替换插件：

https://github.com/Physton/sd-webui-image-background-replace

11. 擦除插件：
https://github.com/Physton/sd-webui-eraser

12. 图片清理插件：
https://github.com/novitalabs/sd-webui-cleaner

13. Civitai插件

https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper#civitai-api-key

14. AnimateDiff

AnimateDiff提示词动画

使用动词可以驱动anime，例如walking、running、dancing、jumping、swimming、eating、drinking、talking、reading、writing、listening、playing、cooking、working、relaxing、sleeping、working out、exercising、reading books、painting、painting portraits、painting landscapes、painting sculptures、painting architecture、painting animals、painting monsters、painting fantasy、painting abstract、painting cityscapes、painting landmarks、painting landscapes、painting architecture、painting animals


```
masterpiece,best quality,(photorealistic:1.1),(detailed:1.2),a lady,walking,(cyborg:1.1),(abstract,science fiction,cyberpunk,alternate reality,vivid colors,neon lights:1.1),full body,skinny,large breasts,mechanical parts,cyberwear,short hair,blue eyes,<lora:add_detail:0.8>,(4dsh4t4r4n:0.8),armo
```

```
Best quality,masterpiece,ultra high res,(photorealistic:1.2),raw photo,1girl,(smile:0.6),medium chest,running in the street,city streets in los angeles,solo,navel,short hair,(white tight_pants:1.1),black hair,realistic,looking at viewer,
```

```
(masterpiece,best quality,hires,high resolution:1.2),extremely detailed,realistic,intricate details,highres,1girl,solo,light smile,blush,black hair,Top Knot with Accessories,(sunlight,cinematic lighting,perfect lighting,bloom),looking at viewer,neon light,stage lighting,brisk step,(waltz dance:1.2),ballroom,stage,(high_heels:1.2),thighhighs,lace-trimmed_dress,
```

```
masterpiece,best quality,realistic,hand painted textures,intricate details,medieval,China Great Wall,2 ancient sexy Chinese warriors holding bronze spear,kung_fu,jumping,(fightting with each other:1.2),combat boots,wind,trees,<lora:more_details:0.8>,(smoke arround background:1.1),winter,
```

AnimateDiff提示词游历(Prompt Travel)

Prompt Travel提示词游历语法：

```
帧数1: 提示词1,
帧数2: 提示词2,
```

如果生成的时候日志显示"You are using prompt travel"，就代表提示词游历语法激活了。

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


## 训练准备

1. 准备图片
2. 打标
3. 训练模型
4. 导出模型
5. 导入模型


高质量的图片和打标非常重要，一般准备20-50张图片，每张图片至少要标注5个关键点，并保证关键点的准确性。如果想要训练更精细，一般最多100张图片，每张图片至少要标注10个关键点。
一定要注意质量大于数量，因为不好的图片可能干扰学习，最后的结果可能不是AI学会了，而是学废了。

原始图片要求：

1. 要求不太精细的，准备20到50张。要求很精细的，准备100张。
2. 要求清晰的，不要出现模糊的，光线不好的
3. 不要太小的，太大的图片，大的不要超过1000x1000，小的不要小于100x100。
4. 要求背景干净的，不要出现有其他物体的图片。
5. 要求没有噪声的，不要出现光线不均匀的，反光的，雾霾的图片。
6. 要求没有遮挡的，不要出现被其他物体遮挡的图片，脸部不要被遮挡。
7. 要求没有过多的背景，不要出现太多的背景，影响关键点的识别。
8. 不能是动作扭曲的，不要出现头部抬起，手指乱动的图片。
9. 不能是带有血迹的，不要出现血腥的，恐怖的，暴力的图片。
10. 不能是带有刺绣的，不要出现刺绣的图片。
11. 图片不要太杂乱，不要出现一张图片有多个人。
12. 图片不要太杂乱，不要出现一张图片有多个场景。
13. 图片不要太杂乱，不要出现一张图片有多个背景。
14. 图片不要太杂乱，不要出现一张图片有多个角度。
15. 不要有太多同一个角度，同一个表情的图片，尤其在张数少的情况下，训练出来的Lora会有人物表情僵直的问题
16. 最好能有面孔多角度，不同光影，不同表情，不同服装配件，让模型能够涵盖较多的情况。

图片裁剪要求：

1. 如果是StableDiffusion1.*版本，建议裁剪成512x512大小。
2. 如果是StableDiffusion2.*版本，图片的尺寸至少是768x768，建议裁剪成1024x1024大小。
3. 裁剪时，建议不要裁剪太多，不要裁剪太小，否则会影响关键点的识别。
4. 图片裁剪的时候选择创建镜像副本，它可以将图片翻转，增加一倍的图片，这样使数据集也更加丰富一些，而且使人物左右两侧达到均衡。

可以用这个网站做图片裁剪： https://www.iloveimg.com/crop-image， https://www.birme.net

标注工具：

为图片打标，我们需要用到两个插件工具：

* Tagger
* dataset tag editor

Tagger打标，是根据图片内容识别出提示词，并放到和图片同名的txt文件中。

dataset tag editor，是用来编辑标签的。一般会用到批量删除重复词、删除选中词汇功能。对于需要保留的特征，标签需要删掉，比如属于人物特征的眼睛、嘴巴、鼻子、眉毛、头发长度等，代表人物本身属性的是要绑定到人物身上的，就要把这些tag删掉。可改变部分的tag就需要保留，比如背景、衣服、头发、配饰等。

屏蔽VAE文件：

有些人推荐训练角色的时候要屏蔽掉VAE文件，说是如果训练的时候不屏蔽掉VAE文件的话很容易出现问题，这个道理我暂时还没深究：

如何屏蔽VAE文件：

1. 在设置里面找到训练选项卡，把“训练时将 VAE 和 CLIP 从显存(VRAM)移放到内存(RAM)如果可行的话，节省显存(VRAM)Move VAE and CLIP to RAM when training if possible. Saves VRAM.”这一项的勾选去掉。
2. 将VAE文件暂时移动到别的地方，训练完模型之后再移动回来。

训练模型：

1. 训练模型之前，需要安装好tensorflow，keras，opencv等库。
2. 训练模型之前，需要准备好训练数据，包括图片和标注文件。
3. 训练模型之前，需要修改配置文件，主要修改的是训练参数，比如batch_size，epochs等。
4. 训练模型之前，需要修改模型参数，比如模型的大小，激活函数等。
5. 训练模型之前，需要修改训练脚本，主要修改的是训练数据的路径，模型的保存路径等。
6. 训练模型之前，需要修改数据预处理脚本，主要修改的是图片的大小，数据增强等。
7. 训练模型之前，需要修改模型结构，主要修改的是网络结构，比如添加卷积层，池化层等。
8. 训练模型之前，需要修改损失函数，主要修改的是损失函数的选择，比如分类损失函数，回归损失函数等。
9. 训练模型之前，需要修改优化器，主要修改的是优化器的选择，比如Adam，SGD等。
10. 训练模型之前，需要修改评估函数，主要修改的是评估函数的选择，比如准确率，损失函数等。
11. 训练模型之前，需要修改训练数据，主要修改的是训练数据，比如图片的大小，数据增强等。
12. 训练模型之前，需要修改训练脚本，主要修改的是训练数据的路径，模型的保存路径等。

## Embedding训练

Embeddings的训练大约需要消耗8~10G左右的显存

1. 创建Embedding文件
2. 设置训练参数
3. 训练Embedding

参数配置：

Prompt template：

* 人物角色：subject_filewords.txt

## LoRA训练

而LoRA训练在最低6GB的设备上也可以进行

目前最流行的LoRA训练项目框架：https://github.com/bmaltais/kohya_ss

Run the gui with:
```
./gui.sh --share --headless
./gui.sh --username USERNAME --password PASSWORD --share --headless  // 开启用户名密码登陆
```

or with this if you expose 7860 directly via the runpod configuration
```
./gui.sh --listen=0.0.0.0 --headless
```



## 提示词

提示词分为：正向提示词、反向提示词

### 正向提示词

正向提示词由多个词缀构成

类型： 英文、数字、符号、emoji
语法：单词、短句
语序：画面质量,主要元素,细节

* 画面质量：风格镜头灯光主体构图
* 主要元素：人物动物事物人物动物事物
* 细节：场景环境细小元素其他提示词

正向提示词语序语序详细划分：

1. 概念

* 图像质量：高细节、高分辨率、超写实主义、HD、8K、16K、高品质等
* 风格：卡通、贴纸、漫画、印象、肖像、像素、新成海、赛博朋克
* 镜头：鱼眼、DSLR、360全景、长焦镜头、超广角、移轴效果、景深、微距等
* 灯光：工作室、电影照明、美丽的灯光、柔光、逆光、人物发光、侧光、云隙光等
* 构图：中心、水平、垂直、三分法、对称法、对角线、框架、重复构图等

2. 主体

* 人物：武士、护士、魔法师、美少女战士、男人、女人、女孩、男孩、兔女郎、特定人物等
* 动物：猴子、鸡、狗、兔、十二生肖、怪兽、鱼、老鼠、鸟、鸭、鹅等
* 事物：瓶子、伞、武器、背包、墨镜、手机、电脑、工具等
* 风景：天空、森林、海洋、山、水、花、道路桥梁等
* 姿态：站立、坐、行走、奔跑、跳跃、半蹲、抬头、回身、侧卧、手放身后、二郎腿等
* 服装：短袖、长衫、连衣裙、长袍、短裤、丝袜、手套、吊带、牛仔裤、围巾、高跟鞋等
* 道具：帽子、眼镜、武器、手环、手链、项链、耳坠、耳环等

3. 细节

* 场景：室内 室外 客厅 餐厅 咖啡店 酒吧 幻想场景等
* 环境：晴天、雨天、阴天、春、夏、秋、冬、白天、傍晚、夜晚等
* 细小元素：表情、妆容、发簪、雷、电、水、火等不影响整体构图的元素

### 更好的控制细节

Stable diffusion提供了一些特株的符号来帮助我们更加精确的的控制图像扩散的过程。我们把这些符号分为四类：

1. 分割符号：

./!?%^*;:=`~换行空格

这些符号都有同样的作用，权重排序的作用，分割符号前权重高分割符号后权重低，但是一般情况下我们都使用逗号和换行，便于修改和避免造成提示词相互污染的情况。

2. 权重符号：

()、{}、[]、(:)

（提示词）= 提示词×1.1
｛提示词｝=提示词×1.05
［提示词］=提示词×0.9
（提示词：1.2）= 提示词×1.2

* 圆括号表示括号内提示词权重乘以1.1
* 花括号表示括号类提示词权重乘以1.05
* 方括号表示括号类提示词权重乘以0.9
* 原括号加冒号表示自定义权重

权重符号全部可以叠加使用

* （（提示词））= 提示词×1.1*1.1
* ｛｛提示词｝｝=提示词×1.05*1.05
* ［［提示词］］= 提示词×0.9*0.9
* （（提示词：1.2））=提示词×1.2*1.2

注意：当我们希望某一个提示词能够在结果中出现更多的元素，就可以使用权重符号。但是权重符号一旦超过1.5之后，可能就会出现图片崩坏的情況，所以权重的安全值范围一般在1.5以下。

3. 连接符号

* +_：并列权重，连接符号前后提示词的权重
* ｜：循环竖线前后提示词影响扩散效果，例如：提示词1｜提示词2，迭代步数第1.3.5.提示词1生效，迭代步数第2.4.6...提示词2生效
* AND：大写的AND，前后需加上空格。对按的前后提示词产生融合效果，概率融合，和其它参数算法有关

4. 分步扩散符号

* 比如在方括号里使用冒号，可以指定提示词在指定的步数开始生效
* 而在方括号里使用双冒号，则可以使提示词在指定的步数停止生效
* 如果在方括号里加上两个提示词，那么则可以同时控制两个提示词，影响扩散过程的步数
* 也可以在方括号内加上竖线，达到循环影响单独词缀的扩散结果

正向提示词［狗：13］，花，女孩，

方括号内狗这个词缀元素从13步开始出现并影响图像扩散13步之前是均没有出现狗元素直到最终狗头结果

正向提示词［狗：13］，花，女孩

方括号内狗这个词缀元素从13步停止影响图像扩散13步之前都有狗元素但是随着停止影响狗元素最后消失

正向提示词［狗：书：13］，花，女孩

13步前狗元素生效，13步后书元素生效

正向提示词［红|蓝］头发，女孩

红元素与蓝元素循环生效扩散达到渐变色头发的结果

## 相关链接

1. colab训练链接：https://github.com/Linaqruf/kohya-trainer 
2. 训练集标签编辑器：https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor 
3. 批量调整图片尺寸：https://www.birme.net/?target_width=512&target_height=512 
4. 批量调整图片格式：https://www.wdku.net/image/imageformat  

## SD使用相关链接

1. 使用Colab 搭建Stable Diffusion的链接： https://github.com/camenduru/stable-diffusion-webui-colab 
2. 使用Colab 搭建Stable Diffusion的教程： https://www.youtube.com/watch?v=u6LWc1y4e0Y&t=3s 
3. 模型下载网站：https://civitai.com/ 
4. Colab + google drive 云端安装stable diffusion 教程：https://youtu.be/0PZtgkeqAQE  

## SD相关视频

1. 用Colab一键免费搭建AI画图神器Stable Diffusion，无限出图，白嫖google GPU，无电脑配置和显卡要求 https://www.youtube.com/watch?v=u6LWc1y4e0Y&t=18s 
2. Checkpoint + Lora 模型使用教程, Stable Diffusion 4种训练模型的介绍，使用 MeinaMix 动漫风格模型+ hanfu Lora 制作动漫汉服小姐姐 https://www.youtube.com/watch?v=MOOWFHCPb2k&t=1s 
3. 20种 Sampling method 采样方法详解，直接出图对比 Stable Diffusion中哪个采样器最好？我的建议是... https://www.youtube.com/watch?v=b8thoOFfy7E 
4. AI绘图-使用 Inpaint & Extras 让画质大幅提升|高清修复4K美图|stable diffusion img2img图生图 + Inpaint + Extras 让AI好朋友效果惊艳 https://www.youtube.com/watch?v=tXACCyDMXEM 
5. AI动画制作，gif2gif 快速生成风格化动图｜stable diffusion 教程｜让AI人物动起来｜插件安装 & 视频教程｜denoising strength 设置建议 https://www.youtube.com/watch?v=t-SdEHFQJa8 
6. 将Stable diffusion 安装到Google drive云端教程，免费GPU无限跑图，随时随地运行｜Google colab｜AI绘图攻略｜免费硬盘 免费GPU https://youtu.be/0PZtgkeqAQE 
7. Stable diffusion AI视频制作，Controlnet + mov2mov 准确控制动作，画面丝滑，让AI老婆动起来，效果真不错｜视频教程｜AI跳舞｜AI换装｜视频生视频｜图生图 https://youtu.be/U0JFVZWf8Is 
8. Controlnet 1.1新版本功能详解，14个控制模型+30个预处理器讲解，Stable diffusion AI绘图教程｜Preprocessor使用教程｜我的使用建议｜文生图｜图生图｜插件下载 https://www.youtube.com/watch?v=c8ZyBBHFoUI  # Short： 欣赏AI老婆跳舞，视频由stable diffusion制作 https://youtube.com/shorts/HU9jdD7x1o0?feature=share  

## GPT相关视频

1. 我用Auto GPT自动开发了个网站，结果么... Auto GPT实测｜无需人类插手｜自动完成任务｜自动化AI｜GPT3.5｜GPT4｜ https://www.youtube.com/watch?v=LxrhPAYhb4A