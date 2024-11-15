# 大模型训练常见问题

## 1. 微调时出现ms-bench数据集

问题：

微调时总会出现ms-bench数据集，但已经加了Modelscope数据集了，不知是否正常?

答案：

这个是防止知识遗忘的通用知识数据集，--train_dataset_mix_ratio默认为0，不影响您的训练。此回答整理自钉群“魔搭ModelScope开发者联盟群 ①”