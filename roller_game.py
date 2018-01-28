#!/usr/bin/python

class Park(object):

    def __init__(self):
        self.buildings = []
        self.money = 150000

    def build(self, b):
        if self.money >= b.cost:
            self.money -= b.cost
            self.buildings.append(b)

    def buy_advertisement(self, d):
        pass

    def turn(self):
        for b in self.buildings:
            b.produce_income()


class Building(object):

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
        if (park.money >= self.upgrade_cost):
            park.money -= self.upgrade_cost
            self.real_income += self.base_income
            self.upgrade_cost *= 2
            self.level += 1

park = Park()
park.build(Building("Körhinta", 100, 20))
park.turn()