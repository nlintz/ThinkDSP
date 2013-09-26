import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot

import helpers

def sawToothSignal(freq=440, amp=1.0, offset=0, duration=2, start=0, framerate=11025):
	sawtooth = thinkdsp.SawtoothSignal(freq, amp, offset)
	return sawtooth

def getWave(signal, duration=2, start=0, framerate=11025):
	return signal.make_wave(duration, start, framerate)

def computeDFT(wave):
	return signal.make_spectrum()

def removeHarmonics(signal, i):
	"""
	returns the spectrum and the wave
	"""
	baseFrequency = signal.freq
	wave = getWave(signal)
	spectrum = wave.make_spectrum()
	index = 0
	for freq in spectrum.fs:
		if freq > baseFrequency*i:
			spectrum.amps[index] = 0
		index += 1
	return [spectrum, spectrum.make_wave()]

def main():
	frequency = 10
	for i in xrange(3):
		helpers.plot(removeHarmonics(sawToothSignal(freq=frequency), i)[1])
		helpers.plot(getWave(sawToothSignal(freq=frequency)))

if __name__ == "__main__":
	main()
