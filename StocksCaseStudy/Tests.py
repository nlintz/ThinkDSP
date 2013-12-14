from StockData import StockData
from Presentation import *
from Synthesis import synthesize
import matplotlib.pyplot as pyplot
import numpy as np

"""
Test Getting Google Data
"""

def testGoogleData():
	framerate = 1
	s = StockData("GOOG", [2010, 1, 1], [2012, 1, 1])
	stockData = s.getStockData("Adj Close")

	fig = pyplot.figure()
	ax = fig.add_subplot(2,1,1)
	pyplot.title("Google Adjusted Close Data Over 2 Year")
	bx = fig.add_subplot(2,1,2)
	pyplot.title("Google Adjusted Close Spectrum 2 Year")
	# bx.set_xscale('log')
	bx.set_yscale('log')

	wave = synthesize(stockData, framerate)
	spectrum = wave.make_spectrum()

	# print np.polyfit(range(len(spectrum.hs)), abs(spectrum.hs), 1)
	ax.plot(wave.ys)
	bx.plot(abs(spectrum.hs))


	pyplot.show()

if __name__ == "__main__":
	testGoogleData()