from processos import *
import operator
from recursos import *
from filas import *
from memoria import *
from arquivos import *

dic_processos = {}
dic_process_id = {}
dic_process_tempo = {}

def carrega_processos():

    file = open('processes.txt')
    id = 0


    for line in file:
        line = line[:-1].split(',')
        line = [int(x) for x in line]

        
        processo = Processo(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],id)
        prio = int(line[1])
        memoria  = int(line[3])
        print(prio, memoria)
        if (prio == 0 and memoria > 64):
            continue 
        if (prio == 1 and memoria > 960):
            continue
        

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
    memory = Memoria()

    log_executados = {}

    tempo_atual = 1
    processo_atual = None

    while( True ):
        #verifica se existem items chegando na fila de prioridade.
        if(tempo_atual in  dic_process_tempo):
            for elem in dic_process_tempo[tempo_atual]:
                #trata os itens que foram encontrados na fila de prioridade.

                # valida se possuem os recursos necessários disponíveis para ser executado.
                if (recur.valida_recursos(elem) and memory.verificar_espaco(elem)):
                    filas.insere_processo(elem)
                else:
                    """ Se o recurso não pode ser utilizado naquele momento, modifica o tempo inicial do
                    processo e faz com que ele seja inicializado mais tarde.""" 
                    elem.tempo_inicial += 1
                    #verifica se já existe uma lista. se não cria uma.                    
                    try:
                        dic_process_tempo[tempo_atual + 1].append(elem)
                    except:
                        dic_process_tempo[tempo_atual + 1] = [elem]
                           


        print(tempo_atual,'\t',filas ,'UE: ',end='')
        #print(recur)

        #guarda o log dos executados.
        log_executados[tempo_atual] = filas.log_filas()

        #executa o processo com mais prioridade.
        if filas.executa_processo() :
            #print('entrou para desalocar',filas.dic_process_id[filas.ultimo_executado])
            recur.desaloca_recursos(filas.dic_process_id[filas.ultimo_executado])
            memory.desaloca_memoria(filas.dic_process_id[filas.ultimo_executado])
        else:
            pass

        print(filas.ultimo_executado)
        filas.aumenta_prioridade()

        
        #print(memory.blocos_kernel)
        #print(memory.blocos_usuario)
        tempo_atual += 1
        if(filas.qtd_proc_fin == filas.qtd_processos):
            break

        if(tempo_atual > 15):
            break
    print('---------------------')
    print(tempo_atual,'\t',filas,'UE:',filas.ultimo_executado)
    print(log_executados)

    return log_executados




if __name__ == "__main__":
    #monta lista de processos

    carrega_processos()
    log_executados = simula_processos()

    # simula arquivos.
    arq = Arquivos(dic_process_id,log_executados)
    arq.le_disco()
    