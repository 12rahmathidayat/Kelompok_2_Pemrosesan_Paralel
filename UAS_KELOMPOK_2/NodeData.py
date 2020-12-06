import os
import json


def showIp():
	ip = os.popen('ip addr show enp0s3').read().split("inet ")[1].split("/")[0]
	print("|---------------------|")
	print("----- From Node 1 -----")
	print("-->IP-Node :",ip)
	print("|---------------------|")

def DataBD(getFm="",getBD="",dataBD=""):
	
