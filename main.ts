input.onButtonPressed(Button.A, function () {
    fahterten = 1.8 * input.temperature() + 32
    basic.showNumber(fahterten)
    basic.showNumber(0)
    basic.showString("p")
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    kelvin = 0
    fahterten = 0
})
input.onButtonPressed(Button.B, function () {
    kelvin = input.temperature() + 273.15
    basic.showNumber(kelvin)
    basic.showString("k")
    basic.pause(1000)
    basic.clearScreen()
})
let kelvin = 0
let fahterten = 0
fahterten = 0
kelvin = 0
basic.showNumber(input.temperature())
basic.showString("c")
basic.pause(1000)
game.resume()
basic.clearScreen()
basic.forever(function () {
    basic.showLeds(`
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        `)
})
basic.forever(function () {
    basic.showIcon(IconNames.StickFigure)
})
