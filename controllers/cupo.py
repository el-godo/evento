@auth.requires_membership('Administrador')
def cupo():
	
	set_cupo=db(db.cupo).select().first()
	
	fecha1=set_cupo.cupo1
	fecha2=set_cupo.cupo2
	
	form=SQLFORM.factory(
		Field('cupo1','integer',label='DEFINIR EL CUPO'),
		Field('cupo2','integer',label='DEFINIR EL CUPO'),
			)
	if form.accepts(request,session):
				

				set_cupo.update_record(cupo1=form.vars.cupo1)
				set_cupo.update_record(cupo2=form.vars.cupo2)
				redirect(URL(c='cupo',f='aceptado',args=[form.vars.cupo1,form.vars.cupo2]))

    				response.flash = 'formulario aceptado'
	elif form.errors:
        		response.flash = 'el formulario tiene errores'
    	else:
        		response.flash = 'por favor complete el formulario' 

	return dict(form=form,fecha1=fecha1,fecha2=fecha2)
def aceptado():
	cupo1=request.args[0]
	cupo2=request.args[1]
	return dict(cupo1=cupo1,cupo2=cupo2)

