import re
import os.path


class LRCObject:
    TAG_MAP = {'al': 'album', 'ar': 'artist', 'by': 'lyrics_creator', 'offset':
            'offset', 're': 'software_used', 'ti': 'song_title', 've':
            'software_version', 'file_name': 'file_name'}

    def __init__(self, album="", artist="", lyrics_creator="", lines=[],
            tags={}, offset=0, software_used="", song_title="",
            software_version="", file_name=""):
        self.album = album
        self.artist = artist
        self.lyrics_creator = lyrics_creator
        self.offset = offset
        self.software_used = software_used
        self.song_title = song_title
        self.software_version = software_version
        self.tags = tags
        self.lines = lines
        self.file_name = file_name

    def add_line(self, line, index=None):
        self.lines.append(line)

    def add_tag(self, tag_name, tag_content):
        self.tags[tag_name] = tag_content
        setattr(self, LRCObject.TAG_MAP[tag_name], tag_content)


class LRCLine:
    def __init__(self, time="", lyrics="", mins=0, secs=0, millis=0):
        self.time = time
        self.lyrics = lyrics
        self.mins = mins
        self.secs = secs
        self.millis = millis


class LRCParser:
    """
    This class contains utilities to parse an .lrc file and construct an
    LRCObject from it.
    """
    def parse(self, filename):
        lines = []
        lrc_object = LRCObject()
        lrc_object.add_tag("file_name", os.path.basename(filename.replace(".lrc","")))
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            lrc_object = self.parse_line(lrc_object, line)

        return lrc_object

    def parse_line(self, lrc_object, line):
        tag_match = re.match(r'^\[[a-z][a-z]:', line)
        if tag_match:
            tag_name = tag_match.group()[1:3]
            tag_content_match = re.search(r':.*\]', line)
            tag_content = tag_content_match.group()[1:-1]
            lrc_object.add_tag(tag_name, tag_content)
        else:
            lrc_time_match = re.match(r'^\[\d\d:\d\d.\d\d\]', line)
            if lrc_time_match:
                lrc_time = lrc_time_match.group()[1:-1]
                lrc_mins = lrc_time[0:2]
                lrc_secs = lrc_time[3:5]
                lrc_millis = lrc_time[6:]
                lrc_lyrics_match = re.search(r'\d\d\].*', line)
                lrc_lyrics = lrc_lyrics_match.group()[3:]
                lrc_line = LRCLine(lrc_time, lrc_lyrics, lrc_mins, lrc_secs,
                        lrc_millis)
                lrc_object.add_line(lrc_line)
        return lrc_object
