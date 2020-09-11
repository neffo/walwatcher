#!/bin/python3

from gi.repository import Gio
import time
import os
try:
    import pywal
except:
    print('WARNING: pywal module not found, using wal command instead')

class WallWatcher(object):
    BASE_KEY = 'org.gnome.desktop.background'
    background = ''
    settings = Gio.Settings.new(BASE_KEY)
    changed = False
    
    def __init__(self):
        #settings = Gio.Settings.new(self.BASE_KEY)
        #self.settings.connect("changed::picture-uri", self.wallpaper_changed) # this doesn't seem to work???
        self.background = self.settings.get_string('picture-uri')
    
    def refresh(self):
        self.settings.sync()
        if self.settings.get_string('picture-uri') != self.background:
            self.background = self.settings.get_string('picture-uri')
            self.pywal_set_wallpaper(self.background)
    
    def pywal_set_wallpaper(self,image):
        filename = image.replace('file://', '')
        print('new wallaper: ', image)
        if 'pywall' in dir():
            # Set the wallpaper, add additional pywal stuff here
            pywal.wallpaper.change(image)
        else:
            try:
                os.system('wal -n -i "{}"'.format(filename))
            except:
                prinf('WARNING: error running command, is pywal installed?')

if __name__ == "__main__":
    ww = WallWatcher()
    while 1:
        ww.refresh()
        time.sleep(10)
