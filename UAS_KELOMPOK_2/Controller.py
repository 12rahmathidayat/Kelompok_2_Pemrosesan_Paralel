import sys
from os import system
import paramiko
import json

def systemClean():
    system("clear")

def Exit():
    exit()

def validateNode(data="1", default = 1):
    number_s = ["1","2","3","4"]
    number = [1,2,3,4]
    if default == 1 :
        node = data.split(";")
        for i in node :
            if i == "" or i not in number_s or int(i) not in number :
                print("[!] Input Tidak Valid")
                loop_app()

def validateBd(data="2", default = 2):
    number_s = ["1","2","3"]
    number = [1,2,3]
    if default == 2 :
        bd = data.split(";")
        for i in bd :
            if i == "" or i not in number_s or int(i) not in number :
                print("[!] Input Tidak Valid")
                loop_app()

def validateFm(data="3", default = 3):
    var_fm = ["k", "l", "K", "L"]
    if default == 3 :
        bd = data.split(";")
        for i in bd :
            if i == "" or i not in var_fm :
                print("[!] Input Tidak Valid")
                loop_app()

def DataBdValid(bd_data = ""):
    try :
        float(bd_data)
    except ValueError:
        print("[!] Input Tidak Valid")
        loop_app()

def loop_app():
    user_acc=input("ingin mengulang Y/y/N/n :")
    userDecission(user_acc)

def userDecission(user_acc):
    if user_acc == "Y" or user_acc == "y":
        systemClean()
        menuHeader()
        getInputUser()
    elif user_acc == "N" or user_acc == "n":
        print("program Exit")
        Exit()
    else:
        print("Perintah Tidak Tersedia !!")
        loop_app()

def menuHeader():
	print("+------------------------------+")
	print("|  SELAMAT DATANG DI OPERASI   |")
	print("|         MATEMATIKA           |")
	print("| PYTHON PEMROSESAN PARALEL    |")
	print("|   created by kelompok 2      |")
	print("+------------------------------+")
	print("|==============================|")
	print("|     SILAHKAN PILIH MENU      |")
	print("+==============================+")

def menuNode():
	print("+==============================+")
	print("|          NODE MENU           |")
	print("+==============================+")
	print("+------------------------------+")
	print("|[1]Node1 || [3]Node3          |")
	print("|[2]Node2 || [4]Node4          |")
	print("+------------------------------+")

def menuBangunDatar():
		print("+==============================+")
		print("|       BANGUN DATAR MENU      |")
		print("+==============================+")
		print("+------------------------------+")
		print("|[1]Segitiga   || [3]Persegi   |")
		print("|[2]Lingkaran  ||              |")
		print("+------------------------------+")
def menuFormula():
		print("+==============================+")
		print("|         FORMULA MENU         |")
		print("+==============================+")
		print("+------------------------------+")
		print("|[k]KELILING   || [l]LUAS      |")
		print("+------------------------------+")


def interfaceKllSgt():
    print("[]===========================[]")
    print("-------keliling Segitiga-------")
    print("[]---------------------------[]")

def interfaceLSgt():
    print("[]===========================[]")
    print("-------Luas Segitiga-------")
    print("[]---------------------------[]")

def interfaceLSgt():
    print("[]===========================[]")
    print("-------Luas Segitiga-------")
    print("[]---------------------------[]")

def interfaceKlLlingkaran():
     print("[]-------------------------------------[]")
     print("[]------keliling & luas Lingkaran------[]")
     print("[]-------------------------------------[]")

def interfaceKlLPersegi():
     print("[]-------------------------------------[]")
     print("[]------keliling & luas Persegi------[]")
     print("[]-------------------------------------[]")


def getBdData(get_bd = "", get_fm = ""):
    bd_var = get_bd.split(";")
    fm_var = get_fm.split(";")

    data = {}

    for bd in bd_var :
        if int(bd) == 1 :
            for fm in fm_var :
                if fm == "k" :
                    interfaceKllSgt()
                    data['side1'] = input("Sisi 1 : ")
                    DataBdValid(data['side1'])
                    data['side2'] = input("Sisi 2 : ")
                    DataBdValid(data['side2'])
                    data['side3'] = input("Sisi 3 : ")
                    DataBdValid(data['side3'])

                elif fm == "l" :
                    interfaceLSgt()
                    data['base'] = input("Alas   : ")
                    DataBdValid(data['base'])
                    data['high'] = input("Tinggi : ")
                    DataBdValid(data['high'])

        elif int(bd) == 2 :
            interfaceKlLlingkaran()
            data['r'] = input("Jari-jari Lingkaran : ")
            DataBdValid(data['r'])
            
        elif int(bd) == 3 :
            data['side1'] = input("Sisi 1 : ")
            DataBdValid(data['side1'])
            data['side2'] = input("Sisi 2 : ")
            DataBdValid(data['side2'])

    return data

def getInputUser():
    data = []

    menuNode()
    nd = input("[-->]Node\t\t: ")
    validateNode(nd,1)
    menuBangunDatar()
    bd = input("[-->]Bangun Datar\t: ")
    validateBd(bd,2)
    menuFormula()
    fm = input("[-->]Formula\t\t: ")
    validateFm(fm,3)

    data_bd = getBdData(bd, fm)

    data.append(nd)
    data.append(bd)
    data.append(fm)
    data.append(data_bd)

    prepareData(data)


def prepareData(data = []):
    proc_nd = data[0].split(";")

    for node in proc_nd :
        sendRequestToNode(int(node) - 1, data[1], data[2], data[3])
    
    loop_app()

def sendRequestToNode(node = 1, bd = "", formula = "", data_bd = {}):
    node_list = ["192.168.43.116", "192.168.43.44", "192.168.43.100", "192.168.43.178"]

    Conn = paramiko.SSHClient()
    Conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Conn.connect(hostname=node_list[node], username="root", password="123")
    cmd = 'cd /home/apps; python3 -c "from nodeData import sendData; sendData(' + "'" + bd + "' , '" + formula + "' , " + str(data_bd) + ')"'
    stdin,stdout,stderr = Conn.exec_command(cmd)
    output = stdout.readlines()
    for i in output:
        print(i, end="")

    Conn.close()

systemClean()
menuHeader()
getInputUser()
