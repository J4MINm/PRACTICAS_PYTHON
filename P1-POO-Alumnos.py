""" 
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´
""" 

# Author: EV3TH

class Alumno():
    
    # Atributos Objeto
    def __init__(self, Nombre, Apellido, Promedio):
        self.Nombre = Nombre;
        self.Apellido = Apellido;
        self.Promedio = Promedio;
    
    # Calular promedio (Si reprobo o no)
    def getPromedio(self):
        if (self.Promedio >= 70) or (self.Promedio <=100):
            print("Status: APROBADO");
        if (self.Promedio <=0 ) or (self.Promedio <= 69):
            print("Status: REPROBADO");

# Instanciamos (Creamos un objeto)
Cilvana = Alumno("Cilvana", "Mejia", 69);

# Print datos
print("##__ DATOS DEL ALUMNO __##", "\n");
print(f"Nombre: {Cilvana.Nombre}");
print(f"Apellido:  {Cilvana.Apellido}");
# print(f"Numero de control: {Cilvana.NoControl}");
# print(f"Edad: {Cilvana.Edad}");
Cilvana.getPromedio();
