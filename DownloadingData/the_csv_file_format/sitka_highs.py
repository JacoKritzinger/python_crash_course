import csv
import matplotlib.pyplot as plt
from datetime import datetime
first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)



	# Get dates and high temperatures from this file.
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

	# Plot the high temperatures.
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c='red')
	# Format plot.
	plt.title("Daily high temperatures - 2018", fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	plt.show()

	print(highs)
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	