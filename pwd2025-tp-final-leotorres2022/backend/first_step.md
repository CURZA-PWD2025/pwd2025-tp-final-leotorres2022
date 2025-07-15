# Migrando y poblando nuestra base de datos

Es una buena práctica tener un archivo para configurar nuestra base de datos al inicializar un proyecto que trabaja con ella.
Para lo cual vamos a trabajar con dos conceptos nuevos: ``MIGRACION`` e ``SEEDING``
 
 ### QUE SON LAS MIGRACIONES:
 Son scripts que definen cambios en la estructura de la base de datos (crear, modificar o eliminar tablas y columnas) usando código, 
 en lugar de hacerlo manualmente con SQL.

#### Sintéticamente:
Son instrucciones versionadas para construir y modificar la base de datos de forma controlada y reproducible.

🔧 Se usan para:

- Crear tablas y relaciones.
- Agregar o quitar columnas.
- Sincronizar el esquema de la base de datos con el código del proyecto.
- Mantener historial de cambios.

### SEEDING
Seeding (en español, sembrar) en desarrollo de software y bases de datos es el proceso de poblar una base de datos con datos iniciales o de prueba automáticamente.

Seeding es insertar datos de ejemplo o básicos en la base de datos para tener un entorno listo para desarrollo, pruebas o demostraciones.

🔹 Usos comunes:
- Poner usuarios, productos, configuraciones por defecto.
- Facilitar pruebas sin ingresar datos manualmente.
- Ayudar a mantener consistencia entre entornos.

### Como migrar y sembrar o poblar nuestra base?

En la raiz del proyecto encontraran dos archivos ``db_init.py`` y ``db_rollback.py`` los mismos van a serles utiles para migrar e sembrar y eliminar todo respectivamente, el archivo ``db_init`` tiene la logica para crear tambien la base de datos sino la tiene creada, los datos los va a tomar del archivo ``.env`` (variables de entorno de la aplicacion), recuerden usar el ``.env-dev``  renombrarlo y agregar sus propios datos.

```bash
python db_init.py
```
Les va a crear toda la estructura de la base asi como los datos para podrar nuestra aplicacion correctamente

```bash
python db_rollback.py
```
Dropea (elimina) todas las tablas con los datos pero no la base de datos, luego pueden volver a ejecutar el migrador sin problemas


