class vehicle:
    def __init__(self,name,maxspeed,mileage,colour):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.colour=colour
class bus(vehicle):
    pass
bus1=bus("school bus",130,40,"yellow")
print("bus named as", bus1.name,bus1.maxspeed,bus1.colour)