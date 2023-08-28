from turtle import Turtle, Screen

tony = Turtle()
tony.shape('turtle')
tony.color('darkolivegreen')
tony.fd(100)
tony.left(120)
tony.fd(100)
tony.left(120)
tony.fd(100)
tony.lt(120)

my_screen = Screen()
my_screen.exitonclick()

# to install any packages from pypi just go to that site
# find it
# open hamburger menu in pycharm
# go to settings
# then project -> python interpreter
# then click + in top and search for required package and then install
# we can use it by importing as usual

from prettytable import PrettyTable  # importing the package class PrettyTable from package pretty table

table = PrettyTable()  # assigning it to an object

table.add_column("Pokemon", ["Pikachu", "Eevee", "Charizard"])  # accessing add_ column function/method from class
table.add_column("Power type", ["Electric", "Fire", "Fire"])
table.align = "l"  # here the align is an attribute unlike add_colum which is a method , attributes are accessed like this
print(table)
