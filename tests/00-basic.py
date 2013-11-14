#!/bin/env python -tt

import sys
sys.path.append( '.' )
hattai = __import__( 'hattai-fortune' )
assert hattai

assert hattai.initializeStuff() == None
assert hattai.getNewNews() == None
article_index = hattai.chooseArticle()
assert article_index != None
assert hattai.closeUpShop( article_index ) == None
