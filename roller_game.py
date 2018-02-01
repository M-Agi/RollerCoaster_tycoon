#!/usr/bin/python

import menus
import simulation

menus.menu()

input_build_building = "1"
input_upgrade_building = "2"
input_buy_advertisement = "3"
input_employ = "4"
input_end_turn = "5"
input_exit = "9"

selectable_items = [input_build_building, input_upgrade_building, input_buy_advertisement, input_employ, input_end_turn, input_exit]
modes = ["easy", "normal", "hard"]

my_park = simulation.Park()
while True:
    selected_menu = ""
    while selected_menu not in selectable_items:
        selected_menu = raw_input("Select an item from the menu")
    if selected_menu == input_build_building:
        menus.building_menu(my_park)


    elif selected_menu == input_upgrade_building:
        if len(my_park.buildings) != 0:
            menus.upgrade_menu()
        else:
            selected_menu = raw_input("You have no buildings to upgrade")
    elif selected_menu == input_buy_advertisement:
        pass #TODO
    elif selected_menu == input_employ:
        pass #TODO
    elif selected_menu == input_exit:
        break


my_park.turn()
