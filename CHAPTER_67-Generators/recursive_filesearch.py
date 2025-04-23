from os import listdir
from os.path import isfile, join, exists

def dateien_im_ordner(pfad):
    for datei in listdir(pfad):
        vollpfad = join(pfad, datei)
        if isfile(vollpfad) and exists(vollpfad):
            yield vollpfad

def unterordner(pfad):
    for d in listdir(pfad):
        vollpfad = join(pfad, d)
        if not isfile(vollpfad) and exists(vollpfad):
            yield vollpfad

def alles_durchsuchen(pfad):
    yield from dateien_im_ordner(pfad)
    for unter in unterordner(pfad):
        yield from alles_durchsuchen(unter)


if __name__ == '__main__':
    pfad = "C:\\Users\\musab\\Downloads"
    for datei in alles_durchsuchen(pfad):
        print(datei)
