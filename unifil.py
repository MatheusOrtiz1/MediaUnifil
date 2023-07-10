import PySimpleGUI as sg

sg.theme('DarkAmber')   # Adiciona um toque de cor
# Todos os elementos dentro da janela.
layout = [  [sg.Text('AVA1'), sg.InputText(key='ava1')],
            [sg.Text('AVA2'), sg.InputText(key='ava2')],
            [sg.Text('AVA3'), sg.InputText(key='ava3')],
            [sg.Text('AVA4'), sg.InputText(key='ava4')],
            [sg.Button('Calcular'), sg.Button('Sair')]]

# Cria a janela
window = sg.Window('Calculadora de Média', layout)

# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # Se o usuário fechar a janela ou clicar em cancelar
        break
    avas = [float(values['ava1']), float(values['ava2']), float(values['ava3']), float(values['ava4'])]
    media = avas[0]*0.1 + avas[1]*0.3 + avas[2]*0.2 + avas[3]*0.4

    if media >= 70:
        sg.popup(f'Parabéns! Você foi aprovado com média {media:.2f}!')
    else:
        sg.popup(f'Infelizmente você foi reprovado com média {media:.2f}.')

window.close()