from __future__ import print_function

import os
import time
from mojo.events import addObserver

class autoSaviour(object):
	def __init__ (self, interval=600):
		print('AutoSaviour will save all your open fonts every %i seconds automatically.' % interval)
		addObserver(self, "_checkTime", "currentGlyphChanged")
		self.timeLastSave = time.time()
		self.interval = interval

	def saveFonts (self):
		for font in AllFonts():
			ROOT_PATH = '/'.join(font.path.split('/')[:-1]) + '/'
			AUTOSAVE_PATH = '_autosave/'
			newDir = ROOT_PATH + AUTOSAVE_PATH

			if not os.path.exists(newDir):
				os.mkdir(newDir)
				print(f'{AUTOSAVE_PATH} is now a directory')
			else:
				print(f'{AUTOSAVE_PATH} is already a directory')
			
			fontName = font.path.split('/')[-1].split('.')[0]
			newName = font.path.replace(fontName, AUTOSAVE_PATH + fontName + '-autosaved')
			copyfont = font.copy()
			print('Autosaving font...', font)
			copyfont.save(newName)
			print(newName)

	def _checkTime (self, info):
		curtime = time.time()
		delta = curtime - self.timeLastSave
		if delta > self.interval:
			self.saveFonts()
			self.timeLastSave = time.time()


autoSaviour(600) # 10 min
# autoSaviour(300) # 5 min
