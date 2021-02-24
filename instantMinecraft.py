import os, socket, time
from configure import configure as c
import MinecraftQuery as MQ

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
s.bind(('0.0.0.0', 25565))
# become a server socket
s.listen(1)

while True:
    (clientsocket, address) = s.accept()
    
    os.system('aws ec2 start-instances --instance-ids {}'.format(c.serverInstance))
    os.system('aws ec2 associate-address --instance-id  {} --public-ip {} --allow-reassociation'.format(c.serverInstance, c.elasticIP))
    
    time.sleep(60 * 3)
    while True:
        time.sleep(60 * 3)
        j = MQ.get_info(c.serverInstance,25565)
        if j['players']['online'] == 0:
            break

    os.system('aws ec2 associate-address --instance-id  {} --public-ip {} --allow-reassociation'.format(c.proxyInstance, c.elasticIP))
    os.system('aws ec2 stop-instances --instance-ids {}'.format(c.serverInstance))
