def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def getinput():
    userinput=input("please enter the numbers")
    strlist=userinput.split(",")
    floatlist=[]
    for x in strlist:
        floatnum=float(x)
        floatlist.append(floatnum)
    return(floatlist)


def avgtemp():
    totallist=(getinput())
    add=sum(totallist)
    div=len(totallist)
    avg=add/div
    print(avg)
    


def minmax():
    input=getinput()
    mini=min(input)
    maxi=max(input)
    print("minimum is ",mini,"maximum is ",maxi)
        
    




    
avgtemp()
minmax()

