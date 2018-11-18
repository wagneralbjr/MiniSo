"""memoria.py"""

class Memoria():
    
    def __init__(self):

        self.tam_mem = 1024
        self.tam_mem_real = 64

        self.tam_mem_usu = self.tam_mem - self.tam_mem_real

        self.blocos_kernel  = [-1 for x in range (0,self.tam_mem_real) ] # -1 significa livre.
        self.blocos_usuario  = [-1 for x in range (0,self.tam_mem_usu) ] # -1 significa livre.

        #armazena a quantidade de blocos livres.
        self.blocos_kernel_livre = self.tam_mem_real
        self.blocos_usuario_livre = self.tam_mem_usu


    def verificar_espaco(self, processo):
        """ retorna True se conseguir espaço livre para executar o processo."""
        
        qtd_blocos = processo.blocos_mem

        if processo.prioridade == 0 :
            
            i = 0          
            while i < self.tam_mem_real:
                
                if (self.blocos_kernel[i] == -1):
                    # se é vazio, começa a contar quantos tem e vê se o programa cabe.
                    inicial = i
                    espacos = 0
                    while (i < self.tam_mem_real and self.blocos_kernel[i] == -1 ):
                        espacos +=1
                        i+=1
                        
                    if (qtd_blocos <= espacos):
                        """  se encontrou espaco livre o suficiente aloca os recursos para o processo """
                        processo.mem_offset = inicial
                        
                        for i in range(inicial,  inicial + qtd_blocos):
                            self.blocos_kernel[i] = processo.id
                            #self.blocos_kernel_livre -= qtd_blocos

                        return True
                else:
                    i+=1
                    #se não é livre, só anda na lista de blocos.
                
            return False

        else:
            """ aloca espaço memoria continua usuário""" 
                        
            i = 0
            while i < self.tam_mem_usu:

                if ( self.blocos_usuario[i] == -1):

                    inicial = i 
                    espacos = 0 
                    while(i < self.tam_mem_usu and self.blocos_usuario[i] == -1):
                        espacos +=1
                        i+=1
                    if(qtd_blocos <= espacos):
                        processo.mem_offset  = inicial
                        for i in range(inicial, inicial + qtd_blocos):
                            self.blocos_usuario[i] = processo.id          
                        return True
                else:
                    i+=1
                
            return False

              

    def desaloca_memoria(self, processo):
        """ desaloca a memoria utilizada por um processo quando ele termina sua execução.""" 


        if (processo.prioridade == 0):
            for i in range(processo.mem_offset, processo.mem_offset + processo.blocos_mem):
                self.blocos_kernel[i] = -1
        else:
            """ tempo de usuario"""
            for i in range(processo.mem_offset, processo.mem_offset + processo.blocos_mem):
                self.blocos_usuario[i] = -1




        
    

