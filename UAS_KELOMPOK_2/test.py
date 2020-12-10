import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(hostname=Node_host[node], username="root", password="0312")
dataSend=con.send(2+2)
command=
stdin,stdout,stderr = sshConn.exec_command(command)
output = stdout.readlines()

for i in output:
        print(i, end="")

conn.close()