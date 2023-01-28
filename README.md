## CLIBB &middot; [![GitHub license](https://img.shields.io/badge/License-GPL--3.0-blue)](https://github.com/facebook/react/blob/main/LICENSE)
CLIBB (_Command-Line Interface Building Blocks_) is a Python library that streamlines, simplifies and speeds up your CLI creation.

## Getting Started
Setting up CLIBB for your awesome projects is as easy as it gets: Either install the library via pip by running `pip install clibb` or clone this repository by running the following commands in your git-enabled terminal of choice.
```cmd
git clone https://github.com/Perytron/CLIBB.git
cd CLIBB
```

### 

## Documentation
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Examples
Read the documentation to get a detailed insight into using CLIBB and unleash its full potential. Have a look at the many different examples and templates included with this repository. I know this sounds so 🦆-ing boring; that is why I present you a simple yet complete application that will get you started:
```python
import clibb

# Variables used across windows
message = clibb.Mutable("I am CLIBB!")
mode = clibb.Mutable("Light")

# Functions executed by the 'Action' element
def change_message() -> None:
    message.set("I can change!")

# Example window showing every available element
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
        clibb.Display("Mode", mode),
        clibb.Seperator("filled"),
        clibb.Seperator("empty"),
        clibb.Navigation("c", "Configuration", message),
        clibb.Seperator("empty"),
        clibb.Action("m", "Message", action = change_message),
        clibb.Seperator("empty"),
        clibb.Configuration(mode, "Mode", "Light", "Dark", "Contrast"),
        clibb.Seperator("filled"),
        clibb.Seperator("empty")
    ]
}

# Start CLIBB application
console = clibb.Application()
console.add_window(window_1)
console.run()
```

## Contributing
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

CLIBB is [GPL-3.0 licensed](https://github.com/Perytron/CLIBB/blob/doc/LICENSE.md).