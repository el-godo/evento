@auth.requires_login()
def imprimir():

	return dict()
def print_fecha1():
	
	import json
	

    	ordenar=db(db.evento.nom_ape).select()
	set_evento=db(db.evento.fecha=="11-06-2019").select(orderby=db.evento.nom_ape)
	evento=set_evento.first() 	

    	
    	
	return dict(set_evento=set_evento,evento=evento)

   	
    	
def print_fecha2():
	

    	ordenar=db(db.evento.nom_ape).select()
	set_evento=db(db.evento.fecha=="12-06-2019").select(orderby=db.evento.nom_ape)
	evento=set_evento.first() 


    	
    	
	return dict(set_evento=set_evento,evento=evento)
def todo():
	

    	ordenar=db(db.evento.nom_ape).select()
	set_evento=db(db.evento.fecha).select(orderby=db.evento.nom_ape)
	evento=set_evento.first() 
		

    	
    	
	return dict(set_evento=set_evento,evento=evento)

	