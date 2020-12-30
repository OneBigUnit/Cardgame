**Kieran's GCSE Project: Card Game Project**
--

This is the **Python Flask Version** of the project (created using the Python Flask Microframework *- linked*) of my GCSE Card Game Project Coursework. It is the full version of my project, running as a WSGI Web Application. I have also create a repl project, using the repl IDE *- linked -* which houses just the raw logic of the Card Game itself. However, being a CLI game, it has no account / user based features, and no web application logic. Below is a run through of features / techniques used in the project, a guide on how to run this Flask Project, and links to related sites. Docstrings can also be found in the code of both this repl.it project and my Github Repository for the Flask Version.

---

**How To Run This Project:**

After opening this project in an IDE that supports the libraries used in this project (e.g. PyCharm *- linked*), type in the IDE terminal `python run.py`. This should initiate the web application. Then go into your web browser and enter the address `http://localhost:8080/`. You can use the GUI to navigate the web application. If you wish to clear the application's User Database, you must type the following in your IDE Python Console, first ensuring that the web application is not running (exit using ctrl + c)

```
from cardgame import setup_db
setup_db()
```

This will drop and recreate the tables entirely.

Please do not alter any code, else the web application may be liable to failure.

---

**Features & Techniques Used:**

*Disclaimer: Features and Techniques mentioned are all present in my Flask App, but not all in this repl.it version, as this is just the logic behind the card game itself. Links are provided to the location of each of the mentioned teachniques*

**Purple Belt Techniques:**

- Lists for storage: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Line 49
- Functions: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/__init__.py - Line 36
- Casting functions: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Line 69
- Boolean Conditions: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Line 20

**Red Belt Techniques:**

- Manipulation of data (in lists): https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Line 58
- Parameters (in functions): https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/models.py - Line 9
- Return (in functions): https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/models.py - Line 10
- Validation Routines: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/users/routes.py - Line 18

**Gold Belt Techniques:**

- OOP: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Line 10
- Modules: https://github.com/OneBigUnit/Cardgame/tree/main/cardgame
- Import libraries: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Lines 1-7
- Try / Except Keywords: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Lines 21 / 23
- Raise Keyword: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/components/cards.py - Line 26

**Black Belt Techniques:**

- OOP Inheritance: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/models.py - Line 13
- ADTs: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/components/adts.py - Lines 1 - 30 / 33 - 54
- Packages / Libraries: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/__init__.py - Line 1 - 5
- DBMS: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/__init__.py - Line 9

**Other Techniques:**

- Generators: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/game.py - Lines 19 - 31
- Custom Context Managers: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/components/context_managers.py - Lines 4 - 14
- Custom Exceptions: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/game/logic/components/exceptions.py - Lines 1 - 4
- MVC Structure: https://github.com/OneBigUnit/Cardgame
- iFrames: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/templates/about.html - Lines 15 - 18
- Key Word Arguments (function parameters): https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/__init__.py - Line 17
- Decorators: https://github.com/OneBigUnit/Cardgame/blob/main/cardgame/users/routes.py - Lines 82 - 83

---

**Other Links:**

- My GCSE Card Game Github Repository: https://github.com/OneBigUnit/Cardgame
- Flask Python Microframework: https://flask.palletsprojects.com/en/1.1.x/
- Pycharm (My Main IDE): https://www.jetbrains.com/pycharm/
- Repl (My Secondary IDE): https://www.repl.it/
- My Repl Card Game README.md File & Project: https://repl.it/@KieranLock/Card-Game-Logic#README.md

---

**Closing Notes:**

Instructions on how to run this app, external links and coding techniques are listed above. Read the repl.it README.MD file for more information on the repl.it version. Enjoy :)

---

Kieran Lock
