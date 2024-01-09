# 深入理解Arduino下的ESP8266_Non-OS_SDK API⑤ Wi-Fi接口

qq60daea2ce90cb2021-07-28 14:07:46博主文章分类：ESP8266 SDK
文章标签ESP8266文章分类物联网阅读数597

授人以鱼不如授人以渔，目的不是为了教会你具体项目开发，而是学会学习的能力。希望大家分享给你周边需要的朋友或者同学，说不定大神成长之路有博哥的奠基石。。。

快速导航
单片机菜鸟的博客快速索引(快速找到你要的)

如果觉得有用，麻烦点赞收藏，您的支持是博主创作的动力。

文章目录
 1. Wi-Fi接口
 2. Common
 2.1 wifi_get_opmode —— 查询 Wi-Fi 当前工作模式
 2.2 wifi_get_opmode_default —— 查询保存在 Flash 中的 Wi-Fi 工作模式设置
 2.3 wifi_set_opmode —— 设置 Wi-Fi 工作模式（Station，SoftAP 或者 Station+SoftAP），并保存到 Flash
 2.4 wifi_set_opmode_current —— 设置 Wi-Fi工作模式（Station，SoftAP 或者 Station + SoftAP），不保存到 Flash
 2.5 wifi_set_phy_mode —— 设置 ESP8266 物理理层模式 (802.11 b/g/n)
 2.6 wifi_get_phy_mode —— 查询 ESP8266 物理理层模式 (802.11 b/g/n)
 2.7 wifi_get_ip_info —— 查询 Wi-Fi Station 接口或者 SoftAP 接口的 IP 地址
 2.8 wifi_set_ip_info —— 设置 Wi-Fi Station 或者 SoftAP 的 IP 地址
 2.9 wifi_set_macaddr —— 设置 MAC 地址
 2.10 wifi_get_macaddr —— 查询 MAC 地址
 2.11 wifi_set_sleep_type —— 设置省电模式。设置为 NONE_SLEEP_T，则关闭省电模式
 2.12 wifi_get_sleep_type —— 查询省电模式
 2.13 wifi_set_broadcast_if —— 设置 ESP8266 发送 UDP 广播包时，从 Station 接口还是 SoftAP 接口发送。默认从 SoftAP 接口发送
 2.14 wifi_get_broadcast_if —— 查询 ESP8266 发送 UDP 广播包时，从 Station 接口还是 SoftAP 接口发送
 2.15 wifi_set_event_handler_cb —— 注册 Wi-Fi event 处理回调
 2.16 wifi_register_send_pkt_freedom_cb —— 注册 freedom 发包的回调函数。freedom 发包功能，即支持发送用户自定义 802.11 的包
 2.17 wifi_unregister_send_pkt_freedom_cb —— 注销 freedom 发包的回调函数
 2.18 wifi_send_pkt_freedom ——发包函数
 3. station
 3.1 wifi_station_get_config —— 查询 Wi-Fi Station 接口的当前配置参数
 3.2 wifi_station_get_config_default —— 查询 Wi-Fi Station 接口保存在 Flash 中的配置参数
 3.3 wifi_station_set_config —— 设置 Wi-Fi Station 接口的配置参数，并保存到 Flash
 3.4 wifi_station_set_config_current —— 设置 Wi-Fi Station 接口的配置参数，不保存到 Flash
 3.5 wifi_station_set_cert_key —— 设置 ESP8266 Wi-Fi Station 接口连接 WPA2-ENTERPRISE AP 使用的证书
 3.6 wifi_station_clear_cert_key —— 释放连接 WPA2-ENTERPRISE AP 使⽤用证书占用的资源，并清除相关状态
 3.7 wifi_station_set_username —— 设置连接 WPA2-ENTERPRISE AP 时，ESP8266 Station 的用户名
 3.8 wifi_station_clear_username —— 释放连接 WPA2-ENTERPRISE AP 设置用户名占用的资源，并清除相关状态
 3.9 wifi_station_connect —— ESP8266 Wi-Fi Station 接口连接 AP
 3.10 wifi_station_disconnect—— ESP8266 Wi-Fi Station 接口从 AP 断开连接
 3.11 wifi_station_get_connect_status—— 查询 ESP8266 Wi-Fi Station 接⼝口连接 AP 的状态
 3.12 wifi_station_scan—— 获取 AP 的信息
 3.13 scan_done_cb_t—— wifi_station_scan 的回调函数
 3.14 wifi_station_ap_number_set—— 设置 ESP8266 Station 最多可记录⼏几个 AP 的信息
 3.15 wifi_station_get_ap_info—— 获取 ESP8266 Station 保存的 AP 信息，最多记录 5 个
 3.16 wifi_station_ap_change—— ESP8266 Station 切换到已记录的某号 AP 配置连接
 3.17 wifi_station_get_current_ap_id—— 获取当前连接的 AP 保存记录 ID 值。ESP8266 可记录每一个配置连接的 AP，从 0 开始计数
 3.18 wifi_station_get_auto_connect—— 查询 ESP8266 Station 上电是否会⾃自动连接已记录的 AP（路由）
 3.19 wifi_station_set_auto_connect—— 设置 ESP8266 Station 上电是否⾃自动连接已记录的 AP（路由），默认为自动连接
 3.20 wifi_station_dhcpc_start—— 开启 ESP8266 Station DHCP client
 3.21 wifi_station_dhcpc_stop—— 关闭 ESP8266 Station DHCP client
 3.22 wifi_station_dhcpc_status—— 查询 ESP8266 Station DHCP client 状态
 3.23 wifi_station_dhcpc_set_maxtry—— 设置 ESP8266 Station DHCP client 最大重连次数 (默认会一直重连)
 3.24 wifi_station_set_reconnect_policy—— 设置 ESP8266 Station 连接 AP 失败或断开后是否重连。默认重连。
 3.25 wifi_station_get_rssi—— 获取ESP8266 Station 已连接的 AP 信号强度
 3.26 wifi_station_set_hostname—— 设置 ESP8266 Station DHCP 分配的主机名称
 3.27 wifi_station_get_hostname—— 查询 ESP8266 Station DHCP 分配的主机名称
 4.Soft-AP
 4.1 wifi_softap_get_config—— 查询 ESP8266 Wi-Fi SoftAP 接口的当前配置
 4.2 wifi_softap_get_config_default—— 查询 ESP8266 Wi-Fi SoftAP 接口保存在 Flash 中的配置
 4.3 wifi_softap_set_config—— 设置 Wi-Fi SoftAP 接口配置，并保存到Flash
 4.4 wifi_softap_set_config_current—— 设置 Wi-Fi SoftAP 接口配置，不保存到Flash
 4.5 wifi_softap_get_station_num—— 获取 ESP8266 SoftAP 下连接的Station 个数
 4.6 wifi_softap_get_station_info—— 获取 ESP8266 SoftAP 接口下连入的 Station 的信息，包括 MAC 和 IP
 4.7 wifi_softap_free_station_info—— 释放调用 wifi_softap_get_station_info 时结构体 station_info 占用的空间
 4.8 wifi_softap_dhcps_start—— 开启 ESP8266 SoftAP DHCP server
 4.9 wifi_softap_dhcps_stop—— 关闭 ESP8266 SoftAP DHCP server。默认开启 DHCP。
 4.10 wifi_softap_set_dhcps_lease—— 设置 ESP8266 SoftAP DHCP server 分配 IP 地址的范围
 4.11 wifi_softap_get_dhcps_lease—— 查询 ESP8266 SoftAP DHCP server 分配 IP 地址的范围
 4.12 wifi_softap_set_dhcps_lease_time—— 设置 ESP8266 SoftAP DHCP server 的租约时间。默认为 120 分钟。
 4.13 wifi_softap_get_dhcps_lease_time—— 查询 ESP8266 SoftAP DHCP server 的租约时间
 4.14 wifi_softap_reset_dhcps_lease_time—— 复位 ESP8266 SoftAP DHCP server 的租约时间。恢复到 120 分钟。
 4.15 wifi_softap_dhcps_status—— 获取 ESP8266 SoftAP DHCP server 状态
 4.16 wifi_softap_set_dhcps_offer_option—— 设置 ESP8266 SoftAP DHCP server 属性
 

