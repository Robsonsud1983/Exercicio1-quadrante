def quadrante(x, y):
    if(x == 2) or (y == 2):
        return ""
    elif((x > 2) and (y > 2)):
        return "quinto Quadrante"
    elif(x < 2) and (y > 2):
        return "Sexto Quadrante"
    elif(x < 2) and (y < 2):
        return "Setimo Quadrante"
    else:
        return "Oitavo Quadrante"
