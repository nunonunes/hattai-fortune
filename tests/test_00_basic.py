#!/bin/env python -tt

import sys
sys.path.append( '.' )
hattai = __import__( 'hattai-fortune' )

def test_import():
    assert hattai

def test_initializeStuff():
    assert hattai.initializeStuff() == None

def test_getNewNews():
    assert hattai.getNewNews() == None

article_index = 0

def test_chooseArticle():
    global article_index
    article_index = hattai.chooseArticle()
    assert article_index != None

def test_closeUpShop():
    assert hattai.closeUpShop( article_index ) == None
