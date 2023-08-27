# 车牌识别

* 一个开源的车牌识别项目
https://github.com/openalpr/openalpr

使用docker快速体验
```
# Build docker image
docker build -t openalpr https://github.com/openalpr/openalpr.git
# Download test image
wget http://plates.openalpr.com/h786poj.jpg
# Run alpr on image
docker run -it --rm -v $(pwd):/data:ro openalpr -c eu h786poj.jpg
```