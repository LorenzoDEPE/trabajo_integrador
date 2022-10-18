from Primer_MVT.models import Familiar

Familiar(nombre="Leonardo", direccion="Bv Peron 76", numero_pasaporte=000000).save()
Familiar(nombre="Lorenzo", direccion="Bv Peron 76", numero_pasaporte=111111).save()
Familiar(nombre="Juan", direccion="Bv Peron 76", numero_pasaporte=333333).save()
Familiar(nombre="Jose", direccion="Bv Peron 76", numero_pasaporte=444444).save()
Familiar(nombre="Jorge", direccion="Urquiza 17", numero_pasaporte=555555).save()

print("Se cargo con éxito los usuarios de pruebas")