# supervisord

## 安装

```
pip install supervisor
```

## 生成配置

```
echo_supervisord_conf > /etc/supervisord.conf
```

## 开启配置项

```
[include]
files = supervisord.d/*.ini
```

## 创建配置文件夹

```
/etc/supervisord.d
```

## 配置

例如创建一个frp服务的配置文件：

```
vi /etc/supervisord.d/frp.ini
```

配置：

```
[program:frps]
command=/你的文件夹/frps -c /你的文件夹/frps.toml
autostart=true
autorestart=false
stderr_logfile=/你的文件夹/logs/frp.log
stdout_logfile=/你的文件夹/logs/frp.log
#user=test
```

## 启动

```
supervisord -c /etc/supervisord.conf
```

## 配置成开机启动

```
cd /usr/lib/systemd/system/
```

新建系统服务配置文件：

```
vi supervisord.service
```

配置例如下面：

```
[Unit]
Description=Supervisor daemon
 
[Service]
Type=forking
ExecStart=/root/miniconda3/bin/supervisord -c /etc/supervisor/supervisord.conf
ExecStop=/root/miniconda3/bin/supervisorctl shutdown
ExecReload=/root/miniconda3/bin/supervisorctl reload
KillMode=process
Restart=on-failure
RestartSec=42s
 
[Install]
WantedBy=multi-user.target
```

设置开机自启：

```
systemctl enable supervisord
```

验证是否开机自启动：

```
systemctl is-enabled supervisord
```