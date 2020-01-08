# epic7_automation
This script automates the repetition of doing the same stage over and over again to level up Heroes.
You can enable the auto sell equipments feature to sell them every 10 runs.

## Requirements

• Python 3 (Tested with 3.7.3)

• NoxPlayer (Tested with 6.3.0.2)

## Setting up

You'll have to set some things before start using this script.

First you'll have to edit the ***config.ini*** file and replace your NoxPlayer instalation path

```noxPath: D:\Program Files\Nox```

Now, open the game and choose a phase, preferably the ones with no dialog. (this script do not expect them)

<div>
  <img src="https://i.imgur.com/5O90Agi.png" width="auto" height="100%">
</div>
<br></br>

Then select the team you want to use and hit ***Start***

<div>
  <img src="https://i.imgur.com/pMGjSnK.png" width="auto" height="100%">
</div>
<br></br>

When the phase starts hit the Auto ⟳ button.

<div>
  <img src="https://i.imgur.com/80HiWgy.png" width="auto" height="100%">
</div>
<br></br>

It would be good to time the time it takes to finish the battle because we will be using it.

Now you're ready to go.

## Usage

To use the automation you'll have to pass as an argument, the time, in seconds it takes for the battle to end.

Open the game and select the phase you want and hit ***Ready*** to make sure you're on the Select Supporter screen.

<div>
  <img src="https://i.imgur.com/uGE5RFS.png" width="auto" height="100%">
</div>
<br></br>

Now run de code passing the time, in seconds, as an argument.

```
python bot.py 100
```

## Optional Argument

You can use the optional argument ``` -s ``` to enable the auto sell equipments.

But fisrt you have to setup some options first for the safety of your items.

Go to your backpack and on the Equipment tab select ***Sell*** then ***Auto Select***

This is the config I use to autosell equipments (make sure to test to find what suits you)

<div>
  <img src="https://i.imgur.com/Q5lMVEe.png" width="auto" height="100%">
</div>

***I'm not responsible for what happens to your equipments***

You can user the optional argument ``` -h ``` to enable Heal all heroes.

Don't heall heroes by default.

## Final Thoughts

The script will show on the console every steps that it makes.

<div>
  <img src="https://i.imgur.com/7mIXWIZ.png" width="auto" height="100%">
</div>
<br></br>

At any time you can stop the script by typing ```Ctrl + C``` on the console. You'll be questioned if you want to restart the script or if you want to exit.

<div>
  <img src="https://i.imgur.com/9r3kZLh.png" width="auto" height="100%">
</div>
<br></br>

If you type Y the script will resume from the start (Select Supporter screen).

Have fun!
