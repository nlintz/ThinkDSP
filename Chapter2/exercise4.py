import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import numpy
import helpers

def frequencyLimit(wave, highPassFrequency, lowPassFrequency):
	spectrum = wave.make_spectrum()
	for i in range(len(spectrum.fs)):
		if spectrum.fs[i] > lowPassFrequency:
			spectrum.amps[i] = 0
			spectrum.hs[i] = 0
		if spectrum.fs[i] < highPassFrequency:
			spectrum.amps[i] = 0
			spectrum.hs[i] = 0
	return [spectrum, spectrum.make_wave()]

def main(freq=440, amp=1, offset=0):
	sawToothSignal = thinkdsp.SawtoothSignal(freq, amp, offset)

	spectrum, wave = frequencyLimit(sawToothSignal.make_wave(), 400, 4000)
	wave.write('frequencyLimitedSawTooth.wav')
	
	sawToothSignal.make_wave().write('sawTooth.wav')

if __name__ == "__main__":
	main()