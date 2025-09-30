# takes an equation, a method, a set of initial values
# the step value, and the duration, then runs that method
# against the equation at that step value until the duration is reached.
def generate_points(f, method, init, step, duration):
    start = [*init, f(init)]  
    return reduce(
        lambda prev, s: prev + [method(f, prev[-1], s)], 
        (step for _ in range(int(duration / step))), 
        [start]
    )
    # In Haskell it would be    
    # iter = replicate (floor (duration / step)) step
    # foldl ((prev, s -> method f prev s) start iter

    # To do the same thing imperitavely:
    # result = [start]
    # for i in range(int(duration / step)):
    #     result = result + [method(f, result[-1], step)]
    # return result

# Increment each order by its order+1 from the previous step
# Except for the highest order which uses f(x, y,...)
def eulers_method(f, prev, step):
    start = [prev[0] + step] 

    for i in range(1, len(prev) - 1):
        start.append(prev[i] + step*prev[i + 1])
        
    # + list(map(
    #     lambda i: prev[i] + step*prev[i + 1],
    #     range(1, len(prev) - 1)
    # ))
    return start + [f(start)]

# Do the same thing as before, but calculate for the midpoint first
# and use that instead of just using the values from the previous iteration.
def second_order_runge_kutta(f, prev, step):
    half_euler = eulers_method(f, prev, step/2)
    start = [prev[0] + step] + list(map(
        lambda i: prev[i] + step*half_euler[i + 1],
        range(1, len(prev) - 1)
    ))
    return start + [f(start)]

# def fourth_order_runge_kutta(f, prev, step):
