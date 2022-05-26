#Aşağıdakı ədədlər arasında rəqəmlərinin cəmi ən yüksək olanı çıxarın.
# 85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400

numbers=[85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]
def reqemlerin_toplami(numbers):
    result={}
    for number in numbers:
        sum=0
        for reqem in str(number):
            sum+=int(reqem)
        result.setdefault(sum,str(number)) 
    # alinan result dictionary:
    # print(result)
    # son netice   
    return get_max(result)

def get_max(result):
    max_value=max(result.keys())
    return result.get(max_value)

print(f'Rəqəmlərinin cəmi ən yüksək olan ədəd: {reqemlerin_toplami(numbers)}-dir')



#2: Aşağıdakı mətndən istifadə edərək sait ilə başlayıb, sait ilə bitən sözlərdən ibarət set yaradın:
text='Python dili - interpretasiya olunan, yüksək səviyyəli və ümumi-məqsədli proqramlaşdırma dilidir. 1991-ci ildə Guido van Rossum tərəfindən yaradılmışdır. Python dilinin dizayn fəlsəfəsi boşluqlardan istifadə edərək kod oxunaqlılığını vurğulayır. Bu dilin məqsədi onun dil quruluşu və obyekt-yönümlülüyü ilə proqramçılara xırda və iri həcimli layihələrdə aydın, məntiqli kod yazmağa kömək etməkdir.Python dinamik yazıla bilən və avtomatik yaddaş idarəetmə xüsusiyyətinə malikdir. Müxtəlif proqramlaşdırma paradiqmalarını dəstəkləyir, buna daxildir strukturlu (qismən, prosedurlu), obyekt-yönümlü və funksional proqramlaşdırma paradiqmaları. Onun geniş standart kitabxanası olduğuna görə Pythona "bataryaları daxildir" də deyilir.Python 1980-ci illərin sonlarında ABC dilinin davamçısı olaraq yaradıldı. Python 2.0 2000-ci ildə təqdim edildi, o özü ilə birlikdə siyahı anlama və zibil toplayıcı sistemlə birgə referans sayıcı xüsusiyyətlərini gətirdi.Python 3.0 2008-ci ildə təqdim edildi, o dilin böyük reviziyası olduğundan onun əvvələ-uyğunluğu tam deyil və bir çox Python 2 kodu dəyişikliyə ehtiyac olmadan Python 3-də işləyə bilmir.Python 2 dili 2020-ci ildə rəsmi olaraq dayandırıldı (ilk dəfə 2015-ildə dayandırılması planlaşdırılmışdı) və Python 2.7.18 son Python 2.7 buraxılışı oldu və beləliklə son Python 2.7 buraxılışı da o oldu. Bunun üçün daha heç bir təhlükəsizlik yamağı yada başqa təkmilləşdirmə buraxılmayacaq. Python 2-lər üçün hər şey dayandırılıb, yalnız Python 3.6.x və daha sonrası dəstəklənir.Bir çox əməliyyat sistemləri üçün Python interpretatorları mövcuddur. Bir qlobal proqramçılar cəmiyyəti azad və açıq-qaynaq kodlu istinad proqram olan CPythonu yazıb və inkişaf etdirir. Python və CPython-un inkişafı üçün qaynaqlari gəlir məqsədi güdməyən qurum olan Python Software Foundation idarə edir və yönləndirir.'
print(set(filter(lambda word: word[0] in ['a','ı','o','u','e','ə','i','ö','ü'] and word[len(word)-1] in ['a','ı','o','u','e','ə','i','ö','ü'] ,list(filter(lambda x: x.isalpha(),text.split(' '))))))


#3: Şaxta baba uşaqlara hədiyyələr paylayır, ancaq bu təsadüfi şəkildə olduğu üçün bəzi ədalətsizliklər yaranır və uşaqlar şikayət üçün list hazırlamaq istəyirlər. Bu listi hazırlamaq üçün sizə müraciət edib, bahadan ucuza kimə hansı hədiyyəni və hansı qiymətə olduğunu yazmağınızı istəyiblər. Hədiyyələr və uşaqların adlarının indeksləri eynidir. Datalardan istifadə edərək məlumatı hazırlayın.
# Outputdan bir hissə:
# ...
# Babək 1100 manat dəyərində Iphone götürüb
# ...

children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Sock': 10, 'Play Station': 1200}

print('\n'.join('{} {} manat deyerinde {} goturub'.format(*info) for info in list(zip(children,prices.values(),gifts))))

#4: Aşağıdakı dataları tiplərinə görə sıralamaq lazımdır. Sıra bu şəkildə olacaq: Listlər, Setlər, Dictonarylər, Booleanlar, İntegerlər, Floatlar, Stringlər.
datas = [{1, 2}, {'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True, {5, 6}, False]
types=[list, set, dict, bool, int, float, str]

for type in types:
    datas.sort(key=lambda data: isinstance(data,type))
   
print(datas)

