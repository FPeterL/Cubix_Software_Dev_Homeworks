def calc(súly,magasság):

    if isinstance(magasság, int) :
        magasság = magasság / 100

    bmi = súly / magasság ** 2
    return bmi