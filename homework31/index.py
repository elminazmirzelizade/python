#Bioloji araşdırmalar institutuna araşdırmaçı proqramist olaraq işə alınmısınız və sizə aşağıakı kimi bir data verilib. Həmin datalara əsasən qeyd edilən tapşırıqları yerinə yetirin
baliqlar = {
    'qeleseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}
cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}
amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
    'yumurtlama', 'dis yoxdur'
}
surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}
quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}
memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}
sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}
#1: Quşların xüsusiyyətlərinə "2 ayaq" əlavə edin.
quslar.add("2 ayaq")
print(quslar)
#2: Balıqların xüsusiyyətlərindən "4 ayaq" məlumatını çıxarın
baliqlar.remove("4 ayaq")
print(baliqlar)
#3: Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
print(amfibialar.intersection(cuculer))
#4: Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
print(baliqlar.symmetric_difference(amfibialar))
#5: Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
print(''.join(f'cavab {sinif} sinfidir' for sinif,xususiyyetler in sinifler.items()  if xususiyyetler.isdisjoint(baliqlar)))  
#6: Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
netice={}
for sinif,xususiyyetler in sinifler.items():
    if sinif!='quslar':
        netice[sinif]=len(quslar.intersection(xususiyyetler))
print(max(netice))
#7: İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın hansı sinifə aid ola biləcəyini təxmin edən kod yazın. Örnək
# input: dis yoxdur, agciyer teneffusu, korteks vardir
# output: Bu heyvan quslar alemine aid ola biler
user_input=set(input('xususiyyetleri daxil edin:').split(', '))
for sinif,xususiyyetler in sinifler.items():
    if  user_input.issubset(xususiyyetler):
        print(f'Bu heyvan {sinif} alemine aid ola biler')


