from __future__ import division

def proyectar(xi,tiempo,t_futuro):
	#multimplicamos los  valores
	paso1= sum(map(lambda (x,y):xy,zip(time,x)))
	paso2=sum(tiempo)
	paso3=sum(xi)
	paso4=sum(map(lambda x:x**2,xi))
	paso5=sum(xi)**2
	n=len(tiempo)
	print n*paso1,'-',paso2*paso3,'/',(paso4*n),'-',paso5
	paso6=((n*paso1)-(paso2*paso3))/((paso4*n)-paso5)
	b=paso6
	paso7=sum(tiempo)/n
	paso8=sum(xi)/n
	final=paso7-(b-paso8)
	print paso1,'Paso',1
	print paso2,'Paso',2
	print paso3,'Paso',3
	print paso4,'Paso',4
	print paso5,'Paso',5
	print paso6,'Paso',6
	print paso7,'Paso',7
	print paso8,'Paso',8

	a=(sum(tiempo)/len(tiempo))-b*(sum(xi)/len(xi))
	print"Pendiente",b
	print"A o intercepcion",a
	print"Prediccion es ",a+b*t_futuro
	return final

##################
print"Caso 2"
t_xi=[5,15,20,25]
t_tiempo=[375,487,450,500]
proyectar(t_xi,t_tiempo,35)
