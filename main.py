from lib import *
alum1= alumnograduado(601049     ,"ACOSTA  ZAIRA" ,    35 )
alum1.setCalif(10)
alum1.setCalif(9) 
alum1.setCalif(8)
alum1.setCalif (7)
alum1.setCalif (9)
alum1.set_graduado("si","01/07/2013",	"Los neutrinos saben a jugo de Uva")
#print (alum1)


alum2 = alumnograduado( 601048, "Frainé Durán", 34)
alum2.setCalif(6)
alum2.setCalif(5)
alum2.setCalif(5)
alum2.setCalif(4)
alum2.setCalif(3)
alum2.set_graduado
#print(alum2)

alum3 = alumnograduado( 100738, "Víctor García", 20)
alum3.setCalif(8)
alum3.setCalif(3)
alum3.setCalif(4)
alum3.setCalif(5)
alum3.setCalif(4)
alum3.set_graduado
#print(alum3)




alum4 = alumnograduado( 100744, "Diego López", 18)
alum4.setCalif(10)
alum4.setCalif(9)
alum4.setCalif(8)
alum4.setCalif(10)
alum4.setCalif(8)
alum4.set_graduado("Si","01/05/2026","Por que los polleros cortan 2 veces al aire y una al pollo")

#print(alum4)


alum5 = alumnograduado( 100692, "Evelyn López", 19)
alum5.setCalif(10)
alum5.setCalif(8)
alum5.setCalif(9)
alum5.setCalif(5)
alum5.setCalif(9)
alum5.set_graduado("Si","01/05/2027"	,"El hot dog ¿mas cerca del sandwich o del taco?")
#print(alum5)



alum6 = alumnograduado( 99999 , "Daniel Rojas",20)
alum6.setCalif(6)
alum6.setCalif(5)
alum6.setCalif(4)
alum6.setCalif(4)
alum6.setCalif(3)
alum6.set_graduado



alum7 = alumnograduado(100870, "Mauricio Rosas", 20)
alum7.setCalif(10)
alum7.setCalif(6)
alum7.setCalif(10)
alum7.setCalif(9)
alum7.setCalif(8)

alum7.set_graduado("Si",	"01/08/2026", "La telenovela Mirada de mujer como fenomeno social ")
#print(alum7)


alum8 = alumnograduado( 100437, "Annibal Villegas",20)
alum8.setCalif(10)
alum8.setCalif(5)
alum8.setCalif(7)
alum8.setCalif(8)
alum8.setCalif(9)
alum8.set_graduado("si","	01/12/2026"	," Como influyen los corridos tumbados en la sociedad" )
#print(alum8)

print("")
print("\033[46m Calificaciones de los estudiantes de actuaria UTECA  \033[0m")
print("")
print("                                  |  Calificaciones  |")
print("Mat | Nombre        |Edad| 1  | 2 | 3  | 4  | 5 |Final|Grad?| Fecha      | Tesis")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum1)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum2)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum3)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum4)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum5)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum6)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum7)
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(alum8)


print("")
print("\033[46m Datos de los estudiantes de actuaria UTECA\033[0m")


print("Matricula:" + str (alum1.matricula)+" " "Nombre Completo:"+ str (alum1.nombre)+ " " "Edad:"+str (alum1.edad)+" ""Graduado el:"+str (alum1.fecha)+" " "Con la Tesis:"+str(alum1.tesis))

print("Matricula:" + str (alum2.matricula)+" " "Nombre Completo:"+ str (alum2.nombre)+ " " "Edad:"+str (alum2.edad)+" ""NO graduado")

print("Matricula:" + str (alum3.matricula)+" " "Nombre Completo:"+ str (alum3.nombre)+ " " "Edad:"+str (alum3.edad)+" ""No Graduado ")

print("Matricula:" + str (alum4.matricula)+" " "Nombre Completo:"+ str (alum4.nombre)+ " " "Edad:"+str (alum4.edad)+" ""Graduado el:"+str (alum4.fecha)+" " "Con la Tesis:"+str(alum4.tesis))

print("Matricula:" + str (alum5.matricula)+" " "Nombre Completo:"+ str (alum5.nombre)+ " " "Edad:"+str (alum5.edad)+" ""Graduado el:"+str (alum5.fecha)+" " "Con la Tesis:"+str(alum5.tesis))


print("Matricula:" + str (alum6.matricula)+" " "Nombre Completo:"+ str (alum6.nombre)+ " " "Edad:"+str (alum6.edad)+" ""NO graduado")

print("Matricula:" + str (alum7.matricula)+" " "Nombre Completo:"+ str (alum7.nombre)+ " " "Edad:"+str (alum7.edad)+" ""Graduado el:"+str (alum7.fecha)+" " "Con la Tesis:"+str(alum7.tesis))

print("Matricula:" + str (alum8.matricula)+" " "Nombre Completo:"+ str (alum8.nombre)+ " " "Edad:"+str (alum8.edad)+" ""Graduado el:"+str (alum8.fecha)+" " "Con la Tesis:"+str(alum8.tesis))


 


