#!/usr/bin/python3
import subprocess
import cgi
print("contect-type: text/html")
print()
data = cgi.FieldStorage()
x = data.getvalue("x")
if (("a" in x) and ("q" in x)):
    cmd = "sudo docker ps -aq"
elif ("q" in x):
    cmd = "sudo docker ps -q"
elif ("a" in x ) :
    cmd = "sudo docker ps -a"
else:
    cmd = "sudo docker ps"
output = subprocess.getoutput(cmd)
print(output)
