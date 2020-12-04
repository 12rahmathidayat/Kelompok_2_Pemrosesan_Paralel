import paramiko
pr = paramiko.SSHClient()

def pilihNode():
	print("------------+ Menu Node +------------")
	print("1. Node 1 [IP: " + node_1_h + "]")
	print("2. Node 2 [IP: " + node_2_h + "]")
	print()
	node = int(input("Pilih Node yang ingin dilihat: "))
	return node

def connect(h, u, p):
	pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	pr.connect(hostname=h, username=u, password=p)


hostname = ["10.1.13.92", "10.1.15.3"]
username = ["reader", "reader"]
password = ["paramiko1", "paramiko2"]

node = pilihNode()
if(node < len(hostname)):
	connect(hostname[node  1], username[node - 1], password[node - 1])
else:
	print("Pilihan salah")
	exit()

bash_command = input("Command: ")
param = []
stdin,stdout,stderr = pr.exec_command(bash_command)
stdin.channel.shutdown_write()
output = stdout.readlines()
output_length = len(output) - 1
for x in output:
    print(x, end='')

while 'Keliling' not in output[-1]:
    stdin,stdout,stderr = pr.exec_command(bash_command)
    param_temp = input(" ")
    param.append(param_temp)
    for x in param:
        stdin.write(x + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    output = stdout.readlines()
    for x in output[output_length:]:
        if("Silahkan" in x):
            print(output[-1].split(' ')[-1], end='')
        else:
            print(x, end='')
    output_length = len(output)
