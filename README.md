定时检测是否存在超时 SQL 查询，并将其杀死（KILL）

## 快速开始

```shell
git clone git@github.com:helingfeng/close-slow-query.git

cp config.ini.example config.ini

python run.py
```

## 定时执行

```shell

crontab -e

# 添加每分钟执行
*/1 * * * * python run.py
```

## 配置文件

配置 MYSQL DB 账号密码，任务终止最大时间，结束任务记录

```
host=localhost
port=3306
user=root
password=123456
execute_time=60
kill_log=./log/slow.log
```

