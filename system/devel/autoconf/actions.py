#!/usr/bin/python
# Created for SolusOS

from pisi.actionsapi import pisitools, autotools,get

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=\%s" % get.installDIR())

    pisitools.dodoc("README", "BUGS", "ChangeLog*", "NEWS", "AUTHORS")
