import clibb

# Example Variables
class Settings():
    image_output_directory = clibb.Mutable("images")
    openai_status = clibb.Mutable("Running")
    color_variable = clibb.Mutable("Option 2")
    menu_variable = clibb.Mutable("Option B")
    sound_variable = clibb.Mutable("Option IV")

# Example Functions
def generate_image() -> None:
    Settings.openai_status.set("Changeable!")
    input("Wait...")

# Example Windows
window_1 = {
    "name": "Home",
    "width": 75,
    "colors": {
        "text": clibb.Color(255, 255, 255),
        "background": clibb.Color(112, 60, 160),
        "pass": clibb.Color(0, 255, 0),
        "fail": clibb.Color(255, 0, 0),
        "alert": clibb.Color(255, 255, 0),
    },
    "elements": [
        clibb.Title("CLIBB", "by Perytron with <3"),
        clibb.Seperator("empty"),
        clibb.Display("OpenAI Status", Settings.openai_status),
        clibb.Seperator("filled"),
        clibb.Seperator("empty"),
        clibb.Navigation("o", "OpenAI Settings", "VAR2"),
        clibb.Seperator("empty"),
        clibb.Configuration(Settings.color_variable, "Color", "Option 1", "Option 2", "Option 3"),
        clibb.Seperator("empty"),
        clibb.Configuration(Settings.menu_variable, "Size", "Option A", "Option B"),
        clibb.Seperator("empty"),
        clibb.Navigation("t", "Text"),
        clibb.Seperator("empty"),
        clibb.Configuration(Settings.sound_variable, "Volume", "Option I", "Option II", "Option III", "Option IV"),
        clibb.Seperator("empty"),
        clibb.Navigation("i", "Image"),
        clibb.Seperator("empty"),
        clibb.Navigation("c", "Code"),
        clibb.Seperator("empty"),
        clibb.Navigation("s", "Settings"),
        clibb.Seperator("filled"),
        clibb.Seperator("empty")
    ]
}

window_2 = {
    "name": "OpenAI Settings",
    "colors": {
        "text": clibb.Color(255, 255, 255),
        "background": clibb.Color(112, 60, 160),
        "pass": clibb.Color(0, 255, 0),
        "fail": clibb.Color(255, 0, 0),
        "alert": clibb.Color(255, 255, 0),
    },
    "elements": [
        clibb.Title("OpenAI Settings"),
        clibb.Seperator("empty"),
        clibb.Action("g", "Generate", action = generate_image),
        clibb.Seperator("empty"),
        clibb.Navigation("y", "Yes"),
        clibb.Seperator("empty"),
        clibb.Navigation("n", "No"),
        clibb.Seperator("filled"),
        clibb.Seperator("empty")
    ]
}

console = clibb.Application()
console.add_window(window_2)
console.add_window(window_1)
console.run()