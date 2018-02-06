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
    print "1. Build an item"
    print "2. Upgrade an item"
    print "3. Buy advertisement"
    print "4. Employ a specialist"
    print "5. End turn"
    print "9. Back"
    print separator_line


def building_menu(my_park):
    separator_line = "-" * 50
    i = 1
    for item in simulation.Park.modes[my_park.mode]:
        print i, vars(item)
        i += 1
    print separator_line


def upgrade_menu():
    separator_line = "-" * 50
    print 'a11. Cotton candy vendor (easy) cost: 50.000 gain: 10'
    print 'a12. Cotton candy vendor (normal) cost: 100.000 gain: 5'
    print 'a13. Cotton candy vendor (hard) cost: 150.000 gain: 2'
    print 'b11. Carousel (easy) cost: 100.000 gain: 20'
    print 'b12. Carousel (normal) cost: 150.000 gain: 10'
    print 'b13. Carousel (hard) cost: 200.000 gain: 5'
    print separator_line

