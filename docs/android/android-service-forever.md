# 安卓中如何保持一个程序不在前台的时候不被系统杀掉

### 背景
一个同事问我怎么在DMac中实现不被系统杀掉的，并且惊奇的告诉我说我们公司的DMac在Pico升级到4之后，仍然可以不被系统杀掉。

其实严格意义上，可能没有这种办法吧。并且想要应用一直保持这种能力，严格上来说，系统升级就得重新测试调整代码。

### 解答一下

为什么我们的DMac可以实现不被系统杀掉呢？  

其实我们的DMac并不能保持不被所有同版本安卓系统杀掉，只能保证在Pico头盔中实际上不被系统杀掉。

最关键的几行代码：

```
PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, 0);
AlarmManager manager = (AlarmManager) getSystemService(ALARM_SERVICE);
long triggerAtTime = SystemClock.elapsedRealtime() + Minutes;
manager.set(AlarmManager.ELAPSED_REALTIME_WAKEUP, triggerAtTime, pendingIntent);
```

如上代码，借助PendingIntent和AlarmManager，其实就是暴力的定时启动DMac。而在Pico中，系统杀死进程有一个能确定的缺省等待时间，所以在等待时间到来之前启动一下DMac，又重新进入了等待计时。