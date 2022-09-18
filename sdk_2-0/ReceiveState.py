import socket
import threading

# Device
host = ''
port = 8890
locaddr = (host, port)
msg_length = 1518

print ('\n[Tello]: Receiving State.')

# UDP socket
sock_timeout = 15
sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(locaddr)

def recv():
    while True:
        try :
            sock.settimeout(sock_timeout)
            message, cli_addr = sock.recvfrom(msg_length)
            message = message.decode(encoding='utf-8')
            print(f'Received message is [{message}]')
        except socket.timeout:
            print('\n[Tello]: Sorry... Closing by timeout.')
            sock.close()
            break
        except KeyboardInterrupt:
            print('\n[Tello]: Sorry... Closing by KeyboardInterrupt.')
            sock.close()
            break

recvThread = threading.Thread(target=recv)
recvThread.start()
