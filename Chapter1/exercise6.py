import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers

def constantFrequencyExample(start=1.9, duration=.5):
	filteredSignal = helpers.getSignal(start, duration, low_pass=100, high_pass=90, input_file="raw-epdf.wav")
	spectrum = helpers.getSpectrum(start, duration, low_pass=100, high_pass=90, input_file="raw-epdf.wav")
	
	segment = helpers.getSegment(start, duration, input_file="raw-epdf.wav")
	helpers.makeWavFromSpectrum(spectrum, segment, outputFile="recoveredWav.wav")
	# firstPeak = min([i[0] for i in spectrum.peaks()])
	helpers.plot(spectrum)

def main():
	constantFrequencyExample()

if __name__ == "__main__":
	main()
