from fleet import Fleet
from thing import Thing

fleet = Fleet()

get_milk = Thing('Get milk')
remove_obstacles = Thing('Remove obstacles')
stand_up = Thing('Stand up')
eat_lunch = Thing('Eat lunch')
stand_up.complete()
eat_lunch.complete()

fleet.add(get_milk)
fleet.add(remove_obstacles)
fleet.add(stand_up)
fleet.add(eat_lunch)

print(fleet)
