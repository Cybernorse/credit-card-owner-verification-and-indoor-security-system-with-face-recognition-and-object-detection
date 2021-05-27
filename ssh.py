import paramiko
from scp import SCPClient
import os
import requests
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
def uploadFunction():
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('73.137.12.79', 22, 'Cronjobs!9')
        print("Here1")
        scp = SCPClient(client.get_transport())
        pathofifl=dir_path+'/'+'ZIP'+'/'
        ABC=os.listdir(dir_path+ '/' + 'ZIP')
        print("Here2")
        for filename in ABC:
            print(filename)
            scp.put(files= pathofifl + filename,
                remote_path='/home/linuxadmin/Scripts/')
        client.close()
        scp.close()
    except Exception as e:
        print(e)
uploadFunction()
print("Uploaded")
