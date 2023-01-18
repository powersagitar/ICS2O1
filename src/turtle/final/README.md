# LastFirstFallingGame
## prerequisites
### module `playsound`
* the game uses a third party module called `playsound` to provide cross platform sound support
* the module installation requires `pip`
  * [learn more about it](https://pip.pypa.io/en/stable/installation/)
* module installation
  1. open command prompt / windows powershell (for windows); terminal.app / iterm2 (for macOS)
  2. paste the command: `pip install playsound` into the prompt then hit enter
  3. wait for the installation process to complete
  4. for more instructions, check [here](https://pypi.org/project/playsound/)
* module uninstallation
  1. open command prompt / windows powershell (for windows); terminal.app / iterm2 (for macOS)
  2. paste the command: `pip uninstall playsound` into the prompt then hit enter
  3. wait for the uninstallation process to complete
  4. for more instructions, check [here](https://www.activestate.com/resources/quick-reads/how-to-uninstall-python-packages/)

## skip prerequisites by removing `playsound` module from code
* note: after removing `playsound` module, the game will no longer have sound support
* instructions
    1. open the [game source file](./main.py)
    2. comment `line 12`, `line 149` and `line 159` out

## file structure
please make sure the actual file structure looks like this, or please update the file path in the [source file](./main.py)

```
project root directory/
├── README.md
├── background.gif
├── catcher.gif
├── falling.gif
├── caught.wav
├── missed.wav
└── main.py
```