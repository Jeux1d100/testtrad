#!/usr/bin/env python
# -*- coding: utf-8 -*-

def trad_FR():
    # from lang_FR import *
    pass

def trad_EN():
    # from lang_EN import *
    pass

lang_file = "EN"
lang_filename = ("lang." + lang_file)

from lang_EN import *

Hello_World = lang["Hello_World"]
It_s_a_sentence = lang["It_s_a_sentence"]
To_be_translated = lang["To_be_translated"]

# Hello_World = "%(Hello_World)s" % lang
# It_s_a_sentence = "%(It_s_a_sentence)s" % lang
# To_be_translated = "%(To_be_translated)s" % lang