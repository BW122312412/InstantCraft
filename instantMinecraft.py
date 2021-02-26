import os, socket, time
from configure import configure as c
from mcstatus import MinecraftServer

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
s.bind(('0.0.0.0', 25565))
# become a server socket
s.listen(1)

while True:
    try:
        os.system('aws ec2 associate-address --instance-id  {} --public-ip {} --allow-reassociation'.format(c.proxyInstance, c.elasticIP))
        # waits for signal
        (clientsocket, address) = s.accept()

        print('Starting server')
        
        os.system('aws ec2 start-instances --instance-ids {}'.format(c.serverInstance))
        time.sleep(60)
        os.system('aws ec2 associate-address --instance-id  {} --public-ip {} --allow-reassociation'.format(c.serverInstance, c.elasticIP))
        
        playersOnline = True
        while playersOnline:
            print('People are online')
            time.sleep(120)
            server = MinecraftServer.lookup(c.elasticIP+':25565')
            status = server.status()
            if status.players.online == 0:
                playersOnline = False
        
        print('Shutting down')
        os.system('aws ec2 stop-instances --instance-ids {} --hibernate'.format(c.serverInstance))
        time.sleep(120)
    except Exception as ex:
        print(ex)
