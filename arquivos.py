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
        print('dicionario de processos', self.dic_processos_id)
        print('\n\n\n\n')
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
        tempo_execução = {}
        for line in file:
            print('\nOPERAÇÃO  [%s] ================== '%(operacao))
            line = line.split(',')
            pid = int(line[0])
            
            # gerencia tempo de execução, implementando da maneira q a prof explicou.
            #cada linha decresce um no tempo de execução.
            if (pid not in tempo_execução):
                if (pid in self.dic_processos_id):
                    tempo_execução[pid] = 1
                else:
                    print('Não existe  o processo' + str(pid) +'.')
                    operacao+=1
                    continue
            else:
                tempo_execução[pid] += 1
                print(int(self.dic_processos_id[pid].tempo_arquivo))
                if tempo_execução[pid] > int(self.dic_processos_id[pid].tempo_arquivo) :
                    print(' o processo já encerrou seu tempo de processamento')
                    operacao+=1
                    continue

            if (len(line) == 3):
                ### deletar arquivos.
                
                ### trata leitura dos arquivos.
                pid, cod_operacao, nome_arquivo = line
                pid = int(pid)
                cod_operacao = int(cod_operacao)
                nome_arquivo = nome_arquivo.strip()

                # print(pid, cod_operacao, nome_arquivo)

                # prioridade do processo.
                processo = self.dic_processos_id[pid]
                # print('encontrou o processo ', processo)
                if (processo.prioridade == 0):
                    # print('nome arquivo',nome_arquivo, self.arquivos_existentes)
                    if nome_arquivo  in self.arquivos_existentes:
                        #verificar prioridade dos 2.
                    
                        if (self.arquivos_existentes[nome_arquivo] == None or self.arquivos_existentes[nome_arquivo] == pid):
                            print('entrou delete.')
                            self.blocos_disco = [x if x != nome_arquivo else -1 for x in self.blocos_disco ]                        
                            self.arquivos_existentes.pop(nome_arquivo)
                        else:
                            print('erro :não pode deletar o arquivo, pois pertence a outro processo de prioridade zero.')
                    else:
                        print('não existe o arquivo: ',nome_arquivo)
                else:
                    # prioridade de usuario
                    #deletar prioridade de usuario.
                    if nome_arquivo in self.arquivos_existentes:
                        if self.arquivos_existentes[nome_arquivo] == pid:
                            self.blocos_disco = [x if x != nome_arquivo else -1 for x in self.blocos_disco ]                       
                            self.arquivos_existentes.pop(nome_arquivo)
                        else:
                            print('erro :não pode deletar o arquivo, pois pertence a outro processo de prioridade zero.')
                    

                    else:
                        print('não existe o arquivo: ', nome_arquivo)
            else:
                # implementar adicionar arquivo.
                #formato ID PROCESSO, codigo_OP , nome_arquivo, qtd_blocos
                pid, cod_op, nome_arquivo, qtd_blocos = line
                pid = int(pid)
                cod_op = int(cod_op)
                qtd_blocos = int(qtd_blocos)
                nome_arquivo = nome_arquivo.strip()
                
                if (nome_arquivo in self.arquivos_existentes):
                    print('erro : já existe o arquivo: '  + nome_arquivo + '. Impossível criar.')
                    operacao +=1 
                    continue
                if ( pid not in self.dic_processos_id):
                    print('erro : não existe o processo: ' + str(pid) + '.')
                    operacao +=1 
                    continue
                else:
                    escreveu = False
                    i = 0 
                    while ( i < len(self.blocos_disco)):
                        if self.blocos_disco[i] == -1:
                            inicial = i
                            espacos = 0
                            while(i < len(self.blocos_disco)  and self.blocos_disco[i] == -1):
                                espacos+=1
                                i+=1
                            #se encontrou espaço suficiente.
                            if (qtd_blocos <= espacos):
                                for i in range(inicial, inicial + qtd_blocos):
                                    self.blocos_disco[i] = nome_arquivo
                                self.arquivos_existentes[nome_arquivo] = pid
                                escreveu = True
                                break
                        else:
                            i+=1
                    if not escreveu:
                        print('O processo ' + str(pid) + ' não pode criar o arquivo '  + nome_arquivo + ' falta de espaço')
            
            operacao += 1
            print(self.blocos_disco)
            print(self.arquivos_existentes)


    def escreve_arquivo(self, espaco):

        pass