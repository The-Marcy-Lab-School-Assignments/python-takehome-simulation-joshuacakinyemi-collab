import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
residential_count = 0
bronx = 0
brooklyn = 0
manhattan = 0
queens = 0
staten_island = 0
complaint_count = 0
complaint = ''

for row in rows:
    if row['resolution_status'] == 'Open':
        open_requests += 1

for row in rows:
    if row['borough'] == 'Brooklyn':
        brooklyn += 1
    elif row['borough'] == 'Manhattan':
        manhattan += 1
    elif row['borough'] == 'Queens':
        queens += 1
    elif row['borough'] == 'Bronx':
        bronx += 1
    elif row['borough'] == 'Staten Island':
        staten_island += 1

complaint_count = {}

for row in rows: 
    complaint = row['complaint_type']
    if complaint in complaint_count:
        complaint_count[complaint] += 1
    else:
        complaint_count[complaint] = 1

most_common = max(complaint_count, key=complaint_count.get)
top_count = complaint_count[most_common]



with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_requests}\n")
    f.write(f" \n")

    f.write(f"Most common complaint type: {most_common}: ({top_count} requests)\n")
    f.write(f" \n")
    
    f.write(f"- Bronx: {bronx}:\n")
    f.write(f"- Brooklyn: {brooklyn}:\n")
    f.write(f"- Manhattan: {manhattan}:\n")
    f.write(f"- Queens: {queens}:\n")
    f.write(f"- Staten Island: {staten_island}:\n")


print("Output saved to output.txt")