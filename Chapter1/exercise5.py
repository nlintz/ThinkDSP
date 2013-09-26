"""
Add thinkdsp.py code to the python path so I can import it here
"""
import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import helpers

def periodic_signal_example(start=1.9, duration=4.8):
	filteredSignal = helpers.getSignal(start, duration, low_pass=100, high_pass=90, input_file="raw-epdf.wav")
	helpers.plot(filteredSignal)

def periodic_signal_spectrum(start=1.9, duration=4.8):
    spectrum = helpers.getSpectrum(start, duration, low_pass=100, high_pass=90, input_file="raw-epdf.wav")
    helpers.plot(spectrum)

def main():
    periodic_signal_example()
    periodic_signal_spectrum()


if __name__ == '__main__':
    main()


