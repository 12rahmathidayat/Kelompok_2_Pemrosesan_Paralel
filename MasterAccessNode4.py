import paramiko

pr = paramiko.SSHClient()
pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pr.connect(hostname='192.168.43.253', username="root", password="0312")
#ip linux,username linux,password linux
stdin,stdout,stderr = pr.exec_command("python3 /home/Node4.py")#file execution
output = stdout.readlines()
   for i in output:
       print(i, end="")
# print(stdout.readlines())
# print(stderr.readlines()