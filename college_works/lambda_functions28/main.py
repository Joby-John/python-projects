choice = int(input("Which shapes area you want to calculate \n1-square\n2-rectangle\n3-triangle:-"))
ar_sq = lambda side: side ** 2
ar_tri = lambda base, height: base * height * .5
ar_rect = lambda length, breadth: length * breadth
match choice:
    case 1:
        area = ar_sq(float(input("Enter the length of the side:-")))
        print(f'{round(area,2)} sq.units')
    case 2:
        area = ar_rect(float(input("Enter length:-")), float(input("Enter breadth:-")))
        print(f'{round(area,2)} sq.units')
    case 3:
        area = ar_tri(float(input("Enter base:- ")), float(input("Enter height:-")))
        print(f'{round(area,2)} sq.units')
    case _:
        print("Invalid choice")
