def calc_bmi(h,w):
    print("height= "+ str(h))
    print("weight= "+ str(w))
    bmi=float(w)/float(h)**2
    print("The BMI is ",bmi)
    if bmi<18.5:
        print("under weight")
    elif bmi>25.0:
        print("over weight")
    else:
        print("normal weight")
calc_bmi(w=57, h=1.73) 