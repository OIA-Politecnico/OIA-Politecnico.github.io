import csv

# Este script construye la tabla en markdown a partir de un csv (data.csv) con
# las participaciones de todos los alumnos.
#
# Los campos del csv son (año, nivel, puesto, observaciones, nombre, apellido)
# Actualmente, observaciones puede ser '' o 'empate'
#
# Por ejemplo esta fila representa que Martín Villagra obtuvo el puesto 1 de
# nivel 2 en 2011:
#    2011,2,1,,Martín,Villagra

class Person:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.medals = {"gold": 0, "silver": 0, "bronze": 0}
		self.participations = []

	def add_participation(self, year, level, rank, tie):
		self.participations.append((year, level, rank, tie))
		if 1 <= rank <= 3:
			medals = ["gold", "silver", "bronze"]
			medal = medals[rank-1]
			if medal not in self.medals:
				self.medals[medal] = 0
			self.medals[medal] += 1

	def show(self):
		return (
			'| '
			f'{self.name} {self.surname}'
			' | '
			f'{len(self.participations)}'
			' | '
			f'{self.medals["gold"]}'
			' | '
			f'{self.medals["silver"]}'
			' | '
			f'{self.medals["bronze"]}'
			' |'
		)

	def sort_key(self):
		gold = self.medals["gold"]
		silver = self.medals["silver"]
		bronze = self.medals["bronze"]
		participations = len(self.participations)
		fullname = f'{self.name} {self.surname}'
		return (-gold, -silver, -bronze, -participations, fullname)

with open('data.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	data = list(reader)

people = {}

for year, level, rank, obs, name, surname in data[1:]:
	if obs == 'no data':
		continue

	key = (name, surname)

	if key not in people:
		people[key] = Person(name, surname)

	people[key].add_participation(int(year), int(level), int(rank), obs == 'empate')

ranking = list(people.values())

ranking.sort(key=lambda p: p.sort_key())

print("# Salón de la fama")
print("")
fields = ["Competidor", "Participaciones", "Oro", "Plata", "Bronce"]
print("| ", " | ".join(fields), " |");
separator = map(lambda _: "---", fields)
print("| ", " | ".join(separator), " |");

for p in ranking:
	print(p.show())
