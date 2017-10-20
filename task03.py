fin = open ("running-config.cfg")
import string

for lin in fin:
	ip_number = lin.replace('172' , '192')
	print (ip_number)



