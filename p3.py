def human_years():
    hyear = int(input("Enter an age in human years: "))
    if(hyear>0):
        dog_years(hyear)
    else:
        quit

def dog_years(hyear):
    if(hyear <= 2):
        dyear = hyear*10.5
        print_year(dyear)
    elif(hyear>2):
        a = 2
        b = hyear-a
        dyear = (a*10.5) + (b*4)
        print_year(dyear)
        
def print_year(dyear):
    print("Thats equivalent to ",dyear," dog years")

human_years()