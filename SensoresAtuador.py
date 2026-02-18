import random
import datetime

from threading import Thread, Event
from PySide6.QtCore import QObject, Signal

class Sensores(QObject):

    # Sinais para atualizar a UI
    dados_atualizados = Signal(dict)            # Sinal para enviar os dados dos sensores para a UI
    
    def __init__(self,ui_principal=None):
        super().__init__()
        self.ui_principal = ui_principal
        self.xB = 0.0
        self.xD = 0.0
        self.MB = 0.0
        self.MD = 0.0
        self.TA = 0.0
        self.T_prato = [0.0] * 14
        self.VD = 0.0
        self.VL = 0.0
        self.VF = 0.0
        self.RB = 0.0
        self.R1 = 0.0
        self.R2 = 0.0
        self._stop_event = Event()
        self.thread = None                                      # Thread para leitura dos sensores.
    
    def iniciar_leitura_escrita(self):
        #Inicia a thread de leitura dos sensores
        if self.thread and self.thread.is_alive():              #Verifica se não há um thread já rodando para evitar múltiplas threads
            return
            
        self._stop_event.clear()                                #Limpa o evento de parada para garantir que a thread possa rodar
        self.thread = Thread(target=self._ler_sensores_atuadores)         #Cria a thread para ler os sensores
        self.thread.daemon = True                               #Define como daemon para que a thread seja encerrada quando o programa fechar  
        self.thread.start()                                     #Inicia a thread
        print("Thread de sensores iniciada")
    
    def parar_leitura_escrita(self):

        #Para a thread de leitura dos sensores
        self._stop_event.set()                      #Sinaliza para a thread parar
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2.0)           #Aguarda a thread terminar, com timeout para evitar bloqueio indefinido
            print("Thread de sensores parada")
    
    def _ler_sensores_atuadores(self):

        #Loop principal de leitura dos sensores 
        print("Iniciando leitura de sensores...")
        
        while not self._stop_event.is_set():

            #Dados de data de hora
            
            self.data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Gerar novos valores aleatórios
            self.T_prato = [random.uniform(i * 10 + 1, (i + 1) * 10) for i in range(14)]
            self.MB = random.uniform(0, 100)
            self.MD = random.uniform(0, 100)
            self.xB = random.uniform(0, 1)  # Fração molar entre 0 e 1                
            self.xD = random.uniform(0, 1)  # Fração molar entre 0 e 1

             # Leitura dos atuadores
            self.VD = self.ui_principal.lcd_VD.value()  
            self.VL = self.ui_principal.lcd_VL.value()
            self.VF = self.ui_principal.lcd_VF.value()
            self.VB = self.ui_principal.lcd_VB.value()
            self.RB = self.ui_principal.lcd_RB.value()
            self.R1 = 1.0 if self.ui_principal.button_R1.isChecked() else 0.0
            self.R2 = 1.0 if self.ui_principal.button_R2.isChecked() else 0.0
                           
                # Emitir sinal com os dados atualizados
            dados = {
                    'Data/Hora': self.data_hora,
                    'xB': self.xB * 100,  # Converter para porcentagem para display
                    'xD': self.xD * 100,  # Converter para porcentagem para display
                    'MB': self.MB,
                    'MD': self.MD,
                    'TA': self.TA,
                    'T_prato': self.T_prato,
                    'VD': self.VD,
                    'VL': self.VL,
                    'VF': self.VF,
                    'VB': self.VB,
                    'RB': self.RB,
                    'R1': self.R1,
                    'R2': self.R2                  
                }
            self.dados_atualizados.emit(dados)
                
                # Aguardar com possibilidade de interrupção
            self._stop_event.wait(1.0)  # Aguarda 1 segundo ou até ser interrompido
        
        print("Leitura de sensores finalizada")