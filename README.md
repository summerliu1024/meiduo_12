# meiduo_12
大型电商项目 docker fastdfs celery
##启动步骤
1.cd到front_end_pc,live-server启动前端静态页面

2.开启redis服务 redis-server

3.cd到celery_tasks文件夹，开启celery异步任务
celery -A celery_tasks.main worker -l info

4.运行fastdfs 

tracker 需要修改映射目录

docker run -dti --network=host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker

storage 需要修改trackerip地址和映射目录

docker run -dti --network=host --name storage -e TRACKER_SERVER=10.211.55.5:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage

5.运行项目manage.py文件
