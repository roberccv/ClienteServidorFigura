import socket, sys, os
class Servidor:

    def __init__(self):
        self.s = None

    def servidor(self):
        s = self.s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.bind(('localhost', 5002))
        s.listen(2)
        

        while True:
            ns, _ = s.accept()
            x_min = ns.recv(1024).decode()
            ns.send(b'ACK')
            x_max = ns.recv(1024).decode()
            ns.send(b'ACK')
            y_min = ns.recv(1024).decode()
            ns.send(b'ACK')
            y_max = ns.recv(1024).decode()
            ns.send(b'ACK')
            calculo = ns.recv(1024).decode()

            resultado = self.calculo(x_min, x_max, y_min, y_max, calculo)
            ns.send(resultado.encode())
            ns.close()



    def calculo(self, x_min, x_max, y_min, y_max, calculo):
        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)

        if x_min > x_max:
            return 'X_min no puede ser mayor que X_max'
        elif y_min > y_max:
            return 'Y_min no puede ser mayor que Y_max'
        
        if calculo == 'area':
            return self.area(x_min, x_max, y_min, y_max)
        if calculo == 'centro':
            return self.centro(x_min, x_max, y_min, y_max)

    def area(self, x_min, x_max, y_min, y_max):
        resultado = str((x_max - x_min) * (y_max - y_min))
        return resultado
    
    def centro(self, x_min, x_max, y_min, y_max):
        resultado = str((x_min + x_max) / 2) + ' , ' + str((y_min + y_max) / 2)
        return resultado
    
if __name__ == '__main__':
    server = Servidor()
    server.servidor()