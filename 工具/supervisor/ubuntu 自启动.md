进入/lib/systemd/system目录，查看是否有supervisor.service文件,若没有创建supervisor.service文件（一般情况下都已经自动创建好了）

```
[Unit]
Description=supervisor
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```


设置开机启动
```
chmod 766 supervisor.service
systemctl enable supervisor.service
systemctl daemon-reload
```