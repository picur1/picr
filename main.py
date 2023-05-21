def on_sound_loud():
    global lamp
    if lamp == 0:
        basic.clear_screen()
        lamp = 1
    else:
        lamp = 0
input.on_sound(DetectedSound.LOUD, on_sound_loud)

lamp = 0
basic.show_icon(IconNames.ASLEEP)
basic.pause(500)
basic.show_string("f")
basic.pause(500)
lamp = 0
basic.clear_screen()