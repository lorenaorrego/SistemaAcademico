import sys
import os

# Esto le indica a Python que busque dentro de la carpeta 'src' y 'src/Menus'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Menus')))
from autenticacion import logeo
from Menus.MenuAdmi import Menuadmin
from Menus.MenuEstudiante import MenuEstudiante
from Menus.MenuDocente import MenuDocente
def Main():
  usuarios = [{'Nombre':'Goku',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'ADMIN'},
              {'Nombre':'crilin',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'ESTUDIANTE'},
              {'Nombre':'vegeta',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'DOCENTE'}]
  UsuarioLogueado,Estado=logeo(usuarios)
  if Estado==1:
    if UsuarioLogueado['Rol'] == "ADMIN":
      usuarios=Menuadmin(usuarios)
    elif UsuarioLogueado['Rol'] == "ESTUDIANTE":
      MenuEstudiante()
    elif UsuarioLogueado['Rol'] == "DOCENTE":
      MenuDocente()
  elif Estado==2:
    print("El usuario no existe.")
  elif Estado==3:
    print("Contraseña invalada. :()")
Main()