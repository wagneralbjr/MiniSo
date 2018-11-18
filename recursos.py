"""
    1 scanner
    2 impressoras
    1 modem
    2 dispositivos SATA
"""

class Recursos():

    def __init__(self):

        self.scanner = False
        self.printer1 = False
        self.printer2 = False
        self.modem = False
        self.sata1 = False
        self.sata2 = False
        
        

    def __repr__(self):

        return (""" scanner  => %s , printer1 => %s, printer2 => %s, modem => %s, sata1 => %s, sata2 => %s""")%(
            self.scanner,self.printer1,self.printer2, self.modem, self.sata1, self.sata2 )
    
    def valida_recursos(self,processo):
        """retorna Falso se já estiverem utilizando algusn dos recursos necessários. """
        #condições que não podem ocorrer.
        impressora = ( (self.scanner == True) and (processo.scanner == 1))
        printer_1 = ((self.printer1 == True) and processo.cod_impressora == 1)
        printer_2 = ((self.printer2 == True) and processo.cod_impressora == 2)
        modem = ((self.modem == True) and processo.modem == 1)
        sata1 = ((self.sata1 == True) and processo.disco == 1)
        sata2 = ((self.sata2 == True) and processo.disco == 2)
        
        
        condicoes = [impressora, printer_1,printer_2, modem,sata1,sata2]

        """ se algum dos dispositivos que não podem ser utilizados já está sendo
            retorna falso"""
        if any(condicoes):
            return False
        

        # salva qual dispositivo deve ser utilizado.
        if not impressora:
            self.impressora = (processo.scanner == 1)
        if not printer_1:
            self.printer1 = processo.cod_impressora == 1
        if not printer_2:
            self.printer2 = processo.cod_impressora == 2
        if not modem:
            self.modem = processo.modem == 1
        if not sata1:
            self.sata1 = processo.disco == 1
        if not sata2:
            self.sata2 = processo.disco == 2
        
        return True

        
    def desaloca_recursos(self, processo):
        """ desaloca os recursos do último processo executado se utilizou algum.""" 

        if processo.cod_impressora == 1:
            self.printer1 = False
        
        if processo.cod_impressora == 2:
            self.printer2 = False
        
        if processo.scanner == 1:
            self.scanner = False
        
        if processo.disco == 1:
            self.sata1 = False
        
        if processo.disco == 2:
            self.sata2 = False
        
        if processo.modem == 1:
            
            self.modem = False

        

        