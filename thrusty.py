# Attempting to write programs about rocket stuff.  For Python practice.
def thrust():
	print " "
	print "Let's calculate thrust at sea level!" #may remove sea level for more options
	print 'First, will we be using metric or "standard" units?' 
	units = raw_input("Enter 1 for metric, 2 for standard:  ").lower()
	print " "
# Providing responses
	if units == "1":
		weight = "kg"
		force = "kN"
		print "Yay for units that make sense!"
	elif units == "2":
		weight = "lbs"
		force = "lbf"
		print "Ok, if you insist..."
	else:
		print "You do understand how a keyboard works, right?"
		print " "
		thrust()
# Entering values
	print " "
	heavy = raw_input("Enter weight in %s :" % weight) 
	power = raw_input("Enter thrust in %s :" % force) 
	w = float(heavy)
	t = float(power)
	
	if units == "2":
		w = w * 0.45359237
		t = t * 0.004448
		
	gravity = 9.807
	
# Math
	wg = w * gravity
	tw = t / wg
	twr = tw * 1000
	print " "
	print "The thrust to weight ratio is %s" % format(twr, '.1f') 

	if twr >= 1: 
		print 'You "might" go to space today!'
		print " "
	else:
		print "You will not go to space today :("
		print " "
thrust()
# Code written by DMT.  Frackkin yay it works it works!  ^_^
