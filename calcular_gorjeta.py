
'''
Autor: Alfredo Miranda Egranfonte
Data: 13/04/2016
Atualizado:
Programa: Tem como objetivo calcular imposto e gorjeta de um restaurante
'''
def taxa(valor):
    """Soma 8% de imposto a uma conta de restaurante."""
    valor *= 1.08
    print "Com imposto: %f" % valor
    return valor

def tipo(valor):
    """Soma uma gorjeta de 15% a uma conta de restaurante."""
    valor *= 1.15
    print "com gorjeta de: %f" % valor
    return valor
    
meal_cost = 100
meal_with_taxa = taxa(meal_cost)
meal_with_tipo = tipo(meal_with_taxa)
