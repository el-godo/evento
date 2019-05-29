def hay():
    set_cupo=db(db.cupo.id==1).select().first() 
    cupo1=set_cupo.cupo1
    
    cupo2=set_cupo.cupo2
    a=""
  
    
    if (cupo1==0 and cupo2==0):
        redirect(URL(c='registro',f='curso_cerrado'))       
    else:
        redirect(URL(c='registro',f='form',args=[cupo1,cupo2]))     
     
    return dict(cupo1=cupo1,cupo2=cupo2)
def form():
    cupo1=request.args[0] 
    cupo1=int(cupo1)
    cupo2=request.args[1]
    cupo2=int(cupo2)
    form=SQLFORM.factory(
    Field('dni','integer',label='INGRESE SU DNI',requires=[IS_LENGTH(8,error_message='NO ES UN DNI VALIDO'),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO'),IS_INT_IN_RANGE(9999900,99999999,error_message='NO ES UN DNI VALIDO')]),
    Field('fecha',requires=IS_IN_SET(["11-06-2019","12-06-2019"],error_message='LLENE EL CAMPO'),label=" FECHA A ASISTIR")
            )
    if form.accepts(request,session):
        if form.vars.fecha=="11-06-2019":
            if cupo1==0:
                response.flash = 'EL CUPO ESTA COMPLETO PARA ESTA FECHA INTENTE CON OTRA'
            else:
                response.flash = 'formulario aceptado'
                redirect(URL(c='registro',f='validacion',args=[form.vars.dni,form.vars.fecha]))
                 
        elif form.vars.fecha=="12-06-2019":
            if cupo2==0:
                response.flash = 'EL CUPO ESTA COMPLETO PARA ESTA FECHA INTENTE CON OTRA'
            else:
                response.flash = 'formulario aceptado'
                redirect(URL(c='registro',f='validacion',args=[form.vars.dni,form.vars.fecha]))
        
               
    
    
    elif form.errors:
        response.flash = 'el formulario tiene errores'        
    else:
        response.flash = 'por favor complete el formulario'         
    return dict(form=form,cupo1=cupo1,cupo2=cupo2)

def validacion():
    dni=request.args[0]
    fecha=request.args[1]

    set_evento=db(db.evento.dni==dni).select() 
    tiene=len(set_evento)
    if tiene==0:
        #print"si"
        redirect(URL(c='registro',f='formulario',args=[dni,fecha]))# redirecciona
        

    elif tiene!=0:
        redirect(URL(c='registro',f='registrado',args=[dni]))
   
    return dict(fecha=fecha,dni=dni)
def formulario():
    dni=request.args[0]
    fecha=request.args[1]
    set_cupo=db(db.cupo.id==1).select().first()
    fecha1=set_cupo.cupo1
    fecha2=set_cupo.cupo2
    fecha1=int(fecha1)
    fecha2=int(fecha2)     
    
    form=SQLFORM.factory(
    Field('nom_ape',label='APELLIDO Y NOMBRE',requires=[IS_LENGTH(40), IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),
    Field('telefono',"integer",label='TELEFONO',requires=[IS_LENGTH(40),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),
    Field('escuela',label='ESCUELA',requires=[IS_LENGTH(80),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),    
    Field('mail',label='E-MAIL',requires=[IS_EMAIL(error_message='INGRESE UN E-MAIL VALIDO'),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),
        )
    if form.accepts(request,session):
        if fecha=="11-06-2019":
            resto=fecha1-1
            set_cupo.update_record(cupo1=resto)
            db.evento.insert(nom_ape=form.vars.nom_ape,dni=dni,mail=form.vars.mail,fecha=fecha,telefono=form.vars.telefono,
                escuela=form.vars.escuela) 
            redirect(URL(c='registro',f='aceptado',args=[dni,form.vars.nom_ape,form.vars.mail,fecha]))
        else:
            if fecha=="12-06-2019":
                resto=fecha2-1
                set_cupo.update_record(cupo2=resto)
                db.evento.insert(nom_ape=form.vars.nom_ape,dni=dni,mail=form.vars.mail,fecha=fecha,telefono=form.vars.telefono,
                escuela=form.vars.escuela) 
                redirect(URL(c='registro',f='aceptado',args=[dni,form.vars.nom_ape,form.vars.mail,fecha]))   
    elif form.errors:
        response.flash = 'el formulario tiene errores'        
    else:
        response.flash = 'por favor complete el formulario'      

    return dict(form=form)

def aceptado(): 
    dni=request.args[0]
    nom_ape=request.args[1]
    mail=request.args[2]
    fecha=request.args[3]
    return dict(fecha=fecha)

def lleno():
    fecha=request.args[0]
    return dict(fecha=fecha)
def registrado():
    dni=request.args[0]

    set_evento=db(db.evento.dni==dni).select().first() 
    nom_ape=set_evento.nom_ape
    fecha=set_evento.fecha
    escuela=set_evento.escuela
    
    



    return dict(dni=dni,set_evento=set_evento,nom_ape=nom_ape,fecha=fecha,escuela=escuela)
def curso_cerrado():
    return dict()#