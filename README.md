[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7c51539e67b483bb8d7749acca51d3a)](https://app.codacy.com/gh/legendx22/LEGEND-BOT?utm_source=github.com&utm_medium=referral&utm_content=legendx22/LEGEND-BOT&utm_campaign=Badge_Grade_Settings)
[![Python 3.8.6](https://img.shields.io/badge/Python-3.8.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-386/)
![GitHub repo size](https://img.shields.io/github/repo-size/ULTRA-OP/ULTRA-X)
[![HitCount](http://hits.dwyl.com/legendx22/LEGEND-BOT.svg)](http://hits.dwyl.com/legendx22/LEGEND-BOT)
[![Contact Me](https://img.shields.io/badge/Telegram-Contact%20Me-informational)](https://t.me/legendx22)


# υℓтяα χ вσт
This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official υℓтяα χ вσт made by [ Team Ultra](https://t.me/ULTRAXOT) Also join support channel and group :- https://telegram.me/UltraX_Support Enjoy Your Bot!!💝
[![υℓтяα χ вσт ℓσgσ](https://telegra.ph/file/e234b6871c00f90b0fe3b.jpg)](https://t.me/ULTRAXOT)

## STATUS OF THIS BOTS 
<p align="left"><a href="https://github.com/ULTRAX-OP/ULTRA-X/network/members"><img src="https://img.shields.io/github/forks/ULTRA-OP/ULTRA-X?label=Forks&logoColor=Silver&style=social"></a><p align="left"><a href="https://github.com/ULTRA-OP/ULTRA-X/stargazers"><img src="https://img.shields.io/github/stars/ULTRA-OP/ULTRA-X?logoColor=Blue&style=social"></a><p align="left"><a href="https://github.com/ULTRA-OP/ULTRA-X"><img src="https://github-readme-stats.vercel.app/api/pin?username=legendx22&show_icons=true&theme=meta&hide_border=true&repo=ULTRA-OP/ULTRA-X"></a><p align="left"><a href="https://github.com/ULTRA-OP/ULTRA-x"><img src="https://img.shields.io/github/last-commit/legendx22/LEGEND-BOT?style=plastic"></a>

## The owner would not be responsible for any kind of bans due to the bot...


# STRING SESSION:-
## [String Session](https://repl.it/@legendx22/LEGEND-BOT#main.py)

## FORK AT YOUR OWN RISK
## Installing


-------------------------------------------------

## FOR DEPLOY BOT 

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack)

------------------------------------------------


# Credits👀
### • [LEGEND BOT](https://github.com/TeamLEGENDX/LegendBOT)
### One and only. Others with some misfuntioning brain stay out from this SUPER POWERFULL BOT😏

## Official Support 💖
<a href="https://t.me/UltraXChat"><img src="https://img.shields.io/badge/Join-Support%20Channel-red.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/UltraX_Support"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>

## The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/legendx22/LEGEND-BOT
cd LEGEND-BOT
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
