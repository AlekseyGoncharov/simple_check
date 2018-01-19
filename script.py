
import subprocess
# get processlist
spisok = subprocess.Popen(['mysql', '-uroot','-ppassword', '-e', "show processlist"], stdout=subprocess.PIPE)
st = True
res = []
while st:
	st = spisok.stdout.readline()
	st1 = st.decode('utf-8')
	#print(st1)
	res.append(st1.split('\t'))
res.pop(0)
res.pop()

code = 0
# check running time and return id from zabbix
for i in res:
	if int(i[5]) >= 86400 :
		code = 2
		break
	elif int(i[5]) >= 10800:
		code = 1
print(code)
	

