from bottle import route, run, static_file, url, get, post, request, jinja2_template as template
import lrc
import os
import unicodedata
import string


@route("/")
def index():
    filenames = os.listdir("lrc/")
    available_songs = []
    if len(filenames) > 0:
        available_songs = [name[:str.find(name, '.')] for name in filenames if not name.startswith('.') and name.endswith(".lrc")]
        lrc_parser = lrc.LRCParser()
        available_songs = [lrc_parser.parse("lrc/" + song + ".lrc") for song in available_songs]
    return template("index.html", available_songs=available_songs)


@route("/static/:path#.+#", name="static")
def static(path):
    return static_file(path, root="static")


@route("/play/:name")
def load_game(name=None):
    lrc_parser = lrc.LRCParser()
    lrc_object = lrc_parser.parse("lrc/" + name + ".lrc")
    line_count = len(lrc_object.lines)
    line_enumeration = enumerate(lrc_object.lines)
    return template("game.html", name=name, lrc_object=lrc_object,
            line_count=line_count, line_enumeration=line_enumeration,
            get_url=url)


@get("/upload")
def upload_form():
    return template("upload.html")


@post("/upload")
def create_song():
    name = request.forms.name 
    mp3 = request.files.song_mp3
    lrc = request.files.song_lrc
    name = sanitize_filename(name)
    if name and hasattr(mp3, "file") and hasattr(lrc, "file"):
        mp3_file = open("static/media/" + name + ".mp3", "w")
        mp3_file.write(mp3.file.read())
        mp3_file.close()
        lrc_file = open("lrc/" + name + ".lrc", "w")
        lrc_file.write(lrc.file.read())
        lrc_file.close()
        return template("upload.html", success=True)
    else:
        return template("upload.html", success=False)


def sanitize_filename(filename):
    filename = filename.replace(' ', '_')
    valid_chars = "-_%s%s" % (string.ascii_letters, string.digits)
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(c for c in cleaned_filename if c in valid_chars)

run(host='0.0.0.0', port=80)
