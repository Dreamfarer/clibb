from Color import Color
from elements.Title import Title
from elements.Display import Display
from elements.Seperator import Seperator
from elements.Navigation import Navigation
from elements.Action import Action
from elements.Configuration import Configuration
from configuration.Actions import *


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
        Display("OpenAI Status", Settings.openai_status),
        Seperator("filled"),
        Seperator("empty"),
        Navigation("o", "OpenAI Settings", "VAR2"),
        Seperator("empty"),
        Navigation("t", "Text"),
        Seperator("empty"),
        Navigation("i", "Image"),
        Seperator("empty"),
        Navigation("c", "Code"),
        Seperator("empty"),
        Navigation("s", "Settings"),
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
        Action("g", "Generate", action = generate_image),
        Seperator("empty"),
        Navigation("y", "Yes"),
        Seperator("empty"),
        Navigation("n", "No"),
        Seperator("filled"),
        Seperator("empty")
    ]
}