# frp

## 一个泛域名内网穿透用来做微信小程序开发的例子

frps配置：
```
[common]
bind_port = 5002
vhost_https_port = 443
subdomain_host = bgenius.cn
```


frpc配置：
```
[common]
server_addr = *.*.*.*
server_port = 5002

[web]
type = https
#local_port = 19821
subdomain = test

plugin = https2http
plugin_local_addr = 127.0.0.1:19821

# HTTPS 证书相关的配置
plugin_crt_path = ./ca/test.bgenius.cn.crt
plugin_key_path = ./ca/test.bgenius.cn.key
plugin_host_header_rewrite = 127.0.0.1
plugin_header_X-From-Where = frp
```