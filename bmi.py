def calc_bmi(h,w):
    print("height= "+ str(h))
    print("weight= "+ str(w))
    bmi=float(w)/float(h)**2
    print("The BMI is ",bmi)
    if bmi<18.5:
        print("under weight")
        return -1
    elif bmi>25.0:
        print("over weight")
        return 1 
    else:
        print("normal weight")
        return 0
print(calc_bmi(w=57, h=1.73))