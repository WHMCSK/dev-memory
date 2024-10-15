# IP_LAP

开源代码地址： https://github.com/Weizhi-Zhong/IP_LAP

## 安装依赖

```
conda create -n iplap Python 3.7.13
conda activate iplap
pip install torch torchvision torchaudio // 如果不行，就在官网查看安装命令https://pytorch.org/
pip install face-alignment==1.3.4
pip install -r requirements.txt
conda install ffmpeg
```

Download the pre-trained models from [OneDrive](https://onedrive.live.com/?id=625AA3DEDF6AE6A%21187017&resid=625AA3DEDF6AE6A%21187017&ithint=folder&authkey=%21ACAA8wggva04ZKU&cid=0625aa3dedf6ae6a) or [jianguoyun](https://www.jianguoyun.com/p/DeXpK34QgZ-EChjI9YcFIAA), and place them to the folder test/checkpoints . Then run the inference command.

预训练模型备份：

```
local_oss/IP_LAP/renderer_checkpoint.pth
local_oss/IP_LAP/landmarkgenerator_checkpoint.pth
```

The evaluation code is similar to [this repo](https://github.com/dc3ea9f/vico_challenge_baseline/tree/a282472ea99a1983ca2ce194665a51c2634a1416/evaluations).

## 推理

```
CUDA_VISIBLE_DEVICES=0 python inference_single.py # 测试

python inference_single.py --input './test/template_video/129.mp4' --audio './upload/t1.m4a' --landmark_gen_checkpoint_path './test/checkpoints/landmarkgenerator_checkpoint.pth'
```