import socket
import time
import sys
import logging 

server_ip='0.0.0.0'
server_port=5555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect((server_ip,server_port))

# ask the user to enter the number without country code
pn='03214038977'

if len(pn)!=11:
    print(f"WARNING:root: Wrong key Format, got key length {len(pn)}, should be 11 ")
if pn.isdigit()==False:
    print('WARNING:root: Key should consist only numbers, got alphabet or character')

server.send(pn.encode("UTF-8"))

ph_info=(server.recv(6000).decode('UTF-8'))

print(ph_info)

init_cam=input('Press 0 to initilize camera & capture photo --> ')

server.send(init_cam.encode("UTF-8"))

img_info=(server.recv(8000).decode('UTF-8'))

print(img_info)

result_info=(server.recv(8000).decode('UTF-8'))

print(result_info)
# data_show=input("enter y to confirm the data or n to exit >> : ")
# if (data_show=="y" or data_show=="Y"):
# 	while True:
# 		print("Data recieved from the server : ")
# 		print(raw_data)
# 		break
# elif (data_show=="n" or data_show=="N"):
# 	while True:
# 		print("Exiting the session....")
# 		time.sleep(2)
# 		break
sys.exit()

