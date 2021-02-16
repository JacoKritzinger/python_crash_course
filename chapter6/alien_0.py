alien_0 = {'color': 'green', 'points': 5}

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")




# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

alien_0 = {'color': 'green', 'points': 5}

	if alien_0['speed'] == 'slow':
		x_increment = 1
	elif alien_0['speed'] == 'medium':
		x_increment = 2
	else:
		# This must be a fast alien.
		x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")