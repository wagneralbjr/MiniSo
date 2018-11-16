class Filas():

    def __init__(self):

        self.filas = [[],[],[],[]]



        return

    def insere_processo(self, processo) :
        ## insere um processo de acordo com sua prioridade na lista 

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
    
    def remove_processo(self):
        ## remove  um processo de acordo com sua prioridade na lista 
        pass

    def aumenta_prioridade(self):

        pass
    

    def __repr__(self):

        return str(self.filas)