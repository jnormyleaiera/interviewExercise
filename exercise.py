
log = [1,0,1,1,1,1,1]

num_hours = 4

def calculate_penalty(log, num_hours):
    penalty = 0
    daysDown = 0

    if len(log) > num_hours:
        daysDown = len(log) - num_hours
        
    for i in range(num_hours):
        if log[i] == 0:
            penalty += 1

    for j in range(daysDown):

        penalty +=1
            
           
    print(penalty)       

   

calculate_penalty(log, num_hours) 
    
