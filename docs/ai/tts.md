# 文本转语音行情和概述

## 免费工具

1. [文本转语音](https://logspot.hocgin.top/addone-speak-text/?active=home) https://logspot.hocgin.top/网站收录的免费工具，可以直接在线转换文本到语音，形态：Edge、Chrome、微信小程序。
2. [顶伯在线网站](http://www.shdbtool.com/#/Azuretts) http://www.shdbtool.com/#/，在线试听下载
3. [语音合成](https://www.ivsky.com/sousuon/yuyinhecheng) https://www.ivsky.com/网站收录的免费工具，可以直接在线合成语音。
4. [语音识别](https://www.ivsky.com/sousuon/yuyinshibie) https://www.ivsky.com/网站收录的免费工具，可以直接在线识别语音。

## 付费工具

1. [Google Text-to-Speech](https://www.google.com/intl/en/chrome/demos/speech.html)
2. [Microsoft Speech API](https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/)
3. [Alibaba Cloud Text-to-Speech](https://www.alibabacloud.com/product/tts)
4. [Wit.ai Text-to-Speech](https://wit.ai/docs/http/20160330#post-speech)
5. [IBM Watson Text-to-Speech](https://www.ibm.com/watson/services/text-to-speech/)
6. [DeepL Translate](https://www.deepl.com/en/translator)


## 公有云服务

讯飞： 

上海话语音合成试听页面： https://peiyin.xunfei.cn/make?speakerNo=130032  
AI配音主播列表： https://peiyin.xunfei.cn/tts/anchor  

## 免费数据集

https://www.openslr.org/resources.php

https://magichub.com/datasets/

1.SLR18-THCHS-30

THCHS30是一个很经典的中文语音数据集了，包含了1万余条语音文件，大约40小时的中文语音数据，内容以文章诗句为主，全部为女声。它是由清华大学语音与语言技术中心（CSLT）出版的开放式中文语音数据库。原创录音于2002年由朱晓燕教授在清华大学计算机科学系智能与系统重点实验室监督下进行，原名为“TCMSD”，代表“清华连续”普通话语音数据库’。13年后的出版由王东博士发起，并得到了朱晓燕教授的支持。他们希望为语音识别领域的新入门的研究人员提供玩具级别的数据库，因此，数据库对学术用户完全免费。

2.SLR33 Aishell

AISHELL是由北京希尔公司发布的一个中文语音数据集，其中包含约178小时的开源版数据。该数据集包含400个来自中国不同地区、具有不同的口音的人的声音。录音是在安静的室内环境中使用高保真麦克风进行录音，并采样降至16kHz。通过专业的语音注释和严格的质量检查，手动转录准确率达到95％以上。该数据免费供学术使用。他们希望为语音识别领域的新研究人员提供适量的数据。

3.SLR38 ST-CMDS

ST-CMDS是由一个AI数据公司发布的中文语音数据集，包含10万余条语音文件，大约100余小时的语音数据。数据内容以平时的网上语音聊天和智能语音控制语句为主，855个不同说话者，同时有男声和女声，适合多种场景下使用。

4.SLR47 Primewords Chinese Corpus Set 1

Primewords包含了大约100小时的中文语音数据，这个免费的中文普通话语料库由上海普力信息技术有限公司发布。语料库由296名母语为英语的智能手机录制。转录准确度大于98％，置信水平为95％，学术用途免费。抄本和话语之间的映射以JSON格式给出。

5.SLR68 magicdata

Magic Data技术有限公司的语料库，语料库包含755小时的语音数据，其主要是移动终端的录音数据。邀请来自中国不同重点区域的1080名演讲者参与录制。句子转录准确率高于98％。录音在安静的室内环境中进行。数据库分为训练集，验证集和测试集，比例为51：1：2。诸如语音数据编码和说话者信息的细节信息被保存在元数据文件中。录音文本领域多样化，包括互动问答，音乐搜索，SNS信息，家庭指挥和控制等。还提供了分段的成绩单。该语料库旨在支持语音识别，机器翻译，说话人识别和其他语音相关领域的研究人员。因此，语料库完全免费用于学术用途。

6. ASR-SCSHHIDIADUSC: A SCRIPTED CHINESE SHANGHAI DIALECT DAILY-USE SPEECH CORPUS

下载页面： https://magichub.com/datasets/shanghai-dialect-scripted-speech-corpus-daily-use-sentence/


## 相关产品/公司

希尔贝壳 https://www.aishelltech.com/ ， 提供免费的中文普通话数据集下载和使用，他家只有普通话

海天瑞声 https://www.haitianruisheng.com/dsvoice/catid-59.htm， 提供收费的上海话语音数据集，每人3H左右，包含通用数据和情绪数据。  新发音人：2男1女。  老发音人：1女，录音时长13.6小时。

## 开源项目

ChatTTS音色试听查找： https://www.modelscope.cn/studios/ttwwwaa/ChatTTS_Speaker

# 试验

## 第二次试验

本次语音合成系列对比说明：

1. 不训练语音合成基座模型，只做微调训练
2. 开源模型自带的音色
3. 以开源模型为基座，抽取样本音色的特征，训练自己的声学模型，基于声学模型，训练自己的语音合成模型
4. 上海话采用讯飞语音的“上海阮灵”音色。

### 试验过程

#### 数据来源：

1. 朱总给的在用公交车上报站语音文件
2. 讯飞语音的聆小珊
3. 郭德纲采访节目的视频
4. ChatTTS抽卡得到的Speaker音频

#### 数据集搜集整理：

朱总给的在用公交车上报站语音文件处理：
1. 通过人工手动剪辑分离出普通话、英语、上海话三种语音文件。
2. 通过语音识别模型进行自动识别打标
3. 人工核对打标结果，删除无效语音
4. 剩余的语音文件，制作训练集

讯飞语音的聆小珊处理：
1. 在线生成聆小珊的语音文件并下载聆小珊的语音文件
2. 通过语音识别模型进行自动识别打标
3. 人工核对语音文件，删除无效语音
4. 剩余的语音文件，制作训练集

郭德纲采访节目的视频处理：
1. 大量观看视频平台上郭德纲采访节目的视频，找到音质不错的视频并下载
2. 通过人工手动剪辑分离出合适的视频片段，分离出视频中的语音
3. 通过语音识别模型进行自动识别打标
4. 人工核对语音文件，删除无效语音
5. 剩余的语音文件，制作训练集

ChatTTS抽卡得到的Speaker音频处理：
1. 改变生成随机数种子，生成不同音色的语音文件，细听，选择合适的音色



#### 模型和工具：
1. GPT-SoVITS预训练模型
2. G2PW
3. UVR5
4. funasr iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
5. funasr iic/speech_fsmn_vad_zh-cn-16k-common-pytorch
6. funasr iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch
7. faster-whisper-large-v3

#### 本次试验主要调教参数参数：

本次试验中GPT模型和VITS模型的微调训练参数，除了如下记录外，其余参数均采用默认参数。

基于声学模型的语音切分：

| 参数 | 值 |
| --- | --- |
| threshold | -34 |
| min_length | 4000 |
| min_interval | 300 |
| hop_size | 10 |
| max | 0.9 |
| alpha_mix | 0.25 |

声学模型微调训练参数：

| 参数 | 值 |
| --- | --- |
| batch_size | 8 |
| total_epoch | 8 |
| learning_rate | 0.4 |
| save_every_epoch | 4 |

GPT模型微调训练参数：

| 参数 | 值 |
| --- | --- |
| batch_size | 8 |
| total_epoch | 15 |
| dpo | false |
| save_every_epoch | 5 |

推理参数：

| 参数 | 值 |
| --- | --- |
| top_k | 15 |
| top_p | 1 |
| temperature | 1 |

相关参数：

```
{
  "train": {
    "log_interval": 100,
    "eval_interval": 500,
    "seed": 1234,
    "epochs": 8,
    "learning_rate": 0.0001,
    "betas": [0.8, 0.99],
    "eps": 1e-9,
    "batch_size": 8,
    "fp16_run": true,
    "lr_decay": 0.999875,
    "segment_size": 20480,
    "init_lr_ratio": 1,
    "warmup_epochs": 0,
    "c_mel": 45,
    "c_kl": 1.0,
    "text_low_lr_rate": 0.4,
    "pretrained_s2G": "GPT_SoVITS/pretrained_models/gsv-v2final-pretrained/s2G2333k.pth",
    "pretrained_s2D": "GPT_SoVITS/pretrained_models/gsv-v2final-pretrained/s2D2333k.pth",
    "if_save_latest": true,
    "if_save_every_weights": true,
    "save_every_epoch": 4,
    "gpu_numbers": "0"
  },
  "data": {
    "max_wav_value": 32768.0,
    "sampling_rate": 32000,
    "filter_length": 2048,
    "hop_length": 640,
    "win_length": 2048,
    "n_mel_channels": 128,
    "mel_fmin": 0.0,
    "mel_fmax": null,
    "add_blank": true,
    "n_speakers": 300,
    "cleaned_text": true,
    "exp_dir": "logs/\u8046\u5c0f\u73ca_v1"
  },
  "model": {
    "inter_channels": 192,
    "hidden_channels": 192,
    "filter_channels": 768,
    "n_heads": 2,
    "n_layers": 6,
    "kernel_size": 3,
    "p_dropout": 0.1,
    "resblock": "1",
    "resblock_kernel_sizes": [3, 7, 11],
    "resblock_dilation_sizes": [
      [1, 3, 5],
      [1, 3, 5],
      [1, 3, 5]
    ],
    "upsample_rates": [10, 8, 2, 2, 2],
    "upsample_initial_channel": 512,
    "upsample_kernel_sizes": [16, 16, 8, 2, 2],
    "n_layers_q": 3,
    "use_spectral_norm": false,
    "gin_channels": 512,
    "semantic_frame_rate": "25hz",
    "freeze_quantizer": true,
    "version": "v2"
  },
  "s2_ckpt_dir": "logs/\u8046\u5c0f\u73ca_v1",
  "content_module": "cnhubert",
  "save_weight_dir": "SoVITS_weights_v2",
  "name": "\u8046\u5c0f\u73ca_v1",
  "version": "v2"
}

```



### 试验产出样本


| 盲测名称 | 标准名称 | 参考音频 |
| --- | --- | --- |
| 中文报站-1 | aoma-edge-一二八纪念路江杨南路-zh |  |
| 中文报站-2 | chatts-1528-车辆起步-zh |  |
| 中文报站-3 | chattts-1528-一二八纪念路江杨南路-zh |  |
| 中文报站-4 | 合成-车辆起步下一站，江阳南路通南路-zh |  |
| 中文报站-5 | chattts-zh-0918-111017_8.0s-seed1528-temp0.1-top_p0.701-top_k20-len51-61860-merge |  |
| 中文报站-6 | chattts-zh-0918-134216_9.0s-seed2-temp0.12427-top_p0.701-top_k20-len59-18714-merge |  |
| 中文报站-7 | chattts-zh-0918-140651_8.1s-seed1509-temp0.10067-top_p0.701-top_k20-len58-74126-merge |  |
| 中文报站-8 | GPT_weights_v2-guodegang_01-e15-zh_1 | 如果有一天一睁眼，所有的艺人都不翼而飞了，那是我们导演组需要的。  -- vocal_不装郭德纲采访之我是个无趣的人  金句频出_01.wav.reformatted.wav_10.wav_0001344000_0001503360 |
| 中文报站-9 | GPT_weights_v2-guodegang_01-e15-zh_2 | 其实说一千道一万还是个节目，啊，这个每一个人在里边表现都是很真实的。 --vocal_不装郭德纲采访之我是个无趣的人  金句频出_01.wav.reformatted.wav_10.wav_0001765440_0001996800 |
| 中文报站-10 | 讯飞语音-聆小珊-咨询讲解-zh |  |
| 中文报站-11 | 讯飞语音-千雪-叙述品质-zh |  |
| 中文报站-12 | 讯飞语音-聆小珊-咨询讲解-zh-1 |  |
| 英语报站-1 | aoma-edge-江阳南路通南路-en |  |
| 英语报站-2 | 合成-松发路逸仙路-en |  |
| 英语报站-3 | 逸仙路何家弯路-en |  |
| 英语报站-4 | 合成-128纪念路阳曲路-en |  |
| 英语报站-5 | chatts-en-0918-112011_33.3s-seed1528-temp0.1-top_p0.701-top_k20-len73-98929-merge |  |
| 英语报站-6 | chattts-en-0918-132112_31.5s-seed1244-temp0.1-top_p0.701-top_k20-len64-59882-merge |  |
| 英语报站-7 | chattts-en-0918-135359_5.0s-seed2-temp0.12427-top_p0.701-top_k20-len47-34033-merge |  |
| 英语报站-8 | chattts-zh-0918-141751_5.2s-seed1996-temp0.10067-top_p0.701-top_k20-len47-39130-merge |  |
| 英语报站-9 | 讯飞语音-千雪-叙述品质-en |  |
| 英语报站-10 | 讯飞语音-聆小珊-咨询讲解-en |  |
| 上海报站-1 | 讯飞-上海阮灵-车辆进站请注意安全，一二八纪念路江杨南路到了，请配合从后门下车，开门请当心 |  |
| 普通话英语混合-1 | 聆小珊-中英文一分钟多-1 |  |


#### 评估结果：

| 评估人 | 选择 |
| --- | --- |
| 喻斯进 | 英语报站-5.wav、中文报站-4.wav、英语报站-3.wav、中文报站-9.wav |
| 殷剑 | 中文4和中文10、英文选  2、3 |
| 朱总 |  |

相关评价：

1. 英文站名挺别扭
2. 中文都还行吧，只是从报站角度有的不合适
3. 口语话，其中一个还一股子北京味道
4. 要洪亮，有朝气
5. 语调不太对
6. 中文8、中文9两个是郭德纲的声纹，中文9从声纹还原度和效果上 比较好，2nd中文选了中文9中文9的超参可以用来合成有需求的其它声纹
7. 中文10的 音色可以。语速间隔有问题。路名要连读，不能过快。要让人听清楚。路名后稍微停顿一下  报送“到了”，路名报的一定调整语速，太慢了拖沓，快了听不清，报站语音要听清楚每一个字，特别是路名，所以有间隔和重音的
8. 你听中文四，人语言训练的会有连读的问题，我们先说信息的清晰度，中文四最清楚，只是感觉像机器人
9. 中文2、3 听的清楚，但是音色不行，你或者实时2、3可以换音色么，太低沉了，要洪亮。听上去很累的样子


## 第二次试验后续剩余

目的： 
1. 解决第一次实验中，评估人员提出的评价问题。
2. 语音合成上海方言

目的1预计后续所需实验：

1. 弄清VITS和SoVITS中支持的语气、语调、停顿符号
2. 拿应用场景下的原话高质量语音制作训练数据集，单独训练GPT网络
3. 微调训练GPTSoVITS模型

目的2预计后续所需实验：

1. 搜集到正确的上海话语音制作训练集，训练方言语音合成的VITS基座模型
2. 拿应用场景下的原话高质量语音制作训练数据集，单独训练GPT网络
3. 微调训练GPTSoVITS模型