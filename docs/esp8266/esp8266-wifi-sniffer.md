# 深入理解Arduino下的ESP8266_Non-OS_SDK API⑥ Sniffer(混杂模式) 相关接口

## 文章目录
```
    1. Sniffer 相关接口
    1.1 混杂模式
    2.相关API
    2.1 wifi_promiscuous_enable —— 开启混杂模式 (sniffer)
    2.2 wifi_promiscuous_set_mac —— 设置 sniffer 模式时的 MAC 地址过滤，可过滤出发给指定 MAC 地址的包（也包含广播包）
    2.3 wifi_set_promiscuous_rx_cb —— 注册混杂模式下的接收数据回调函数，每收到一包数据，都会进入注册的回调函数
    2.4 wifi_get_channel —— 获取信道号
    2.5 wifi_set_channel —— 设置信道号，用于混杂模式
```


1. Sniffer 相关接口

    Sniffer 接口位于 tools/sdk/include/user_interface.h

1.1 混杂模式

    混杂模式（英语：promiscuous mode）是电脑网络中的术语。是指一台机器的网卡能够接收所有经过它的数据流，而不论其目的地址是否是它。  
    混杂模式就是接收所有经过网卡的数据包，包括不是发给本机的包。默认情况下网卡只把发给本机的包（包括广播包）传递给上层程序，其它的包一律丢弃。简单的讲,混杂模式就是指网卡能接受所有通过它的数据流，不管是什么格式，什么地址的。事实上，计算机收到数据包后，由网络层进行判断，确定是递交上层（传输层），还是丢弃，还是递交下层（数据链路层、MAC子层）转发。  
    简单的说，网卡的混杂模式是为网络分析而提供的。（wifi杀手探测器也是基于这个原理 ESP8266开发之旅 应用篇⑥ 检测周边WiFi杀手）  

2. 相关API

2.1 wifi_promiscuous_enable —— 开启混杂模式 (sniffer)  

函数定义
```
void wifi_promiscuous_enable(uint8 promiscuous)
```

参数

```
uint8 promiscuous
• 0：关闭混杂模式
• 1：开启混杂模式
```

返回值

```
⽆无
```

注意

```
• 仅支持在 ESP8266 单 Station 模式下，开启混杂模式

• 混杂模式中，ESP8266 Station 和 SoftAP 接口均失效

• 若开启混杂模式，请先调用 wifi_station_disconnect 确保没有连接

• 混杂模式中请勿调用其他 API，请先调用 wifi_promiscuous_enable(0) 退出 sniffer
```

2.2 wifi_promiscuous_set_mac —— 设置 sniffer 模式时的 MAC 地址过滤，可过滤出发给指定 MAC 地址的包（也包含广播包）

函数定义

```
void wifi_promiscuous_set_mac(const uint8_t *address)
```

参数

```
const uint8_t *address：MAC 地址
```

返回值

```
⽆无
```

注意

```
• 本接口需在 wifi_promiscuous_enable(1) 使能混杂模式后调用；

• MAC 地址过滤仅对当前这次的 sniffer 有效；

• 如果停止 sniffer，又再次 sniffer，需要重新设置 MAC 地址过滤。
```

示例

```
char ap_mac[6] = {0x16, 0x34, 0x56, 0x78, 0x90, 0xab};
wifi_promiscuous_set_mac(ap_mac);
```

2.3 wifi_set_promiscuous_rx_cb —— 注册混杂模式下的接收数据回调函数，每收到一包数据，都会进入注册的回调函数

函数定义

```
void wifi_set_promiscuous_rx_cb(wifi_promiscuous_cb_t cb)
```

参数

```
wifi_promiscuous_cb_t cb：回调函数
```

返回值

```
无
```

2.4 wifi_get_channel —— 获取信道号

函数定义

```
uint8 wifi_get_channel(void)
```

参数

```
无
```

返回值

```
信道号
```

2.5 wifi_set_channel —— 设置信道号，用于混杂模式

函数定义

```
bool wifi_set_channel (uint8 channel)
```

参数

```
uint8 channel：信道号
```

返回值
```
true：成功
false：失败
```
