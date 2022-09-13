class Mars_rover:
    def __init__(self,x,y,cardinal,commend):
        self.x = x
        self.commend = commend
        self.y = y
        self.cardinal = cardinal

    def getfinalposition (mars_rover):

        list = []
        for index in mars_rover.commend:
            if index == "L":
              if mars_rover.cardinal == "N":
                  mars_rover.cardinal = 'W'

              elif mars_rover.cardinal == "W":
                  mars_rover.cardinal ='S'

              elif mars_rover.cardinal == "S":
                  mars_rover.cardinal = 'E'

              elif mars_rover.cardinal == "E":
                  mars_rover.cardinal = 'N'

            elif index == "R":
                if mars_rover.cardinal == "N":
                    mars_rover.cardinal = 'E'

                elif mars_rover.cardinal == "E":
                    mars_rover.cardinal = 'S'

                elif mars_rover.cardinal == "S":
                    mars_rover.cardinal = 'W'

                elif mars_rover.cardinal == "W":
                    mars_rover.cardinal = 'N'

            elif index == "M":
                if mars_rover.cardinal == "N":
                    mars_rover.y = mars_rover.y + 1
                elif mars_rover.cardinal == "S":
                    mars_rover.y = mars_rover.y - 1
                elif mars_rover.cardinal == "W":
                     mars_rover.x = mars_rover.x - 1
                elif mars_rover.cardinal == "E":
                    mars_rover.x = mars_rover.x + 1

        list.insert(0,mars_rover.x)
        list.append(mars_rover.y)
        list.append(mars_rover.cardinal)
        return list



x,y,card = input("Input first rovers starting point:").split()
commend_1 = input("Enter Commend List : ")
rover_1 = Mars_rover(int (x),int(y),card,commend_1)

x,y,card = input("Input second rovers starting point:").split()
commend_2 = input("Enter Commend List : ")
rover_2 = Mars_rover(int (x),int(y),card,commend_2)


print(Mars_rover.getfinalposition(rover_1))
print(Mars_rover.getfinalposition(rover_2))






