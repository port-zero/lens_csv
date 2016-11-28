import csv
from io import StringIO

from lens.parsers.base import LensParser

class Parser(LensParser):
    def treat(self, inpt, keys):
        f = StringIO(inpt)
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        loaded = list(csv.reader(f, dialect))

        for key in keys:
            loaded = loaded[key]

        return str(loaded)
