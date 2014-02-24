How to play, using the latest version of the code:
==================================================
1. Clone the repo or download/unzip the code.
2. Download and install the dependencies (a python module called "bottle", and another called "jinja2). 
    - Install them in one go by first installing a virtualenv, then installing from the requirements file
      - virtualenv virtualenv\_plover\_game
      - source virtualenv\_plover\_game/bin/activate
      - pip install -r requirements.txt
    - Alternatively, install them to your system-wide Python installation
      - Get bottle by running "sudo pip install bottle" or otherwise it should be available at http://pypi.python.org/pypi/bottle/0.10.9.
      - Jinja2 can be acquired similarly by running "sudo pip install jinja2", or get it from PyPi at http://pypi.python.org/pypi/Jinja2/2.6
3. Run the server process: python server.py
4. Connect to localhost:8080/

If you own the rights and/or the rights to the files are permissive enough, fork the code, add your .lrc/.mp3 files, and submit a pull request, and I'll add it to the master branch so others can play these songs by default.
Please don't hesitate to leave feedback, whether for bugs or feature requests.

Thanks, and enjoy!
