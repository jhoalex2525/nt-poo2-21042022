# Importando la clase
from Clases.Personaje import Personaje

# Creo el objeto, a la variable personaje la igualo a la clase y le doy el constructor en ()
personaje=Personaje()

# Accedo al atributo nombre del objeto
# Viene el concepto de integridad de datos, por ejemplo la edad podría ponerse
# cualquier valor y la clase lo pasará como correcto. Debe modificarse el acceso.
# Vammos a la clase Personaje.py en comentario 123
print(personaje.nombre)
print(personaje.edad)

# Utilizo el setter
personaje.nombre="Pedro"
personaje.edad=-40
