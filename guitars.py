"""
Guitars
Estimate: 40 minutes
Actual:   50 minutes
"""


from prac_06.guitar import Guitar


def main():
    """ Program to store all the user's guitars and then print their details"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{name} ({year}) : ${cost} added.")
        print(" ")
        name = input("Name: ")

    print(" ")
    print("...snip...")

    if guitars:
        print(" ")
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No Guitars in list")


main()
