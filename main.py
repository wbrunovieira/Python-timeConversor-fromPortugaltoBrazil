from datetime import datetime, timedelta
import pytz

# Definindo a data e hora para Portugal

entrada_usuario =   input("informe o horário Portugal para converter para o horário do Brasil: AAAA,MM,DD,HH,MM : ")


ano, mes, dia, hora, minuto = map(int, entrada_usuario.split(','))

data_hora_portugal = datetime(ano, mes, dia, hora, minuto)
# Definindo o fuso horário de Portugal (Lisbon) e Brasil (São Paulo)
fuso_portugal = pytz.timezone('Europe/Lisbon')
fuso_brasil = pytz.timezone('America/Sao_Paulo')

# Convertendo a data e hora de Portugal para o fuso horário do Brasil
data_hora_portugal = fuso_portugal.localize(data_hora_portugal)
data_hora_brasil = data_hora_portugal.astimezone(fuso_brasil)

hora_portugal_formatada = data_hora_portugal.strftime("%Y-%m-%d %H:%M:%S")
hora_brasil_formatada = data_hora_brasil.strftime("%Y-%m-%d %H:%M:%S")

print( f"O horário de Portugal é: {hora_portugal_formatada} será o horario do Brasil: ",hora_brasil_formatada)