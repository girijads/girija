rivers={'Ganga':'Haridwar','Yamuna':'Agra','Musi':'Hyderabad','Krishna':'Vijayawada'}
for river, city in rivers.items():
    print("The" + river.title() + "Runs Through " +
        city.title() + "." + "\n")
for river in rivers.keys(): 
	print(river.title()+"\n")

for city in rivers.values():
	print(city.title()+"\n")


