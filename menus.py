import simulation


def mode_menu():
    separator_line = "-" * 50
    print "Choose gameplay mode"
    print "1. Easy"
    print "2. Normal"
    print "3. Hard"
    print "9. Quit"
    print separator_line


def menu():
    separator_line = "-" * 50
    screen_options = ["Build an item", "Upgrade an item", "Buy advertisement", "Employ a specialist", "End turn", "Back"]
    for i in xrange(0, len(screen_options)):
        print i + 1, "-", screen_options[i]
    print separator_line


def building_menu(my_park):
    separator_line = "-" * 50
    i = 1
    for item in simulation.Park.modes[my_park.mode]:
        print i, vars(item)
        i += 1
    print "6 - Back"
    print separator_line


def upgrade_menu(my_park):
    separator_line = "-" * 50
    i = 1
    for building in my_park.buildings:
        print i, building
        i += 1
    print separator_line

