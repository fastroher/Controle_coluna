# Frames relacionados a imagens e gráficos do supervisório
from PySide6.QtWidgets import QApplication, QMainWindow, QLCDNumber, QDial, QVBoxLayout, QWidget, QGraphicsSimpleTextItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis

#Integração entre módulos
from UIs.Supervisorio_ui import Ui_Superv_geral
from SensoresAtuador import Sensores
from UIs.Dados_ui import Ui_Dados

#Frames diversos para manipulação de dados
import atexit
import sys
import pandas as pd
from datetime import datetime
import os
import traceback

#classe relacionada a tela geral do supervisório
class SupervisaoGeralApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Superv_geral()                     # Criar instância da UI, sem atributos
        self.ui.setupUi(self)                           # Organiza os widgets na janela
        
        # Tornar os elementos da UI acessíveis
        self.lcd_xD = self.ui.lcd_xD
        self.lcd_xB = self.ui.lcd_xB
        self.lcd_MB = self.ui.lcd_MB
        self.lcd_MD = self.ui.lcd_MD
        self.lcd_VL = self.ui.lcd_VL
        self.lcd_VD = self.ui.lcd_VD
        self.lcd_VF = self.ui.lcd_VF
        self.lcd_VB = self.ui.lcd_VB
        self.lcd_RB = self.ui.lcd_RB
        self.dial_ctr_VL = self.ui.dial_ctr_VL
        self.dial_ctr_VD = self.ui.dial_ctr_VD
        self.dial_RB = self.ui.dial_RB

        self.ui.button_Dados.clicked.connect(self.open_Dados_window)     # Atribuindo Sinal aos botões      
        self.setup_graficos()                                            # Substituir QGraphicsView por QChartView para os gráficos
        self.tempo = 0                                                   # Dados históricos para os gráficos
        
    #Configura os gráficos substituindo QGraphicsView por QChartView
    def setup_graficos(self):
        
        # Obter as políticas de tamanho dos gráficos originais para manter a responsividade
        size_policy_T = self.ui.graph_T.sizePolicy()
        size_policy_xD = self.ui.graph_xD.sizePolicy()

        #Substituir graph_T por QChartView
        layout_T = QVBoxLayout()
        self.chart_view_T = QChartView()
        self.chart_view_T.setRenderHint(QPainter.Antialiasing)
        self.chart_view_T.setSizePolicy(size_policy_T)  
        layout_T.addWidget(self.chart_view_T)

        #Substituir graph_xD por QChartView
        layout_xD = QVBoxLayout()
        self.chart_view_xD = QChartView()
        self.chart_view_xD.setRenderHint(QPainter.Antialiasing)
        self.chart_view_xD.setSizePolicy(size_policy_xD) 
        layout_xD.addWidget(self.chart_view_xD)

        # Configurar os layouts nos widgets existentes
        widget_T = QWidget()
        widget_T.setLayout(layout_T)
        widget_xD = QWidget()
        widget_xD.setLayout(layout_xD)

        # Remover os QGraphicsView originais
        self.ui.graph_T.setParent(None)
        self.ui.graph_xD.setParent(None)

        # Remover espaçamento entre os gráficos
        self.ui.verticalLayout_7.setSpacing(0)
        self.ui.verticalLayout_7.addWidget(widget_xD)
        self.ui.verticalLayout_7.addWidget(widget_T)

        # Ajuste de proporção: gráfico de temperatura maior que gráfico xD
        self.ui.verticalLayout_7.setStretch(0, 1)  # widget_xD ocupa 1 parte
        self.ui.verticalLayout_7.setStretch(1, 2)  # widget_T ocupa 2 partes

        # Configurar os gráficos
        self.setup_grafico_temperaturas()
        self.setup_grafico_xD()

    #Configura gráfico de temperaturas, criando as séries para cada prato e configurando os eixos   
    def setup_grafico_temperaturas(self):

        # Criar chart
        self.chart_T = QChart()
        self.chart_T.setTitle("Temperatura dos Pratos")
        self.chart_T.setAnimationOptions(QChart.SeriesAnimations)
        
        # Configurar eixos
        self.axis_x_T = QValueAxis()
        self.axis_x_T.setTitleText("Tempo (s)")
        self.axis_x_T.setRange(0, 100)               #Range inicial para os primeiros 100 segundos, depois atualizar dinamicamente
        self.axis_y_T = QValueAxis()
        self.axis_y_T.setTitleText("Temperatura (°C)")
        self.axis_y_T.setRange(0, 140)               #Range de temperatura, pode ser ajustada conforme necessário
        self.chart_T.addAxis(self.axis_x_T, Qt.AlignBottom)
        self.chart_T.addAxis(self.axis_y_T, Qt.AlignLeft)
        
        # Criar séries para cada prato
        self.series_T = []
        colors = [QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255), 
                 QColor(255, 255, 0), QColor(255, 0, 255), QColor(0, 255, 255),
                 QColor(128, 0, 0), QColor(0, 128, 0), QColor(0, 0, 128),
                 QColor(128, 128, 0), QColor(128, 0, 128), QColor(0, 128, 128),
                 QColor(192, 192, 192), QColor(128, 128, 128)]
        
        for i in range(14):
            series = QLineSeries()
            series.setName(f"P{i+1}")
            pen = QPen(colors[i % len(colors)])
            pen.setWidth(2)
            series.setPen(pen)
            self.series_T.append(series)
            self.chart_T.addSeries(series)
            series.attachAxis(self.axis_x_T)
            series.attachAxis(self.axis_y_T)
        
        # Configurar o chart view
        self.chart_view_T.setChart(self.chart_T)

        # Garantir que a legenda está visível e bem posicionada
        legend = self.chart_T.legend()
        legend.setVisible(True)
        legend.setAlignment(Qt.AlignBottom)  
    
    #Configura gráfico de composição xD, criando a série para xD e configurando os eixos
    def setup_grafico_xD(self):
        self.chart_xD = QChart()
        self.chart_xD.setTitle("Composição do Destilado (xD)")
        self.chart_xD.setAnimationOptions(QChart.SeriesAnimations)
        
        # Configurar eixos
        self.axis_x_xD = QValueAxis()
        self.axis_x_xD.setTitleText("Tempo (s)")
        self.axis_x_xD.setRange(0, 100)                   #Inicialmente mostrar os primeiros 100 segundos, depois atualizar dinamicamente
        self.axis_y_xD = QValueAxis()
        self.axis_y_xD.setTitleText("xD (%)")
        self.axis_y_xD.setRange(0, 100)                   #Range de 0 a 100% para composição, pode ser ajustada conforme necessário
        self.chart_xD.addAxis(self.axis_x_xD, Qt.AlignBottom)
        self.chart_xD.addAxis(self.axis_y_xD, Qt.AlignLeft)
        
        # Cria série para xD
        self.series_xD = QLineSeries()
        self.series_xD.setName("Composição xD")
        pen = QPen(QColor(0, 0, 255))
        pen.setWidth(3)
        self.series_xD.setPen(pen)
        self.chart_xD.addSeries(self.series_xD)
        self.series_xD.attachAxis(self.axis_x_xD)
        self.series_xD.attachAxis(self.axis_y_xD)
        
        # Configurar o chart view
        self.chart_view_xD.setChart(self.chart_xD)
    
    #Atualiza o gráfico de temperaturas e insere rótulo do último valor
    def atualizar_grafico_temperaturas(self, temperaturas):
        self.tempo += 1

        # Mantem apenas os últimos 100 pontos
        if self.tempo > 100:
            for series in self.series_T:
                if series.count() > 0:
                    series.removePoints(0, 1)
            self.axis_x_T.setRange(self.tempo - 100, self.tempo)

        # Adicionar novos pontos
        for i, temp in enumerate(temperaturas):
            self.series_T[i].append(self.tempo, temp)

            # Remover rótulo anterior, se existir
            if hasattr(self, f'label_T_{i}'):
                self.chart_T.scene().removeItem(getattr(self, f'label_T_{i}'))

            # Adicionar rótulo do último valor
            label = QGraphicsSimpleTextItem(f"{temp:.2f}")
            pos = self.chart_T.mapToPosition(self.series_T[i].pointsVector()[-1], self.series_T[i])
            label.setPos(pos.x(), pos.y() - 20)  # Ajuste vertical
            self.chart_T.scene().addItem(label)
            setattr(self, f'label_T_{i}', label)
    
    #Atualiza o gráfico de composição xD e insere rótulo do último valor
    def atualizar_grafico_xD(self, xD):

        # Manter apenas os últimos 100 pontos
        if self.series_xD.count() >= 100:
            self.series_xD.removePoints(0, 1)
            self.axis_x_xD.setRange(self.tempo - 100, self.tempo)

        # Adicionar novo ponto
        self.series_xD.append(self.tempo, xD)

        # Remover rótulo anterior, se existir
        if hasattr(self, 'label_xD'):
            self.chart_xD.scene().removeItem(self.label_xD)

        # Adicionar rótulo do último valor
        label = QGraphicsSimpleTextItem(f"{xD:.2f}")
        pos = self.chart_xD.mapToPosition(self.series_xD.pointsVector()[-1], self.series_xD)
        label.setPos(pos.x(), pos.y() - 20)
        self.chart_xD.scene().addItem(label)
        self.label_xD = label

    # Criar nova janela com a UI de Dados
    def open_Dados_window(self):
        self.dados_window.show()   # agora usa a instância única

