# UNIVERSIDAD DEL VALLE DE GUATEMALA
# FACULTAD DE INGENIERÍA
# DEPARTAMENTO DE CIENCIA DE LA COMPUTACIÓN
# ALGORITMOS Y PROGRAMACIÓN BÁSICA
# SECCIÓN 30
# Autor: José Morales
# carné: 21286
# Fecha: 9 de mayo de 2021
# Parcial 2

from database import Database

def main():
    db = Database() # inicializa la base de datos de series
    print('###################################### BIENVENIDO ######################################')
    while(True):
        print('----------------------------------------- MENU -----------------------------------------')
        print('# Presione un número para acceder a alguna de las siguientes acciones:')
        print()
        print('1. Datos de cursos.')
        print('2. Estudiantes que aprobaron los 3 cursos.')
        print('3. Estudiantes que reprobaron los 3 cursos.')
        print('4. Promedio de cada estudiante (guarda en el archivo).')
        print('0. Salir.')
        print()
        accion = input('# Ingrese número de acción > ')
        if(accion == '0'):
            print('Adios')
            break
        elif(accion == '1'):
            print('----------------------------------------- Datos de cursos -----------------------------------------')
            print('# Estudiantes aprobados por curso')
            db.get_aprobado_curso()
            print('# Promedio por curso')
            db.get_prom_curso()
        elif(accion == '2'):
            print('----------------------------- Estudiantes que aprobaron los 3 cursos ------------------------------')
            db.get_aprobado()
        elif(accion == '3'):
            print('----------------------------- Estudiantes que reprobaron los 3 cursos -----------------------------')
            db.get_no_aprobado()
        elif(accion == '4'):
            print('----------------------------------- Promedio de cada estudiante -----------------------------------')
            db.set_prom()
        else:
            print('# Acción no valida, intente de nuevo')

        input('# Presiona Enter para continuar>')


if __name__ == '__main__':
    main()