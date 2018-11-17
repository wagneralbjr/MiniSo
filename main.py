from processos import *
import operator
from recursos import *
from filas import *

dic_processos = {}
dic_process_id = {}
dic_process_tempo = {}


def carrega_processos():

    file = open('processes.txt')
    id = 0


    for line in file:
        line = line[:-1].split(',')
        line = [int(x) for x in line]
        #print(line)
        
        processo = Processo(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],id)

        #dicionário de processos por id.
        dic_process_id[id] = processo
        id+=1

        #monta dicionario de tempo
        if (line[0] in  dic_process_tempo):
            dic_process_tempo[line[0]].append( processo)
        else:
            dic_process_tempo[line[0]] = [processo]

    print(dic_process_tempo)
    
    return 


def simula_processos():
   
    #inicializa dispositivos.
    recur = Recursos()

    #inicializa filas

    filas = Filas(dic_process_id)

    log_executados = []

    tempo_atual = 1
    processo_atual = None



    while( True ):
        
        
        #verifica se existem items chegando na fila de prioridade.
        if(tempo_atual in  dic_process_tempo):
            for elem in dic_process_tempo[tempo_atual]:
                #trata os itens que foram encontrados na fila de prioridade.
                filas.insere_processo(elem)

        print(tempo_atual,'\t',filas ,'UE: ',end='')
        filas.executa_processo()
        print(filas.ultimo_executado)
        


        #passa o tempo na simulação        
        tempo_atual += 1
        if(tempo_atual > 50):
            break
    print('---------------------')
    print(tempo_atual,'\t',filas,'UE:',filas.ultimo_executado)
    




if __name__ == "__main__":
    #monta lista de processos

    carrega_processos()
    simula_processos()