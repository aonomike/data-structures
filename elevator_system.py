
# capacity = N
def elevator_system(capacity, number_on_gf, floors):
   
    # base conditions
    if capacity is None or number_on_gf is None or floors is None:
        return "error"
    if capacity <= 0 or number_on_gf <=0 or len(floors) == 0:
        return 0
    # sort the list n log n
    floors.sort() 
    duration = 0
    while number_on_gf > 0:
        current_pick = floors[capacity:]
        [floors.pop() for i in range(capacity)]
        duration += (current_pick[0] * 2)
    # max guys going to the top floor then remove them from list
    
    
    # recurse until list is empty
    

    time = elevator_system(capacity, number_on_gf - capacity, floors[:capacity], time)
    return time

elevator_system(2, 3, [2, 3, 4])
elevator_system(3, 3, [5, 5, 4])