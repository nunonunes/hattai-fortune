#!/bin/env python -tt
# -*- coding: utf-8 -*-

import sys
sys.path.append( '.' )
hattai = __import__( 'hattai-fortune' )
assert hattai

# String cleaning
assert hattai.clean_string( 'This is a perfectly harmless string.' ) \
                         == 'This is a perfectly harmless string.'
assert hattai.clean_string( '<i>This is wrong</i>' ) == 'This is wrong'
assert hattai.clean_string( 'This is also <b>wrong</b>' ) \
                         == 'This is also wrong'
assert hattai.clean_string( 'No “ allowed' ) == 'No " allowed'
assert hattai.clean_string( 'No ” allowed' ) == 'No " allowed'
