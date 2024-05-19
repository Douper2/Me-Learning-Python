def trapezoid_area():
    a = float(input("what is the value of a's side?"))
    b = float(input("what is the value of b's side?"))
    h = float(input("what is the value of the height, aka h?"))
    result = ((a + b) * h) / 2
    print("the area of the trapezoid is: " + str(result))

trapezoid_area()