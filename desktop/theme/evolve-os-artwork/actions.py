#!/usr/bin/python

from pisi.actionsapi import autotools, pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/themes", "../gtk/Vertex")
    pisitools.dosym("/usr/share/themes/Vertex", "/usr/share/themes/Evotex")
