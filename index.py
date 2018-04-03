import csv
import pymysql
import time
import testvxnew as obj1
import cgi


from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def mainpage():
	return render_template('index.html')
#inserring csv file to RDS
@app.route('/loadFileRDS',methods=['GET','POST'])
def loadFileRDS():
		#if(request.form['rds'] == "Upload to RDS"):
		if request.method == 'POST':
		# Connect to Amazon S3			
			mydb = pymysql.connect(host='vxdbinstance.cwo47igf50ip.us-west-2.rds.amazonaws.com',user='vineethxavier',passwd='password',db='dbinstancename',local_infile=True)
			cursor = mydb.cursor()
			#data_files = request.files['RDS']
			startTime = time.time()
			cursor.execute("load data local infile 'C:/Users/Vineeth Xavier/Desktop/UNPrecip.csv' into table dbinstancename.UNPrecip_15 fields terminated by ',' optionally enclosed by '\"' lines terminated by '\r\n' IGNORE 1 LINES")
			mydb.commit()
			endTime = time.time()
			totalTime = endTime - startTime
			print 'total time is '+str(totalTime)+' seconds'
			session['total_time'] = totalTime   #passing time to html
			cursor.close()
			return render_template('index.html')


# without mem
@app.route('/fetchWithoutMem', methods=['GET', 'POST'])
def fetchWithoutMem():
    if request.method == 'POST':
		
		passquery =  request.form['text']
		obj1.no_memcache(passquery)
    return render_template('index.html')

#with mem
@app.route('/fetchWithMem', methods=['GET', 'POST'])
def fetchWithMem():
    if request.method == 'POST':
		
		passquery =  request.form['text']
		obj1.memcache(passquery)
    return render_template('index.html')



if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.debug=True
	app.run(
		host='127.0.0.1',
		port=int('5000'),
		debug=True
	)