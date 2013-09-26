import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers

def getSquareWaveSignal(freq, amplitude=1, offset=0):
	squareSignal= thinkdsp.SquareSignal(freq, amplitude, offset)
	return squareSignal

def main():
	spectrum = getSquareWaveSignal(1100).make_wave().make_spectrum()
	helpers.plot(spectrum)

if __name__ == "__main__":
	main()
