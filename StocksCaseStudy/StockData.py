from pandas.io.data import DataReader
from datetime import datetime

class StockData(object):
	def __init__(self, _ticker=None, _startDate=None, _endDate=None):
		self._ticker = _ticker
		self._startDate = _startDate
		self._endDate = _endDate
		self._dataSource = "yahoo"
		self._stockData = None

	def setTicker(self, ticker):
		self._ticker = ticker

	def setStartDate(self, startDate):
		self._startDate = startDate

	def setEndDate(self, endDate):
		self._endDate = endDate

	def getTicker(self):
		return self._ticker

	def getStartDate(self):
		return self._startDate

	def getEndDate(self):
		return self._endDate

	def getStockData(self, stockAttr=None):
		data = DataReader(self._ticker,  "yahoo", datetime(*self._startDate), datetime(*self._endDate))

		if (stockAttr):
			self._stockData = data[stockAttr]
			return data[stockAttr]

		else:
			self._stockData = data
			return data

