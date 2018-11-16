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



    while( 1 ):
        
        
        #verifica se existem items chegando na fila de prioridade.
        if(tempo_atual in  dic_process_tempo):
            for elem in dic_process_tempo[tempo_atual]:
                #trata os itens que foram encontrados na fila de prioridade.
                filas.insere_processo(elem)

        print(tempo_atual,'\t',filas)
        filas.executa_processo()

        
        # #encontra o processo atual a ser executado.
        # fila_atual = None
        # if (processo_atual is None):
        #     # se nenhum processo está sendo executado, executa um.
        #     if (len(fila_0) > 0 ):
        #         processo_atual = fila_0[0]
        #         fila_atual = 0
        #     elif( len(fila_1) > 0 ):
        #         processo_atual = fila_1[0]
        #         fila_atual = 1
        #     elif( len(fila_2) > 0 ):
        #         processo_atual = fila_2[0]
        #         fila_atual = 2
        #     elif( len(fila_3) > 0 ):
        #         processo_atual = fila_3[0]
        #         fila_atual = 3
        # else :
        #     candidato = None
        #     if (len(fila_0) > 0 ):
        #         candidato = fila_0[0]
        #     elif( len(fila_1) > 0 ):
        #         candidato = fila_1[0]
        #     elif( len(fila_2) > 0 ):
        #         candidato = fila_2[0]
        #     elif( len(fila_3) > 0 ):
        #         candidato = fila_3[0]    
        #     if (dic_process_id[processo_atual] > dic_process_id[candidato]):
        #         # a ideia aqui é aumentar a prioridade do processo que era atual ?
        #         processo_atual = candidato

        # #print(processo_atual)
        # #executa o processo. diminui o tempo do processo atual e etc. se acabou tira ele da fila.
        # if (processo_atual is not None):
        #     print('antes de executar',dic_process_id[processo_atual].tempo_processador)
        #     dic_process_id[processo_atual].tempo_processador -= 1
        #     print('apos executar',dic_process_id[processo_atual].tempo_processador)

        #     # if(dic_process_id[processo_atual].tempo_processador == 0):
        #     #     if (fila_atual == 0):
        #     #         fila_0 = [1:]
        #     #     if (fila_atual == 1):
        #     #         fila_1 = [1:]
        #     #     if (fila_atual == 2):
        #     #         fila_2 = [1:]
        #     #     if (fila_atual == 3):
        #     #         fila_3 = [1:]
            

        #     # dic_ 
                

        # implementar condição de saida.

        

        #aumenta o tempo.
        
        tempo_atual += 1
        if(tempo_atual > 50):
            break
    print(tempo_atual,'\t',filas)
    




if __name__ == "__main__":
    #monta lista de processos

    carrega_processos()
    simula_processos()