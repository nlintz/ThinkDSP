import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers
import random

def harmonics(base_frequency=400):
	# cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)

	base_signal = thinkdsp.CosSignal(base_frequency, amp=1.0, offset=0)
	for i in xrange(2, 6):
		base_signal += thinkdsp.CosSignal(base_frequency * i, amp=1.0, offset=0)

	wave = base_signal.make_wave(duration=0.5, start=0, framerate=11025)
	spectrum = wave.make_spectrum()

	# helpers.makeWavFromSpectrum(spectrum, wave, 'exercise7.wav')
	helpers.plot(spectrum)

def nonHarmonicFrequencies(base_frequency=400):
	"""
	When you add non-harmonic frequencies, you make chords
	"""
	# cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)

	base_signal = thinkdsp.CosSignal(base_frequency, amp=1.0, offset=0)
	for i in xrange(2, 6):
		base_signal += thinkdsp.CosSignal(base_frequency * (i + random.random()), amp=1.0, offset=0)

	wave = base_signal.make_wave(duration=1, start=0, framerate=11025)
	spectrum = wave.make_spectrum()

	helpers.makeWavFromSpectrum(spectrum, wave, 'exercise7_with_nonHarmonics.wav')
	# helpers.plot(spectrum)

def writeMajorChord(rootFrequency, thirdFrequency, fifthFrequency):
	root = thinkdsp.CosSignal(rootFrequency, amp=1.0, offset=0)
	third = thinkdsp.CosSignal(thirdFrequency, amp=1.0, offset=0)
	fifth = thinkdsp.CosSignal(fifthFrequency, amp=1.0, offset=0)

	chord = root + third + fifth
	wave = chord.make_wave(duration=1, start=0, framerate=11025)
	spectrum = wave.make_spectrum()

	helpers.makeWavFromSpectrum(spectrum, wave, 'chord.wav')


def main():
	# harmonics()
	# nonHarmonicFrequencies()
	writeMajorChord(440, 523, 659)

if __name__ == "__main__":
	main()