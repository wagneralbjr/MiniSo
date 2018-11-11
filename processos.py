

""" FORMATO ENTRADA: 
<tempo de inicialização>, <prioridade>, <tempo de processador>, <blocos em memória>, <número-
código da impressora requisitada>, <requisição do scanner>, <requisição do modem>, <número-
código do disco> """

    
class Processo():
    
    def __init__(self, tempo_inicial, prioridade, tempo_processador,
                blocos_mem, cod_impressora, scanner, modem,disco):

        self.tempo_inicial = tempo_inicial
        self.prioridade = prioridade
        self.tempo_processador = tempo_processador
        self.blocos_mem = blocos_mem
        self.cod_impressora = cod_impressora
        self.scanner = scanner
        self.modem = modem
        self.disco = disco
    
    def __repr__(self):
        return """( TEMP_INI : %s, PRI : %s, T_PRO: %s, BL_MEM: %s,COD_IMP: %s, SCANNER: %s, MODEM: %s, DISCO %s)""" % (self.tempo_inicial, self.prioridade,
         self.tempo_processador, self.blocos_mem, self.cod_impressora, self.scanner, self.modem, self.disco)
    
            


    
