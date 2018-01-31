class Park(object):
    """An amusement park with different buildings.

    Variables:
        buildings: A list that contain the buildings of the amusement park.
        money: The budget of the amusement park.
    """

    def __init__(self):
        """Return a aprk object which has empty building list and have 150000 budget money."""
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


class Building(object):
    """Building that can be bought for the amusement park.

    Variables:
        name: it the name of the building
        cost: the cost of the building
        income:
        base_income:
        real_income:
        upgrade_cost: the cost of upgrading the building, the cost of the upgrading is doubles each time (the first is equal to the cost of the building)
        level: the level of the building

    """

    def __init__(self, name, cost, income):
        self.name = name
        self.cost = cost
        self.income = income
        self.base_income = income
        self.real_income = income
        self.upgrade_cost = cost
        self.level = 0

    def produce_income(self, park):
        park.money += self.real_income

    def upgrade(self, park):
        if park.money >= self.upgrade_cost:
            park.money -= self.upgrade_cost
            self.real_income += self.base_income
            self.upgrade_cost *= 2
            self.level += 1
