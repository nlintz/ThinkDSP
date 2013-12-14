import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
from StockData import StockData

def synthesize(ys, framerate):
	wave = thinkdsp.Wave(ys, framerate)
	return wave
