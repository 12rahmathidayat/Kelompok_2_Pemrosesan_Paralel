import paramiko

def Node1Access():
    pr = paramiko.SSHClient()
    pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pr.connect(hostname='192.168.43.240',username="root",password="0312")
    stdin,stdout,stderr = pr.exec_command("python3 /home/MasterAccessNode1.py")
    output = stdout.readlines()
    for i in output:
        print(i,end="")

def Node2Access():
    pr = paramiko.SSHClient()
    pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pr.connect(hostname='192.168.43.240',username="root",password="0312")
    stdin,stdout,stderr = pr.exec_command("python3 /home/MasterAccessNode2.py")
    output = stdout.readlines()
    for i in output:
        print(i,end="")

def Node3Access():
    pr = paramiko.SSHClient()
    pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pr.connect(hostname='192.168.43.240',username="root",password="0312")
    stdin,stdout,stderr = pr.exec_command("python3 /home/MasterAccessNode3.py")
    output = stdout.readlines()
    for i in output:
        print(i,end="")

def Node4Access():
    pr = paramiko.SSHClient()
    pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pr.connect(hostname='192.168.43.240',username="root",password="0312")
    stdin,stdout,stderr = pr.exec_command("python3 /home/MasterAccessNode4.py")
    output = stdout.readlines()
    for i in output:
        print(i,end="")


print("=====================================================")
print("---------[SELAMAT DATANG OPERATOR ADMIN]-------------")
print("=====================================================")
print("SILAHKAN PILIH MENU PERINTAH DIBAWAH")
print("|1. ACCESS NODE 1")
print("|2. ACCESS NODE 2")
print("|3. ACCESS NODE 3")
print("|4. ACCESS NODE 4")
print("-----------------------------------------------------")
ch=int(input("SILAHKAN MASUKKAN PERINTAH :"))
if(ch==1):
    Node1Access()
elif(ch==2):
    Node2Access()
elif(ch==3):
    Node3Access()
elif(ch==4):
    Node4Access()
else:
    print("perintah yang anda masukkan tidak ada")
       
