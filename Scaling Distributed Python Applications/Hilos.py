import threading
import multiprocessing
import time

# Clase para el hilo
class Hilo(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre
        
    def run(self):
        print(f"Hilo {self.nombre} iniciado")
        time.sleep(5)
        print(f"Hilo {self.nombre} finalizado")

# Función para el proceso
def proceso(nombre):
    print(f"Proceso {nombre} iniciado")
    time.sleep(5)
    print(f"Proceso {nombre} finalizado")

if __name__ == '__main__':
    # Crear y ejecutar el hilo
    hilo1 = Hilo("1")
    hilo1.start()
    
    # Crear y ejecutar el proceso
    proceso1 = multiprocessing.Process(target=proceso, args=("1",))
    proceso1.start()

    # Crear y ejecutar el demonio
    demonio1 = multiprocessing.Process(target=proceso, args=("2",))
    demonio1.daemon = True
    demonio1.start()

    # Esperar a que finalicen todos los hilos y procesos
    hilo1.join()
    proceso1.join()
    demonio1.join()
    
    print("Todos los hilos y procesos han finalizado")