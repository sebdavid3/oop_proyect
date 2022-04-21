import usuarios
import gatos
import gspread

class consulta:
    fecha = None
    hora = None
    
    def __init__(fecha, hora):
        pass



gc = gspread.service_account(filename='oop_proyect_a07fd0e4b4ad.json')

sh = gc.open("oop_proyect")
worksheet = sh.get_worksheet(0)

worksheet.update("A1","HOLA")


