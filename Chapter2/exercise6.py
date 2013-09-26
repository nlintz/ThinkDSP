import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers
import numpy as np

def getTriangleSignal(freq, amplitude=1, offset=0):
	triangleSignal = thinkdsp.TriangleSignal(freq, amplitude, offset)
	return triangleSignal

def getSampledTriangleWave(samplingRate=10000, freq=440):
	sampledTriangleWave = getTriangleSignal(freq).make_wave(framerate=samplingRate)
	return sampledTriangleWave

def appendWaves(waves):
	firstWave = waves[0]
	for i in range(1, len(waves)):
		firstWave.ys=np.append(firstWave.ys, waves[i].ys)
	return firstWave

def cSharpMajorArpeggio(samplingRate):
	frequencies = {'c':1108, 'e':1318, 'g':1661}
	c = getSampledTriangleWave(freq=frequencies['c'], samplingRate=samplingRate)
	e = getSampledTriangleWave(freq=frequencies['e'], samplingRate=samplingRate)
	g = getSampledTriangleWave(freq=frequencies['g'], samplingRate=samplingRate)
	c2 = getSampledTriangleWave(freq=frequencies['c']*2, samplingRate=samplingRate)
	return appendWaves([c, e, g, c2])

def main():
	aliasedArpeggio = cSharpMajorArpeggio(10000)
	unaliasedArpeggio = cSharpMajorArpeggio(11025)
	aliasedArpeggio.write('aliasedTriangleWave.wav')
	unaliasedArpeggio.write('unaliasedTriangleWave.wav')

if __name__ == "__main__":
	main()