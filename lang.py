#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import importlib

def trad_FR():
    lang_file = "FR"
    from lang_FR import lang
    lang_filename = ("lang_" + lang_file)
    print("Test "+lang_file+" : "+lang["Hello_World"])

def trad_EN():
    lang_file = "EN"
    from lang_EN import lang
    lang_filename = ("lang_" + lang_file)
    print("Test "+lang_file+" : "+lang["Hello_World"])

from lang_EN import *

Hello_World = lang["Hello_World"]
It_s_a_sentence = lang["It_s_a_sentence"]
To_be_translated = lang["To_be_translated"]