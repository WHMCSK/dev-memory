# Sad Talker

conda create -n sadtalker python=3.8

pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

conda install ffmpeg

pip install -r requirements.txt

pip install TTS

bash scripts/download_models.sh

