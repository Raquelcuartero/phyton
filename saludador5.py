del saludador():
    hora=input("Dime que hora es")
    if (hora>=6 and hora<14):
       print "Buenos dias"
    if (hora>=14 and hora<20):
       print "Buenas tardes"
    if ((hora>=20 and hora<=24)or(h>=0 and hora<6)):
       print "Buenas noches"
saludador()
