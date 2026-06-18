import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
bronx = 0
brooklyn = 0
manhattan = 0
queens = 0
staten_island = 0

noise = 0
heat = 0
rodent = 0
parking = 0 

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

for row in rows:
    if row['complaint_type'] == 'Noise - Residential':
        noise += 1
    elif row['complaint_type'] == 'HEAT/HOT WATER':
        heat += 1
    elif row['complaint_type'] == 'Rodent':
        rodent += 1
    elif row['complaint_type'] == 'Illegal Parking':
        parking += 1


for row in rows:
    if row['resolution_status'] == 'Open':
        open_requests += 1

borough_counts = {
    'Bronx': bronx,
    'Brooklyn': brooklyn,
    'Manhattan': manhattan,
    'Queens': queens,
    'Staten Island': staten_island
}

borough_open_counts = {
    'Bronx': 0, 'Brooklyn': 0, 'Manhattan': 0,
    'Queens': 0, 'Staten Island': 0
}

for row in rows:
    if row['resolution_status'] == 'Open':
        borough_open_counts[row['borough']] += 1

most_open = max(borough_open_counts, key=borough_open_counts.get)
open_count = borough_open_counts[most_open]

bronx_rate = round((bronx - borough_open_counts['Bronx']) / bronx * 100, 1)
brooklyn_rate = round((brooklyn - borough_open_counts['Brooklyn']) / brooklyn * 100, 1)
manhattan_rate = round((manhattan - borough_open_counts['Manhattan']) / manhattan * 100, 1)
queens_rate = round((queens - borough_open_counts['Queens']) / queens * 100, 1)
staten_rate = round((staten_island - borough_open_counts['Staten Island']) / staten_island * 100, 1)

complaint_count = {}

for row in rows: 
    complaint = row['complaint_type']
    if complaint in complaint_count:
        complaint_count[complaint] += 1
    else:
        complaint_count[complaint] = 1

most_common = max(complaint_count, key=complaint_count.get)
top_count = complaint_count[most_common]

sorted_complaints = sorted(complaint_count, key=complaint_count.get, reverse=True)
sorted_boroughs = sorted(borough_counts, key=borough_counts.get, reverse=True)
first, second, third = sorted_boroughs[0], sorted_boroughs[1], sorted_boroughs[2]
first_count = borough_counts[first]
second_count = borough_counts[second]
third_count = borough_counts[third]

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_requests}\n")
    f.write(f"\n")
    f.write(f"Most common complaint type: {most_common}: ({top_count} requests)\n")
    f.write(f"\n")
    f.write(f"Requests per borough:\n")
    f.write(f"- Bronx: {bronx}\n")
    f.write(f"- Brooklyn: {brooklyn}\n")
    f.write(f"- Manhattan: {manhattan}\n")
    f.write(f"- Queens: {queens}\n")
    f.write(f"- Staten Island: {staten_island}\n")
    f.write(f"\n")
    f.write(f"Requests by complaint type:\n")
    f.write(f"- Noise - Residential: {noise}\n")
    f.write(f"- HEAT/HOT WATER: {heat}\n")
    f.write(f"- Rodent: {rodent}\n")
    f.write(f"- Illegal Parking: {parking}\n")
    f.write(f"\n")
    f.write(f"Borough with most open requests: {most_open}: ({open_count} open)\n")
    f.write(f"\n")
    f.write(f"- Bronx: {bronx_rate}%\n")
    f.write(f"- Brooklyn: {brooklyn_rate}%\n")
    f.write(f"- Manhattan: {manhattan_rate}%\n")
    f.write(f"- Queens: {queens_rate}%\n")
    f.write(f"- Staten Island: {staten_rate}%\n")  
    f.write(f"\n")
    f.write(f"Top 3 boroughs by total requests\n")
    f.write(f"1. {first} ({first_count} requests)\n")
    f.write(f"2. {second}({second_count} requests)\n")
    f.write(f"3. {third}({third_count} requests)\n")

print("Output saved to output.txt")