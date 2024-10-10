import BMILib as bmi

magasság= input("Add meg a magasságod: ")
súly= input("Add meg a súlyodat: ")

try:
    magasság = int(magasság)
    súly = float(súly)
except ValueError:
    try:
        magasság = float(magasság)
        súly = float(súly)
    except ValueError:
        pass

print(f"A BMI értéked: {bmi.calc(súly=súly,magasság=magasság):.2f}")



