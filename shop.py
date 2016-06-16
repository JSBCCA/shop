def myshop(game=0, system=0, movie=0, pizza=0, soda=0):
    first = game * 39.99
    second = system * 249.99
    third = movie * 19.99
    fourth = pizza * 5.99
    fifth = soda * 1.50
    sixth = (first + second + third + fourth + fifth)
    seventh = round((sixth * 1.07), 2)
    print("Here is your receipt. $" + str(seventh) +
          "\nThank you for shopping with us!")


def shop():
    print("Welcome! What would you like to purchase today?\n")
    print("game = $39.99\n"
          "system = $249.99\n"
          "movie = $19.99\n"
          "pizza = $5.99\n"
          "soda = $1.50\n")
    myshop(
        int(input("game: ")), int(input("system: ")), int(input("movie: ")),
        int(input("pizza: ")), int(input("soda: ")))


shop()
