#1: 1000-dən 0001-ə qədər sağında nöqtə ilə düzülmüş bir text faylı hazırlayın. Örnək:
# ...
# 0056
# 0057
# ...

with open('text.txt', 'w') as file1:
    file1.writelines([str(i).zfill(4)+'.\n' for i in range(1000,0,-1)])

#2: HTML, CSS, JS fayllarını minify (tək sətr) edən program hazırlayın. Örnək:
# input ⇒ Minify etmek istediyiniz faylin adresini girin: C:\Users\Profile\Desktop\Project\app.js
# output ⇒ Fayl uğurla minify edildi!    


file_path=input('Minify etmek istediyiniz faylin adresini girin\n>>>')
with open('file_path', mode='w') as file2:
    file2.write(str(file2).replace('\n',''))

#3: Bu fayldaki sətrləri maaşa görə çoxdan aza sıralanmış hala salın
# Fuad Backend 3800 120
# Elminaz FrontEnd 2500 60
# Vasif FullStack 5000 100
# Asif DevOps 3500 200  


with open('ders.txt','r') as file3:
    persons = file3.readlines()
    persons.sort(key = lambda i: i.split()[2], reverse=True)
    print(persons)