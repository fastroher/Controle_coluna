import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLCDNumber, QDial, QVBoxLayout, QWidget, QGraphicsSimpleTextItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from Supervisorio_ui import Ui_Superv_geral
from Sensores import Sensores
import atexit

class SupervisaoGeralApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Superv_geral()
        self.ui.setupUi(self)
        
        # Tornar os elementos da UI acessíveis
        self.lcd_xD = self.ui.lcd_xD
        self.lcd_xB = self.ui.lcd_xB
        self.lcd_MB = self.ui.lcd_MB
        self.lcd_MD = self.ui.lcd_MD
        self.lcd_VL = self.ui.lcd_VL
        self.lcd_VD = self.ui.lcd_VD
        self.lcd_RB = self.ui.lcd_RB
        self.dial_ctr_VL = self.ui.dial_ctr_VL
        self.dial_ctr_VD = self.ui.dial_ctr_VD
        self.dial_RB = self.ui.dial_RB
        
        # Substituir QGraphicsView por QChartView para os gráficos
        self.setup_graficos()
        
        # Dados históricos para os gráficos
        self.tempo = 0
        
    def setup_graficos(self):
        """Configura os gráficos substituindo QGraphicsView por QChartView"""
        # Substituir graph_T por QChartView
        layout_T = QVBoxLayout()
        self.chart_view_T = QChartView()
        self.chart_view_T.setRenderHint(QPainter.Antialiasing)
        layout_T.addWidget(self.chart_view_T)
        
        # Substituir graph_xD por QChartView
        layout_xD = QVBoxLayout()
        self.chart_view_xD = QChartView()
        self.chart_view_xD.setRenderHint(QPainter.Antialiasing)
        layout_xD.addWidget(self.chart_view_xD)
        
        # Configurar os layouts nos widgets existentes
        widget_T = QWidget()
        widget_T.setLayout(layout_T)
        widget_xD = QWidget()
        widget_xD.setLayout(layout_xD)
        
        # Adicionar aos layouts existentes
        self.ui.graph_T.setParent(None)  # Remover o QGraphicsView original
        self.ui.graph_xD.setParent(None)  # Remover o QGraphicsView original
        
        # Adicionar os novos chart views no layout
        self.ui.layout_graph.insertWidget(0, widget_xD)
        self.ui.layout_graph.insertWidget(1, widget_T)
        
        # Configurar os gráficos
        self.setup_grafico_temperaturas()
        self.setup_grafico_xD()
    
    def setup_grafico_temperaturas(self):
        """Configura o gráfico de temperaturas dos pratos"""
        # Criar chart
        self.chart_T = QChart()
        self.chart_T.setTitle("Temperatura dos Pratos")
        self.chart_T.setAnimationOptions(QChart.SeriesAnimations)
        
        # Configurar eixos
        self.axis_x_T = QValueAxis()
        self.axis_x_T.setTitleText("Tempo (s)")
        self.axis_x_T.setRange(0, 100)
        
        self.axis_y_T = QValueAxis()
        self.axis_y_T.setTitleText("Temperatura (°C)")
        self.axis_y_T.setRange(0, 100)
        
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
            series.setName(f"Prato {i+1}")
            pen = QPen(colors[i % len(colors)])
            pen.setWidth(2)
            series.setPen(pen)
            self.series_T.append(series)
            self.chart_T.addSeries(series)
            series.attachAxis(self.axis_x_T)
            series.attachAxis(self.axis_y_T)
        
        # Configurar o chart view
        self.chart_view_T.setChart(self.chart_T)
    
    def setup_grafico_xD(self):
        """Configura o gráfico da composição xD"""
        self.chart_xD = QChart()
        self.chart_xD.setTitle("Composição do Destilado (xD)")
        self.chart_xD.setAnimationOptions(QChart.SeriesAnimations)
        
        # Configurar eixos
        self.axis_x_xD = QValueAxis()
        self.axis_x_xD.setTitleText("Tempo (s)")
        self.axis_x_xD.setRange(0, 100)
        
        self.axis_y_xD = QValueAxis()
        self.axis_y_xD.setTitleText("xD (%)")
        self.axis_y_xD.setRange(0, 100)
        
        self.chart_xD.addAxis(self.axis_x_xD, Qt.AlignBottom)
        self.chart_xD.addAxis(self.axis_y_xD, Qt.AlignLeft)
        
        # Criar série para xD
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
    
    def atualizar_grafico_temperaturas(self, temperaturas):
        """Atualiza o gráfico de temperaturas e insere rótulo do último valor"""
        self.tempo += 1

        # Manter apenas os últimos 100 pontos
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

    def atualizar_grafico_xD(self, xD):
        """Atualiza o gráfico da composição xD e insere rótulo do último valor"""
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

