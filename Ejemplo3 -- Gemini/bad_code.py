import threading
import time
import random

# Variables globales compartidas (PELIGRO EN CONCURRENCIA)
GLOBAL_BALANCE = 10000
transaction_log = []
error_flags = {"db": False, "net": False}

class BankSystem:
    def __init__(self):
        self.data = []
        self.users = {}
        self.temp_cache = {}

    def load_data_from_messy_source(self, raw_data):
        # Nombres de variables terribles y lógica confusa
        for d in raw_data:
            if d != None:
                if len(d) > 0:
                    if d[0] == 'U':
                        self.users[d[1]] = d[2]
                    elif d[0] == 'T':
                        self.data.append(d)
                    else:
                        pass # Ignorar silenciosamente errores

    def process_batch(self, mode, workers):
        # ESTE MÉTODO ES UNA BOMBA DE COMPLEJIDAD CICLOMÁTICA
        global GLOBAL_BALANCE
        
        if mode == "nightly":
            for i in range(workers):
                def worker_logic():
                    global GLOBAL_BALANCE
                    # Variable magica sin explicar
                    retry = 3
                    while retry > 0:
                        try:
                            for tx in self.data:
                                if tx[2] == 'DEBIT':
                                    if GLOBAL_BALANCE > tx[3]:
                                        # Simula latencia para provocar race condition
                                        time.sleep(0.001) 
                                        if not error_flags["db"]:
                                            if tx[3] < 1000:
                                                GLOBAL_BALANCE -= tx[3]
                                            elif tx[3] >= 1000:
                                                if self.users.get(tx[1]) == "VIP":
                                                    GLOBAL_BALANCE -= tx[3]
                                                else:
                                                    print("Error auth")
                                        else:
                                            break
                                    else:
                                        print("Fondos insuficientes")
                                elif tx[2] == 'CREDIT':
                                    if tx[3] > 0:
                                        if len(self.users) > 0:
                                            GLOBAL_BALANCE += tx[3]
                                        else:
                                            retry -= 1
                                    else:
                                        continue
                                elif tx[2] == 'TRANSFER':
                                    if tx[4] in self.users:
                                        if GLOBAL_BALANCE > tx[3]:
                                            GLOBAL_BALANCE -= tx[3]
                                            # Lógica anidada innecesaria
                                            if tx[3] > 5000:
                                                print("Alerta lavado dinero")
                                                if mode == "nightly":
                                                    error_flags["net"] = True
                            retry = 0
                        except Exception as e:
                            retry -= 1
                            if retry == 0:
                                print("Fallo fatal en thread")

                t = threading.Thread(target=worker_logic)
                t.start()
        
        elif mode == "maintenance":
            # Más código duplicado y anidado
            if len(self.users) > 100:
                for k, v in self.users.items():
                    if v == "BANNED":
                        del self.users[k]
                    elif v == "SUSPICIOUS":
                        print("Revisar")
                        if GLOBAL_BALANCE < 0:
                            print("CRITICO")
            else:
                return False

    def report(self):
        # Método inútil para añadir líneas
        print(GLOBAL_BALANCE)
        if GLOBAL_BALANCE < 0:
            return "ROJO"
        else:
            if len(transaction_log) > 0:
                return "VERDE"
            return "AMARILLO"

# Ejecución simulada
sys = BankSystem()
sys.load_data_from_messy_source([['U', 1, 'VIP'], ['T', 1, 'DEBIT', 500]])
sys.process_batch("nightly", 5)