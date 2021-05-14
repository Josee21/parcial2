import matplotlib.pyplot as plt

class Database:
    database = []

    def __init__(self) -> None:
        with open('registroUVW.csv', 'r', encoding='utf-8') as archivo: # lee el archivo y lo cierra de una vez cuando sale del bloque
            lineas = archivo.read()
            i = 0
            for linea in lineas.split('\n'):
                i += 1
                datos = linea.split(',')
                if(datos[0] == '' or i == 1): # se salta la primera linea de titulos o cuando la linea está vacía
                    continue
                d = {}
                d['id'] = int(datos[0].lstrip().rstrip()) # toma cada dato y los coloca dentro de un arreglo quitando los espacios 
                d['carnet'] = int(datos[1].lstrip().rstrip()) # al inicio y al final de los datos si los hubiera
                d['sexo'] = datos[2].lstrip().rstrip()
                d['etnicidad'] = datos[3].lstrip().rstrip()
                d['nivelEducPadres'] = datos[4].lstrip().rstrip()
                d['matematicas'] = int(datos[5].lstrip().rstrip())
                d['algoritmos'] = int(datos[6].lstrip().rstrip())
                d['sociales'] = int(datos[7].lstrip().rstrip())
                self.database.append(d)

    
    def get_aprobado_curso(self):
        aprobado_mate = 0
        aprobado_algo = 0
        aprobado_soci = 0

        for data in self.database:
            if(data['matematicas'] >= 61):
                aprobado_mate+=1
            if(data['algoritmos'] >= 61):
                aprobado_algo+=1
            if(data['sociales'] >= 61):
                aprobado_soci+=1

        print('# Matemática: {:>4}/{}'.format(aprobado_mate,len(self.database)))
        print('# Algoritmos: {:>4}/{}'.format(aprobado_algo,len(self.database)))
        print('# Sociales:   {:>4}/{}'.format(aprobado_soci,len(self.database)))

        data = [aprobado_mate,aprobado_algo,aprobado_soci]
        plt.bar(['Matematica','Algoritmo','Sociales'], height=data)
        plt.show()



    def get_prom_curso(self):
        sum_mate = 0
        sum_algo = 0
        sum_soci = 0
        
        for data in self.database:
            sum_mate += data['matematicas']
            sum_algo += data['algoritmos']
            sum_soci += data['sociales']

        data_len = len(self.database)
        prom_mate = sum_mate/data_len
        prom_algo = sum_algo/data_len
        prom_soci = sum_soci/data_len

        print('# Matemática: {:>7}'.format(prom_mate))
        print('# Algoritmos: {:>7}'.format(prom_algo))
        print('# Sociales:   {:>7}'.format(prom_soci))

        data = [prom_mate,prom_algo,prom_soci]
        plt.bar(['Matematica','Algoritmo','Sociales'], height=data)
        plt.show()

    
    def get_aprobado(self):
        aprobado = 0

        for data in self.database:
            if(data['matematicas'] >= 61 and data['algoritmos'] >= 61 and data['sociales'] >= 61):
                aprobado += 1

        print('# Aprobados: {:>4}/{}'.format(aprobado,len(self.database)))
        data = [aprobado,len(self.database)-aprobado]
        plt.pie(data,labels=['aprobados','otros'])
        plt.show()

    
    def get_no_aprobado(self):
        no_aprobado = 0

        for data in self.database:
            if(data['matematicas'] < 61 and data['algoritmos'] < 61 and data['sociales'] < 61):
                no_aprobado += 1

        print('# Reprobados: {:>4}/{}'.format(no_aprobado,len(self.database)))

        data = [no_aprobado,len(self.database)-no_aprobado]
        plt.pie(data,labels=['reprobados','otros'])
        plt.show()


    def set_prom(self):
        for data in self.database:
            prom = ( data['matematicas'] + data['algoritmos'] + data['sociales'] ) / 3
            data['promedio'] = prom
        self.save_data()

        print('# Promedio guardado por estudiante en "registroUVW.csv"')


    def save_data(self):
        with open('registroUVW.csv', 'w', encoding='utf-8') as archivo: # guarda los datos y cuando salga del bloque se cierra automaticamente
            archivo.write(',carnet,sexo,etnicidad,nivelEducPadres,matematicas,algoritmos,sociales,promedio\n')
            for d in self.database:
                archivo.write('{},{},{},{},{},{},{},{},{}\n'.format(
                    d['id'],
                    d['carnet'],
                    d['sexo'],
                    d['etnicidad'],
                    d['nivelEducPadres'],
                    d['matematicas'],
                    d['algoritmos'],
                    d['sociales'],
                    d['promedio']
                ))

