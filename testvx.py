import pymysql
import timeit
import random
import memcache
#clouddb.cbozhbcc3p5p.us-west-2.rds.amazonaws.com:3306
conn = pymysql.connect(user='vineethxavier', passwd='password',host='vxdbinstance.cwo47igf50ip.us-west-2.rds.amazonaws.com',database='dbinstancename')
cur = conn.cursor()
memc = memcache.Client(['vxcluster.tgwymm.cfg.usw2.cache.amazonaws.com:11211'],debug =1)
Query1="SELECT * from ajfull order by rand() limit 1"
Query2="SELECT * from ajfull where STNAME = 'Montana' LIMIT 1"
Query3="SELECT Max(AGEGRP) as MaxAGEGRP,Max(IMPRACE) as MaxIMPRACE,min(AGEGRP) as MinSTATE,min(IMPRACE) as MinIMPRACE from ajfull where AGEGRP != 'AGEGRP' and IMPRACE != 'IMPRACE' and AGEGRP>0 and IMPRACE>0 limit 1"
Query4="SELECT * from ajfull where RESPOP = '3' limit 1"

#query_option=1
def execute_query(Que):

    start_time = timeit.default_timer()
    cur.execute(Que)
    finish_time_tmp = timeit.default_timer() - start_time
    print finish_time_tmp
    count = 0
    for rows in cur.fetchall():
        count = count + 1
    print cur.fetchall()
    finish_time = timeit.default_timer() - start_time
    #print finish_time
    return finish_time
def no_memcache():
    query_option = random.randint(1, 4)
    if query_option == 1:
        execution_time=execute_query(Query1)
        print Query1 + ' Execution time is ' + str(execution_time)
    elif query_option == 2:
        execution_time=execute_query(Query2)
        print Query2 + ' Execution time is ' + str(execution_time)
    elif query_option == 3:
        execution_time=execute_query(Query3)
        print Query3 + ' Execution time is ' + str(execution_time)
    elif query_option == 4:
        execution_time=execute_query(Query4)
        print Query4 + ' Execution time is ' + str(execution_time)

def memcache():
    query_option = random.randint(1, 3)
    print "query option : \n"
    print query_option
    q1mc = memc.get('q1result')
    q2mc = memc.get('q2result')
    q3mc = memc.get('q3result')
    #q4mc = memc.get('q4result')
    print "q1mc :\n"
    print q1mc
    print "q2mc :\n"
    print q2mc
    print "q3mc :\n"
    print q3mc
    #print "q4mc :\n"
    #print q4mc 
    if query_option == 1:
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
    elif query_option == 2:
        if not q2mc:
            execution_time = execute_query(Query2)
            print Query2 + ' Execution time without memcache first time is ' + str(execution_time)
            cur.execute(Query2)
            rows = cur.fetchall()
            memc.set('q2result', rows)
        else:
            count = 0
            print "loaded data from memcache"
            start_time = timeit.default_timer()
            for row in q2mc:
                count = count + 1
            finish_time_tmp = timeit.default_timer() - start_time
            print Query2 + ' Execution time with memcache is ' + str(finish_time_tmp)
    elif query_option == 3:
        if not q3mc:
            execution_time = execute_query(Query3)
            print Query3 + ' Execution time without memcache first time is ' + str(execution_time)
            cur.execute(Query3)
            rows = cur.fetchall()
            memc.set('q3result', rows)
        else:
            count = 0
            print "loaded data from memcache"
            start_time = timeit.default_timer()
            for row in q3mc:
                count = count + 1
            finish_time_tmp = timeit.default_timer() - start_time
            print Query3 + ' Execution time with memcache is ' + str(finish_time_tmp)
    

### Main:
while(1):
    choice=raw_input("Enter your choice \n1.without cache \n2.using memcahe\n3.exit\n")
    if int(choice) == 1:
        no_memcache()
    elif int(choice) == 2:
        memcache()
    elif int(choice) == 3:
        break
    else:
        print "Enter correct choice"
cur.close()
conn.close()
