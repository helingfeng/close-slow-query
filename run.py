import sys
import os
import configparser

# 读取配置文件
script_path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'

cp = configparser.ConfigParser()
cp.read(script_path, encoding="utf-8")

config = {}
try:
    config['host'] = cp.get('server', 'host')
    config['port'] = cp.get('server', 'port')
    config['user'] = cp.get('server', 'user')
    config['password'] = cp.get('server', 'password')
    config['execute_time'] = cp.get('server', 'execute_time')
except:
    print("config.ini ERROR: section [server]")
    exit()

print("[mysql config] MySQLdb://%s:%s@%s %ss" % (
    config['user'], config['password'], config['host'], config['port']))

try:
    import pymysql
except ImportError:
    raise ImportError('\n\nMySQLdb not installed, exit\n\nyum install MySQL-python\npip install mysql-python')

print("running...")

execute_time = int(config['execute_time'])

try:
    db = pymysql.connect(host=config['host'], user=config['user'], password=config['password'])
except ConnectionError:
    print('ERROR: db connect failed.\n  Check you configure in config.ini')
    sys.exit(502)

# and `USER`!='root'
sql = '''SELECT `ID`, `USER`, `HOST`, `DB`, `COMMAND`, `TIME`, `STATE`, `INFO`
FROM `information_schema`.`PROCESSLIST`
WHERE (
`DB`!='information_schema' and `STATE`!='' and `STATE`!='Waiting for INSERT' and `STATE`!='Locked'
)
and  `TIME` >= %s 
''' % execute_time

cursor = db.cursor()
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)
    cursor.execute("kill %s" % row[0])
