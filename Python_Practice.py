counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

print()

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# numvotes:,.0f   the coma inserts thousands separators
for county,numvotes in counties_dict.items():
    print(f'{county} county has {numvotes:,.0f} voters')