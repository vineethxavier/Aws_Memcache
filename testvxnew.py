import pymysql
import timeit
import random
import memcache
#clouddb.cbozhbcc3p5p.us-west-2.rds.amazonaws.com:3306
conn = pymysql.connect(user='vineethxavier', passwd='password',host='vxdbinstance.cwo47igf50ip.us-west-2.rds.amazonaws.com',database='dbinstancename')
cur = conn.cursor()
memc = memcache.Client(['vxcluster.tgwymm.cfg.usw2.cache.amazonaws.com:11211'],debug =1)


def no_memcache(passquery):   
    Query1=passquery
    execution_time=execute_query1(Query1)
    print Query1 + ' Execution time is ' + str(execution_time)

def execute_query1(Que):
    onn = pymysql.connect(user='vineethxavier', passwd='password',host='vxdbinstance.cwo47igf50ip.us-west-2.rds.amazonaws.com',database='dbinstancename')
    cur = conn.cursor()
    #memc = memcache.Client(['vxcluster.tgwymm.cfg.usw2.cache.amazonaws.com:11211'],debug =1)

    start_time = timeit.default_timer()
    cur.execute(Que)
    finish_time_tmp = timeit.default_timer() - start_time
    print finish_time_tmp
    count = 0
    for rows in cur.fetchall():
        count = count + 1
    print cur.fetchall()
    finish_time = timeit.default_timer() - start_time



def memcache(passquery):
    q1result=passquery
    
    
    q1mc = memc.get('q1result')
    print "q1mc :\n"
    print q1mc
    #print "q4mc :\n"
    #print q4mc 
    if not q1mc:  #cache is empty
        execution_time = execute_query(Query1)
        print Query1 + ' Execution time without memcache first time is ' + str(execution_time)
        cur.execute(Query1)
        rows=cur.fetchall()
        memc.set('q1result',rows)
    else: #cache not empty, access it
        count = 0
        print "loaded data from memcache"
        start_time = timeit.default_timer()
        for row in q1mc:
            count = count + 1
        finish_time_tmp = timeit.default_timer() - start_time
        print Query1 + ' Execution time with memcache is ' + str(finish_time_tmp)


def execute_query(Que):
    onn = pymysql.connect(user='vineethxavier', passwd='password',host='vxdbinstance.cwo47igf50ip.us-west-2.rds.amazonaws.com',database='dbinstancename')
    cur = conn.cursor()
    #memc = memcache.Client(['vxcluster.tgwymm.cfg.usw2.cache.amazonaws.com:11211'],debug =1)

    start_time = timeit.default_timer()
    cur.execute(Que)
    finish_time_tmp = timeit.default_timer() - start_time
    print finish_time_tmp
    count = 0
    for rows in cur.fetchall():
        count = count + 1
    print cur.fetchall()
    finish_time = timeit.default_timer() - start_time
    