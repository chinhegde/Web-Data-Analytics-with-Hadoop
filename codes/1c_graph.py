# input.txt is the OUTPUT of REDUCER

count = dict()

with open("input.txt") as f:
    for line in f:
       (key, val) = line.split()
       count[key] = val

# Separate plot for each city (all years)

for c, y in count.items():
    names = list(y.keys())
    values = list(y.values())

    plt.bar(range(len(y)), values, tick_label=names)
    plt.title(c,fontsize=14)
    plt.xlabel("Year",fontsize=12)
    plt.ylabel("Number of conferences",fontsize=12)
    plt.show()

# All cities in one graph

g_count = dict()

for c,years in count.items():
    for y, cnt in years.items():
        g_count[c+'_'+y] = int(cnt)

plt.rcParams["figure.figsize"] = (70,10)

names = list(g_count.keys())
values = list(g_count.values())

plt.plot(names, values)
plt.title("Number for conferences for each city",fontsize=32)
plt.xlabel("Cities and year",fontsize=24)
plt.ylabel("Number of conferences",fontsize=24)
plt.xticks(fontsize=10,rotation=90, ha='right')
plt.savefig('city_timeseries2')
plt.show()