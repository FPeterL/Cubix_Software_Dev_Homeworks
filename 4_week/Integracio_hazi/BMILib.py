def calc(weight,height):

    if isinstance(height, int) :
        height = height / 100

    bmi = weight / height ** 2
    return bmi