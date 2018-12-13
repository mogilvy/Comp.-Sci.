import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

show = pg.prompt(" What is your Favorite Show? ")

if show == "Modern Family":
    pg.alert (" That is the best show!")
    wb.open("https://www.youtube.com/watch?v=q39eWOMd18E")
    points += 5
elif show ==  "Game of Thrones ":
    pg.alert (" EWWWW WHY?")
    wb.open("https://www.youtube.com/watch?v=3-fiwBPyAa4")
    points += 5
elif show == "frozen":
    pg.alert (" That's my Favorite")
    wb.open("https://www.youtube.com/watch?v=3-fiwBPyAa4")
    points += 5
elif show == "Dora the Explorer":
    pg.alert (" That's a cute show!")
    wb.open("https://www.youtube.com/watch?v=rGyLz5219Lg")
    points += 5
elif show == "South Park":
    pg.alert (" I love that")
elif show == "Backyardagins":
    pg.alert ("Kate loves that show!")
else:
    pg.alert (" your favorite show is" + str(show))

food = pg.prompt(" What is your Favorite Food?")

if food == "fish":
    pg.alert (" Never!")
    wb.open("https://www.youtube.com/watch?v=uCF3vBuxXS8")
    points += 5
elif food == "Smoothies":
    pg.alert (" That Is The Greatest Food Of All Time!!!")
    wb.open("https://www.youtube.com/watch?v=hieFxbBDw5c")
    points += 5
elif food == "Pasta":
    pg.alert (" That good")
    wb.open("https://www.youtube.com/watch?v=fx1gYHoUJSU")
    points += 5
elif food == "Veggies":
    pg.alert (" Who likes veggies")
    wb.open("https://www.youtube.com/watch?v=Ds6tUxatnTs")
elif food == " Chinese":
    pg.alert (" Yummy!")
    points += 5
elif food == " Italian":
    pg.alert (" It's not that good")
else:
    pg.alert (" your favorite food is " + str(food))

dessert = pg.prompt(" What is your Favorite dessert? ")

if dessert == " Mint Chocolate Chip Icecream":
    pg.alert (" That is the best dessert!")
    wb.open("https://www.youtube.com/watch?v=5t-IKxx9ttU")
    points += 5
elif dessert ==  " Reeces ":
    pg.alert (" EWWWW WHY?")
    wb.open("https://www.youtube.com/watch?v=6IdKTZwdBb8")
elif dessert == " Twix Candy Bar":
    pg.alert (" That's my Favorite")
    points += 5
elif dessert == " Tiramisu":
    pg.alert (" That nice!")
    wb.open("https://www.youtube.com/watch?v=LPnZTY79mR4")
elif dessert == " Coffee":
    pg.alert (" I love that")
    points += 5
elif dessert == " brownies":
    pg.alert  (" They are super chocolatly")
    wb.open("https://www.youtube.com/watch?v=KQLo5VuKwyE")
    points += 5
else:
    pg.alert (" your favorite dessert is" + str(dessert))

sport = pg.prompt(" What is your Favorite sport?")

if sport == " soccer":
    pg.alert (" Never!")
    wb.open("https://www.youtube.com/watch?v=S_IAqwrvEuU")
    points += 5
elif sport == " skiing":
    pg.alert (" That Is The Greatest sport Of All Time!!!")
    wb.open("https://www.youtube.com/watch?v=c5mt4WKb5OY")
    points += 5
elif sport == " lacrosse":
    pg.alert (" That's good")
    wb.open("https://www.youtube.com/watch?v=BolcTIIXsw0")
    points += 5
elif sport == " hockey":
    pg.alert (" That's fun")
    wb.open("https://www.youtube.com/watch?v=6R9-3cgyOk8")
elif sport == " field hockey":
    pg.alert (" YAY!")
    points += 5
elif sport == " basketball":
    pg.alert (" It's not that good")
else:
    pg.alert (" your favorite sport is " + str(sport))



animal = pg.prompt(" What is your Favorite animal? ")

if animal == " dogs":
    pg.alert (" That is the best animal!")
    wb.open("https://www.youtube.com/watch?v=0IvC6fZYGMM")
    points += 5
elif animal ==  " snakes ":
    pg.alert (" EWWWW WHY?")
    wb.open("https://www.youtube.com/watch?v=j24_xH5uvdA")
    points += 5
elif animal == " horses":
    pg.alert (" That's my Favorite")
elif animal == " cat":
    pg.alert (" That's a cute animal!")
    wb.open("https://www.youtube.com/watch?v=wZZ7oFKsKzY")
    points += 5
elif animal == " hamsters":
    pg.alert (" I love that")
    wb.open("https://www.youtube.com/watch?v=XTgFtxHhCQ0")
elif animal == "turtle":
    pg.alert (" Kate likes that too")
    wb.open("https://www.youtube.com/watch?v=PBVtZbpiRZA")
    points += 5
else:
    pg.alert (" your favorite animal is" + str(animal))

pg.alert(points)
