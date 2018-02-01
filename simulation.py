class Park(object):
    """An amusement park with different buildings.

    Variables:
        buildings: A list that contain the buildings of the amusement park.
        money: The budget of the amusement park.
        building_types: These type of building exist in the game.
    """
    building_types = ["Cotton Candy Vendor", "Carousel", "Boating Lake", "Ghost Train", "Roller Coaster"]
    """
    easy = [BuildingType(building_types[0], 50000, 10),
            bt.BuildingType(Park.building_types[1], 100000, 20),
            bt.BuildingType(Park.building_types[2], 200000, 40),
            bt.BuildingType(Park.building_types[3], 400000, 80),
            bt.BuildingType(Park.building_types[4], 800000, 160)
            ]

    normal = [bt.BuildingType(Park.building_types[0], 100000, 5),
              bt.BuildingType(Park.building_types[1], 150000, 10),
              bt.BuildingType(Park.building_types[2], 300000, 20),
              bt.BuildingType(Park.building_types[3], 600000, 40),
              bt.BuildingType(Park.building_types[4], 1000000, 80)
              ]

    hard = [bt.BuildingType(Park.building_types[0], 150000, 2),
            bt.BuildingType(Park.building_types[1], 200000, 5),
            bt.BuildingType(Park.building_types[2], 400000, 10),
            bt.BuildingType(Park.building_types[3], 800000, 20),
            bt.BuildingType(Park.building_types[4], 1600000, 40)
            ]
    """

    def __init__(self):
        """Return a park object which has empty building list and have 150000 budget money."""
        self.buildings = []
        self.money = 150000

    def build(self, b):
        """Check whether your park has enough money to build *b* building.
        Then return the building list with the newly added building and subtracts the cost of the building.
        :param b: is the type of the building
        """
        if self.money >= b.cost:
            self.money -= b.cost
            self.buildings.append(b)

    def buy_advertisement(self, d):
        pass

    def turn(self):
        """After each turn you produce money after your buildings.
        """
        for b in self.buildings:
            b.produce_income(self)


class BuildingType(object):
    """"Building types, that can be build in the game."""

    def __init__(self, name, cost, income):
        self.name = name
        self.cost = cost
        self.income = income


class Building(object):
    """Buildings that can be bought for the amusement park.

    Variables:
        name: it the name of the building
        cost: the cost of the building
        income: after each turn your building generates this much money
        real_income:
        upgrade_cost: the cost of upgrading the building, the cost of the upgrading is doubles each time (the first is equal to the cost of the building)
        level: the level of the building

    """

    def __init__(self, type):
        self.real_income = type.income
        self.upgrade_cost = type.cost
        self.level = 0

    def produce_income(self, park):
        park.money += self.real_income

    def upgrade(self, park, type):
        if park.money >= self.upgrade_cost:
            park.money -= self.upgrade_cost
            self.real_income += type.income
            self.upgrade_cost *= 2
            self.level += 1
