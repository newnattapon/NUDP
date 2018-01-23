import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5003
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    factorial = 1
    num = int(data)
    while num >1:
        factorial *= num
        num = num-1
    print "Factorail = ",  factorial
    print "received message:", data
    sock.sendto(str(factorial),addr)
