#coding:utf8
import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    try:
        rediscli = redis.StrictRedis(host='192.168.2.212', port=6379, db=0)
        # 指定mysql数据库
        mysqlcli = MySQLdb.connect(host='192.168.2.196', user='root', passwd='123', db='text', port=3306, charset='utf8')
        print '数据库连接成功'
    except Exception,e:
        print '数据库连接失败'
        print str(e)
        exit()

    while True:
        print '数据从redis提取数据'
        source, data = rediscli.blpop(["boss:items"])
        # print source # redis里的键
        # print data # 返回的数据
        item = json.loads(data)
        print('提出数据')

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            print item

            # 使用execute方法执行SQL INSERT语句
            # sql = "insert into Tiger(position, company,location, time,job_duty,salary,url) values('%s','%s', '%s', '%s','%s','%s','%s') on duplicate key update " \
            #       "position=values(position),company=values(company),location=values(location),time=values(time),job_duty=values(job_duty),salary=values(salary),url=values(url)," % (item['position'], item['company'], item['location'], item['time'],item['job_duty'],item['salary'],item['url'])
            sql = "insert into Tiger(position,company,location,time,duty,salary,url) values('%s','%s', '%s', '%s','%s','%s','%s') on duplicate key update position=values(position),company=values(company),location=values(location),time=values(time),duty=values(duty),salary=values(salary)" % (item['position'], item['company'], item['location'], item['time'],item['duty'],item['salary'],item['url'])
            # sql = "insert into Tiger(position,company,location,time,duty,salary,url) values('%s','%s', '%s', '%s','%s','%s','%s') on duplicate key update position=values(position),company=values(company),location=values(location),time=values(time),duty=values(duty),salary=values(salary)" % ('test','test','test','test','test','test','test',)
            # sql = 'insert ignore into Tiger(position,company,location,time,job_duty,salary,url,) VALUES(%s,%s,%s,%s,%s,%s,%s,)'
            # cur.execute(sql, (item['position'], item['company'], item['location'], item['time'], item['job_duty'], item['salary'],item['url']))
            cur.execute(sql)
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "插入成功"
        except Exception,e:
            print '插入失败'
            print str(e)

if __name__ == '__main__':
    main()