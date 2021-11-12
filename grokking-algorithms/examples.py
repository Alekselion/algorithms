# stack
def greet(name):
	print(f"hello, {name}!")
	greet2(name)
	print("getting ready to say bye...")
	bye()


def greet2(name):
	print(f"how are you, {name}?")


def bye():
	print("ok, bye!")


# hash table
voted = {}


def sigIn(name):
	if voted.get(name) == True:
		print(f"{name}. Kick them out!")
	else:
		voted[name] = True
		print(f"{name}. Let them vote!")


if __name__ == "__main__":
	greet('Tom')

	print()
	
	names = ["Tom", "Mike", "Tim", "Mike", "Jhon"]
	for name in names:
		sigIn(name)