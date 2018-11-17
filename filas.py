from memoria import *


class Filas():

    def __init__(self, dic_process_id):

        self.filas = [[],[],[],[]] 
        self.dic_process_id = dic_process_id
        self.memoria = Memoria()
        self.ultimo_executado = None


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
    
    

    # debugar essa parte.

    def executa_processo(self):
        """ verifica qual é o processoa  ser executado.
            e executa o mesmo.
            se acabar o tempo, apaga ele da fila.
        """

        def _executa( id , fila_atual):
            
            self.ultimo_executado = id

            if ( self.dic_process_id[id].tempo_processador > 0):
                self.dic_process_id[id].tempo_processador -= 1

            if (self.dic_process_id[id].tempo_processador == 0 ) :
                self.remove_processo(fila_atual)
            
            # else:
            #     #aumenta prioridade se não for processo de tempo real.
                
            #     if (self.dic_process_id[id].prioridade > 1):
            #         # se a prioridade é maior q 1. devemos remover da fila atual
            #         # e inserir uma fila abaixo da que ele está.

            #         self.remove_processo(fila_atual)
            #         self.dic_process_id[id].prioridade -= 1
            #         self.insere_processo(self.dic_process_id[id])
                    
                    
            #     elif ( self.dic_process_id[id].prioridade == 1):
            #         # se é de prioridade 1, simplesmente remove do início e adiciona no final.
            #         self.remove_processo(fila_atual)                
            #         self.insere_processo(self.dic_process_id[id])

        self.ultimo_executado  = None   
        for i in range(0,4):
            if (len(self.filas[i]) > 0):
                _executa(self.filas[i][0] , i)
                return


        return


    def remove_processo(self, fila_atual):
        ## remove  um processo de acordo com sua fila
        self.filas[fila_atual] = self.filas[fila_atual][1:]
               
        return

    def aumenta_prioridade(self):
        

        pass
    

    def __repr__(self):

        return str(self.filas)