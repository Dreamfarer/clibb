## CLIBB &middot; [![GitHub license](https://img.shields.io/badge/License-GPL--3.0-blue)](https://github.com/facebook/react/blob/main/LICENSE)
CLIBB (_Command-Line Interface Building Blocks_) is a Python library that streamlines, simplifies and speeds up your CLI creation. It provides **eight** unique and customizable building blocks to help you build a pretty, robust, and interactive CLI.

## Getting Started
1. Install CLIBB using `pip` by running `pip install clibb`.
1. Create a new Python file in your IDE of choice.
1. Setup window configurations using the provided building blocks detailed [here](https://github.com/Perytron/clibb/tree/doc#documentation).
1. Initialize CLIBB with `console = clibb.Application()`
1. Add your previously created window configurations with `console.add(window_1, ...)`.
1. Set the initial window with `console.activate(window_1)`.
1. Finally execute CLIBB and enjoy with `console.run()`


## Documentation
Proper documentation will be provided in a future deployment. For the time being, please refer to the detailed example below and use the information provided by your IDE based on the code documentation.

## Example
To help you get started without wading through the 🦆-ing boring documentation; here is a complete example that shows you everything CLIBB has to offer:
```python
import clibb

# Example class
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
    def change_name(self) -> None:
        self.__name = "Sophie"
    def get_name(self) -> str:
        return self.__name

# Example object
adult = Person("Hannah")

# Example variables
class Settings:
    options = clibb.Mutable("Option IV")
    user_input = clibb.Mutable("Change me below!")
    checkbox_state = clibb.Mutable(True)

# Example window configuration showing all available building blocks.
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
        clibb.Display("Current Option:", Settings.options),
        clibb.Separator("empty"),
        clibb.Configuration(Settings.options,"Options:","Option I","Option II","Option III","Option IV",),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Name:", adult.get_name),
        clibb.Separator("empty"),
        clibb.Action("o", "Set Name to 'Sophie'", action=adult.change_name, stealth=False),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Text", Settings.user_input),
        clibb.Separator("empty"),
        clibb.Input("Input Text", Settings.user_input),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Display("Current Text", Settings.checkbox_state),
        clibb.Separator("empty"),
        clibb.Checkbox("Checkbox", Settings.checkbox_state),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
        clibb.Navigation("c", "Configuration", "Go to the 'Configuration' window with 'c'"),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
    ],
}

# Another example window configuration to show navigation between windows.
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
        clibb.Navigation("h", "Home", "Go to the 'Home' window with 'h' or return with 'e'"),
        clibb.Separator("filled"),
        clibb.Separator("empty"),
    ],
}

# Setup and run CLIBB!
console = clibb.Application()
console.add(window_2, window_1)
console.remove(window_2)
console.add(window_2)
console.activate(window_1)
console.run()
```

## Contributing
I'd love to collaborate with you! Feel free to fork this repository, implement or refactor as desired, and create a pull request for integration into the main branch. If you encounter any issues or have questions, open an [issue](https://github.com/Perytron/clibb/issues/new), and I'll be happy to assist.

CLIBB is [GPL-3.0 licensed](https://github.com/Perytron/CLIBB/blob/doc/LICENSE.md).