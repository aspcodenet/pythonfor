d = { "AA":1, "BB":2 }

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

if 2 in d.values():
    print("hoho")


# range - ni ska 
#           range mellan a och b
#           range mellanb b och a (baklänges)
#           step 2, -2

# skriv ut alla os-år (vart fjärde) mellan 1980 och 1992

class OS:
    def __init__(self,year, place):
        self.__year = year
        self.__place = place
    def GetYear(self):
        return self.__year
#        self.__swedishContenders = []

o  = OS(1968, "Mexico City")
o2  = OS(1988, "Calgary")
o3  = OS(1984, "Los Angeles")

lista = [o, o2, o3]         
# ta fram en ny lista med alla OS senare än 1980
newLista = []
for os in lista:
    if os.GetYear() > 1979:
        newLista[os]

# skriv ut alla årtal som det blev
for os in newLista:
    print(os.GetYear())



namn = "Stefan"
for x in namn:
    print(x)


for year in range(1992,1979,-4): 
    print(year)

year = 1992
while year > 1979:
    print(year)
    year = year - 4

year = 1992
while True:
    print(year)
    year = year - 4
    if year < 1980:
        break



for year in range(1979,1992,4): 
    print(year)

for year in range(1979,1992): 
    print(year)

for year in range(1992,1980,-1): 
    print(year)
