# request modules pip install Pillow
# rendezési szempont
#   képeknél dátum szerint
#   fájloknál kiterjesztés szerint
#   jelenlegi könyvtár

from PIL import Image
import os

def get_exif_create_date(path):
    try:
        return Image.open(path)._getexif()[36867].split()[0].replace(':','_')
    except:
        return None
def get_file_extension(path):
    file_name, file_extension = os.path.splitext(path)
    if file_extension:
        return file_extension
def start():
    cwd = os.getcwd()
    print('Munkakönyvtár: ', cwd)
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd,f))]
    print('%d darab fájl rendezése...'%len(files))
    menu = int(input('Rendezési szempont:\n\t(1)képek\n\t(2)kiterjesztés\n'))
    if menu == 1:
        for f in files:
            date = get_exif_create_date(os.path.join(cwd,f))
            if date:
                if not os.path.isdir(date):
                    os.mkdir(date)
                print('%s áthelyezése...'%f)
                os.rename(f, os.path.join(cwd,date,f))
    elif menu == 2:
        for f in files:
            ext = get_file_extension(os.path.join(cwd,f))
            if ext:
                if not os.path.isdir(ext):
                    os.mkdir(ext)
                print('%s áthelyezése...'%f)
                os.rename(f, os.path.join(cwd,ext,f))

if __name__ == '__main__':
    start()
