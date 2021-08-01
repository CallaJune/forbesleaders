import csv

filename = "export.csv"

company_name = "Apple"
width = 150

print("<h1>{}</h1>".format(company_name))

rows = []
with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)

for row in rows:
	if row[1] == company_name:
		print('<img src="{}" width={} alt="{}" />'.format(row[6], str(width), row[0]))