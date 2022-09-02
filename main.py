def calculate_simple_interest():
    print("Calulating Simple Interest:\n")
    p = int(input('Principle:  '))
    n = int(input('Number of years:  '))
    r = int(input('Rate of interest:  '))
    simple_interest = (p*n*r)/100
    print (f"Simple Interest: {simple_interest}")

def lists():
    favs: list[str] = ["Raspberries", "Ribs", "Rice", "Ramen", "Rib-Eye Steak"]
    print(favs[2])
    favs.extend(["Mac & Cheese", "Milkshake", "Mashed Potatoes"])
    print(favs)
    favs.insert(2, "Tacos")
    print(favs)


def for_and_square():
    for i in range(0, 5):
        print("I am a programmer.")
    show_square()

def show_square():
    for i in range(1, 9):
        print(f"{i} squared is {i*i}.")

if __name__ == '__main__':
    # Part 1
    calculate_simple_interest()
    # Part 2
    lists()
    # Part 3
    for_and_square()