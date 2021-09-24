def on_button_pressed_a():
    global fahterten
    fahterten = 1.8 * input.temperature() + 32
    basic.show_number(fahterten)
    basic.show_number(0)
    basic.show_string("p")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global kelvin, fahterten
    kelvin = 0
    fahterten = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global kelvin
    kelvin = input.temperature() + 273.15
    basic.show_number(kelvin)
    basic.show_string("k")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

kelvin = 0
fahterten = 0
fahterten = 0
kelvin = 0
basic.show_number(input.temperature())
basic.show_string("c")
basic.pause(1000)
basic.clear_screen()

def on_forever():
    basic.show_leds("""
        . . # . .
                # # # # #
                . . # . .
                . # . # .
                # . . . #
    """)
basic.forever(on_forever)

def on_forever2():
    basic.show_icon(IconNames.STICK_FIGURE)
basic.forever(on_forever2)
