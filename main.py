# projeto bater_ponto
# 1- importar as bibilotecas necessária.
from datetime import datetime

#2- perguntar o nome da pessoa a bater o ponto.
quem = input('Quem vai bater o ponto? ').title()

#3- qual a linguagem estudada?
estudado = input('''O que foi/vai ser estudado? ''').title()
nome_arquivo = f'{estudado}.txt'

#4- perguntar se é de entrada ou de saída e coletar tempo de batida de ponto.
bater_ponto = input('É o ponto de saída ou de entrada? ' ).title()
agora = datetime.now()

#5- condições pra cada situação.
if bater_ponto in ['Entrada'] :
    print(f'{quem} bateu o ponto de {bater_ponto} as {agora.strftime("%H:%M")} na data {agora.strftime("%d/%m/%Y")} e estudou {estudado}!')
elif bater_ponto in ['Saída', 'Saida'] :
        print(f'{quem} bateu o ponto de {bater_ponto} as {agora.strftime("%H:%M")} na data {agora.strftime("%d/%m/%Y")} e estudou {estudado}!')
        
#6- registrar isso em um arquivo (pdf, c=txt e entre outros).
with open (nome_arquivo, "a") as documento:
    documento.write(f'\n{quem} bateu o ponto de {bater_ponto} as {agora.strftime("%H:%M")} na data {agora.strftime("%d/%m/%Y")} e estudou {estudado}!\n')
#FALTA FAZER:
        #1- cada coisa que foi estudada salva em um arquivo diferente *FEITO
        #2- mostrar quanto tempo eu estudei.
        #3- perguntar se foi só essa linguagem que estudei ou tem mais.
        #4- registrar isso em um arquivo (pdf, c=txt e entre outros).