#!/usr/bin/python

import menus
import simulation

#input_build_building = "1"
#input_upgrade_building = "2"
#input_buy_advertisement = "3"
#input_employ = "4"
#input_end_turn = "5"
#input_exit = "9"

#selectable_items = [input_build_building, input_upgrade_building, input_buy_advertisement, input_employ, input_end_turn,
 #                   input_exit]
#screen_action_menu = False
#screen_build_menu = False
#screen_upgrade_menu = False
#screen_mode_menu = False
#ui_screen = [screen_mode_menu, screen_action_menu, screen_build_menu, screen_upgrade_menu]

my_park = simulation.Park(0)

screen_mode = 0
screen_action = 1
screen_build = 2
screen_upgrade = 3
screen_advertisement = 4
screen_employ = 5

screens = [screen_mode, screen_action, screen_build, screen_upgrade, screen_advertisement, screen_employ]

ui_screen = screen_mode
game_is_active = True

while game_is_active:
    game_mode = ""
    if ui_screen == screen_mode:
        while game_mode not in ["1", "2", "3", "9"]:
            menus.mode_menu()
            game_mode = raw_input("")
            if game_mode == "9":
                game_is_active = False
            else:
                ui_screen = screen_action
    elif ui_screen == screen_action:
        while ui_screen == screen_action:
            menus.clear_screen()
            menus.menu()
            selected_menu = int(raw_input("Select an item from the menu"))
            if selected_menu in range(1,6):
                ui_screen = screens[selected_menu + 1]
            elif selected_menu == 5:
                my_park.turn()
            elif selected_menu == 6:
                ui_screen = screen_mode

    elif ui_screen == screen_build:
        menus.clear_screen()
        menus.building_menu(my_park)
        selected_building = int(raw_input("Select a building for the list"))
        if selected_building in range(1,6):
            my_park.build(simulation.Park.modes[my_park.mode][selected_building - 1])
        elif selected_building == 6:
            ui_screen = screen_action

    elif ui_screen == screen_upgrade:
        if len(my_park.buildings) != 0:
            menus.clear_screen()
            menus.upgrade_menu(my_park)
            selected_menu = int(raw_input("Select a building to upgrade"))
            if selected_menu in range(1, len(my_park.buildings) + 1):
                if my_park.buildings[selected_menu - 1].upgrade_cost <= my_park.money:
                    my_park.buildings[selected_menu - 1].upgrade(my_park, my_park.buildings[selected_menu - 1].type)
                else:
                    print "You have not enough money to upgrade this building"
                #    ui_screen = screen_upgrade
            if selected_menu == len(my_park.buildings) + 1:
                ui_screen = screen_action
        else:
            print "You have no buildings to upgrade"
            ui_screen = screen_action
    elif ui_screen == screen_advertisement:
        pass  # TODO
    elif ui_screen == screen_employ:
        pass  # TODO


