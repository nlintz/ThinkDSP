import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot

def plot(signal):
	signal.plot()
	pyplot.show()

def getSegment(start=0, duration=1, input_file="raw-epdf.wav"):
	wave = thinkdsp.read_wave(input_file)
	segment = wave.segment(start, duration)
	return segment

def getSignal(start=0, duration=1, input_file="raw-epdf.wav", low_pass=22000, high_pass=20):
	# read the recording
	wave = thinkdsp.read_wave(input_file)

	segment = wave.segment(start, duration)
	spectrum = segment.make_spectrum()

	spectrum.low_pass(low_pass)
	spectrum.high_pass(high_pass)

	# invert the spectrum
	filtered = spectrum.make_wave()

	# prepare the original and filtered segments
	filtered.normalize()
	filtered.apodize()
	# segment.apodize()

	return filtered

def getSpectrum(start=0, duration=1, input_file="raw-epdf.wav", low_pass=22000, high_pass=20):
	# read the recording
	wave = thinkdsp.read_wave(input_file)

	segment = wave.segment(start, duration)
	spectrum = segment.make_spectrum()

	spectrum.low_pass(low_pass)
	spectrum.high_pass(high_pass)

	return spectrum

def makeWavFromSpectrum(spectrum, segment, outputFile="wave.wav"):
	filtered = spectrum.make_wave()

	# prepare the original and filtered segments
	filtered.normalize()
	filtered.apodize()

	wfile = thinkdsp.WavFileWriter(outputFile, segment.framerate)
	wfile.write(segment)
	wfile.write(filtered)
	wfile.close()

def violinSignal(start=1.2, duration=0.6):
    """Demonstrates methods in the thinkdsp module.
    """
    # read the violin recording
    wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')

    # extract a segment
    segment = wave.segment(start, duration)

    # make the spectrum
    spectrum = segment.make_spectrum()

    # apply a filter
    spectrum.low_pass(600)

    # invert the spectrum
    filtered = spectrum.make_wave()

    # prepare the original and filtered segments
    filtered.normalize()
    filtered.apodize()

    return filtered

