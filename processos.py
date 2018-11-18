

""" FORMATO ENTRADA: 
<tempo de inicialização>, <prioridade>, <tempo de processador>, <blocos em memória>, <número-
código da impressora requisitada>, <requisição do scanner>, <requisição do modem>, <número-
código do disco> """

    
class Processo():
    
    def __init__( self,tempo_inicial, prioridade, tempo_processador,
                blocos_mem, cod_impressora, scanner, modem,disco,id):

        self.tempo_inicial = tempo_inicial
        self.prioridade = prioridade
        self.tempo_processador = tempo_processador
        
        self.mem_offset = None # offset da memoria.
        self.blocos_mem = blocos_mem # blocos de memoria necessários.
        self.cod_impressora = cod_impressora
        self.scanner = scanner
        self.modem = modem
        self.disco = disco
        self.id = id
        self.tempo_ultima_execucao = 0

        
    
    def __repr__(self):
        return """(ID:  %s, TEMP_INI : %s, PRI : %s, T_PRO: %s, BL_MEM: %s,COD_IMP: %s, SCANNER: %s, MODEM: %s, DISCO %s)"""%(
            self.id,
            self.tempo_inicial, self.prioridade,
            self.tempo_processador, self.blocos_mem,
            self.cod_impressora, self.scanner, self.modem, self.disco)
    
    def __lt__(self, other):
        return self.tempo_inicial < other.tempo_inicial



    