1. Wi-Fi接口
Wi-Fi 接口位于 tools/sdk/include/user_interface.h
wifi_station_xxx 系列接口以及ESP8266 Station相关的设置、查询接口，请在ESP8266 Station使能的情况下调用；
wifi_softap_xxx 系列接口以及ESP8266 SoftAP相关的设置、查询接口，请在ESP8266 SoftAP使能的情况下调用；
2. Common
2.1 wifi_get_opmode —— 查询 Wi-Fi 当前工作模式
函数定义

uint8 wifi_get_opmode (void)
1.
参数

无
1.
返回值

Wi-Fi 工作模式：
- **0x01：Station 模式**
- **0x02：SoftAP 模式**
- **0x03：Station+SoftAP 模式**
1.
2.
3.
4.
2.2 wifi_get_opmode_default —— 查询保存在 Flash 中的 Wi-Fi 工作模式设置
函数定义

uint8 wifi_get_opmode_default (void)
1.
参数

无
返回值

Wi-Fi 工作模式：
- **0x01：Station 模式**
- **0x02：SoftAP 模式**
- **0x03：Station+SoftAP 模式**
1.
2.
3.
4.
2.3 wifi_set_opmode —— 设置 Wi-Fi 工作模式（Station，SoftAP 或者 Station+SoftAP），并保存到 Flash
函数定义

bool wifi_set_opmode (uint8 opmode)
1.
参数
1、opmode —— Wi-Fi 工作模式

uint8 opmode：Wi-Fi工作模式
• 0x01：Station 模式
• 0x02：SoftAP 模式
• 0x03：Station+SoftAP 模式
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

• ESP8266_NONOS_SDK_V0.9.2 以及之前版本，设置之后需要调用 system_restart() 重启
⽣生效；
• ESP8266_NONOS_SDK_V0.9.2 之后的版本，不需要重启，即时生效。
• 本设置如果与原设置不不同，会更更新保存到 Flash 系统参数区。
1.
2.
3.
4.
2.4 wifi_set_opmode_current —— 设置 Wi-Fi工作模式（Station，SoftAP 或者 Station + SoftAP），不保存到 Flash
函数定义

bool wifi_set_opmode_current (uint8 opmode)
1.
参数
1、opmode —— Wi-Fi 工作模式

uint8 opmode：Wi-Fi工作模式
• 0x01：Station 模式
• 0x02：SoftAP 模式
• 0x03：Station+SoftAP 模式
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
2.5 wifi_set_phy_mode —— 设置 ESP8266 物理理层模式 (802.11 b/g/n)
函数定义

bool wifi_set_phy_mode(enum phy_mode mode)
1.
参数

enum phy_mode mode : 物理层模式
enum phy_mode {
PHY_MODE_11B = 1,
PHY_MODE_11G = 2,
PHY_MODE_11N = 3
};
1.
2.
3.
4.
5.
6.
返回值

true：成功
false：失败
1.
2.
2.6 wifi_get_phy_mode —— 查询 ESP8266 物理理层模式 (802.11 b/g/n)
函数定义

enum phy_mode wifi_get_phy_mode(void)
1.
参数

无
1.
返回值

enum phy_mode{
PHY_MODE_11B = 1,
PHY_MODE_11G = 2,
PHY_MODE_11N = 3
};
1.
2.
3.
4.
5.
2.7 wifi_get_ip_info —— 查询 Wi-Fi Station 接口或者 SoftAP 接口的 IP 地址
函数定义

bool wifi_get_ip_info(
uint8 if_index,
struct ip_info *info
)
1.
2.
3.
4.
参数

uint8 if_index：获取 Station 或者 SoftAP 接口的信息
#define STATION_IF 0x00
#define SOFTAP_IF 0x01
struct ip_info *info：获取到的 IP 信息
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

在 user_init 中，由于初始化尚未完成，无法通过本接口查询到有效 IP 地址。
1.
2.8 wifi_set_ip_info —— 设置 Wi-Fi Station 或者 SoftAP 的 IP 地址
函数定义

bool wifi_set_ip_info(
uint8 if_index,
struct ip_info *info
)
1.
2.
3.
4.
参数

uint8 if_index：设置 Station 或者 SoftAP 接⼝口
#define STATION_IF 0x00
#define SOFTAP_IF 0x01
struct ip_info *info：IP 信息
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

