#!usr/bin/python    
#Filename:backup_ver1.py


import os
import time
source=['D:\\test_backup','d:\\teleport_ultra']
#on windows  source=[r'D:\test_backup',r'd:\teleport_ultra']
target_dir='D:\\backup\\'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')

if len(comment) == 0: # check if a comment was entered
	target_name = today + os.sep + now + '.zip'
else:
	target_name = today + os.sep + now + '_' +\
	comment.replace(' ', '_') + '.zip'

#用斜杠来连接下一行代码

if not os.path.exists(today):
	os.mkdir(today) # make directory
	print 'Successfully created directory', today


zip_command="HaoZipC a -tzip %s %s"%(target_name,' '.join(source))

if os.system(zip_command)==0:
    print 'Successful backup to',target_name
else:
    print 'Backup fail'
    