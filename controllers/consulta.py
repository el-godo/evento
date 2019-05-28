def form():

	return dict()
def consulta():
	Fields=db.evento.nom_ape,db.evento.dni,db.evento.escuela
	set_evento=db(db.evento)
	grid=SQLFORM.grid(set_evento,fields=Fields,csv=False,paginate=20,deletable=False,editable=False,searchable=True,search_widget='default',create=False,)
	

	return dict(grid=grid)
