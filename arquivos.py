""" 
    linha 1 : qtd blocos disco
    linha 2 : qtd segmentos ocupado do disco(n)
    linha 3 até n+2:
            id_arquivo, prim_bloco ,qtd de blocos
    Linha n+3:
        <ID_Processo>,  <Código_Operação>,  <Nome_arquivo>, 
        <se_operacaoCriar_numero_blocos>. 

    codigos OP : 
    codigo 0 escreve
    codigo 1 apaga
""" 



class Arquivos():


    def __init__(self,dic_processos_id, log_executados):


        self.blocos_disco  = None
        self.log_executados = log_executados
        self.arquivos_existentes = dict()
        self.dic_processos_id = dic_processos_id
        

    def le_disco(self):

        file = open('files.txt') 
        self.blocos_disco = [-1 for x in range(0, int(next(file)))]
        
        qtd_segmentos = (int(next(file)))

        for i in range(0, qtd_segmentos):
            nome_arquivo, prim_bloco, qtd_blocos = next(file).split(',')
            prim_bloco = int(prim_bloco)
            qtd_blocos = int(qtd_blocos)

            self.arquivos_existentes[nome_arquivo] = None 

            for i in range( prim_bloco, prim_bloco + qtd_blocos):
                self.blocos_disco[i] = nome_arquivo

        print(self.blocos_disco)
        operacao = 0
        for line in file:
            line = line.split(',')

            if (len(line) == 3):
                ### deletar arquivos.
                
                pid, cod_operacao, nome_arquivo = line
                pid = int(pid)
                cod_operacao = int(cod_operacao)

                print(pid, cod_operacao, nome_arquivo)

                # prioridade do processo.
                processo = self.dic_processos_id[pid]
                if (processo.prioridade == 0):
                    if nome_arquivo  in self.arquivos_existentes:
                        self.blocos_disco = [x if x != nome_arquivo else -1 for x in self.blocos_disco ]                        
                    else:
                        print('não existe o arquivo: ',nome_arquivo)
                else:
                    # prioridade de usuario
                    #implementar deletar prioridade de usuario.

                    pass
            else:
                # le 
                # implementar adicionar arquivo.
                pass
            operacao += 1
            

        print(self.blocos_disco)
        print(self.arquivos_existentes)


    def escreve_arquivo(self, espaco):

        pass