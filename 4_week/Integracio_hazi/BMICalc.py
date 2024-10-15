import BMILib as bmi

height= input("Add meg a magasságod: ")
weight= input("Add meg a súlyodat: ")

try:
    height = int(height)
    weight = float(weight)
except ValueError:
    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        pass

print(f"A BMI értéked: {bmi.calc(weight=weight,height=height):.2f}")



