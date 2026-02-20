import matplotlib.pyplot as plt


xs = []
ys = []

name = "Marvin"
gender = "M"
state = "CA"

with open("../Kursmaterialien/data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        
        line_splitted = line.strip().split(",")
        if (
            line_splitted[1] == name and 
            line_splitted[3] == gender and 
            line_splitted[4] == state
        ):
            xs.append(int(line_splitted[2]))     # Das Jahr auf der x-Achse.
            ys.append(int(line_splitted[5]))     # Die Anzahl auf der y-Achse.
        
            # print(line_splitted)
            # break
            
print(xs)
print(ys)

print(counter)

plt.plot(xs, ys)
plt.xlabel("Jahr")
plt.ylabel("Anzahl")
plt.title("Marvin's in Kalifornien 1910 - 2014")
plt.show()
