定时检测是否存在超时 SQL 查询，若存在将其结束（KILL）

## quick start

```shell
git clone git@github.com:helingfeng/close-slow-query.git

cp config.ini.example config.ini

python run.py
```

## config

配置 MYSQL DB 账号密码，任务终止最大时间，结束任务记录

```
host=localhost
port=3306
user=root
password=123456
execute_time=60
kill_log=./log/slow.log
```

