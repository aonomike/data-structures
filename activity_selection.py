activities = [[1,4],[3,5],[5,7],[6,20], [10, 11]]

def select_activity(activities):
    sorted_activities = sorted(activities, key = lambda x: x[1])
    initial_activity = sorted_activities[0]
    print(initial_activity)
    for activity in sorted_activities[1:]:
        if activity[0] > initial_activity[1]:
            initial_activity = activity
            print(initial_activity)


select_activity(activities)