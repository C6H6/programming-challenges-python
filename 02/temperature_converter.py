def get_scale(question):
    print("1.Celsius\n2.Fahrenheit\n3.Kelvin")
    try:
        scale = int(input(question + ": "))
        if 1 <= scale <= 3:
            return scale
        else:
            raise ValueError
    except ValueError:
        print("Invalid parameter")
        exit(255)


def convert(in_scale, out_scale, value):
    if in_scale == 1:
        if out_scale == 1:
            return value
        elif out_scale == 2:
            return value * 9 / 5 + 32
        else:
            return value + 273.15
    elif in_scale == 2:
        if out_scale == 1:
            return (value - 32) * 5 / 9
        elif out_scale == 2:
            return value
        else:
            return (value + 459.67) * 5 / 9
    else:
        if out_scale == 1:
            return value - 273.15
        elif out_scale == 2:
            return value * 9 / 5 - 459.67
        else:
            return value


input_scale = get_scale("Input scale")
output_scale = get_scale("Output scale")

value = 0
try:
    value = float(input("Value: "))
except ValueError:
    print("Invalid parameter")
    exit(255)

print("Result: " + str(round(convert(input_scale, output_scale, value), 2)))