• 本接口设置静态 IP，请先关闭对应 DHCP 功能 wifi_station_dhcpc_stop 或者
wifi_softap_dhcps_stop

• 设置静态 IP，则关闭 DHCP；DHCP 开启，则静态 IP 失效。
1.
2.
3.
4.
示例

wifi_set_opmode(STATIONAP_MODE); //Set softAP + station mode
struct ip_info info;
wifi_station_dhcpc_stop();
wifi_softap_dhcps_stop();
IP4_ADDR(&info.ip, 192, 168, 3, 200);
IP4_ADDR(&info.gw, 192, 168, 3, 1);
IP4_ADDR(&info.netmask, 255, 255, 255, 0);
wifi_set_ip_info(STATION_IF, &info);
IP4_ADDR(&info.ip, 10, 10, 10, 1);
IP4_ADDR(&info.gw, 10, 10, 10, 1);
IP4_ADDR(&info.netmask, 255, 255, 255, 0);
wifi_set_ip_info(SOFTAP_IF, &info);
wifi_softap_dhcps_start();
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
2.9 wifi_set_macaddr —— 设置 MAC 地址
函数定义

bool wifi_set_macaddr(
uint8 if_index,
uint8 *macaddr
)
1.
2.
3.
4.
参数

uint8 if_index：设置 Station 或者 SoftAP 接⼝口
#define STATION_IF 0x00
#define SOFTAP_IF 0x01
uint8 *macaddr：MAC 地址
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

• 本接口必须在 user_init 中调⽤用
• ESP8266 SoftAP 和 Station MAC 地址不不同，请勿将两者设置为同一 MAC 地址
• ESP8266 MAC 地址第一个字节的 bit 0 不能为 1。例例如，MAC 地址可以设置为
1a:XX:XX:XX:XX:XX，但不能设置为 15:XX:XX:XX:XX:XX。
1.
2.
3.
4.
示例

wifi_set_opmode(STATIONAP_MODE);
char sofap_mac[6] = {0x16, 0x34, 0x56, 0x78, 0x90, 0xab};
char sta_mac[6] = {0x12, 0x34, 0x56, 0x78, 0x90, 0xab};
wifi_set_macaddr(SOFTAP_IF, sofap_mac);
wifi_set_macaddr(STATION_IF, sta_mac);
1.
2.
3.
4.
5.
2.10 wifi_get_macaddr —— 查询 MAC 地址
函数定义

bool wifi_get_macaddr(
uint8 if_index,
uint8 *macaddr
)
1.
2.
3.
4.
参数

uint8 if_index：设置 Station 或者 SoftAP 接⼝口
#define STATION_IF 0x00
#define SOFTAP_IF 0x01
uint8 *macaddr：MAC 地址
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
2.11 wifi_set_sleep_type —— 设置省电模式。设置为 NONE_SLEEP_T，则关闭省电模式
函数定义

bool wifi_set_sleep_type(enum sleep_type type)
1.
参数

typedef enum {
    NONE_SLEEP_T    = 0,
    LIGHT_SLEEP_T,
    MODEM_SLEEP_T
} sleep_type_t;

enum sleep_type type：省电模式
1.
2.
3.
4.
5.
6.
7.
返回值

true：成功
false：失败
1.
2.
注意

• 默认为 Modem-sleep 模式。

• Light Sleep 为了了降低功耗，将 TCP timer tick 由原本的 250ms 改为了 3s，这将导致 TCP
timer 超时时间相应增加；如果用户对 TCP timer 的准确度有要求，请使用 modem sleep 或
者 deep sleep 模式。
1.
2.
3.
4.
5.
2.12 wifi_get_sleep_type —— 查询省电模式
函数定义

enum sleep_type wifi_get_sleep_type(void)
1.
参数

无
1.
返回值

enum sleep_type {
NONE_SLEEP_T = 0;
LIGHT_SLEEP_T,
MODEM_SLEEP_T
};
1.
2.
3.
4.
5.
2.13 wifi_set_broadcast_if —— 设置 ESP8266 发送 UDP 广播包时，从 Station 接口还是 SoftAP 接口发送。默认从 SoftAP 接口发送
函数定义

bool wifi_set_broadcast_if (uint8 interface)
1.
参数

uint8 interface
• 1：station
• 2：SoftAP
• 3：Station 和 SoftAP 接⼝口均发送
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

如果设置仅从 Station 接口发 UDP 广播包，会影响 ESP8266 SoftAP 的功能，DHCP server ⽆无
法使用。需要使能 SoftAP 的⼴广播包功能，才可正常使用 ESP8266 SoftAP。
1.
2.
2.14 wifi_get_broadcast_if —— 查询 ESP8266 发送 UDP 广播包时，从 Station 接口还是 SoftAP 接口发送
函数定义

uint8 wifi_get_broadcast_if (void)
1.
参数

无
1.
返回值

• 1：Station
• 2：SoftAP
• 3：Station 和 SoftAP 接⼝口均发送
1.
2.
3.
2.15 wifi_set_event_handler_cb —— 注册 Wi-Fi event 处理回调
函数定义

void wifi_set_event_handler_cb(wifi_event_handler_cb_t cb)
1.
参数

wifi_event_handler_cb_t cb：回调函数
1.
返回值

无
1.
示例

