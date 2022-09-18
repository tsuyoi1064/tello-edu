import socket

# Tello
svr_address = ('192.168.10.1', 8889)
msg_length = 1518
msg_hello = '\n[Tello]: Hello! Enter \"command\" or \"help\" or \"end\".'

# UDP socket
sock_timeout = 15
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print (msg_hello)

while True:
    try:
        message = input()
        if message == 'end':
            print('\n[Tello]: Goodbye!')
            sock.close()
            break
        elif message == 'help':
            print ('\n[Tello]:')
            print ('command, takeoff, land,')
            print ('up, down, left, right, forward, back, cw, ccw')
            print ('flip f/b/l/r, speed, speed?, battery?')
            print (msg_hello)
        else:
            sock.settimeout(sock_timeout)
            send_len = sock.sendto(message.encode('utf-8'), svr_address)
            recv_meesage, addr = sock.recvfrom(msg_length)
            print(f"\n[Tello]: {recv_meesage.decode(encoding='utf-8')}")
    except socket.timeout:
        print('\n[Tello]: Sorry... Closing by timeout.')
        sock.close()
        break
    except KeyboardInterrupt:
        print('\n[Tello]: Sorry... Closing by KeyboardInterrupt.')
        sock.close()
        break
