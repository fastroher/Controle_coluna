import sqlite3

banco = sqlite3.connect('Sensores_Atuadores.db')
cursor = banco.cursor()
cursor.execute('''SELECT * FROM Historico''')
dados = cursor.fetchall()
print(dados)