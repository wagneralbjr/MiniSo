from processos import *




lista_processos = []




def carrega_processos():

    file = open('processes.txt')
    for line in file:
        line = line[:-1].split(',')
        lista_processos.append( Processo(line[0],line[1],line[2],line[3]
            ,line[4],line[5],line[6],line[7]))
        
    for elem in lista_processos:
        print(elem)


if __name__ == "__main__":
    #monta lista de processos

    carrega_processos()