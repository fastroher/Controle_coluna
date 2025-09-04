import random
import time
from threading import Thread, Event
from PySide6.QtCore import QObject, Signal

class Sensores(QObject):
    # Sinais para atualizar a UI
    dados_atualizados = Signal(dict)
    
    def __init__(self):
        super().__init__()
        self.T_prato = [0.0] * 14
        self.MB = 0.0
        self.MD = 0.0
        self.xB = 0.0
        self.xD = 0.0
        self.VL = 0.0
        self.VD = 0.0
        self.RB = 0.0
        self._stop_event = Event()
        self.thread = None
    
    def iniciar_leitura(self):
        """Inicia a thread de leitura dos sensores"""
        if self.thread and self.thread.is_alive():
            return
            
        self._stop_event.clear()
        self.thread = Thread(target=self._ler_sensores)
        self.thread.daemon = True
        self.thread.start()
        print("Thread de sensores iniciada")
    
    def parar_leitura(self):
        """Para a thread de leitura"""
        self._stop_event.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2.0)
            print("Thread de sensores parada")
    
    def _ler_sensores(self):
        """Loop principal de leitura dos sensores"""
        print("Iniciando leitura de sensores...")
        
        while not self._stop_event.is_set():
            try:
                # Gerar novos valores aleatórios
                self.T_prato = [random.uniform(0, 100) for _ in range(14)]
                self.MB = random.uniform(0, 100)
                self.MD = random.uniform(0, 100)
                self.xB = random.uniform(0, 1)  # Fração molar entre 0 e 1
                self.xD = random.uniform(0, 1)  # Fração molar entre 0 e 1
                self.VL = random.uniform(0, 20)
                self.VD = random.uniform(0, 20)
                self.RB = random.uniform(0, 10)
                
                # Emitir sinal com os dados atualizados
                dados = {
                    'T_prato': self.T_prato,
                    'MB': self.MB,
                    'MD': self.MD,
                    'xB': self.xB * 100,  # Converter para porcentagem para display
                    'xD': self.xD * 100,  # Converter para porcentagem para display
                    'VL': self.VL,
                    'VD': self.VD,
                    'RB': self.RB
                }
                self.dados_atualizados.emit(dados)
                
                # Aguardar com possibilidade de interrupção
                self._stop_event.wait(1.0)  # Aguarda 1 segundo ou até ser interrompido
                
            except Exception as e:
                print(f"Erro na leitura de sensores: {e}")
                break
        
        print("Leitura de sensores finalizada")