def main():
    app = QApplication(sys.argv)
    supervisor = SupervisaoGeralApp()
    sensores = Sensores()
    
    # Buscar elementos da UI
    def encontrar_elementos():
        elementos = {}
        
        # Lista de elementos que queremos encontrar
        element_mapping = {
            'lcd_xD': supervisor.lcd_xD,
            'lcd_xB': supervisor.lcd_xB,
            'lcd_MB': supervisor.lcd_MB,
            'lcd_MD': supervisor.lcd_MD,
            #'lcd_VL': supervisor.lcd_VL,
            #'lcd_VD': supervisor.lcd_VD,
            #'lcd_RB': supervisor.lcd_RB,
            #'dial_ctr_VL': supervisor.dial_ctr_VL,
            #'dial_ctr_VD': supervisor.dial_ctr_VD,
            #'dial_RB': supervisor.dial_RB
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
                #'lcd_VL': dados['VL'],
                #'lcd_VD': dados['VD'],
                #'lcd_RB': dados['RB']
            }
            
            for elem_name, value in lcd_mapping.items():
                if elem_name in elementos_ui:
                    try:
                        elementos_ui[elem_name].display(float(value))
                    except Exception as e:
                        print(f"Erro ao atualizar {elem_name}: {e}")
            
            # Atualizar Dials (apenas valores inteiros)
            #dial_mapping = {
            #    'dial_ctr_VL': int(dados['VL']),
            #    'dial_ctr_VD': int(dados['VD']),
            #    'dial_RB': int(dados['RB'])
            #}
            
            #for elem_name, value in dial_mapping.items():
            #    if elem_name in elementos_ui:
            #        try:
            #            elementos_ui[elem_name].blockSignals(True)
            #            elementos_ui[elem_name].setValue(value)
            #            elementos_ui[elem_name].blockSignals(False)
            #        except Exception as e:
            #            print(f"Erro ao atualizar {elem_name}: {e}")
            
            # Atualizar gráficos
            supervisor.atualizar_grafico_temperaturas(dados['T_prato'])
            supervisor.atualizar_grafico_xD(dados['xD'])
                        
        except Exception as e:
            print(f"Erro geral ao atualizar UI: {e}")
    
    # Conectar sinal de atualização
    sensores.dados_atualizados.connect(atualizar_ui)
    
    def parar_sensores():
        print("Parando sensores...")
        sensores.parar_leitura()
    
    # Registrar para executar quando o programa terminar
    atexit.register(parar_sensores)
    
    # Sobrescrever o método closeEvent
    def closeEvent(event):
        print("Fechando aplicação...")
        parar_sensores()
        event.accept()
    
    supervisor.closeEvent = closeEvent
    
    # Iniciar sensores
    sensores.iniciar_leitura()
    print("Sensores iniciados. Feche a janela para parar.")
    
    supervisor.show()
    result = app.exec()
    
    # Garantir parada final
    parar_sensores()
    print("Aplicação encerrada.")
    
    sys.exit(result)

if __name__ == "__main__":
    main()