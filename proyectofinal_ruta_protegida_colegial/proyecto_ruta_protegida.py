op_admin=()
CLAVE="0918"
clave_admin="1234"
clave_estudiante="123"
estudiante_nombre="noemi k. vargas"
estudiante_curso="2B"
estudiante_ruta="sacaba"
estudiante_estado= " en espera"
#BLOQUE DE SEGURIDAD
print("===ACCESO===")
while True:
    clave=input("Contraseña : ")
    if clave == CLAVE:
        print("BIENVENID@")
        break
    else:
        print("contraseña incorrecta")
punto1=" viña central"
punto2="av. tunel"
punto3="colegio Gral. Juan Jose Torrez A "
hora_llegada="8:10 AM"
# MENU PRINCIPAL
while True:
    print("MENU PRINCIPAL")
    print("1. iniciar sesion como administrador")
    print("2. iniciar sesion como estudiante")
    print("3. salir del sistema")
    print("")
    break
opcion= input("elige una opcion : ").strip().lower()
if opcion=="1":
    print("")
    user= input("usuario admin:").strip()
    clave= input ("clave admin:").strip()
    if clave == clave_admin:
        print("")
        print("acceso concedido. Bienvenid@ administrador")
        print("")
        #MENU DEL ADMINISTRADOR
        while True:
            print("MENU ADMINISTRADOR")
            print("1. ver datos del estudiante ")
            print("2. ver puntos de la ruta")
            print("3. cerrar sesion admin")
            print("")
            break
        op_admin= input("elige una opcion : ").strip()
        if op_admin== "1":
            print("")
            print("DATOS DEL ESTUDIANTE")
            print("nombre:",estudiante_nombre)
            print("curso:",estudiante_curso)
            print("ruta asignada:",estudiante_ruta)
            print("estado actual:",estudiante_estado)
            print("")
        elif op_admin== "2":
            print("")
            print("PUNTOS DE LA RUTA PROTEGIDA")
            print("punto 1:",punto1)
            print("punto 2 :",punto2)
            print("punto 3 : ",punto3)
            print("hora de llegada al colegio:",hora_llegada)
            print("")
        elif op_admin== "3":
            print("cerrando sesion de administrador")
            print("")
        else:
            print("opcion no valida")
            print("")

elif opcion=="2":
    print("")
    user= input ("usuario estudiante: ").strip()
    clave= input("clave estudiante: ").strip()
    if clave == clave_estudiante:
        print("")
        print("acceso concedido. Bienvenid@",estudiante_nombre)
    else:
        print("acceso no concedido")
        #MENU ESTUDIANTIL
    while True:
        print("MENU ESTUDIANTIL")
        print("1. ver mi informacion")
        print("2. ver mi ruta y horario ")
        print("3. cerrar sesion estudiantil")
        print("")
        break
    op_est= input ("elige una opcion: ").strip()
    if op_est=="1":
        print("")
        print("MI INFORMACION")
        print("nombre:",estudiante_nombre)
        print("curso:",estudiante_curso)
        print("estado: ",estudiante_estado)
        print("")
    elif op_est=="2":
         print("")
         print("MI RUTA Y HORARIO")
         print("ruta asignada:",estudiante_ruta)
         print("punto de recogida 1: ",punto1)
         print("punto de recogida 2: ",punto2)
         print("llegada al colegio: ",hora_llegada)
         print("")
    elif op_est=="3":
         print("cerrando sesion estudiantil")
         print("")
    else:
     print("opcion no valida")
     print("")
     #SALIENDO DEL PROGRAMA....
elif opcion=="3":
    print("")
    print("cerrando sistema de ruta protegida...")
    print("gracias por usar el sistema :)\3 ")