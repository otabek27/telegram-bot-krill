


from transliterate import to_latin, to_cyrillic




# print(to_cyrillic('salom bolajonlar'))
# print(to_latin('салом болажонлар'))



# print(to_cyrillic(matn))

while True:
    matn = input('lotincha matn kiriting: ')
    matn_1 = input("davom etasizmi (ha,yoq): ")

    if matn_1 == "yoq":
       print(to_cyrillic(matn))
       break 

    elif matn.isascii():
        print(to_cyrillic(matn))

    else:
        print(to_latin(matn))