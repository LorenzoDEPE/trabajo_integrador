from Primer_MVT.models import Familiar,Categoria

Familiar(nombre="Leonardo", direccion="Bv Peron 76", numero_pasaporte=000000, fecha_nacimiento = "05/03/1990").save()
Familiar(nombre="Lorenzo", direccion="Bv Peron 76", numero_pasaporte=111111, fecha_nacimiento = "18/10/1995").save()
Familiar(nombre="Juan", direccion="Bv Peron 76", numero_pasaporte=333333, fecha_nacimiento = "15/03/1998").save()
Familiar(nombre="Jose", direccion="Bv Peron 76", numero_pasaporte=444444, fecha_nacimiento = "04/07/1987").save()
Familiar(nombre="Jorge", direccion="Urquiza 17", numero_pasaporte=555555, fecha_nacimiento = "21/11/1965").save()

Categoria(nombre="Noticias",descripcion= "esto es una descripcion").save()
Categoria(nombre="Noticias",descripcion= "esto es una descripcion").save()
Categoria(nombre="Noticias",descripcion= "esto es una descripcion").save()

print("Se cargo con éxito los usuarios de pruebas")