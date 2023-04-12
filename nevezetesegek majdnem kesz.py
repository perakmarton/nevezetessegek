nevezetessegek = ["Hollókő","Őrség","A villányi borvidék"," Esztergom"," Sopron","Tihany és a Tihanyi-félsziget","Pécs"]
for i in range(0, len(nevezetessegek)):
    print(i+1," ",nevezetessegek[i])
valasztas= int (input("Melyiket válsztod? Add meg a számjelét!"))
valasztott_index=valasztas

if valasztott_index== 1:
    print("Hollókő Magyarország egyetlen faluja, amely az UNESCO világörökségi listán szerepel, és így világszerte ismert.A Világörökség Bizottság 1987-ben")


if valasztott_index== 2:
    print("Hazánk egyik legérintetlenebb régióját, az ország legnyugatibb csücskében található Őrséget fedezzük fel autós túránk során. A kiterjedt erdőségekkel borított, szelíden hullámzó, lankás, dimbes-dombos táj igazi vidéki nyugalmat áraszt. A természetet, autentikus pannon hangulatú, bájos kis falvakat kedvelő turisták körében egyre népszerűbbé váló, három határon át nyúló Őrvidék kicsi, de annál érdekesebb látnivalók sokaságával várja az ide látogatókat.")


if valasztott_index== 3:
    print("A Villányi borvidék (korábban Villány–Siklósi borvidék) úttörő szerepet játszott a magyar borászat újjászületésében. Magyarország egyik legfejlettebb bortermő vidéke ez. Sikerét egyesek a nagyüzemi termelés alatt összeszokott kiváló szakembereknek, mások az idetelepült svábok kitartásának tulajdonítják.")
    
if valasztott_index== 4:
    print("Esztergom (németül: Gran, szlovákul: Ostrihom, törökül: Estergon) fejlett iparú, iskola- és kikötőváros Komárom-Esztergom vármegyében, a Duna jobb partján, megyei jogú város. A mai értelemben vett város 1895-ben Esztergom szabad királyi város és a szomszédos Érseki Víziváros, Szenttamás illetve Szentgyörgymező települések egyesítésével jött létre. A rendszerváltástól 2012-ig az Alkotmánybíróság, 1997-től a Duna–Ipoly Nemzeti Park székhelye. Az esztergomi érsek székvárosaként a római katolikus egyház magyarországi központja.")


if valasztott_index== 4:
    print("Sopron az ország egyik legromantikusabb városa a kanyargós, macskaköves utcákkal, a mesélő kapualjakkal és a színes házakkal együtt, de ezer arcát mutatja a kultúra terén is! A leghűségesebb város és a Fertő-táj ezernyi lehetőséget kínál, akár a természet felfedezése, akár kulturális érdeklődés, akár aktív kikapcsolódás az utazás célja.")


if valasztott_index== 5:
    print("Tihany község a Balaton-felvidéken, Veszprém vármegyében, a Balatonfüredi járásban. Magyarország egyik legszebb fekvésű települése, látványos táji és természeti adottságokban bővelkedő község a Balatonba nyúló Tihanyi-félszigeten. A község központjában áll a Tihanyi Bencés Apátság, amelyet 1055 -ben alapított I. András magyar király, aki az apátság kriptájában lett eltemetve. Az apátság alapító okirata a magyar nyelv első fennmaradt szórványemléke, amelyet a Pannonhalmi Bencés Főapátságban őriznek. Maga a templom 1754-ben épült át barokk stílusban. A ma is működő apátság történelmi és művészeti jelentősége miatt kedvelt turisztikai látványosság. Innen nyílik a legjobb kilátás a Balatonra.")


if valasztott_index== 6:
    print("")