void wifi_handle_event_cb(System_Event_t *evt)
{
	os_printf("event %x\n", evt->event);
	switch (evt->event) {
		case EVENT_STAMODE_CONNECTED:
			os_printf("connect to ssid %s, channel %d\n",
			evt->event_info.connected.ssid,
			evt->event_info.connected.channel);
			break;
		
		case EVENT_STAMODE_DISCONNECTED:
			os_printf("disconnect from ssid %s, reason %d\n",
			evt->event_info.disconnected.ssid,
			evt->event_info.disconnected.reason);
			break;
			
		case EVENT_STAMODE_AUTHMODE_CHANGE:
			os_printf("mode: %d -> %d\n",
			evt->event_info.auth_change.old_mode,
			evt->event_info.auth_change.new_mode);
			break;
			
		case EVENT_STAMODE_GOT_IP:
			os_printf("ip:" IPSTR ",mask:" IPSTR ",gw:" IPSTR,
			IP2STR(&evt->event_info.got_ip.ip),
			IP2STR(&evt->event_info.got_ip.mask),
			IP2STR(&evt->event_info.got_ip.gw));
			os_printf("\n");
			break;
			
		case EVENT_SOFTAPMODE_STACONNECTED:
			os_printf("station: " MACSTR "join, AID = %d\n",
			MAC2STR(evt->event_info.sta_connected.mac),
			evt->event_info.sta_connected.aid);
			break;
			
		case EVENT_SOFTAPMODE_STADISCONNECTED:
			os_printf("station: " MACSTR "leave, AID = %d\n",
			MAC2STR(evt->event_info.sta_disconnected.mac),
			evt->event_info.sta_disconnected.aid);
			break;
			
		default:
			break;
	}
}
void user_init(void)
{
	// TODO: add your own code here....
	wifi_set_event_handler_cb(wifi_handle_event_cb);
}
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.
28.
29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.
40.
41.
42.
43.
44.
45.
46.
47.
48.
49.
50.
51.
2.16 wifi_register_send_pkt_freedom_cb —— 注册 freedom 发包的回调函数。freedom 发包功能，即支持发送用户自定义 802.11 的包
函数定义

int wifi_register_send_pkt_freedom_cb(freedom_outside_cb_t cb);
1.
参数

freedom_outside_cb_t cb：回调函数

typedef void (*freedom_outside_cb_t)(uint8 status);
status：0，发包成功；其他值，发包失败。
1.
2.
3.
4.
返回值

0：注册成功
-1：注册失败
1.
2.
注意

• freedom 发包必须等前一个包发送完毕，进入发包回调 freedom_outside_cb_t 之后，才能
发下一个包。

• 设置发送回调函数可以用来判别包是否发送成功（IEEE802.11 MAC 底层是否发送成功）。
使用发送回调函数请注意如下情况：
	‣ 针对单播包：
		- 回调函数状态显示成功时，对方应用层实际没有收到的状况。原因：
		1. 存在流氓设备进行攻击
		2. 加密密钥设置错误
		3. 应用层丢包
		若需要更更强地发包保证发包成功率，请在应用层实现发包握⼿手机制。
		- 回调函数状态显示失败时，对方应用层实际已收到的状况。原因：
		1. 信道繁忙，未收到对⽅方ACK。
		请注意应用层发包重传，接收方需要检测重传包。
	‣ 针对组播包（包括⼴广播包）：
		- 回调函数状态显示成功，表示组播包已成功发送
		- 回调函数状态显示失败，表示组播包发送失败
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
2.17 wifi_unregister_send_pkt_freedom_cb —— 注销 freedom 发包的回调函数
函数定义

void wifi_unregister_send_pkt_freedom_cb(void)
1.
参数

无
1.
返回值

无
1.
2.18 wifi_send_pkt_freedom ——发包函数
函数定义

int wifi_send_pkt_freedom(uint8 *buf, int len，bool sys_seq)
1.
参数

• uint8 *buf：数据包指针
• int len：数据包⻓长度
• bool sys_seq：是否跟随系统的 802.11 包 sequence number，如果跟随系统，将会在每次
发包后自加 1
1.
2.
3.
4.
返回值

0：成功
-1：失败
1.
2.
注意

• 发送包必须是完整的 802.11 包，⻓长度不包含 FCS。发包长度必须大于最小 802.11 头，即
24 字节，且不能超过 1400 字节，否则返回发包失败。

• duration 域填写无效，由 ESP8266 底层程序决定，自动填充。

• 发包速率限制成管理理包速率，与系统的发包速率一致。

• 支持发送：非加密的数据包，非加密的 beacon/probe req/probe resp。

• 不支持发送：所有加密包 (即包头中的加密 bit 必须为 0，否则返回发包失败)，控制包，除
beacon/probe req/probe resp 以外的其他管理理包。

• freedom 发包必须等前一个包发送完毕，进入发包回调之后，才能发下一个包。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
3. station
3.1 wifi_station_get_config —— 查询 Wi-Fi Station 接口的当前配置参数
函数定义

bool wifi_station_get_config (struct station_config *config)
1.
参数
1、struct station_config *config —— Wi-Fi Station 接口参数指针

struct station_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 bssid_set;    // Note: If bssid_set is 1, station will just connect to the router
                        // with both ssid[] and bssid[] matched. Please check about this.
    uint8 bssid[6];
    wifi_fast_scan_threshold_t threshold;
};
1.
2.
3.
4.
5.
6.
7.
8.
返回值

true：成功
false：失败
1.
2.
3.2 wifi_station_get_config_default —— 查询 Wi-Fi Station 接口保存在 Flash 中的配置参数
函数定义

bool wifi_station_get_config_default (struct station_config *config)
1.
参数
1、struct station_config *config —— Wi-Fi Station 接口参数指针

struct station_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 bssid_set;    // Note: If bssid_set is 1, station will just connect to the router
                        // with both ssid[] and bssid[] matched. Please check about this.
    uint8 bssid[6];
    wifi_fast_scan_threshold_t threshold;
};
1.
2.
3.
4.
5.
6.
7.
8.
返回值

true：成功
false：失败
1.
2.
3.3 wifi_station_set_config —— 设置 Wi-Fi Station 接口的配置参数，并保存到 Flash
函数定义

bool wifi_station_get_config_default (struct station_config *config)
1.
参数
1、struct station_config *config —— Wi-Fi Station 接口参数指针

struct station_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 bssid_set;    // Note: If bssid_set is 1, station will just connect to the router
                        // with both ssid[] and bssid[] matched. Please check about this.
    uint8 bssid[6];
    wifi_fast_scan_threshold_t threshold;
};
1.
2.
3.
4.
5.
6.
7.
8.
返回值

true：成功
false：失败
1.
2.
注意

• 请在 ESP8266 Station 使能的情况下，调用本接口。

• 如果 wifi_station_set_config 在 user_init 中调用，则 ESP8266 Station 接口会在系统初
始化完成后，自动连接 AP（路由），无需再调用 wifi_station_connect

• 否则，需要调用 wifi_station_connect 连接 AP（路由）。

• station_config.bssid_set 一般设置为 0 ，仅当需要检查 AP 的 MAC 地址时（多用于有重
名 AP 的情况下）设置为 1。

