# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# encoding=utf8

import swampy.Gui as spy


def hello():
	"""
    It is a docstring.
	"""
	ca.text([0, 0], 'hello', 'blue')
gui = spy.Gui()
gui.row()
ca = gui.ca(bg='white')
print hello.__doc__
gui.col()
gui.bu(text='Hello', command=hello)
gui.bu(text='Quit', command=gui.quit)
gui.endcol()
gui.endrow()
gui.mainloop()
