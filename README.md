# Autor: Camilo Bonilla


# Entrega Final.
Este proyecto es desarrollado en Python utilizando el framework Django. Trata de una app web sobre la plataforma que toda universidad tiene acerca de sus programas, y que tutores o profesores tiene, ésta renderiza la informacion lmacenada en las bases de datos.
 

# Demostración.


# Documentación.

Para poder encontrar los archivos que nombrare a posterior ingresar  en la carpeta AppCoder.
Los archivos son: models.py, forms.py, urls.py, views.py,la carpeta de templates, entre otros.



# Models.py:
En este archivo podemos encontrar los modelos de datos usados por el backend.

Descripcion: modelo Estudiante. 
En éste se solicitan datos como nombre, edad, programa que estudia y fecha de inscripción en la institución.

Descripcion: modelo Tutor. 
En éste se solicitan datos como nombre y apellido, programa que dicta el tutor y número telefónico.

Descripcion: modelo Programa. 
En éste se solicitan datos como nombre del programa y código del mismo.




# Forms.py:
En este archivo podemos encontrar los formularios usados para cargar los datos que quedan guardados en nuestra base de datos.


# Urls.py:
Contiene cada una de las rutas de las vistas de la app. 

# Views.py:
Aparecen todas las vistas que se utilizan en la app.
Asociado a lo anterior por cada modelo se aplica el concepto de CRUD(Create, Read, Update, Delete); una vista de logueo, registro y edicion de perfil del usuario. Además tenemos la vista para buscar a cualquier estudiante por su nombre. Pro ejemplo:

Create: vista formularioEstudiante

Read: vista leerEstudiante

Update: vista editarEstudiante

Delete: vista eliminarEstudiante

_______________________________________________________________________________________________________________________________________________________________________
# Templates:
Es una carpeta donde se encuentran todos los archivos HTML,usados por la app. Se utilza una platilla de BOOSTRAP y se aplica el concep de herencia a cada archivo.

_______________________________________________________________________________________________________________________________________________________________________

