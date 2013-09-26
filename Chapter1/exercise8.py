import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers

def decibelToAmplitude(db):
	return 10**(db/1.0/20)

def frequencyToAttenuation(absorbtionRate, baseF, f):
	return absorbtionRate*(f/1.0/baseF)**2

def attenuationFactor(distance, absorbtionRate, baseF, f):
	"""
	Distance is in units of Km
	"""
	return decibelToAmplitude(frequencyToAttenuation(distance*absorbtionRate, baseF, f))

def getBaseFrequency(signal):
	spectrum = signal.make_spectrum()
	return spectrum.fs[1]

def underWaterSpectrum(signal, distance, absorbtionRate):
	spectrum = signal.make_spectrum()
	originalSpectrum = signal.make_spectrum()
	baseFrequency = getBaseFrequency(signal)
	index = 0;

	for freq in spectrum.fs:
		attenuation = attenuationFactor(distance, absorbtionRate, baseFrequency, freq)
		spectrum.amps[index] = spectrum.amps[index]/attenuation
		index += 1
	helpers.plot(spectrum)
	return spectrum

segment = helpers.getSegment(input_file='92002__jcveliz__violin-origional.wav')
signal = helpers.getSignal(input_file='92002__jcveliz__violin-origional.wav', duration=2)
spectrum = underWaterSpectrum(signal, 10, 1)
helpers.makeWavFromSpectrum(spectrum, segment, 'underwater.wav')
