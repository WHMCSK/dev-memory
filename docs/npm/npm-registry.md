# npm淘宝镜像与官方源切换

1.临时使用  
```
npm --registry https://registry.npm.taobao.org install 包名
```

2.永久设置为淘宝镜像
```
npm config set registry https://registry.npm.taobao.org
```

3.换回国外官方源 
```
npm config set registry https://registry.npmjs.org
```

4.查看使用的源地址
```
npm config get registry
```

5.使用淘宝的cnpm
```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```