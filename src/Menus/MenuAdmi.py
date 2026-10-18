from Validaciones import ValidarEntero
from UsuariosTemp import RegistrarUsuario, ListarUsuarios
#from Usuarios import * se importa lo necesario para tener lo más limpio posible el código
def Menuadmin(usuarios):
  Opcion=1
  while Opcion!=3:
    print('Opciones del menu:')
    print('   1. Registrar usuario')
    print('   2. Listar usuarios registrado')
    print('   3. Salir')
    Opcion=ValidarEntero('Ingrese una opcion: ')
      #    int(input('Ingrese una opcion: '))
    if Opcion==1:
      usuarios =RegistrarUsuario(usuarios)
    elif Opcion==2:
      print('Listando usuarios registrado')
      ListarUsuarios(usuarios)
    elif Opcion==3:
      print('Que vuelvas pronto!')
      return
    else:
      print('Opcion incorrecta')