import clibb


# Example Class
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    def change_name(self) -> None:
        self.__name = "Sophie"

    def get_name(self) -> str:
        return self.__name


# Example Object
adult = Person("Hannah")


# Example Variables
class Settings:
    color_variable = clibb.Mutable("Option 2")
    menu_variable = clibb.Mutable("Option B")
    sound_variable = clibb.Mutable("Option IV")
    message_variable = clibb.Mutable("Change me below!")
    checkbox_variable = clibb.Mutable(True)


# Example Windows
window_1 = {
    "name": "Home",
    "width": 100,
    "colors": {
        "text": clibb.Color(255, 255, 255),
        "background": clibb.Color(254, 0, 0),
        "pass": clibb.Color(6, 215, 27),
        "fail": clibb.Color(255, 0, 0),
        "alert": clibb.Color(255, 255, 0),
    },
    "elements": [
        clibb.Title("CLIBB", "by Perytron with <3"),
        clibb.Separator("empty"),
        clibb.Display("How-to", "Navigate with 'w', 'a', 's', 'd'"),
        clibb.Display("", "Activate with 'q' and return with 'e'"),
        clibb.Separator("empty"),
        clibb.Display("Current Option:", Settings.sound_variable),
        clibb.Separator("empty"),
        clibb.Configuration(
            Settings.sound_variable,
            "Options:",
            "Option I",
            "Option II",
            "Option III",
            "Option IV",
        ),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Name:", adult.get_name),
        clibb.Separator("empty"),
        clibb.Action(
            "o", "Set Name to 'Sophie'", action=adult.change_name, stealth=False
        ),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Text", Settings.message_variable),
        clibb.Separator("empty"),
        clibb.Input("Input Text", Settings.message_variable),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Text", Settings.checkbox_variable),
        clibb.Separator("empty"),
        clibb.Checkbox("Checkbox", Settings.checkbox_variable),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Navigation(
            "c", "Configuration", "Go to the 'Configuration' window with 'c'"
        ),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
    ],
}

window_2 = {
    "name": "Configuration",
    "colors": {
        "text": clibb.Color(255, 255, 255),
        "background": clibb.Color(112, 60, 160),
        "pass": clibb.Color(0, 255, 0),
        "fail": clibb.Color(255, 0, 0),
        "alert": clibb.Color(255, 255, 0),
    },
    "elements": [
        clibb.Title("Configuration"),
        clibb.Separator("empty"),
        clibb.Navigation(
            "h", "Home", "Go to the 'Home' window with 'h' or return with 'e'"
        ),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
    ],
}

console = clibb.Application()
console.add(window_2, window_1)
console.remove(window_2)
console.add(window_2)
console.activate(window_1)
console.run()
