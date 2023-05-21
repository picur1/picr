input.onSound(DetectedSound.Loud, function () {
    if (lamp == 0) {
        basic.clearScreen()
        lamp = 1
    } else {
        lamp = 0
    }
})
let lamp = 0
basic.showIcon(IconNames.Asleep)
basic.pause(500)
basic.showString("f")
basic.pause(500)
