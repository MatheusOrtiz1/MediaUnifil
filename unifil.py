import PySimpleGUI as sg

sg.theme('DarkAmber')   # Adiciona um toque de cor
# Todos os elementos dentro da janela.
layout = [  [sg.Text('AVA1'), sg.InputText()],
            [sg.Text('AVA2'), sg.InputText()],
            [sg.Text('AVA3'), sg.InputText()],
            [sg.Text('AVA4'), sg.InputText()],
            [sg.Button('Calcular'), sg.Button('Sair')]]

# Cria a janela
window = sg.Window('Calculadora de Média', layout)

# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # Se o usuário fechar a janela ou clicar em cancelar
        break
    avas = [float(values[0]), float(values[1]), float(values[2]), float(values[3])]
    media = avas[0]*0.1 + avas[1]*0.3 + avas[2]*0.2 + avas[3]*0.4
    sg.popup(f'Sua média é {media}')

window.close()