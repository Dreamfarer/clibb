import clibb


# Example Class
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    def change_name(self) -> None:
        self.__name = "Sophie"

    def get_name(self) -> str:
        return self.__name


# Example Variables
class Settings:
    image_output_directory = clibb.Mutable("images")
    openai_status = clibb.Mutable("Running")
    color_variable = clibb.Mutable("Option 2")
    menu_variable = clibb.Mutable("Option B")
    sound_variable = clibb.Mutable("Option IV")
    message_variable = clibb.Mutable("Write below!")
    checkbox_variable = clibb.Mutable(True)


# Example Functions
def generate_image() -> None:
    Settings.openai_status.set("Changeable!")
    input("Wait...")


# Example Object
adult = Person("Hannah")

# Example Windows
window_1 = {
    "name": "Home",
    "width": 75,
    "colors": {
        "text": clibb.Color(255, 255, 255),
        "background": clibb.Color(254, 0, 0),
        "pass": clibb.Color(6, 215, 27),
        "fail": clibb.Color(255, 0, 0),
        "alert": clibb.Color(255, 255, 0),
    },
    "elements": [
        clibb.Title("CLIBB", "by Perytron with <3"),
        clibb.Seperator("empty"),
        clibb.Display("Service", Settings.openai_status),
        clibb.Seperator("empty"),
        clibb.Display("Name", adult.get_name),
        clibb.Seperator("filled"),
        clibb.Seperator("empty"),
        clibb.Navigation("c", "Configuration", Settings.sound_variable),
        clibb.Seperator("empty"),
        clibb.Navigation("m", "Message", Settings.message_variable),
        clibb.Seperator("empty"),
        clibb.Configuration(
            Settings.sound_variable,
            "Volume",
            "Option I",
            "Option II",
            "Option III",
            "Option IV",
        ),
        clibb.Seperator("empty"),
        clibb.Action("o", "Name Change", action=adult.change_name, stealth=False),
        clibb.Seperator("empty"),
        clibb.Checkbox("Checkbox", Settings.checkbox_variable),
        clibb.Seperator("empty"),
        clibb.Navigation("k", "Code"),
        clibb.Navigation("t", "Text"),
        clibb.Seperator("empty"),
        clibb.Configuration(
            Settings.color_variable, "Color", "Option 1", "Option 2", "Option 3"
        ),
        clibb.Seperator("empty"),
        clibb.Input("Write", Settings.message_variable),
        clibb.Seperator("empty"),
        clibb.Configuration(Settings.menu_variable, "Size", "Option A", "Option B"),
        clibb.Seperator("filled"),
        clibb.Seperator("empty"),
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
        clibb.Seperator("empty"),
        clibb.Action("g", "Generate", action=generate_image, stealth=False),
        clibb.Seperator("empty"),
        clibb.Navigation("h", "Home"),
        clibb.Seperator("empty"),
        clibb.Navigation("n", "No"),
        clibb.Seperator("filled"),
        clibb.Seperator("empty"),
    ],
}

console = clibb.Application()
console.add(window_2, window_1)
console.remove(window_2)
console.add(window_2)
console.activate(window_1)
console.run()
