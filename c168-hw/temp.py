class Skins:
    def __init__(self,name,amount,developer,link,about):
        self.name=name
        self.amount=amount
        self.developer=developer
        self.link=link
        self.about=about
    def add_data(self):
        print("")
        print("")
        print('Name: '+self.name)
        print('Amount: '+self.amount+" Minecoins")
        print('Developer: '+self.developer)
        print('Link: '+self.link)
        print('Abour: '+self.about)
        print("We Don't Affilated With mojang Studioes And Microsoft")
        print("")
        print("")
skin1=Skins("Hostile Disguide","490","Pathway Studioes","https://www.minecraft.net/en-us/marketplace/pdp?id=5f7501a4-a9dd-43c5-b0f8-8c22daa37d87","Sneaking around is an artform. Being able to evade mobs or tiptoe through a cavern undetected can be tough at times, but with the proper disguise, it's no problem! This skin pack of disguised mobs will have you sleuthing in the shadows in no time!")
skin1.add_data()
skin2=Skins("Craftee Season 2","310","Logdotzip","https://www.minecraft.net/en-us/marketplace/pdp?id=891c2fed-f71f-4eba-9437-d3e943bba79a","Back by popular demand, it’s Craftee! Hop into these season 2 player skins all based on your favorite “Minecraft But” YouTube series. Show your friends your Custom Hearts, Trees Beat the Game for You, Fast Food costumes, and more! Grab these 15 EXCLUSIVE skins from Craftee Season 2. Craft, Survive and Adventure your way!")
skin2.add_data()
skin3=Skins("HD Camo","490","Pathway Studioes","https://www.minecraft.net/en-us/marketplace/pdp?id=ae66346b-3f0b-405e-a5cb-6fa1992e4030","Are you a master of camouflage? Troll and trick your friends with these HD camouflage skins!")
skin3.add_data()
skin4=Skins("Zombie Sport","In Mine","310","https://www.minecraft.net/en-us/marketplace/pdp?id=ea3ccc4f-42d7-41fd-93c2-ab00bee64c36","Everyone wants to be strong and healthy, even zombies! Take the form and choose what do you want to do today? Basketball, Football and maybe swimming, do not forget to call your zombie friends, sports together are much more fun!")
skin4.add_data()
#skin1=Skins()
#skin1.add_data()