import csv

filename = "positions.csv"

company_name = "UnitedHealth Group"
width = 150

print("<h1>{}</h1>".format(company_name))

rows = []
with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)

for row in rows:
	if row[2] == company_name:
		tags = row[4].split(',')
		tags = map(str.strip, tags) 
		is_board_member = "Board Member" in tags
		if is_board_member:
			print('<img src="{}" width={} alt="{}" />'.format(row[8], str(width), row[0]))