• 本设置如果与原设置不不同，会更新保存到 Flash 系统参数区。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
示例

void ICACHE_FLASH_ATTR
user_set_station_config(void)
{
  char ssid[32] = SSID;
  char password[64] = PASSWORD;
  struct station_config stationConf;
  stationConf.bssid_set = 0; //need not check MAC address of AP
  os_memcpy(&stationConf.ssid, ssid, 32);
  os_memcpy(&stationConf.password, password, 64);
  wifi_station_set_config(&stationConf);
}
void user_init(void)
{
  wifi_set_opmode(STATIONAP_MODE); //Set softAP + station mode
  user_set_station_config();
}
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
3.4 wifi_station_set_config_current —— 设置 Wi-Fi Station 接口的配置参数，不保存到 Flash
函数定义

bool wifi_station_set_config_current (struct station_config *config)
1.
参数
1、struct station_config *config —— Wi-Fi Station 接口参数指针

struct station_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 bssid_set;    // Note: If bssid_set is 1, station will just connect to the router
                        // with both ssid[] and bssid[] matched. Please check about this.
    uint8 bssid[6];
    wifi_fast_scan_threshold_t threshold;
};
1.
2.
3.
4.
5.
6.
7.
8.
返回值

true：成功
false：失败
1.
2.
注意

• 请在 ESP8266 Station 使能的情况下，调用本接口。

• 如果 wifi_station_set_config 在 user_init 中调用，则 ESP8266 Station 接口会在系统初
始化完成后，自动连接 AP（路由），无需再调用 wifi_station_connect

• 否则，需要调用 wifi_station_connect 连接 AP（路由）。

• station_config.bssid_set 一般设置为 0 ，仅当需要检查 AP 的 MAC 地址时（多用于有重
名 AP 的情况下）设置为 1。

• 本设置如果与原设置不不同，会更新保存到 Flash 系统参数区。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
3.5 wifi_station_set_cert_key —— 设置 ESP8266 Wi-Fi Station 接口连接 WPA2-ENTERPRISE AP 使用的证书
函数定义

bool wifi_station_set_cert_key (
uint8 *client_cert, int client_cert_len,
uint8 *private_key, int private_key_len,
uint8 *private_key_passwd, int private_key_passwd_len,)
1.
2.
3.
4.
参数

uint8 *client_cert：⼗十六进制数组的证书指针

int client_cert_len：证书长度

uint8 *private_key：⼗十六进制数组的私钥指针，暂不支持超过 2048 的私钥

int private_key_len：私钥长度，请勿超过 2048

uint8 *private_key_passwd：私钥的提取密码，目前暂不支持，请传入 NULL

int private_key_passwd_len：提取密码的长度，目前暂不支持，请传入 0
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
返回值

true：成功
false：失败
1.
2.
注意

• ⽀支持 WPA2-ENTERPRISE AP 需占用 26KB 以上的内存，调用本接口时请注意内存是否足
够。

• ⽬目前 WPA2-ENTERPRISE 只支持非加密的私钥文件和证书文件，且仅支持 PEM 格式
- ⽀支持的证书⽂文件头信息为：- - - - - BEGIN CERTIFICATE - - - - -
- ⽀支持的私钥⽂文件头信息为：- - - - - BEGIN RSA PRIVATE KEY - - - - -
或者 - - - - - BEGIN PRIVATE KEY - - - - -

• 请在连接 WPA2-ENTERPRISE AP 之前调用本接口设置私钥文件和证书文件，在成功连接
AP 后先调用 wifi_station_clear_cert_key 清除内部状态，应用层再释放私钥文件和证书
⽂文件信息。

• 如果遇到加密的私钥文件，请使用 openssl pkey 命令改为非加密文件使用，或者使用
openssl rsa 等命令，对某些私钥文件进行行加密-非加密的转换（或起始 TAG 转化）。

• 不建议使用本接口，请使用 wifi_station_set_enterprise_cert_key 代替。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
3.6 wifi_station_clear_cert_key —— 释放连接 WPA2-ENTERPRISE AP 使⽤用证书占用的资源，并清除相关状态
函数定义

void wifi_station_clear_cert_key (void)
1.
参数

无
1.
返回值

无
1.
注意

不建议使用本接口，请使用 wifi_station_clear_enterprise_cert_key 代替
1.
3.7 wifi_station_set_username —— 设置连接 WPA2-ENTERPRISE AP 时，ESP8266 Station 的用户名
函数定义

int wifi_station_set_username (uint8 *username, int len)
1.
参数

uint8 *username：⽤用户名称
int len：名称⻓长度
1.
2.
返回值

0：成功
其他：失败
1.
2.
注意

不建议使用本接口，请使用 wifi_station_set_enterprise_username 代替
1.
3.8 wifi_station_clear_username —— 释放连接 WPA2-ENTERPRISE AP 设置用户名占用的资源，并清除相关状态
函数定义

void wifi_station_clear_username (void)
1.
参数

无
1.
返回值

无
1.
注意

不建议使用本接口，请使用 wifi_station_clear_enterprise_username 代替
1.
3.9 wifi_station_connect —— ESP8266 Wi-Fi Station 接口连接 AP
函数定义

