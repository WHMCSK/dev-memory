# Ros

### 下载ROS的Docker镜像

尝试了一圈最终还是发现最好用的就是官方提供的ros环境，干净，鲁棒性强，versionkey也不会失效，没有杂七杂八的东西，推荐使用以下命令拉取镜像。

```
docker pull ros
```

### 使用这个Docker镜像

```
docker run --name ros --mount type=bind,source=/Users/alston/Laboratory/DockerDisk/ros,target=/root/ros_workspaces -itd -p 6080:80 -p 7777:7777 -p 9111:9111 -p 1314:1314 -p 1222:1222 ros
```

docker run --name ros -itd -p 6080:80 -p 7777:7777 -p 9111:9111 -p 1314:1314 -p 1222:1222 ros

docker run  ros