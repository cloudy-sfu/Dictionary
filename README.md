# Dictionary
 A command-line implement for Free Dictionary API

## Acknowledge

https://api.dictionaryapi.dev provides the data source, and https://github.com/TaylorSMarks/playsound provides the module for playing sound.

## Installation

There are the latest release. However, if you want to build it by source code:

```
pip install -r requirements
pyinstaller -F main.py -p config.py -p playsound.py
```
