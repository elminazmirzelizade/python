#1: b'\xff\xfef\x00e\x00r\x00m\x00a\x00' bu bytes datasını UTF-16 ilə decode edib, ekranda göstərin.

bytes=b'\xff\xfef\x00e\x00r\x00m\x00a\x00'
bytes=bytes.decode('UTF-16')
print(bytes)

#2: Rar içindəki png faylının binary kodları tərsinə çevirilərək gizlənmişdir. Bu faylı düzəldəcək kod yazın(hide-image.zip)
with open('hide-image.png', mode='rb+') as file:
    bytes=file.read()
    bytes= bytes.decode(encoding='utf-8', errors='ignore')
    bytes=bytes[::-1]
    print(bytes)

#3: Rar içərisində extensionları (uzantıları) gizlənmiş faylların biri jpg, biri mp4 və digəri də pptx-dir. Həmin faylların extensionlarını (uzantılarını) tapıb düzəldən bir program yazın.(unkown-files.zip)
# mp4-u tapmir

def is_jpg(content):
    return content.startswith(b'\xFF\xD8\xFF')
def is_mp4(content):
    return content.startswith(b'\x66\x74\x79\x70\x69\x73\x6F\x6D')
def is_pptx(content):
    return content.startswith(b'\x50\x4B\x03\x04')

f1=open('file1.unkown', mode='rb')
f2=open('file2.unkown', mode='rb')
f3=open('file3.unkown', mode='rb')

for file in [f1,f2,f3]:
    content=file.read()[:50]
    if is_jpg(content):
        print(file.name, 'is jpg')
    elif is_mp4(content):
        print(file.name, 'is mp4')
    elif is_pptx(content):
        print(file.name, 'is pptx')