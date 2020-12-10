import os
import json


def showIp():
	ip = os.popen('ip addr show enp0s3').read().split("inet ")[1].split("/")[0]
	print("|---------------------|")
	print("----- From Node 1 -----")
	print("-->IP-Node :",ip)
	print("|---------------------|")

def DataBD(getFm="",getBD="",dataBD=""):
    br = getFm.split(",")
    ph = getBD.split(",")
    data = json.loads(json.dumps(dataBD))

    showIp()

    for i in br :
        if int(i) == 1 :
            for j in ph :
                if j == "k" :
                    ph_name = "Keliling"
                elif j == "l" :
                    ph_name = "Luas"
                print(ph_name + " Segitiga\t: " + str(round(segitiga(j, data), 2)))
        elif int(i) == 2 :
            for j in ph :
                if j == "k" :
                    ph_name = "Keliling"
                elif j == "l" :
                    ph_name = "Luas"
                print(ph_name + " Lingkaran\t: " + str(round(lingkaran(j, data), 2)))
        elif int(i) == 3 :
            for j in ph :
                if j == "k" :
                    ph_name = "Keliling"
                elif j == "l" :
                    ph_name = "Luas"
                print(ph_name + " Persegi\t: " + str(round(persegi(j, data), 2)))

    print("---------------------------------------")

def segitiga(req_data = "k", data = {}):
    if req_data == "k" :
        return (float(data['sgt_s1']) + float(data['sgt_s2']) + float(data['sgt_s3']))
    elif req_data == "l" :
        return ((float(data['sgt_a']) * float(data['sgt_t']))/2)

def lingkaran(req_data = "k", data = {}):
    if req_data == "k" :
        return (2 * (22/7) * float(data['lkr_r']))
    elif req_data == "l" :
        return ((22/7) * (float(data['lkr_r']))**2)

def persegi(req_data = "k", data = {}):
    if req_data == "k" :
        return ((2 * (float(data['psg_s1']))) + (2 * (float(data['psg_s2']))))
    elif req_data == "l" :
        return (float(data['psg_s1']) * float(data['psg_s2']))
