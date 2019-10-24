

automake 工具集安装
```
  sudo apt-get install autoconf automake libtool make
  ```
### 下载n2n

```
git clone https://github.com/ntop/n2n.git
```
  

### 手动编译安装n2n
```
./autogen.sh
./configure
make

# optionally install
make install

cp supernode /usr/sbin/
cp edge /usr/sbin/

```



启动服务端节点
```
supernode -l 1000 -v >/dev/null &
```



mount /dev/sda3 /mnt/sda3 ; tar -C /overlay -cvf - . | tar -C /mnt/sda3 -xf - ; umount /mnt/sda3


block detect > /etc/config/fstab; \
   sed -i s/option$'\t'enabled$'\t'\'0\'/option$'\t'enabled$'\t'\'1\'/ /etc/config/fstab; \
   sed -i s#/mnt/sda3#/overlay# /etc/config/fstab; \
   cat /etc/config/fstab;
   
   
   edge -d n2n0 -c mynetwork -k encryptme -a 10.0.0.239 -l 123.207.142.90:1000
   edge -d n2n0 -c mynetwork -k encryptme -a 10.0.0.239 -l 127.0.0.1:1000
   
mirrors.ustc.edu.cn/lede