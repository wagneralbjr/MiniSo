from memoria import *


class Filas():

    def __init__(self, dic_process_id):

        self.filas = [[],[],[],[]] 
        self.dic_process_id = dic_process_id
        self.memoria = Memoria()
        self.ultimo_executado = None
        
        self.qtd_processos = len(dic_process_id) # qtd de processos.
        self.aging = 5 # tanto de tempo para aumentar a prioridade.
        self.qtd_proc_fin = 0

        return

    def insere_processo(self, processo) :
        ## insere um processo de acordo com sua prioridade na lista 
        """verifico aqui se há espaço para ser executado ou na hora de executar? """
        prioridade = processo.prioridade
        if (prioridade == 0 ):
            self.filas[0].append(processo.id)
        elif (prioridade == 1):
            self.filas[1].append(processo.id)
        elif (prioridade == 2):
            self.filas[2].append(processo.id)
        elif (prioridade == 3):
            self.filas[3].append(processo.id)


        return
    

    

    def executa_processo(self):
        """ verifica qual é o processoa  ser executado.
            e executa o mesmo.
            se acabar o tempo, apaga ele da fila.
        """

        def _executa( id , fila_atual):
            """retorna true se um processo acabou. Falso se não. """
            self.ultimo_executado = id

            if ( self.dic_process_id[id].tempo_processador > 0):
                self.dic_process_id[id].tempo_processador -= 1
                
            if (self.dic_process_id[id].tempo_processador == 0 ) :
                self.qtd_proc_fin += 1
                self.remove_processo(fila_atual)

                # retorna se acabou
                return True 
            #retorna q não acabou
            return False

        self.ultimo_executado  = None   
        for i in range(0,4):
            if (len(self.filas[i]) > 0):
                acabou  =_executa(self.filas[i][0] , i)
                return acabou
            
        return False


    def remove_processo(self, fila_atual):
        ## remove  um processo de acordo com sua fila
        self.filas[fila_atual] = self.filas[fila_atual][1:]
               
        return

    def aumenta_prioridade(self):
        
        #print(self.filas)
        for filas in self.filas:
            for processo in filas:
                pid = processo
                #print('pid',pid,'\t','ultimo',self.ultimo_executado)
                if (pid != self.ultimo_executado):
                    self.dic_process_id[pid].tempo_ultima_execucao += 1

                    # se tiver passado de 10 sem executar aumenta em 1 a prioridade.
                    if (self.dic_process_id[pid].tempo_ultima_execucao >= self.aging):
                        if (self.dic_process_id[pid].prioridade > 1):
                            prio = self.dic_process_id[pid].prioridade 

                            #remove o processo da fila antiga
                            self.filas[prio]  =  [x for x in self.filas[prio] if x != pid]
                            self.dic_process_id[pid].prioridade -= 1
                            self.insere_processo(self.dic_process_id[pid])
                            self.dic_process_id[pid].tempo_ultima_execucao = 0
                else:
                    self.dic_process_id[pid].tempo_ultima_execucao = 0
        return




    def __repr__(self):

        return str(self.filas)