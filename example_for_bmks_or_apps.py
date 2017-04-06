'''
Author : ABHIRAJ.G
Email id : abhiraj.garakapati@gmail.com
'''

# Import section:
#########################################
import MySQLdb
import os
import re
import sys
from prettytable import PrettyTable
import HTML
import glob
import commands
#########################################

headers=['C  ','C/C++ Header','C++  ','Fortran']

def app_no_child():

	d = {}
	file_object  = open('all_apps.txt','r')

	t=0
	t = HTML.Table(header_row= HTML.TableRow(["AppName","Total C files","Total lines of C code","Total C/C++ Header files","Total lines of C/C++ Header code","Total C++ files","Total lines of C++ code","Total Fortran files","Total lines of Fortran code"], bgcolor='LightGrey'))

	for line in file_object: 
		a=line
		app_or_bmk_name=a.split(' ')[0]
		# print b
		# os.system('echo '+app_or_bmk_name+'')
		
		d[app_or_bmk_name] = {}
		
		
		os.system('cloc /home/qa/AQI/GROUPS/app_no_child/'+app_or_bmk_name+'/src/'+app_or_bmk_name+'.tar.bz2 > temp.txt')
		
		for i in headers:
			pattern = i
			cmd = "grep '"+pattern+"' temp.txt"
			ret,op = commands.getstatusoutput(cmd)
			if (op == ''):
				d[app_or_bmk_name][pattern] = ['N/A','N/A']
			elif (str(op.split('\n')[0].split()[1]) == 'Header'):
				d[app_or_bmk_name][pattern] = [op.split('\n')[0].split()[2],op.split('\n')[0].split()[-1]]
			else:
				d[app_or_bmk_name][pattern] = [op.split('\n')[0].split()[1],op.split('\n')[0].split()[-1]]
		
		temp=[app_or_bmk_name,d[app_or_bmk_name]['C  '][0],d[app_or_bmk_name]['C  '][1],d[app_or_bmk_name]['C/C++ Header'][0],d[app_or_bmk_name]['C/C++ Header'][1],d[app_or_bmk_name]['C++  '][0],d[app_or_bmk_name]['C++  '][1],d[app_or_bmk_name]['Fortran'][0],d[app_or_bmk_name]['Fortran'][1]]
		
		t.rows.append(temp)
		
	print t
	
def app_child():

	d = {}
	file_object  = open('all_suits.txt','r')

	t=0
	t = HTML.Table(header_row= HTML.TableRow(["SuitName","Total C files","Total lines of C code","Total C/C++ Header files","Total lines of C/C++ Header code","Total C++ files","Total lines of C++ code","Total Fortran files","Total lines of Fortran code"], bgcolor='LightGrey'))

	for line in file_object: 
		a=line
		app_or_bmk_name=a.split(' ')[0]
		# print b
		# os.system('echo '+app_or_bmk_name+'')
		
		d[app_or_bmk_name] = {}
		
		print app_or_bmk_name
		os.system('cloc /home/qa/AQI/GROUPS/app_child/'+app_or_bmk_name+'/src/'+app_or_bmk_name+'.tar.bz2 > temp.txt')
		
		for i in headers:
			pattern = i
			cmd = "grep '"+pattern+"' temp.txt"
			ret,op = commands.getstatusoutput(cmd)
			if (op == ''):
				d[app_or_bmk_name][pattern] = ['N/A','N/A']
			elif (str(op.split('\n')[0].split()[1]) == 'Header'):
				d[app_or_bmk_name][pattern] = [op.split('\n')[0].split()[2],op.split('\n')[0].split()[-1]]
			else:
				d[app_or_bmk_name][pattern] = [op.split('\n')[0].split()[1],op.split('\n')[0].split()[-1]]
		
		temp=[app_or_bmk_name,d[app_or_bmk_name]['C  '][0],d[app_or_bmk_name]['C  '][1],d[app_or_bmk_name]['C/C++ Header'][0],d[app_or_bmk_name]['C/C++ Header'][1],d[app_or_bmk_name]['C++  '][0],d[app_or_bmk_name]['C++  '][1],d[app_or_bmk_name]['Fortran'][0],d[app_or_bmk_name]['Fortran'][1]]
		print "done."
		t.rows.append(temp)
		
	print t
	
# app_no_child()	
app_child()
