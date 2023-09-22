choice = int(input("Which shapes area you want too calculate \n1-square\n2-rectangle\n3-triangle:-"))
ar_sq = lambda side: side ** 2
ar_tri = lambda base, height: base * height * .5
ar_rect = lambda length, breadth: length * breadth
match choice:
    case 1:
        print(f'{round(ar_sq(float(input("Enter the length of the side:-"))),2)} sq.units')
    case 2:
        print(f'{round(ar_rect(float(input("Enter length of length:-")), float(input("Enter breadth:-"))),2)} sq.units')
    case 3:
        print(f'{round(ar_tri(float(input("Enter base:- ")), float(input("Enter height:-"))),2)} sq.units')
    case _:
        print("Invalid choice")
