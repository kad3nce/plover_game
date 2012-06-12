from bottle import route, run, jinja2_template as template
import lrc


@route("/play/:name")
def load_game(name=None):
    lrc_parser = lrc.LRCParser()
    print name + ".html"
    lrc_object = lrc_parser.parse("lrc/" + name + ".lrc")
    line_count = len(lrc_object.lines)
    line_enumeration = enumerate(lrc_object.lines)
    return template("game.html", name=name, lrc_object=lrc_object,
            line_count=line_count, line_enumeration=line_enumeration)

run(host='localhost', port=8080)