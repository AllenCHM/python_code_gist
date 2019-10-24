#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='my-index', ignore=400)
root@20181227

echo -e '# /etc/fstab: static file system information.\n' > /etc/fstab && \
echo -e "# Use 'blkid' to print the universally unique identifier for a\n"  >> /etc/fstab && \
echo -e "# device; this may be used with UUID= as a more robust way to name devices\n" >> /etc/fstab && \
echo -e "# that works even if disks are added and removed. See fstab(5).\n">> /etc/fstab && \
echo -e "#\n">> /etc/fstab && \
echo -e "# <file system> <mount point>   <type>  <options>       <dump>  <pass>\n">> /etc/fstab && \
echo -e "# / was on /dev/vda1 during installation\n">> /etc/fstab && \
echo -e "UUID=3912d405-202c-45a4-96f9-0d5fc39ab7ce /               ext4    errors=remount-ro 0       1  \n">> /etc/fstab && \
echo -e "/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0 \n">> /etc/fstab && \
echo -e "/dev/vdb1 /nash ext4 defaults 0 0' \n">> /etc/fstab


echo -e '# /etc/fstab: static file system information.\n' > /etc/fstab && \
echo -e "# Use 'blkid' to print the universally unique identifier for a\n"  >> /etc/fstab && \
echo -e "# device; this may be used with UUID= as a more robust way to name devices\n" >> /etc/fstab && \
echo -e "# that works even if disks are added and removed. See fstab(5).\n">> /etc/fstab && \
echo -e "#\n">> /etc/fstab && \
echo -e "# <file system> <mount point>   <type>  <options>       <dump>  <pass>\n">> /etc/fstab && \
echo -e "# / was on /dev/vda1 during installation\n">> /etc/fstab && \
echo -e "UUID=3912d405-202c-45a4-96f9-0d5fc39ab7ce /               ext4    errors=remount-ro 0       1  \n">> /etc/fstab && \
echo -e "/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0 \n">> /etc/fstab && \
echo -e "/dev/vdb1 /mnt ext4 defaults 0 0 ">> /etc/fstab

:s/- TRACKER_SERVER_HOST=172\.18\.53\.243/- TRACKER_SERVER_HOST=fdfs_tracker_ci/

    external_links:
      - fdfs_tracker_ci:fdfs_tracker_ci
    networks:
      - mynet

networks:
  mynet:
    external: true