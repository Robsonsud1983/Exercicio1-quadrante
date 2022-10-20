import funcaoQuadrante

def testar():

    x = -6
    y = 20

    quadranteResultado1 = funcaoQuadrante.quadrante(x, y)

    assert quadranteResultado1 == "Quinto Quadrante"

    x = -5
    y =  -9

    quadranteResultado2 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado2 == "Sexto Quadrante"

    x = 5
    y =  -9

    quadranteResultado7 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado3 == "Setimo Quadrante"

    
    x = 5
    y = 9

    quadranteResultado8 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado4 == "Oitavo Quadrante"

    
    x = 0
    y =  -9

    quadranteResultado5 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado8 == "Oitavo Quadrante"