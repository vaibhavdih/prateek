from random import randint

def random_number_generator():
	a=""
	for i in range(4):
		a=a+str(randint(0,10))
	return "PM"+a

def member_id_generator(instance):
	Klass=instance.__class__
	while True:
		member_id = random_number_generator()
		if not Klass.objects.filter(member_id=member_id).exists():
			return member_id