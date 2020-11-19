import paramiko

pr = paramiko.SSHClient()
pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pr.connect(hostname='....', username="...", password="....")
#ip linux,username linux,password linux
stdin,stdout,stderr = pr.exec_command("python3 ....")#file execution
output = stdout.readlines()
   for i in output:
       print(i, end="")
# print(stdout.readlines())
# print(stderr.readlines()