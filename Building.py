class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building_1 =  Building(1, 'один')
building_2 =  Building(2, 'два')
building_1_1 = Building(1, 'один')

print(building_1==building_2)
print(building_1==building_1_1)
print(building_1_1==building_2)