def c2l(data):
    list = ''
    for i in data:
        str = i
        str = str.replace(" ","")
        c = "()"
        for a in c:
            str = str.replace(a,",")
        str = str.strip()
        str = str.upper()

        list += str + ','
        