import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import numpy
import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot

PI2 = 3.14*2

def dct_iv(ys):
    N = len(ys)
    ts = (0.5 + numpy.arange(N)) / N
    freqs = (0.5 + numpy.arange(N)) / 2
    args = numpy.outer(ts, freqs)
    M = numpy.cos(PI2 * args)
    amps = numpy.dot(M, ys) / 2
    return amps

def inverse_dct_iv(amps):
    return dct_iv(amps) * 2

def testCase():
	cos_sig = thinkdsp.CosSignal(freq=2000, amp=1.0, offset=0)
	wave = cos_sig.make_wave(duration=.05, start=0, framerate=11025)
	dct = dct_iv(wave.ys)
	pyplot.plot(dct)
	# wave.plot()
	pyplot.show()

if __name__ == "__main__":
	testCase()