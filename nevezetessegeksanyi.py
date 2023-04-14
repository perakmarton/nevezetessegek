orszagok = {
    "Franciaország": ["Eiffel-torony","Párizs"],
    "Magyarország": ["Parlament","Budapest"],
    "Németország": ["Barndenburgi kapu","Berlin"],
    "Görögország": ["Akropolisz","Athén"],
    "Egyesült Királyság": ["Tower Bridge","London"],
    "Oroszország": ["Colosseum","Roma"],
    "Spanyolország": ["Szent Család-templom","Barcelona"],
   }

print("Kérlek, válassz az alábbi országok közül:")
for orszag in orszagok:
    print("- " + orszag)

valasztott_orszag = input("Add meg az ország nevét: ")

if valasztott_orszag in orszagok:
    nevezetesseg, varos = orszagok[valasztott_orszag]
    print(f" {valasztott_orszag}  nevezetessége a {nevezetesseg} és {varos} városában található.")
else:
    print("Nincs ilyen ország az adatbázisban.")
