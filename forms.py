from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import DateField, SelectField, StringField, RadioField
from wtforms.fields.simple import PasswordField, SubmitField,HiddenField, TextAreaField
from wtforms.fields.html5 import DecimalRangeField
from models import reservas,usuario_final,usuario_administrador

#Inicio formulario validación en Login#######################################################

class formlogin(FlaskForm):
    user = StringField('Usuario', validators=[validators.required(), validators.length(max=100)]) #Cómo se centra aquí?
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=100)])
    tipoUsuario = RadioField('Tipo de usuario', choices=[('UF','Usuario Final'),('A','Administrador'),('SA','Super Administrador')])
    enviar = SubmitField('Ingresar')

#Fin formulario validación en Login##########################################################
   

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS ##################################

#Usuario Final
# 0-1-3-4-modulo_reservas
class formreservas(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-3-4-1-crear_reservas
class formreservanueva(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    # Para consultar la base de datos de usuarios elegir id_usuario
    listado_usuarios = reservas.listado_choices_usuarios()
    largo = len(listado_usuarios)
    choices_usuarios = ["Por favor elija su ID de Usuario"]
    for item in range(largo):
        choices_usuarios.append(listado_usuarios[item]["id_usuario"])
    
    ######################################################################

    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    user = SelectField('ID Usuario', validators=[validators.required()], choices=choices_usuarios)
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')  

# 0-1-3-4-2-modificar_reservas

class formmodificarreserva(FlaskForm):
    
    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-3-4-3-cancelar_reservas
class formcancelarreserva(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva') 

# Usuario Administrador
# 0-1-2-3-4-consulta_reservas
class formreservasadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    lista = reservas.listado_choices_habitaciones()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-2-3-4-1-crear_reservas
class formreservanuevaadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

        ######################################################################

    # Para consultar la base de datos de usuarios elegir id_usuario
    listado_usuarios = reservas.listado_choices_usuarios()
    largo = len(listado_usuarios)
    choices_usuarios = ["Por favor elija su ID de Usuario"]
    for item in range(largo):
        choices_usuarios.append(listado_usuarios[item]["id_usuario"])
    
    ######################################################################

    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    user = SelectField('ID Usuario', validators=[validators.required()], choices=choices_usuarios)
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')

# 0-1-2-3-4-2-modificar_reservas 
class formmodificarreservaadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-2-3-4-3-cancelar_reservas
class formcancelarreservaadmin(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva')

# Usuario SuperAdministrador
# 0-1-1-4-4-consulta_reservas
class formreservassuperadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    lista = reservas.listado_choices_habitaciones()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-1-4-4-1-crear_reservas
class formreservanuevasuperadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    # Para consultar la base de datos de usuarios elegir id_usuario
    listado_usuarios = reservas.listado_choices_usuarios()
    largo = len(listado_usuarios)
    choices_usuarios = ["Por favor elija su ID de Usuario"]
    for item in range(largo):
        choices_usuarios.append(listado_usuarios[item]["id_usuario"])
    
    ######################################################################

    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    user = SelectField('ID Usuario', validators=[validators.required()], choices=choices_usuarios)
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')

# 0-1-1-4-4-2-modificar_reservas
class formmodificarreservasuperadmin(FlaskForm):

    # Para consultar la base de datos de Habitaciones elegir id_habitacion
    listado_habitaciones = reservas.listado_choices_habitaciones()
    largo = len(listado_habitaciones)
    choices_habitaciones = ["Por favor elija una Habitación"]
    for item in range(largo):
        choices_habitaciones.append(listado_habitaciones[item]["id_habitacion"])
    
    ######################################################################

    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=choices_habitaciones)
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-1-4-4-3-cancelar_reservas
class formcancelarreservasuperadmin(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva')

# HTML donde deben completarse los formularios para implementar el CRUD Reservas:

# USUARIO FINAL
# 0-1-3-4-modulo_reservas OK
# 0-1-3-4-1-crear_reservas OK
# 0-1-3-4-2-modificar_reservas OK
# 0-1-3-4-3-cancelar_reservas OK

# ADMINISTRADOR
# 0-1-2-3-4-consulta_reservas OK
# 0-1-2-3-4-1-crear_reservas OK
# 0-1-2-3-4-2-modificar_reservas OK
# 0-1-2-3-4-3-cancelar_reservas OK

# SUPER ADMINISTRADOR
# 0-1-1-4-4-consulta_reservas OK
# 0-1-1-4-4-1-crear_reservas OK
# 0-1-1-4-4-2-modificar_reservas OK
# 0-1-1-4-4-3-cancelar_reservas OK

# USUARIO INVITADO
# No tiene CRUD Reservas


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS #####################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES ##############################
class FormAgregarHabitacion(FlaskForm):
    codigo = StringField('Código') 
    enviar = SubmitField('Agregar') 

class FormModificarHabitacion(FlaskForm):
    id_habitacion = HiddenField('id_habitacion') 
    rol = HiddenField('rol') 
    codigo = StringField('Código') 
    disponible= RadioField('Disponible', choices=[('SI','SI'),('NO','NO')])
    enviar = SubmitField('Modificar') 

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS Y CALIFICACION #################

#0-2-2-consulta_habitaciones_disponibles
# No se necesita formulario es una consulta a la base de datos de habitaciones

#0-2-2-1-consulta_comentarios_habitacion
# No se necesita formulario es una consulta a la base de datos de reservas

# 0-1-3-2-consulta_habitaciones_disponibles_usuario_final
# No se necesita formulario es una consulta a la base de datos de habitaciones

# 0-1-3-2-1-consulta_comentarios_habitacion_usuario
# No se necesita formulario es una consulta a la base de datos de reservas

# 0-1-3-3-gestion_habitaciones_reservadas_usuario_final
# No se necesita formulario es una consulta a la base de datos de reservas

# 0-1-3-3-1-modificar_comentarios_habitacion

class FormModificarComentariosHabitacion(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    reservation = StringField('ID Reserva', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    modifycomment = SubmitField('Modificar Comentario') 

# 0-1-3-3-2-calificar_habitaciones

class FormCalificarHabitaciones(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    reservation = StringField('ID Reserva', validators=[validators.required()])
    calification = DecimalRangeField('Calificación Reserva', validators=[validators.required()])
    send = SubmitField('Calificar Reserva')
# 0-1-2-3-gestion_habitaciones 
# Se actualiza la vista y se retira el uso

# 0-1-2-3-3-consulta_comentarios_habitacion_usuario
# Se actualiza la vista y se retira el uso

# 0-1-1-4-gestion_habitaciones
# Se actualiza la vista y se retira el uso

# 0-1-1-4-3-consulta_comentarios_habitacion_usuario
# Se actualiza la vista y se retira el uso

# 0-1-1-5-restringir_comentarios
# Se retira la funcionalidad, no aporta al Enunciado

# HTML donde deben completarse los formularios para implementar el CRUD Comentarios y Calificación:
# Uusario invitado
#0-2-2-consulta_habitaciones_disponibles OK
#0-2-2-1-consulta_comentarios_habitacion OK

# Usuario final
# 0-1-3-2-consulta_habitaciones_disponibles_usuario_final OK
# 0-1-3-2-1-consulta_comentarios_habitacion_usuario OK
# 0-1-3-3-gestion_habitaciones_reservadas_usuario_final OK
# 0-1-3-3-1-modificar_comentarios_habitacion OK
# 0-1-3-3-2-calificar_habitaciones OK

# Administrador
# 0-1-2-3-gestion_habitaciones OK
# 0-1-2-3-3-consulta_comentarios_habitacion_usuario OK

# SuperAdministrador
# 0-1-1-4-gestion_habitaciones OK
# 0-1-1-4-3-consulta_comentarios_habitacion_usuario OK
# 0-1-1-5-restringir_comentarios OK



# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIO Y CALIFICACION ####################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS ##################################
# Formularios Gestion usuarios 
class FormAgregarUsuarioFinalCRUD(FlaskForm):
    nombre = StringField('Nombres Completos') 
    usuario = StringField('Usuario') 
    documento = StringField('Documento') 
    enviar = SubmitField('Agregar') 

class FormModificarUsuarioFinalCRUD(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    activo= RadioField('Activo', choices=[('SI','SI'),('NO','NO')])
    enviar = SubmitField('Modificar') 

class FormAgregarUsuarioAdmonCRUD(FlaskForm):
    nombre = StringField('Nombres Completos') 
    usuario = StringField('Usuario') 
    documento = StringField('Documento') 
    enviar = SubmitField('Agregar') 

class FormModificarUsuarioAdmonCRUD(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    activo= RadioField('Activo', choices=[('SI','SI'),('NO','NO')])
    enviar = SubmitField('Modificar') 

class FormModificarUsuarioRegistrado(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    usuario = StringField('Usuario') 
    contrasena1 = PasswordField('Contraseña 1')
    contrasena2 = PasswordField('Contraseña 2')
    enviar = SubmitField('Modificar')
    
class FormCrearUsuarioRegistrado(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    usuario = StringField('Usuario') 
    contrasena1 = PasswordField('Contraseña 1')
    contrasena2 = PasswordField('Contraseña 2')
    enviar = SubmitField('Crear')  
    
# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################
