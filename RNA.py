import torch
from torch import nn
import pandas as pd
from RNA_Supervisorio_ui import Ui_RNA



class RNA_LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNA_LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1])
        return output
    
class RNA_GRU(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNA_GRU, self).__init__()
        self.hidden_size = hidden_size
        self.gru = nn.GRU(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        gru_out, _ = self.gru(x)
        output = self.fc(gru_out[:, -1])
        return output
    
class RNA_Transformer(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, nhead=4, num_layers=2):
        super(RNA_Transformer, self).__init__()
        self.hidden_size = hidden_size
        self.transformer = nn.Transformer(input_size, nhead, num_layers)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        transformer_out = self.transformer(x)
        output = self.fc(transformer_out[:, -1])
        return output