bool wifi_station_connect (void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

请勿在 user_init 中调用本接口，请在 ESP8266 Station 使能并初始化完成后调用；
如果 ESP8266 已经连接某个 AP，请先调用 wifi_station_disconnect 断开上一次连接。
1.
2.
3.10 wifi_station_disconnect—— ESP8266 Wi-Fi Station 接口从 AP 断开连接
函数定义

bool wifi_station_disconnect (void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

请勿在 user_init 中调用本接口，本接口必须在系统初始化完成后，并且 ESP8266 Station 接
⼝口使能的情况下调用。
1.
2.
3.11 wifi_station_get_connect_status—— 查询 ESP8266 Wi-Fi Station 接⼝口连接 AP 的状态
函数定义

uint8 wifi_station_get_connect_status (void)
1.
参数

无
1.
返回值

enum{
STATION_IDLE = 0,
STATION_CONNECTING,
STATION_WRONG_PASSWORD,
STATION_NO_AP_FOUND,
STATION_CONNECT_FAIL,
STATION_GOT_IP
};
1.
2.
3.
4.
5.
6.
7.
8.
注意

若为特殊应用场景：调用 wifi_station_set_reconnect_policy 关闭重连功能，且未调用
wifi_set_event_handler_cb 注册 Wi-Fi 事件回调，则本接口失效，无法准确获得连接状态。
1.
2.
3.12 wifi_station_scan—— 获取 AP 的信息
函数定义

bool wifi_station_scan (struct scan_config *config, scan_done_cb_t cb);
1.
参数

struct scan_config {
uint8 *ssid; // AP’s ssid
uint8 *bssid; // AP’s bssid
uint8 channel; //scan a specific channel
uint8 show_hidden; //scan APs of which ssid is hidden.
wifi_scan_type_t scan_type; // scan type, active or passive
wifi_scan_time_t scan_time; // scan time per channel
};

• struct scan_config *config：扫描 AP 的配置参数
- 若 config==null：扫描获取所有可用 AP 的信息
- 若 config.ssid==null && config.bssid==null && config.channel!=null：ESP8266
  Station 接口扫描获取特定信道上的 AP 信息。
- 若 config.ssid!=null && config.bssid==null && config.channel==null：ESP8266
  Station 接口扫描获取所有信道上的某特定名称 AP 的信息。

• scan_done_cb_t cb：扫描完成的 callback
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
返回值

true：成功
false：失败
1.
2.
注意

请勿在 user_init 中调用本接口，本接口必须在系统初始化完成后，并且 ESP8266 Station 接
⼝口使能的情况下调用。
1.
2.
3.13 scan_done_cb_t—— wifi_station_scan 的回调函数
函数定义

void scan_done_cb_t (void *arg, STATUS status)
1.
参数

• void *arg：扫描获取到的 AP 信息指针，以链表形式存储，数据结构 struct bss_info
• STATUS status：扫描结果
1.
2.
返回值

无
1.
注意

请勿在 user_init 中调用本接口，本接口必须在系统初始化完成后，并且 ESP8266 Station 接
⼝口使能的情况下调用。
1.
2.
示例

wifi_station_scan(&config, scan_done);
static void ICACHE_FLASH_ATTR scan_done(void *arg, STATUS status) {
if (status == OK) {
struct bss_info *bss_link = (struct bss_info *)arg;
...
}
}
1.
2.
3.
4.
5.
6.
7.
3.14 wifi_station_ap_number_set—— 设置 ESP8266 Station 最多可记录⼏几个 AP 的信息
函数定义

bool wifi_station_ap_number_set (uint8 ap_number)
1.
参数

uint8 ap_number：记录 AP 信息的最大数目（最大值为 5）
1.
返回值

true：成功
false：失败
1.
2.
注意

ESP8266 Station 成功连入⼀一个 AP 时，可以保存 AP 的 SSID 和 password 记录。
本设置如果与原设置不不同，会更更新保存到 Flash 系统参数区。
1.
2.
3.15 wifi_station_get_ap_info—— 获取 ESP8266 Station 保存的 AP 信息，最多记录 5 个
函数定义

uint8 wifi_station_get_ap_info(struct station_config config[])
1.
参数

struct station_config config[]：AP 的信息，数组⼤大小必须为 5
1.
返回值

记录 AP 的数目
1.
示例

struct station_config config[5];
int i = wifi_station_get_ap_info(config);
1.
2.
3.16 wifi_station_ap_change—— ESP8266 Station 切换到已记录的某号 AP 配置连接
函数定义

bool wifi_station_ap_change (uint8 new_ap_id)
1.
参数

uint8 new_ap_id：AP 记录的 ID 值，从 0 开始计数
1.
返回值

true：成功
false：失败
1.
2.
3.17 wifi_station_get_current_ap_id—— 获取当前连接的 AP 保存记录 ID 值。ESP8266 可记录每一个配置连接的 AP，从 0 开始计数
函数定义

uint8 wifi_station_get_current_ap_id ();
1.
参数

无
1.
返回值

当前连接的 AP 保存记录的 ID 值
1.
3.18 wifi_station_get_auto_connect—— 查询 ESP8266 Station 上电是否会⾃自动连接已记录的 AP（路由）
函数定义

uint8 wifi_station_get_auto_connect(void)
1.
参数

无
1.
返回值

0：    不自动连接 AP
非 0：⾃自动连接 AP。
1.
2.
3.19 wifi_station_set_auto_connect—— 设置 ESP8266 Station 上电是否⾃自动连接已记录的 AP（路由），默认为自动连接
函数定义

bool wifi_station_set_auto_connect(uint8 set)
1.
参数

uint8 set：上电是否⾃自动连接 AP
• 0：不自动连接 AP
• 1：⾃自动连接 AP
1.
2.
3.
返回值

true：成功
false：失败
1.
2.
注意

• 本接口如果在 user_init 中调用，则当前这次上电就生效；如果在其他地方调用，则下一
次上电生效。
• 本设置如果与原设置不同，会更新保存到 Flash 系统参数区
1.
2.
3.
3.20 wifi_station_dhcpc_start—— 开启 ESP8266 Station DHCP client
函数定义

bool wifi_station_dhcpc_start(void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

• DHCP 默认开启。
• DHCP 与静态 IP 功能 wifi_set_ip_info 互相影响，以最后设置的为准：
DHCP 开启，则静态 IP 失效；设置静态 IP，则关闭 DHCP。
1.
2.
3.
3.21 wifi_station_dhcpc_stop—— 关闭 ESP8266 Station DHCP client
函数定义

bool wifi_station_dhcpc_stop(void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

• DHCP 默认开启。
• DHCP 与静态 IP 功能 wifi_set_ip_info 互相影响，以最后设置的为准：
DHCP 开启，则静态 IP 失效；设置静态 IP，则关闭 DHCP。
1.
2.
3.
3.22 wifi_station_dhcpc_status—— 查询 ESP8266 Station DHCP client 状态
函数定义

enum dhcp_status wifi_station_dhcpc_status(void)
1.
参数

无
1.
返回值

enum dhcp_status {
DHCP_STOPPED,
DHCP_STARTED
};
1.
2.
3.
4.
3.23 wifi_station_dhcpc_set_maxtry—— 设置 ESP8266 Station DHCP client 最大重连次数 (默认会一直重连)
函数定义

bool wifi_station_dhcpc_set_maxtry(uint8 num)
1.
参数

uint8 num：最大重连次数
1.
返回值

true：成功
false：失败
1.
2.
3.24 wifi_station_set_reconnect_policy—— 设置 ESP8266 Station 连接 AP 失败或断开后是否重连。默认重连。
函数定义

bool wifi_station_set_reconnect_policy(bool set)
1.
参数

bool set
• true：断开则重连
• false：断开不重连
1.
2.
3.
返回值

true：成功
false：失败
1.
2.
注意

建议在 user_init 中调用本接口
1.
3.25 wifi_station_get_rssi—— 获取ESP8266 Station 已连接的 AP 信号强度
函数定义

uint8 wifi_station_get_rssi(void)
1.
参数

无
1.
返回值

<10：查询成功，返回信号强度
31：查询失败，返回错误码
1.
2.
3.26 wifi_station_set_hostname—— 设置 ESP8266 Station DHCP 分配的主机名称
函数定义

bool wifi_station_set_hostname(char* hostname)
1.
参数

char* hostname：主机名称，最长 32 个字符。
1.
返回值

true：成功
false：失败
1.
2.
3.27 wifi_station_get_hostname—— 查询 ESP8266 Station DHCP 分配的主机名称
函数定义

char* wifi_station_get_hostname(void)
1.
参数

无
1.
返回值

主机名称
1.
4.Soft-AP
4.1 wifi_softap_get_config—— 查询 ESP8266 Wi-Fi SoftAP 接口的当前配置
函数定义

bool wifi_softap_get_config(struct softap_config *config)
1.
参数

struct softap_config *config：ESP8266 SoftAP 配置参数

struct softap_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 ssid_len; // Note: Recommend to set it according to your ssid
    uint8 channel;  // Note: support 1 ~ 13
    AUTH_MODE authmode; // Note: Don't support AUTH_WEP in softAP mode.
    uint8 ssid_hidden;  // Note: default 0
    uint8 max_connection;   // Note: default 4, max 4
    uint16 beacon_interval; // Note: support 100 ~ 60000 ms, default 100
};
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
返回值

true：成功
false：失败
1.
2.
4.2 wifi_softap_get_config_default—— 查询 ESP8266 Wi-Fi SoftAP 接口保存在 Flash 中的配置
函数定义

bool wifi_softap_get_config_default(struct softap_config *config)
1.
参数

struct softap_config *config：ESP8266 SoftAP 配置参数

struct softap_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 ssid_len; // Note: Recommend to set it according to your ssid
    uint8 channel;  // Note: support 1 ~ 13
    AUTH_MODE authmode; // Note: Don't support AUTH_WEP in softAP mode.
    uint8 ssid_hidden;  // Note: default 0
    uint8 max_connection;   // Note: default 4, max 4
    uint16 beacon_interval; // Note: support 100 ~ 60000 ms, default 100
};
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
返回值

true：成功
false：失败
1.
2.
4.3 wifi_softap_set_config—— 设置 Wi-Fi SoftAP 接口配置，并保存到Flash
函数定义

bool wifi_softap_set_config (struct softap_config *config)
1.
参数

struct softap_config *config：ESP8266 SoftAP 配置参数

struct softap_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 ssid_len; // Note: Recommend to set it according to your ssid
    uint8 channel;  // Note: support 1 ~ 13
    AUTH_MODE authmode; // Note: Don't support AUTH_WEP in softAP mode.
    uint8 ssid_hidden;  // Note: default 0
    uint8 max_connection;   // Note: default 4, max 4
    uint16 beacon_interval; // Note: support 100 ~ 60000 ms, default 100
};
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
返回值

true：成功
false：失败
1.
2.
注意

• 请在 ESP8266 SoftAP 使能的情况下，调用本接口。

• 本设置如果与原设置不同，将更更新保存到 Flash 系统参数区。

• 因为 ESP8266 只有一个信道，因此 SoftAP+Station 共存模式时，ESP8266 SoftAP 接口会
⾃自动调节信道与 ESP8266 Station 一致，详细说明请参考附录。
1.
2.
3.
4.
5.
6.
4.4 wifi_softap_set_config_current—— 设置 Wi-Fi SoftAP 接口配置，不保存到Flash
函数定义

bool wifi_softap_set_config_current (struct softap_config *config)
1.
参数

struct softap_config *config：ESP8266 SoftAP 配置参数

struct softap_config {
    uint8 ssid[32];
    uint8 password[64];
    uint8 ssid_len; // Note: Recommend to set it according to your ssid
    uint8 channel;  // Note: support 1 ~ 13
    AUTH_MODE authmode; // Note: Don't support AUTH_WEP in softAP mode.
    uint8 ssid_hidden;  // Note: default 0
    uint8 max_connection;   // Note: default 4, max 4
    uint16 beacon_interval; // Note: support 100 ~ 60000 ms, default 100
};
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
返回值

true：成功
false：失败
1.
2.
注意

• 请在 ESP8266 SoftAP 使能的情况下，调用本接口。

• 本设置如果与原设置不同，将更更新保存到 Flash 系统参数区。

• 因为 ESP8266 只有一个信道，因此 SoftAP+Station 共存模式时，ESP8266 SoftAP 接口会
⾃自动调节信道与 ESP8266 Station 一致，详细说明请参考附录。
1.
2.
3.
4.
5.
6.
4.5 wifi_softap_get_station_num—— 获取 ESP8266 SoftAP 下连接的Station 个数
函数定义

uint8 wifi_softap_get_station_num(void)
1.
参数

无
1.
返回值

ESP8266 SoftAP 下连接的 Station 个数
1.
4.6 wifi_softap_get_station_info—— 获取 ESP8266 SoftAP 接口下连入的 Station 的信息，包括 MAC 和 IP
函数定义

struct station_info * wifi_softap_get_station_info(void)
1.
参数

无
1.
返回值

struct station_info*：Station 信息的结构体

#define	STAILQ_ENTRY(type)						\
struct {								\
	struct type *stqe_next;	/* next element */			\
}

typedef struct ip_addr {
  union {
    ip6_addr_t ip6;
    ip4_addr_t ip4;
  } u_addr;
  /** @ref lwip_ip_addr_type */
  u8_t type;
} ip_addr_t;

struct station_info {
    STAILQ_ENTRY(station_info)    next;

    uint8 bssid[6];
    struct ip_addr ip;
};
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
注意

本接口基于 DHCP 实现，因此不支持静态 IP 或者其他没有重新 DHCP 的情况
1.
4.7 wifi_softap_free_station_info—— 释放调用 wifi_softap_get_station_info 时结构体 station_info 占用的空间
函数定义

void wifi_softap_free_station_info(void)
1.
参数

无
1.
返回值

无
1.
4.8 wifi_softap_dhcps_start—— 开启 ESP8266 SoftAP DHCP server
函数定义

bool wifi_softap_dhcps_start(void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

• DHCP 默认开启。
• DHCP 与静态 IP 功能 wifi_set_ip_info 互相影响，以最后设置的为准：
DHCP 开启，则静态 IP 失效；设置静态 IP，则关闭 DHCP。
1.
2.
3.
4.9 wifi_softap_dhcps_stop—— 关闭 ESP8266 SoftAP DHCP server。默认开启 DHCP。
函数定义

bool wifi_softap_dhcps_stop(void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
4.10 wifi_softap_set_dhcps_lease—— 设置 ESP8266 SoftAP DHCP server 分配 IP 地址的范围
函数定义

bool wifi_softap_set_dhcps_lease(struct dhcps_lease *please)
1.
参数

struct dhcps_lease {
struct ip_addr start_ip;
struct ip_addr end_ip;
};
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

• 设置的 IP 分配范围必须与 ESP8266 SoftAP IP 在同一网段。
• 本接口必须在 ESP8266 SoftAP DHCP server 关闭 wifi_softap_dhcps_stop 的情况下设
置。
• 本设置仅对下一次使能的 DHCP server 生效 wifi_softap_dhcps_start，如果 DHCP server
再次被关闭，则需要重新调用本接口设置 IP 范围；否则之后 DHCP server 重新使能，会使
⽤用默认的 IP 地址分配范围。
1.
2.
3.
4.
5.
6.
示例

void dhcps_lease_test(void)
{
	struct dhcps_lease dhcp_lease;
	const char* start_ip = “192.168.5.100”;
	const char* end_ip = “192.168.5.105”;
	dhcp_lease.start_ip.addr = ipaddr_addr(start_ip);
	dhcp_lease.end_ip.addr = ipaddr_addr(end_ip);
	wifi_softap_set_dhcps_lease(&dhcp_lease);
}
或者
void dhcps_lease_test(void)
{
	struct dhcps_lease dhcp_lease;
	IP4_ADDR(&dhcp_lease.start_ip, 192, 168, 5, 100);
	IP4_ADDR(&dhcp_lease.end_ip, 192, 168, 5, 105);
	wifi_softap_set_dhcps_lease(&dhcp_lease);
}
void user_init(void)
{
	struct ip_info info;
	wifi_set_opmode(STATIONAP_MODE); //Set softAP + station mode
	wifi_softap_dhcps_stop();
	IP4_ADDR(&info.ip, 192, 168, 5, 1);
	IP4_ADDR(&info.gw, 192, 168, 5, 1);
	IP4_ADDR(&info.netmask, 255, 255, 255, 0);
	wifi_set_ip_info(SOFTAP_IF, &info);
	dhcps_lease_test();
	wifi_softap_dhcps_start();
}
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.
28.
29.
4.11 wifi_softap_get_dhcps_lease—— 查询 ESP8266 SoftAP DHCP server 分配 IP 地址的范围
函数定义

bool wifi_softap_get_dhcps_lease(struct dhcps_lease *please)
1.
参数

struct dhcps_lease {
struct ip_addr start_ip;
struct ip_addr end_ip;
};
1.
2.
3.
4.
返回值

true：成功
false：失败
1.
2.
注意

本接口仅支持在 ESP8266 SoftAP DHCP server 使能的情况下查询。
1.
4.12 wifi_softap_set_dhcps_lease_time—— 设置 ESP8266 SoftAP DHCP server 的租约时间。默认为 120 分钟。
函数定义

bool wifi_softap_set_dhcps_lease_time(uint32 minute)
1.
参数

uint32 minute：租约时间，单位：分钟，取值范围：[1，2880]
1.
返回值

true：成功
false：失败
1.
2.
注意

本接口仅支持在 ESP8266 SoftAP DHCP server 使能的情况下查询。
1.
4.13 wifi_softap_get_dhcps_lease_time—— 查询 ESP8266 SoftAP DHCP server 的租约时间
函数定义

uint32 wifi_softap_get_dhcps_lease_time(void)
1.
参数

无
1.
返回值

租约时间，单位：分钟
1.
注意

本接口仅支持在 ESP8266 SoftAP DHCP server 使能的情况下查询。
1.
4.14 wifi_softap_reset_dhcps_lease_time—— 复位 ESP8266 SoftAP DHCP server 的租约时间。恢复到 120 分钟。
函数定义

bool wifi_softap_reset_dhcps_lease_time(void)
1.
参数

无
1.
返回值

true：成功
false：失败
1.
2.
注意

本接口仅支持在 ESP8266 SoftAP DHCP server 使能的情况下查询。
1.
4.15 wifi_softap_dhcps_status—— 获取 ESP8266 SoftAP DHCP server 状态
函数定义

enum dhcp_status wifi_softap_dhcps_status(void)
1.
参数

无
1.
返回值

enum dhcp_status {
DHCP_STOPPED,
DHCP_STARTED
};
1.
2.
3.
4.
4.16 wifi_softap_set_dhcps_offer_option—— 设置 ESP8266 SoftAP DHCP server 属性
函数定义

bool wifi_softap_set_dhcps_offer_option(uint8 level, void* optarg)
1.
参数

enum dhcps_offer_option{
OFFER_START = 0x00,
OFFER_ROUTER = 0x01,
OFFER_END
};

• uint8 level：OFFER_ROUTER，设置 router 信息
• void* optarg：bit0, 0 禁用 router 信息；bit0, 1 启用 router 信息；默认为 1
1.
2.
3.
4.
5.
6.
7.
8.
返回值

登录后复制 
true：成功
false：失败