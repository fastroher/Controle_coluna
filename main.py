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
        super().__init__()                  # Inicializa a janela principal executando o método _init__ da classe pai (QMainWindow). super() localiza a classe base (QMainWindow)
        self.ui = Ui_Superv_geral()         # Criar instância da UI, sem atributos
        self.ui.setupUi(self)               # Organiza os widgets na janela
        
        # Tornar os elementos da UI acessíveis (Atributos da instância)
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
        self.chart_T.setAnimationOptions(QChart.SeriesAnimations)   # Gera a animação para a transição de pontos
        
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

    # Abre a janela de Dados
    def open_Dados_window(self):
        self.dados_window.show()   

#Classe relacionada a tela de Dados
class SupervisaoDadosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_Dados = Ui_Dados()
        self.ui_Dados.setupUi(self)
        self.coleta_dados = self.ui_Dados.Slider_dados

        # Colunas do arquivo histórico (CSV)
        self.colunas = [
            'Data', 'Hora', 'xD', 'xB', 'MB', 'MD', 'VD', 'VL', 'VF',
            'VB', 'RB', 'R1', 'R2', 'TA', 'T1', 'T2', 'T3', 'T4', 'T5',
            'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14'
        ]

        
        self.inicializar_arquivo_historico()

    # Inicializa o arquivo histórico
    def inicializar_arquivo_historico(self):
        arquivo = 'SensorAtuadorHist.csv'
        
        if not os.path.exists(arquivo):           
            pd.DataFrame(columns=self.colunas).to_csv(arquivo, index=False)  # Cria arquivo vazio apenas com cabeçalho
            print(f"Arquivo {arquivo} criado com cabeçalho.")

        else:
            df = pd.read_csv(arquivo)                
            df.columns = df.columns.str.strip()     # Remove espaços dos nomes das colunas

            # Verifica se as colunas necessárias estão presentes e na ordem correta
            if list(df.columns) == self.colunas:
                    print("Arquivo histórico já está no formato correto.")

            # Se não estiver correto, faz backup e recria
            else:
                backup = arquivo.replace('.csv', '_backup.csv')
                os.rename(arquivo, backup)
                print(f"Arquivo histórico corrompido. Backup salvo como {backup}. Recriando...")
                pd.DataFrame(columns=self.colunas).to_csv(arquivo, index=False)
                print(f"Arquivo {arquivo} recriado com cabeçalho.")

    #Coleta dados dos sensores e armazena em arquivos CSV, só executa se o Slider_dados for igual a 1
    def Coletar_dados(self, dados_sensores):
      
        if self.coleta_dados.value() == 0:
            return

        data_hora_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        data, hora = data_hora_str.split(' ')                 #divide em duas colonas (considerando espaoço entre a variável)

            # Prepara dicionário com todos os campos (na ordem das colunas)
        linha = {
                'Data': data,
                'Hora': hora,
                'xD': dados_sensores.get('xD'),
                'xB': dados_sensores.get('xB'),
                'MB': dados_sensores.get('MB'),
                'MD': dados_sensores.get('MD'),
                'VD': dados_sensores.get('VD'),
                'VL': dados_sensores.get('VL'),
                'VF': dados_sensores.get('VF'),
                'VB': dados_sensores.get('VB'),
                'RB': dados_sensores.get('RB'),
                'R1': dados_sensores.get('R1'),
                'R2': dados_sensores.get('R2'),
                'TA': dados_sensores.get('TA'),
            }

        # Temperaturas dos pratos
        temperaturas = dados_sensores.get('T_prato', [0.0]*14)
        for i in range(14):
                linha[f'T{i+1}'] = temperaturas[i]

        # Cria DataFrame com uma única linha
        df_linha = pd.DataFrame([linha])

        # Salva no histórico em modo append (sem cabeçalho)
        df_linha.to_csv('SensorAtuadorHist.csv', mode='a', header=False, index=False)   #mode 'a' para append
        traceback.print_exc()  # Mostra o stack trace completo

def main():
    app = QApplication(sys.argv)
    supervisor = SupervisaoGeralApp()
    Dados_supervisor = SupervisaoDadosApp()
    supervisor.dados_window = Dados_supervisor       # Atribui a janela de dados como atributo da janela principal para acesso posterior
    sensores = Sensores(ui_principal=supervisor.ui)  # Permite que a classe sensores acesse os elementos da UI principal para atualizar os gráficos e LCDs diretamente
        
    # Método para atualizar a UI principal com os dados dos sensores
    def atualizar_ui(dados):

        # Atualizar LCDs
        supervisor.lcd_xD.display(dados['xD'])
        supervisor.lcd_xB.display(dados['xB'])
        supervisor.lcd_MB.display(dados['MB'])
        supervisor.lcd_MD.display(dados['MD'])

        # Atualizar gráficos
        supervisor.atualizar_grafico_temperaturas(dados['T_prato'])
        supervisor.atualizar_grafico_xD(dados['xD'])
                     
        # Coletar dados se o slider estiver habilitado (= 1)
        Dados_supervisor.Coletar_dados(dados)                # Esta dentro do método para que a coleta ocorra na mesma frequencia da atualização gráfica
    
    # Conectar sinal de atualização dos sensores ao método de atualização da UI
    sensores.dados_atualizados.connect(atualizar_ui)
    
    def parar_sensores():
        sensores.parar_leitura_escrita()
        
    atexit.register(parar_sensores)      # Garante a execução do método quando o python é encerrado. Se esquecer alguma janela aberta ele não atua
    
    # Garantir que os sensores sejam parados quando a janela for fechada, evitando threads ou processos em execução após o fechamento da aplicação
    def closeEvent(event):
        parar_sensores()
        event.accept()            # Aceita o evento de fechamento para que a janela seja fechada normalmente
    
    supervisor.closeEvent = closeEvent
    sensores.iniciar_leitura_escrita()
    supervisor.showMaximized()  # Inicia em tela cheia
    result = app.exec()         #Fechando a janela termina o loop e passa para a próxima
    sys.exit(result)

if __name__ == "__main__":
    main()