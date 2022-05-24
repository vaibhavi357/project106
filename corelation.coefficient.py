import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
	coffee_in_ml = []
	sleep_in_hours = []
	with open(data_path) as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			coffee_in_ml.append(float(row["Coffee in ml"]))
			sleep_in_hours.append(float(row["sleep in hours"]))
	return {"x":coffee_in_ml, "y":sleep_in_hours}

def findCorrelation(datasource):
	correlation = np.corrcoef(datasource["x"], datasource["y"])
	print("correlation between cups of coffee and hours of sleep is :", correlation[0,1])

def plotFigure(data_path):
	with open(data_path) as csv_file:
		df = csv.DictReader(csv_file)
		fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
		fig.show()

def setup():
	data_path = "./data/cups of coffee vs hours of sleep.csv"		
	datasource = getDataSource(data_path)
	findCorrelation(datasource)
	plotFigure(data_path)

setup()	
		