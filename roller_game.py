#!/usr/bin/python

import menus
import simulation


input_build_building = "1"
input_upgrade_building = "2"
input_buy_advertisement = "3"
input_employ = "4"
input_end_turn = "5"
input_exit = "9"

selectable_items = [input_build_building, input_upgrade_building, input_buy_advertisement, input_employ, input_end_turn, input_exit]
screen_action_menu = False
screen_build_menu = False
screen_upgrade_menu = False
screen_mode_menu = False
ui_screen = [screen_mode_menu, screen_action_menu, screen_build_menu, screen_upgrade_menu]

my_park = simulation.Park(0)

while True:
    game_mode = ""
    while game_mode not in ["1", "2", "3", "9"]:
        menus.mode_menu()
        game_mode = raw_input("")
        screen_mode_menu = True
        selected_menu = ""
        if game_mode == "9":
            break
        else:
            while selected_menu not in selectable_items and game_mode == 1:
                selected_menu = raw_input("Select an item from the menu")
                menus.menu()
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
    break


my_park.turn()
