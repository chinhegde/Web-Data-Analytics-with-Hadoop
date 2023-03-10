# input.txt is the OUTPUT of REDUCER

count = dict()

with open("input.txt") as f:
    for line in f:
       (key, val) = line.split()
       count[key] = val

# GRAPH WITH ALL DATA POINTS

plt.rcParams["figure.figsize"] = (70,10)

names = list(count.keys())
values = list(count.values())

plt.bar(range(len(count)), values, tick_label=names)
plt.title("Number for conferences for each city",fontsize=28)
plt.xlabel("Cities",fontsize=24)
plt.ylabel("Number of conferences",fontsize=24)
plt.xticks(fontsize=12,rotation=90, ha='right')
plt.savefig('all_cities')
plt.show()

top10 = dict(sorted(count.items(), key=lambda item: item[1], reverse  = True)[:10])

plt.rcParams["figure.figsize"] = (30,10)

names = list(top10.keys())
values = list(top10.values())

plt.bar(range(len(top10)), values, tick_label=names)
plt.title("Top 10 Locations for conferences",fontsize=28)
plt.xticks(fontsize=14)
plt.xlabel("Cities",fontsize=24)
plt.ylabel("Number of conferences",fontsize=24)

plt.savefig('top10_cities')
plt.show()
