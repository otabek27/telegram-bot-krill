


from transliterate import to_latin, to_cyrillic




# print(to_cyrillic('salom bolajonlar'))
# print(to_latin('салом болажонлар'))


matn = input('lotincha matn kiriting: ')

# print(to_cyrillic(matn))


if matn.isascii():
    print(to_cyrillic(matn))

else:
    print(to_latin(matn))