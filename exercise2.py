log = [1,0,1]

def calculate_best_run_time(log):
    optimHours = 0
    for i in range(len(log)):
        if log[i] == 1:
            optimHours += 1
    print(optimHours)

calculate_best_run_time(log)
