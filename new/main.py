from Application import Application
from Color import Color
from elements.Title import Title
from elements.Display import Display
from elements.Seperator import Seperator
from elements.Menu import Menu
from elements.Configuration import Configuration

window_1 = {
    "name": "Home",
    "width": 50,
    "colors": {
        "text": Color(255, 255, 255),
        "background": Color(112, 60, 160),
        "pass": Color(0, 255, 0),
        "fail": Color(255, 0, 0),
        "alert": Color(255, 255, 0),
    },
    "elements": [
        Title("OpenAI-CLI 0.3.0", "by Perytron with <3"),
        Seperator("empty"),
        Display("OpenAI Status", "VAR1"),
        Seperator("filled"),
        Seperator("empty"),
        Menu("o", "OpenAI Settings", "VAR2"),
        Seperator("empty"),
        Menu("t", "Text"),
        Seperator("empty"),
        Menu("i", "Image"),
        Seperator("empty"),
        Menu("c", "Code"),
        Seperator("empty"),
        Menu("s", "Settings"),
        Seperator("filled"),
        Seperator("empty")
    ]
}

window_2 = {
    "name": "OpenAI Settings",
    "width": 50,
    "colors": {
        "text": Color(255, 255, 255),
        "background": Color(112, 60, 160),
        "pass": Color(0, 255, 0),
        "fail": Color(255, 0, 0),
        "alert": Color(255, 255, 0),
    },
    "elements": [
        Title("OpenAI Settings"),
        Seperator("empty"),
        Menu("y", "Yes"),
        Seperator("empty"),
        Menu("n", "No"),
        Seperator("filled"),
        Seperator("empty")
    ]
}

console = Application() # Create new instance
console.add_window(window_2)
console.add_window(window_1)
console.run()