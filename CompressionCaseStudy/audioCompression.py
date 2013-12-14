import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import example4
import pickle
import matplotlib.pyplot as pyplot

class AudioCompressor():
	def __init__(self, inputFile=None):
		self._inputFile = inputFile
		self._wave = thinkdsp.read_wave(inputFile)

	def getInputFile(self):
		return self._inputFile

	def setInputFile(self, inputFile):
		self._inputFile = inputFile
		self._wave = thinkdsp.read_wave(inputFile)

	def getWave(self):
		return self._wave

	def setWave(self, wave):
		self._wave = wave

	def getSamples(self):
		return self._wave.ys

	#Converts wave object into an array of segmented wave objects
	def getWindowedSamples(self, windowSize):
		start = 0
		windowedSamples = [self._wave.segment(i*windowSize, windowSize) for i in xrange(int(self._wave.duration/windowSize))]
		return windowedSamples

	def getDctIV(self, windows):
		return [example4.dct_iv(window.ys) for window in windows]

	def thresholdDCT(self, windowedDCT, threshold):
		processedDCT = []

		for amplitude in windowedDCT:
			if amplitude < threshold:
				processedDCT.append(0)
			else:
				processedDCT.append(amplitude)

		return processedDCT

	def inverseDCT(self, amplitudes):
		return [type(example4.inverse_dct_iv(amplitude)) for amplitude in amplitudes]

	def writeToFile(self, amplitudes, outputFileName):
		pickle.dump( amplitudes, open( outputFileName, "wb" ) )

	def readFromFile(self, inputFileName):
		return cpickle.load( open( inputFileName, "rb" ))

	def combineWindowsToSample(self, windows):
		return [sample for sample in window for window in windows]

	def getCompressedSignal(self, windowSize, cutoffThreshold=0):
		windowedSamples = self.getWindowedSamples(windowSize)
		return self.getDctIV(windowedSamples)

if __name__ == "__main__":
	audioCompressor = AudioCompressor('samples/violin.wav')
	compressedSignal = audioCompressor.getCompressedSignal(.001)
	audioCompressor.writeToFile(compressedSignal, 'compressed.txt')