#Classe relacionada a tela de Dados
class SupervisaoDadosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_Dados = Ui_Dados()
        self.ui_Dados.setupUi(self)
        self.coleta_dados = self.ui_Dados.Slider_dados

        # Colunas padrão (sem espaços)
        self.colunas = [
            'Data', 'Hora', 'xD', 'xB', 'MB', 'MD', 'VD', 'VL', 'VF',
            'VB', 'RB', 'R1', 'R2', 'TA', 'T1', 'T2', 'T3', 'T4', 'T5',
            'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14'
        ]

        # Inicializa o arquivo histórico
        self._inicializar_arquivo_historico()

    def _inicializar_arquivo_historico(self):
        arquivo = 'SensorAtuadorHist.csv'
        if not os.path.exists(arquivo):
            # Cria arquivo vazio apenas com cabeçalho
            pd.DataFrame(columns=self.colunas).to_csv(arquivo, index=False)
            print(f"Arquivo {arquivo} criado com cabeçalho.")
        else:
            try:
                df = pd.read_csv(arquivo)
                # Remove espaços dos nomes das colunas
                df.columns = df.columns.str.strip()
                # Verifica se as colunas necessárias estão presentes e na ordem correta
                if list(df.columns) == self.colunas:
                    print("Arquivo histórico já está no formato correto.")
                else:
                    # Se não estiver correto, faz backup e recria
                    backup = arquivo.replace('.csv', '_backup.csv')
                    os.rename(arquivo, backup)
                    print(f"Arquivo histórico corrompido. Backup salvo como {backup}. Recriando...")
                    pd.DataFrame(columns=self.colunas).to_csv(arquivo, index=False)
            except Exception as e:
                print(f"Erro ao ler arquivo histórico: {e}. Recriando...")
                # Se houver erro, tenta renomear e recriar
                if os.path.exists(arquivo):
                    backup = arquivo.replace('.csv', '_backup_erro.csv')
                    os.rename(arquivo, backup)
                    print(f"Arquivo problemático renomeado para {backup}.")
                pd.DataFrame(columns=self.colunas).to_csv(arquivo, index=False)

    def Coletar_dados(self, dados_sensores):
        """
        Coleta dados dos sensores e armazena em arquivos CSV.
        Só executa se o Slider_dados for igual a 1.
        """
        print(f"Coletar_dados chamado. Slider value: {self.coleta_dados.value()}")  # Debug

        if self.coleta_dados.value() == 0:
            print("Coleta desabilitada (slider=0).")
            return

        print("Coleta habilitada, processando dados...")

        try:
            # Processa data/hora
            data_hora_str = dados_sensores.get('Data/Hora', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            try:
                data, hora = data_hora_str.split(' ')
            except ValueError:
                data = data_hora_str
                hora = "00:00:00"

            # Prepara dicionário com todos os campos (na ordem das colunas)
            linha = {
                'Data': data,
                'Hora': hora,
                'xD': dados_sensores.get('xD', 0.0),
                'xB': dados_sensores.get('xB', 0.0),
                'MB': dados_sensores.get('MB', 0.0),
                'MD': dados_sensores.get('MD', 0.0),
                'VD': dados_sensores.get('VD', 0.0),
                'VL': dados_sensores.get('VL', 0.0),
                'VF': dados_sensores.get('VF', 0.0),
                'VB': dados_sensores.get('VB', 0.0),
                'RB': dados_sensores.get('RB', 0.0),
                'R1': dados_sensores.get('R1', 0.0),
                'R2': dados_sensores.get('R2', 0.0),
                'TA': dados_sensores.get('TA', 0.0),
            }

            # Temperaturas dos pratos
            temperaturas = dados_sensores.get('T_prato', [0.0]*14)
            for i in range(14):
                linha[f'T{i+1}'] = temperaturas[i]

            # Cria DataFrame com uma única linha
            df_linha = pd.DataFrame([linha])

            # Salva no arquivo "atual" (sobrescreve)
            #df_linha.to_csv('SensorAtuadorAtual.csv', index=False)
            #print("Arquivo SensorAtuadorAtual.csv atualizado.")

            # Salva no histórico em modo append (sem cabeçalho)
            df_linha.to_csv('SensorAtuadorHist.csv', mode='a', header=False, index=False)
            print("Dados adicionados ao SensorAtuadorHist.csv")

            print(f"Dados salvos - xD: {dados_sensores.get('xD', 0.0):.2f}")

        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
            traceback.print_exc()  # Mostra o stack trace completo

def main():
    app = QApplication(sys.argv)
    supervisor = SupervisaoGeralApp()
    Dados_supervisor = SupervisaoDadosApp()
    supervisor.dados_window = Dados_supervisor 
    sensores = Sensores(ui_principal=supervisor.ui)
    
    # Buscar elementos da UI
    def encontrar_elementos():
        elementos = {}
        
        # Lista de elementos que queremos encontrar
        element_mapping = {
            'lcd_xD': supervisor.lcd_xD,
            'lcd_xB': supervisor.lcd_xB,
            'lcd_MB': supervisor.lcd_MB,
            'lcd_MD': supervisor.lcd_MD,
        }
        
        for elem_name, element in element_mapping.items():
            if element is not None:
                elementos[elem_name] = element
                print(f"Encontrado: {elem_name}")
            else:
                print(f"Elemento {elem_name} não encontrado")
        
        return elementos
    
    elementos_ui = encontrar_elementos()
    print("Elementos encontrados:", list(elementos_ui.keys()))
    
    def atualizar_ui(dados):
        try:
            print(f"Atualizando UI: xD={dados['xD']:.2f}%")
            
            # Atualizar LCDs
            lcd_mapping = {
                'lcd_xD': dados['xD'],
                'lcd_xB': dados['xB'],
                'lcd_MB': dados['MB'],
                'lcd_MD': dados['MD'],
            }
            
            for elem_name, value in lcd_mapping.items():
                if elem_name in elementos_ui:
                    try:
                        elementos_ui[elem_name].display(float(value))
                    except Exception as e:
                        print(f"Erro ao atualizar {elem_name}: {e}")
         
            # Atualizar gráficos
            supervisor.atualizar_grafico_temperaturas(dados['T_prato'])
            supervisor.atualizar_grafico_xD(dados['xD'])
            
            # Coletar dados se o slider estiver habilitado (= 1)
            Dados_supervisor.Coletar_dados(dados)
                        
        except Exception as e:
            print(f"Erro geral ao atualizar UI: {e}")
    
    # Conectar sinal de atualização
    sensores.dados_atualizados.connect(atualizar_ui)
    
    def parar_sensores():
        print("Parando sensores...")
        sensores.parar_leitura_escrita()
    
    # Registrar para executar quando o programa terminar
    atexit.register(parar_sensores)
    
    # Sobrescrever o método closeEvent
    def closeEvent(event):
        print("Fechando aplicação...")
        parar_sensores()
        event.accept()
    
    supervisor.closeEvent = closeEvent
    
    # Iniciar sensores
    sensores.iniciar_leitura_escrita()
    print("Sensores iniciados. Feche a janela para parar.")
    print(f"Coleta de dados: {Dados_supervisor.coleta_dados.value()}")
    supervisor.showMaximized()  # Inicia em tela cheia
    result = app.exec()
    
    # Garantir parada final
    parar_sensores()
    print("Aplicação encerrada.")
    
    sys.exit(result)



if __name__ == "__main__":
    main()