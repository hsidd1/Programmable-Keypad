# Raspberry Pi Pico Programmable Keypad
<p align="center">
<img src="https://i.imgur.com/2nm9x3Y.jpeg" width="300" height="400">
</p>

A programmable keypad designed to assist a client with joint pain due to Ehlers-Danlos Syndrome. Built using a Raspberry Pi Pico microcontroller and Python. Case designed in Autodesk Inventor.

# Inspiration

The client mentioned that he had joint pain caused by lateral movement with his hands, which often would cause his joints to pop - one of the most prevalent instances where this pain affected him was when using his keyboard.

# The solution
This keypad allows common keyboard commands to be executed in a single click, which removes the lateral movement required to execute such commands.

For example:

Rather than having to do `Windows` + `SHIFT` + `S` for a screenshot, which would be painful for the client to execute, it can now be programmed into this physical keyboard extension to allow the client to execute these commands painlessly with a single click!
Furthermore, the source code can very easily be modified to map any key to any set of keyboard instructions.

# Usage
Solder wires to GPIO as mapped in [main.py](main.py). Feel free to self-configure this but change the code accordingly. Download case STL, 3D print, and place device into case. Then,

1. Download the ZIP file or clone the repository:

```sh
git clone https://github.com/hsidd1/Programmable-Keypad.git
```
2. Flash/upload code to the microcontroller 
3. Device should have the program flashed and will run when the keypad device is plugged in

Code is left configurable, so feel free to map any button to any type of command of your choice.
