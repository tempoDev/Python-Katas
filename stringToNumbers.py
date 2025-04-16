def parse_int(string):
    
    unidades = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, 'twenty': 20, 'thirty': 30, 
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90 }
    multiplicadores = { 'hundred': 100, 'thousand': 1000, 'million': 1000000}
    
    palabras = string.replace("-", " ").replace(" and", "").split()
    total, actual = 0, 0

    for palabra in palabras: 
        if palabra in unidades:
            actual += unidades[palabra]
        elif palabra == 'hundred':
            actual *= 100
        elif palabra in ['thousand', 'million']: 
            total += actual * multiplicadores[palabra]
            actual = 0

    return total + actual

print(parse_int("two hundred forty-six"))