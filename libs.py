def getnamefilter(completename):
    completename.lower()
    for letter in completename:
        if letter==' ':
            completename = completename.replace(letter, '-')
        if letter=='ñ':
            completename = completename.replace(letter, 'n')
        if letter=='á':
             completename = completename.replace(letter, 'a')
        if letter=='é':
             completename = completename.replace(letter, 'e')
        if letter=='í':
             completename = completename.replace(letter, 'i')
        if letter=='ó':
             completename = completename.replace(letter, 'o')
        if letter=='ú':
             completename = completename.replace(letter, 'u')
        if letter=='ü':
             completename = completename.replace(letter, 'u')
    return completename

name = "Pedro Sánchez Castejón"
print(getnamefiltered(name))
