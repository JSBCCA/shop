def myshop(game=0, system=0, movie=0, pizza=0, soda=0):
    first = game * 39.99
    second = system * 249.99
    third = movie * 19.99
    fourth = pizza * 5.99
    fifth = soda * 1.55
    sixth = (first + second + third + fourth + fifth)
    seventh = round((sixth * 1.07), 2)
    if seventh > 0:
        print("Here is your receipt. $" + str(seventh) +
              "\nThank you for shopping with us!")
    else:
        print("Oh, you don't want to buy anything? Well have a good day!")


def shop():
    print("Welcome! What would you like to purchase today?\n")
    print("game = $39.99\n"
          "system = $249.99\n"
          "movie = $19.99\n"
          "pizza = $5.99\n"
          "soda = $1.55\n")
    myshop(
        int(input("games: ")), int(input("systems: ")), int(input("movies: ")),
        int(input("pizzas: ")), int(input("sodas: ")))


shop()
