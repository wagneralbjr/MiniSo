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
        
        

    def __repr__():

        return (""" scanner  => %s , printer1 => %s, printer2 => %s, modem => %s, sata1 => %s, sata2 =>""")%(
            self.scanner,self.printer1,self.printer2, self.modem, self.sata1, self.sata2 )
    
