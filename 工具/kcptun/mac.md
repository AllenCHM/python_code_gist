# 准备工作先
准备什么？当然下载 KcpTun 的客户端啦，访问这里 Releases · xtaci/kcptun。下载哪一个？废话！当然是：kcptun-darwin-amd64-20xxxxxx.tar.gz 这个啦！

# 然后 Follow Me
下载好了吗？好了你怎么不解压？怎么解压还要我教吗？

得到两个文件，client_darwin_amd64 和 server_darwin_amd64，后者不用管，我们只需要使用到 client 客户端那个文件即可

### 放好客户端程序

建议到 /opt 下新建一个目录 KcpTun，然后把 client_darwin_amd64 放到 /opt/KcpTun 里面去。

### 创建 plist 文件
命令行 cd /Library/LaunchDaemons/ 进入 LaunchDaemons 目录

然后 sudo nano local.KcpTunClient.plist 创建 local.KcpTunClient.plist 文件并进入编辑

填入内容如下：
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>             <string>local.KcpTunClient</string>
    <key>Disabled</key>          <false/>
    <key>RunAtLoad</key>         <true/>
    <key>KeepAlive</key>         <false/>
    <key>LaunchOnlyOnce</key>    <true/>
    <key>ProgramArguments</key>
        <array>
            <!-- KcpTun 客户端程序路径 -->
            <string>/opt/KcpTun/client_darwin_amd64</string>
            <string>-r</string>
            <!-- KcpTun 服务端 IP:端口 -->
            <string>1.2.3.4:29900</string>
            <string>-l</string>
            <!-- 监听的本地端口 -->
            <string>:2333</string>
            <string>-mode</string>
            <!-- 加速模式，根据服务端修改 -->
            <string>fast3</string>
            <string>-crypt</string>
            <!-- 加密模式，根据服务端修改 -->
            <string>none</string>
        </array>
</dict>
</plist>
```

根据自身服务器端内容修改上方说明参数，然后 control + O 保存，control + X 退出编辑。

### 设置自启
直接在 LaunchDaemons 目录内执行 launchctl load -w local.KcpTunClient.plist 即可，无需 sudo 亦可。然后打开活动监视器看看有没有“client_darwin_amd64”进程。或者执行 ps aux|grep client_ 查看。

### 设置一下 Shadowsocks(R)

此时的 SS 小飞机新增一个服务器如下：


|服务器	|端口	|加密方式|	密码|	备注|
|---|---|---|---|---|
|127.0.0.1	|本地 KcpTun 监听端口（刚刚 plist 的 2333）|	服务器SS加密，一般是 aes-256-cfb 或 rc4-md5（非 KcpTun 加密方式）	|服务器SS密码（非 KcpTun 密码）
|127.0.0.1	|本地 KcpTun 监听端口（刚刚 plist 的 2333）|	服务器SS加密方式，除了常见的 aes-256-cfb 和 rc4-md5，还有 chacha20 等	|服务器SS密码（非 KcpTun 密码）	|如果服务器端是使用的 SSR，此时的 SSR 客户端还应选择对应的协议和混淆，一定要保证正确。如果是 SSR 客户端需要兼容原版 SS，协议选择 origin，混淆选择 plain 即可。
然后…就没了，发现速度飞起来了