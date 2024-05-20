import socket, os, sys, signal, getpass

x_min = sys.argv[1]
x_max = sys.argv[2]
y_min = sys.argv[3]
y_max = sys.argv[4]

que_calcula = sys.argv[5]

def cliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('localhost', 5002))
    
    s.send(x_min.encode())
    s.recv(1024) # ACK
    s.send(x_max.encode())
    s.recv(1024) # ACK
    s.send(y_min.encode())
    s.recv(1024) # ACK
    s.send(y_max.encode())
    s.recv(1024) # ACK
    s.send(que_calcula.encode())
    

    solucion = s.recv(1024) # Solución

    print(solucion.decode())

if __name__ == '__main__':
    cliente()

