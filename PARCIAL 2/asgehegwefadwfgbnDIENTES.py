def validar (diente):
    d=diente.split(",")
    print(d)
    for i in range (len(d)):
        if 11 <int(d[i]) and int(d[i])<18:
            return True
        elif 21 <int(d[i]) and int(d[i])<28:
            return True
        elif 31 <int(d[i]) and int(d[i])<38:
            return True
        elif 41 <int(d[i]) and int(d[i])<48:
            return True
        elif 51 <int(d[i]) and int(d[i])<55:
            return True
        elif 61 <int(d[i]) and int(d[i])<65:
            return True
        elif 71 <int(d[i]) and int(d[i])<75:
            return True
        elif 81 <int(d[i]) and int(d[i])<85:
            return True
        else:
            return False
      
print(validar("19,29,86"))
