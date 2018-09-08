# pi-sound-button ![alt text](https://www.unifiedremote.com/content/logos/RaspberryPi.png "Raspberry Pi")

Create a device that plays random sound clips at the press of a button. Built with Raspberry Pi and Google's [AIY Voice kit](https://aiyprojects.withgoogle.com/voice/).

![alt text](https://aiyprojects.withgoogle.com/static/images/voice-v2/product_voice@1x.png  "Google AIY kit")
## What it does
The concept is simple. When the button is pressed, a random clip from the ```clips/``` directory is played. That's it.

In order to enable this to run without the use of an attached screen, I have included the steps to have the script run at start-up and allowed the pi to be shutdown using only the botton.

This project was built with the Google AIY kit and a Raspberry Pi 3.

## How to run

Update the ```~/.bashrc``` for the ```pi``` user to run the script automatically after boot. Using a text editor, add the following line to the end of the file. The path should match where the repo was cloned.
```
[/path/to]/pi-sound-button/pi-sound-button.py &
```
If successful, you should be greeted by a sound clip once the pi has booted.

To turn off the pi, hold the button for 3+ seconds. You will hear another clip once shutdown is initiated. It should be safe to unplug the pi once the indicator light stops blinking and remains solid red.