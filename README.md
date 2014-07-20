If you own the rights and/or the rights to the files are permissive enough, fork the code, add your .lrc/.mp3 files, and submit a pull request, and I'll add it to the master branch so others can play these songs by default.
Please don't hesitate to leave feedback, whether for bugs or feature requests.

Thanks, and enjoy!

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

How to play, using Docker:
==========================
1. Install [Docker](https://docs.docker.com/)
2. Launch a Docker container of Plover Game
    - `$ docker run -i -t -p 8080:8080 kad3nce/plover_game`
3. Connect to the running container. On a Linux OS, where you can host Docker containers directly, this will be http://localhost:8080/. On a Windows or Mac OS X system, you'll need to enter the IP address of your virtual Docker host machine. For Boot2Docker (OS X), this would be http://192.168.59.103:8080 by default.

Note: The filesystem in Docker containers is ephemeral, so any tracks you upload will be lost after killing/removing the Docker container. Just consider the Docker option a quick way to fire up the game and poke around.

How to build a new Docker image from the current source:
========================================================
1. Change dir to the root of this repo
2. Build a new Docker image
    - `$ docker build -t [YOUR hub.docker.com USERNAME]/plover_game .`
3. Run the new container locally
    - `$ docker run -i -t -p 8080:8080 [YOUR hub.docker.com USERNAME]/plover_game`
4. Push the image to the Docker registry to share with others
    - `$ docker push [YOUR hub.docker.com USERNAME]/plover_game`
