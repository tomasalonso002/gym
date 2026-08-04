Sistema de Gestión para Gimnasios es una aplicación web desarrollada para facilitar la administración de un gimnasio. 
Permite gestionar usuarios, empleados, planes de entrenamiento, cuotas mensuales y pagos, además de asignar rutinas personalizadas según las necesidades de cada cliente. 
El sistema incorpora autenticación con distintos niveles de permisos, ofreciendo herramientas tanto para administradores como para empleados, con el objetivo de optimizar la organización del gimnasio y mejorar la experiencia de sus usuarios.
Roles usurio, empleado, jefe:
**Usuario**
El usuario ingresa con el username y password que le da el jefe.
Nav: 'Perfil' 'Rutinas' 'Noticias'
Perfil:
- Podes visualizar los datos personales del usuario activo.
- Podes ingresar a las cuotas, donde tenes un registro de todas las cuotas con su informacion, nombre del plan, monto, inicio y vencimiento y el estado de la 
cuota, te da la opcion de pagar por mediante transferencia mandando el comprobante y despues las autoridades de gym revisan el comprobante que le mandaste y si 
el comprobante es valido se acepta el pago y se crea la cuota nueva. Si las autoridades del gym rechazan el pago te aparece la opcion de reintentar pago.
- Podes cambiar la contraseña de la cuenta.
Rutinas:
-Puedo visualizar las rutinas que me crearon los profesores especialemente para mi. Se puede ver el nombre de la rutina y un boton de 'Ver Rutina' e ingresas a la rutina y podes ver la imagen cargada.
Noticias:
-Podes visualizar las noticias que cargan los jefes.(Aumentos de cuota, cerrado por feriado, etc)
**Empleados**
El usuario ingresa con el username y password que le da el jefe.
Nav: 'Perfil' 'Rutinas' 'Noticias' 'Usuarios' 'Buzon Consultas'
Perfil:
- Podes visualizar los datos personales del usuario activo.
- Podes cambiar la contraseña de la cuenta.
Rutinas:
-El empleado puede crear rutinas que solo la van a ver los empleados y el jefe. Las cuales se pueden editar y eliminar.
Noticias:
-Podes visualizar las noticias que cargan los jefes.(Aumentos de cuota, cerrado por feriado, etc)
Usuarios:
-Podes visualizar el listado de usuarios activos. Con informacion personal de los mismos. Username, nombre, apellido, dni email, telefono, foto y un boton para crear una rutina a esa usuario.
-Tenas una barra de busqueda donde podes buscar un usuario por nombre
Buzon Consultas:
-Podes visualizar todas las consultas que realizan todos los usuarios que no estan registrados. Con informacion para responderles y despues la podes eliminar.
**Jefe**
El usuario ingresa con el username y password que le crea el admin con el rol de jefe.
Nav: 'Perfil' 'Rutinas' 'Noticias' 'Usuarios' 'Buzon Consultas'
Perfil:
- Podes visualizar los datos personales del usuario activo.
- Podes cambiar la contraseña de la cuenta.
Rutinas:
-El empleado puede crear rutinas que solo la van a ver los empleados y el jefe. Las cuales se pueden editar y eliminar.
Noticias:
-Podes ver y crear noticias para que las vean los empleados y los usuarios
Usuarios:
-Podes visualizar el listado de usuarios activos. Con informacion personal de los mismos. Username, nombre, apellido, dni, email, telefono, foto y un boton para crear una rutina, dos botones de acciones(Editar datos personales y borrar usuario), y un boton de pagar cuota.
-Podes visualizar un boton para añadir un usuario.
-Podes visualizar un boton 'Pagos Pendientes', donde se ubican todos los comprobantes de pago que mandan los usuarios esperando ser aprovados o rechazados.
-Puedo visualizar un boton de 'Nuevo plan' donde puedo ver los planes activos y editarlos, tambien crear nuevos planes.
-Tenas una barra de busqueda donde podes buscar un usuario por nombre
Empleados:
-Podes visualizar el listado de empleados activos. Con informacion personal de los mismos. Username, nombre, apellido, dni, email, telefono, foto, boton de 'Carga horaria'*, dos botones de acciones(Editar datos personales y borrar usuario) y un boton de 'Valor Hora'**
'Carga Horaria'* Un boton donde te lleva al resumen de horas que el empleado lleva trabajando en el mes corriente y un pequeño form donde podes generar una carga de horas. Tambien se visualiza un historial de cargas, donde se ve la cantidad de horas, fecha, username del jefe , username del empleado.
'Valor hora'**: Un boton que te lleva a ver el valor de la hora actual del empleado. Se puede generar una nueva carga donde se actualiza el valor actual de la hora. Y se puede ver un historial de todas las cargas de los valores, donde se ve la el valor$, fecha, username jefe, username empleado.
-Podes visualizar un boton para añadir un empleado.
Buzon Consultas:
-Podes visualizar todas las consultas que realizan todos los usuarios que no estan registrados. Con informacion para responderles y despues la podes eliminar.
Analisis:
Es un resum general de los numeros del sistema.
-Podes visualizar la cantidad de usuarios activos. 



