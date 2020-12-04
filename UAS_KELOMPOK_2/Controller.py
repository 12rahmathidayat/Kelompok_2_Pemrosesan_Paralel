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
	getNode=input("/=>Masukkan Node :")
	getNode_arr=getNode.split(",")
	user_validate_node(getNode_arr)
	menuBangunDatar()
	getBangundatar = input("/=>Masukkan Bangun Datar :")
	getBD_arr = getBangundatar.split(",")
	user_validate_BD(getBD_arr)
	menuFormula()
	getFormula = input("/=>Masukkan Formula :")
	getFm_arr = getFormula.split(",")
	user_validate_FM(getFm_arr)
	DataProcessBD(getBD_arr,getFm_arr)

	

def Keliling_persegi():
		dataContain={}
		print("<--------------------------------------->")
		print("</>----MENGHITUNG KELILING PERSEGI----</>")	
		print("<--------------------------------------->")
		dataContain['side']=input("input sisi(s) : ")
		user_validate_input_value(dataContain['side'])
		return dataContain

def Luas_persegi():
		dataContain={}
		print("<--------------------------------------->")
		print("</>------MENGHITUNG LUAS PERSEGI------</>")	
		print("<--------------------------------------->")
		dataContain['side']=input("input sisi(s) : ")
		user_validate_input_value(dataContain['side'])
		return dataContain

def Keliling_lingkaran():
		dataContain={}
		print("<----------------------------------------->")
		print("</>----MENGHITUNG KELILING LINGKARAN----</>")	
		print("<----------------------------------------->")
		dataContain['radius']=input("input radius(r) : ")
		user_validate_input_value(dataContain['radius'])
		return dataContain

def Luas_lingkaran():
		dataContain={}
		print("<----------------------------------------->")
		print("</>------MENGHITUNG LUAS LINGKARAN------</>")	
		print("<----------------------------------------->")
		dataContain['radius']=input("input radius(r) : ")
		user_validate_input_value(dataContain['radius'])
		return dataContain

def Keliling_segitiga():
		dataContain={}
		print("<----------------------------------------->")
		print("</>----MENGHITUNG KELILING SEGITIGA-----</>")	
		print("<----------------------------------------->")
		dataContain['sideA']=input("input sisi A : ")
		user_validate_input_value(dataContain['sideA'])
		dataContain['sideB']=input("input sisi B : ")
		user_validate_input_value(dataContain['sideB'])
		dataContain['sideC']=input("input sisi C : ")
		user_validate_input_value(dataContain['sideC'])
		return dataContain


def Luas_segitiga():
		dataContain={}
		print("<----------------------------------------->")
		print("</>------MENGHITUNG LUAS SEGITIGA-------</>")	
		print("<----------------------------------------->")
		dataContain['base']=input("input alas    : ")
		user_validate_input_value(dataContain['base'])
		dataContain['high']=input("input tinggi : ")
		user_validate_input_value(dataContain['high'])
		return dataContain

def DataProcessBD(param_BD=[],param_FM=[]):
	for BD in param_BD:
		for FM in param_FM:
			if int(BD) == 1:
				if int(FM) == 1:
					Keliling_persegi()
					loop_app()
				elif int(FM) == 2:
					Luas_persegi()
					loop_app()
			elif int(BD) == 2:
				if int(FM) == 1:
					Keliling_lingkaran()
					loop_app()
				elif int(FM) == 2:
					Luas_lingkaran()
					loop_app()
			elif int(BD) == 3 :
				if int(FM) == 1:
					Keliling_segitiga()
				elif int(FM) == 2:
					Luas_segitiga()


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




