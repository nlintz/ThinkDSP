import os, sys
lib_path = os.path.abspath('../lib/ThinkDSP/code/')
sys.path.append(lib_path)

import thinkdsp
import thinkplot
import matplotlib.pyplot as pyplot
import numpy
import helpers
import math
import random

PI2 = math.pi * 2

class DiscontinuousSignal(thinkdsp.Sinusoid):
    
    def evaluate(self, ts):

        cycles = self.freq * ts + self.offset / PI2
        frac, _ = numpy.modf(cycles)
        y = self.amp * numpy.sign(thinkdsp.unbias(frac))
        for i in range(len(y)-2):
            if y[i] == -1:
                y[i] = 0
        return y

class DiscontinuousSlopeSignal(thinkdsp.Sinusoid):
    
    def evaluate(self, ts):

        cycles = self.freq * ts + self.offset / PI2
        frac, _ = numpy.modf(cycles)
        y = self.amp * numpy.sign(thinkdsp.unbias(frac))
        for i in range(len(y)-2):
            if y[i] == -1:
                y[i] = 0
            else:
                y[i] = y[i]*random.random()
        return y

def main(duration=2, start=0, framerate=11025):
    discontinuousSignal = DiscontinuousSignal(freq=10, amp=1.0, offset=0)
    discontinuousWave = discontinuousSignal.make_wave(duration, start, framerate)
    discontinuousWave.write('discontinuous_signal.wav')

    discontinuousSlopeSignal = DiscontinuousSlopeSignal(freq=10, amp=1.0, offset=0)
    discontinuousSlopeWave = discontinuousSlopeSignal.make_wave(duration, start, framerate)
    discontinuousSlopeWave.write('discontinuous_slope_signal.wav')

if __name__ == "__main__":
    main()