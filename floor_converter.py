print(" Welcome to lift converter ")
euf = (input("Enter the floor no you want to conert from EU to US: "))
try:
    euf = int(euf)
    usf = euf+1 
    print( "That'll be floor number "+ str(usf) +" in US")
    print("thanks for using")
except:
    print( "Enter a number please")

