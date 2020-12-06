from os import system
import sys

def menuHeader():
	print("<------------------------------>")
	print("|  SELAMAT DATANG DI OPERASI   |")
	print("|         MATEMATIKA           |")
	print("| PYTHON PEMROSESAN PARALEL    |")
	print("|   created by kelompok 2      |")
	print("<------------------------------>")
	print("<==============================>")
	print("|     SILAHKAN PILIH MENU      |")
	print("<==============================>")

def menuNode():
	print("<==============================>")
	print("|          NODE MENU           |")
	print("<==============================>")
	print("--------------------------------")
	print("|[1]Node1 || [3]Node3 |")
	print("|[2]Node2 || [4]Node4 |")
	print("--------------------------------")

def menuBangunDatar():
		print("<==============================>")
		print("|       BANGUN DATAR MENU      |")
		print("<==============================>")
		print("--------------------------------")
		print("|[1]Persegi   || [3]Segitiga |")
		print("|[2]Lingkaran ||             |")
		print("--------------------------------")
def menuFormula():
		print("<==============================>")
		print("|         FORMULA MENU         |")
		print("<==============================>")
		print("--------------------------------")
		print("|[1]KELILING         |")
		print("|[2]LUAS             |")
		print("--------------------------------")

def getInputUser():
	dataInputSend=[]
	dataBD=
	getNode=input("/=>Masukkan Node :")
	getNode_arr=getNode.split(",")
	user_validate_node(getNode_arr)
	dataInputSend.append(getNode_arr)
	menuBangunDatar()
	getBangundatar = input("/=>Masukkan Bangun Datar :")
	getBD_arr = getBangundatar.split(",")
	user_validate_BD(getBD_arr)
	dataInputSend.append(getBD_arr)
	menuFormula()
	getFormula = input("/=>Masukkan Formula :")
	getFm_arr = getFormula.split(",")
	user_validate_FM(getFm_arr)
	dataInputSend.append(getFM_arr)
	dataBD=DataProcessBD(getBD_arr,getFM_arr)
	DataProcessBD(getBD_arr,getFm_arr)
	sendDataNode(dataInputSend)


def Keliling_persegi():
		print("|'''''''''''''''''''''''''''''''''''''''|")
		print("<--------------------------------------->")
		print("</>----MENGHITUNG KELILING PERSEGI----</>")	
		print("<--------------------------------------->")
		print("|.......................................|")

def Luas_persegi():
		print("|'''''''''''''''''''''''''''''''''''''''|")
		print("<--------------------------------------->")
		print("</>------MENGHITUNG LUAS PERSEGI------</>")	
		print("<--------------------------------------->")
		print("|.......................................|")

def Keliling_lingkaran():
		print("|'''''''''''''''''''''''''''''''''''''''''|")
		print("<----------------------------------------->")
		print("</>----MENGHITUNG KELILING LINGKARAN----</>")	
		print("<----------------------------------------->")
		print("|.........................................|")

def Luas_lingkaran():
		print("|'''''''''''''''''''''''''''''''''''''''''|")
		print("<----------------------------------------->")
		print("</>------MENGHITUNG LUAS LINGKARAN------</>")	
		print("<----------------------------------------->")
		print("|.........................................|")

def Keliling_segitiga():
		print("|'''''''''''''''''''''''''''''''''''''''''|")
		print("<----------------------------------------->")
		print("</>----MENGHITUNG KELILING SEGITIGA-----</>")	
		print("<----------------------------------------->")
		print("|.........................................|")

def Luas_segitiga():
		print("|'''''''''''''''''''''''''''''''''''''''''|")
		print("<----------------------------------------->")
		print("</>------MENGHITUNG LUAS SEGITIGA-------</>")	
		print("<----------------------------------------->")
		print("|.........................................|")

def DataProcessBD(param_BD=[],param_FM=[]):
	dataContain={}
	for BD in param_BD:
		for FM in param_FM:
			if int(BD) == 1:
				if int(FM) == 1:
					Keliling_persegi()
					dataContain['side']=input("input sisi(s) : ")
					user_validate_input_value(dataContain['side'])
				elif int(FM) == 2:
					Luas_persegi()
					dataContain['side']=input("input sisi(s) : ")
					user_validate_input_value(dataContain['side'])
			elif int(BD) == 2:
				if int(FM) == 1:
					Keliling_lingkaran()
					dataContain['radius']=input("input radius(r) : ")
					user_validate_input_value(dataContain['radius'])
				elif int(FM) == 2:
					Luas_lingkaran()
					dataContain['radius']=input("input radius(r) : ")
					user_validate_input_value(dataContain['radius'])
			elif int(BD) == 3 :
				if int(FM) == 1:
					Keliling_segitiga()
					dataContain['sideA']=input("input sisi A : ")
					user_validate_input_value(dataContain['sideA'])
					dataContain['sideB']=input("input sisi B : ")
					user_validate_input_value(dataContain['sideB'])
					dataContain['sideC']=input("input sisi C : ")
					user_validate_input_value(dataContain['sideC'])
				elif int(FM) == 2:
					Luas_segitiga()
					dataContain['base']=input("input alas    : ")
					user_validate_input_value(dataContain['base'])
					dataContain['high']=input("input tinggi : ")
					user_validate_input_value(dataContain['high'])

	return dataContain

def loop_app():
	user_acc=input("ingin mengulang Y/y/N/n :")
	userDecission(user_acc)

def userDecission(user_acc):
	if user_acc == "Y" or user_acc == "y":
		app_Clean()
		menuHeader()
		menuNode()
		menuBangunDatar()
		getInputUser()
	elif user_acc == "N" or user_acc == "n":
		app_Clean()
		app_exit()
	else:
		print("Perintah Tidak Tersedia !!")
		loop_app()

def user_validate_node(user_input=[]):
	number_valid = ["1","2","3","4"]
	Node_valid = [1,2,3,4]
	for i in user_input:
		if i == "" or i not in number_valid or int(i) not in Node_valid:
				print("input tidak tersedia !")
				loop_app()

def user_validate_BD(user_input=[]):
	number_valid = ["1","2","3"]
	BD_valid = [1,2,3]
	for i in user_input:
		if i == "" or i not in number_valid or int(i) not in BD_valid:
				print("input tidak tersedia !")
				loop_app()

def user_validate_FM(user_input=[]):
	number_valid = ["1","2"]
	FM_valid = [1,2]
	for i in user_input:
		if i == "" or i not in number_valid or int(i) not in FM_valid:
				print("input tidak tersedia !")
				loop_app()

def sendDataNode(node="",getBD="",dataInputSend=[],getFM="",dataBD={}):
	Node_arr=['node1','node2','node3','node4']
	ProcData=data[0]
	for node in proc_nd :
		data=int(node) - 1, data[1], data[2], data[3]

	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	conn.connect(hostname=Node_host[node], username="root", password="0312")
	command='cd /home/; python3 -c "from DataNode import DataSend; DataSend(' + "'" + getBD + "' , '" + getFM + "' , " + str(dataBD) + ')"'
	stdin,stdout,stderr = sshConn.exec_command(command)
	output = stdout.readlines()
	for i in output:
        print(i, end="")

    conn.close()

def user_validate_input_value(user_v=[]):
	try:
		float(user_v)
	except Exception:
		print("input Error")

def app_Clean():
	system("cls")

def app_exit():
	exit()

app_Clean()
menuHeader()
menuNode()
getInputUser()




