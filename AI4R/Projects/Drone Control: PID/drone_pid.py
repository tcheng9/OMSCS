######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################


def pid_thrust(target_elevation, drone_elevation, tau_p=0, tau_d=0, tau_i=0, data: dict() = {}):
    '''
    Student code for Thrust PID control. Drone's starting x, y position is (0, 0).
    
    Args:
    target_elevation: The target elevation that the drone has to achieve
    drone_elevation: The drone's elevation at the current time step
    tau_p: Proportional gain
    tau_i: Integral gain
    tau_d: Differential gain
    data: Dictionary that you can use to pass values across calls.
        Reserved keys:
            max_rpm_reached: (True|False) - Whether Drone has reached max RPM in both its rotors.
    
    Returns:
        Tuple of thrust, data
        thrust - The calculated change in thrust using PID controller
        data - A dictionary containing any values you want to pass to the next
            iteration of this function call. 
            Reserved keys:
                max_rpm_reached: (True|False) - Whether Drone has reached max RPM in both its rotors.
    '''

    thrust = 0
    #x,y = 0,0 #initial start point of drone  -> I think you pass this across iterations
    ####P controller
    '''
    QUESTION: cte = target_elevation - drone_elevation or is the calculation vice-versa
    ANSWER: I think it should be cte = target_elevation - drone_elevation because you do
    -tau_p * cte. So while you decrease CTE -> 0, -tau_p * cte causes you to provide an increase in output
    '''

    ###Implemented P
    cte_curr = target_elevation - drone_elevation
    P_controller = -tau_p * cte_curr #P controller

    ###Implemented D


    if 'cte_prev' in data.keys():
        cte_prev = data['cte_prev']
    else:
        cte_prev = 0.0

    derivative_cte = cte_curr - cte_prev

    data['cte_prev'] = cte_curr  #update CTE for T+1 derivative_CTE calcs
    D_controller = -tau_d * derivative_cte #D Controller

    '''
    NOTE: derivative_CTE can be: drone.y (current CTE?) - prev_cte (previous_CTE) 
    '''

    ##implemented I
    if 'integral_cte' in data.keys():
        integral_cte = data['integral_cte']
    else:
        integral_cte = 0.0
    #updating integral_Cte to include current T
    integral_cte += cte_curr
    #updating data dict
    data['integral_cte'] = integral_cte
    I_controller = -tau_i * integral_cte
    ##Full equaiton
    delta_thrust = P_controller + I_controller + D_controller


    #What do I return?
    #Return delta_thrust (PID controller value) at time T and data to persist
    '''
    Question: How did P, I, D controllers tell you what delta_thrust is?
    
    ANSWER:
        -it tells you how to:
            1. P - tells you how to adjust to get to 0 CTE  (oscillation)
            2. D - tells you how to adjust change in CTE to maintain 0 (reduce oscillations)
            2. I - tells you how to adjust for systamtic bias (removes systematic bias)
            
        -delta_thrust = is a combination value that achieves all 3? 
        
    Question: How can all 3 values into this one give you the solution?
    '''
    # print('thrust delta', delta_thrust)
    return delta_thrust, data


def pid_roll(target_x, drone_x, tau_p=0, tau_d=0, tau_i=0, data:dict() = {}):
    '''
    Student code for PD control for roll. Drone's starting x,y position is 0, 0.
    
    Args:
    target_x: The target horizontal displacement that the drone has to achieve
    drone_x: The drone's x position at this time step
    tau_p: Proportional gain, supplied by the test suite
    tau_i: Integral gain, supplied by the test suite
    tau_d: Differential gain, supplied by the test suite
    data: Dictionary that you can use to pass values across calls.
    
    Returns:
        Tuple of roll, data
        roll - The calculated change in roll using PID controller
        data - A dictionary containing any values you want to pass to the next
            iteration of this function call.

    '''
    roll = 0

    ##### Implement P controller
    cte_curr = target_x - drone_x
    P_controller = -tau_p * cte_curr

    #### Implement D controller
    if 'cte_prev' in data.keys():
        cte_prev = data['cte_prev']
    else:
        cte_prev = 0.0

    derivative_cte = cte_curr - cte_prev
    data['cte_prev'] = cte_curr
    D_controller = -tau_d * derivative_cte
    #### Implmeent I controller

    if 'integral_cte' in data.keys():
        integral_cte = data['integral_cte']
    else:
        integral_cte = 0.0

    integral_cte += cte_curr

    I_controller = -tau_i * integral_cte

    ##full equation
    delta_roll = P_controller + I_controller + D_controller

    # print('P controller:', P_controller)
    # print('I controller:', I_controller)
    # print('D controller:', D_controller)
    # print('---------')
    # print('roll delta', delta_roll)
    # print('---------')
    return delta_roll, data
    

def find_parameters_thrust(run_callback, tune='thrust', DEBUG=False, VISUALIZE=False): 
    '''
    Student implementation of twiddle algorithm will go here. Here you can focus on 
    tuning gain values for Thrust test cases only.
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''
    
    # Initialize a list to contain your gain values that you want to tune
    # params = [-10,-3,-0.0001]
    
    # Create dicts to pass the parameters to run_callback
    # thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    
    # If tuning roll, then also initialize gain values for roll PID controller
    # roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
    
    # Call run_callback, passing in the dicts of thrust and roll gain values
    # hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
    
    # Calculate best_error from above returned values
    best_error = None
    # Implement your code to use twiddle to tune the params and find the best_error


    '''
    Grid search default setup
    '''
    params = [0, 0, -0.0001]
    # grid_search_arr = [[-9.9, -3.01, -0.0001]]
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    roll_params = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
    tolerance = 0.001

    dparams = [1.0, 1.0, 1.0]

    # default setup for error

    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
        thrust_params, roll_params, VISUALIZE=VISUALIZE)
    best_error = hover_error
    #################      End of default setup       ##################
    # end of default setup for error

    grid_search_arr = [
        [-250, -200, -0.0001],
        [-300, -250, -0.0001],
        [-350, -250, -0.0001],
        [-400, -250, -0.0001],
        [-1000, -250, -0.0001],



    ]

    # grid_search_arr = [[-5, -100, -0.0001]]
    grid_search_arr = [[-5, -8.75, -0.0001]]
    best_params = []
    best_error = hover_error
    for j in range(len(grid_search_arr)):

        '''
                Reseting hover error
                '''

        params = [0, 0, -0.0001]
        # grid_search_arr = [[-9.9, -3.01, -0.0001]]
        thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
        roll_params = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
        tolerance = 0.0001


        # default setup for error

        hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
            thrust_params, roll_params, VISUALIZE=False)
        best_error = hover_error
        '''
        testing new set of params after reset
        '''
        params = grid_search_arr[j]
        print('start params', params)
        dparams = [1, 1, .5]




        # print('current set of params', grid_search_arr[j])
        while sum(dparams) > tolerance:

            for i in range(len(params)):
                params[i] += dparams[i]
                # Updating params -> slight deviation from lecture code
                # Testing the new Tau parameters and receiving the error
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                    thrust_params, roll_params, VISUALIZE=VISUALIZE)
                # print(max_allowed_velocity, 'ZZ', drone_max_velocity)

                ##if hover error is 0, just look at velocity
                if hover_error < 0.0001 and drone_max_velocity >= max_allowed_velocity:
                    dparams[i] -= 1.001
                    params[i] += dparams[i]

                if hover_error < best_error:
                    best_error = hover_error
                    dparams[i] *= 1.1
                else:
                    params[i] -= 2.0 * dparams[i]
                    # Testing the new Tau parameters and receiving the error
                    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                        thrust_params, roll_params, VISUALIZE=VISUALIZE)
                    if hover_error < best_error:
                        best_error = hover_error
                        dparams[i] *= 1.1
                    else:
                        params[i] += dparams[i]
                        dparams[i] *= .9
            # print('end params', params)

        # #Testign with the finalized twiddle -> best params of given grid_search[i]
        # print('end params', params)
        hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
            thrust_params, roll_params, VISUALIZE=False)
        # # print('final params for tuning_arr', i, '-----', params)
        # # print(hover_error)
        # # print('hover error', hover_error)
        # # print('max_velocity', drone_max_velocity)
        # # print('total oscillations', total_oscillations)
        print(hover_error,'|', drone_max_velocity,'|', total_oscillations)
        print(max_allowed_velocity, '@@', drone_max_velocity)
        # total_curr_error = hover_error +drone_max_velocity + total_oscillations
        #
        # print(total_curr_error)
        # print('--------------')
        # if hover_error < best_error:
        #     best_params = params
        #     thrust_params = params
        #     print('best params updated')





    # Return the dict of gain values that give the best error.
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    return thrust_params, roll_params

def find_parameters_with_int(run_callback, tune='thrust', DEBUG=False, VISUALIZE=False): 
    '''
    Student implementation of twiddle algorithm will go here. Here you can focus on 
    tuning gain values for Thrust test case with Integral error
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''
    
    # Initialize a list to contain your gain values that you want to tune, e.g.,
    params = [0,0,0]
    
    # Create dicts to pass the parameters to run_callback
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    
    # If tuning roll, then also initialize gain values for roll PID controller
    roll_params   = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}
    
    # Call run_callback, passing in the dicts of thrust and roll gain values
    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
    
    # Calculate best_error from above returned values
    best_error = None
    tolerance = 0.0001

    dparams = [1.0, 1.0, 1.0]

    # default setup for error

    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
        thrust_params, roll_params, VISUALIZE=VISUALIZE)
    best_error = hover_error
    #################      End of default setup       ##################
    # end of default setup for error

    ###code for twiddle
    while sum(dparams) > tolerance:
        for i in range(len(params)):
            params[i] += dparams[i]
            # Updating params -> slight deviation from lecture code
            # Testing the new Tau parameters and receiving the error
            thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
            hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                thrust_params, roll_params, VISUALIZE=VISUALIZE)

            if hover_error < best_error:
                best_error = hover_error
                dparams[i] *= 1.1
            else:
                params[i] -= 2.0 * dparams[i]
                # Testing the new Tau parameters and receiving the error
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                    thrust_params, roll_params, VISUALIZE=VISUALIZE)
                if hover_error < best_error:
                    best_error = hover_error
                    dparams[i] *= 1.1
                else:
                    params[i] += dparams[i]
                    dparams[i] *= 0.9


    # Return the dict of gain values that give the best error.
    
    return thrust_params, roll_params

def find_parameters_with_roll(run_callback, tune='both', DEBUG=False, VISUALIZE=False):
    '''
    Student implementation of twiddle algorithm will go here. Here you will 
    find gain values for Thrust as well as Roll PID controllers.
    
    Args:
    run_callback: A handle to DroneSimulator.run() method. You should call it with your
                PID gain values that you want to test with. It returns an error value that indicates 
                how well your PID gain values followed the specified path.
        
    tune: This will be passed by the test harness. 
            A value of 'thrust' means you only need to tune gain values for thrust. 
            A value of 'both' means you need to tune gain values for both thrust and roll.
    
    DEBUG: Whether or not to output debugging statements during twiddle runs
    VISUALIZE: Whether or not to output visualizations during twiddle runs
    
    Returns:
        tuple of the thrust_params, roll_params:
            thrust_params: A dict of gain values for the thrust PID controller
              thrust_params = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

            roll_params: A dict of gain values for the roll PID controller
              roll_params   = {'tau_p': 0.0, 'tau_d': 0.0, 'tau_i': 0.0}

    '''
    # Initialize a list to contain your gain values that you want to tune, e.g.,
    params = [0,0,0,0,0,0]
    
    # Create dicts to pass the parameters to run_callback
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
    
    # If tuning roll, then also initialize gain values for roll PID controller
    roll_params   = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
    
    # Call run_callback, passing in the dicts of thrust and roll gain values
    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(thrust_params, roll_params, VISUALIZE=VISUALIZE)
    
    # Calculate best_error from above returned values
    best_error = None
    dparams = [1, 1, 1, 1, 1, 1]

    tolerance = 0.000001



    # default setup for error

    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
        thrust_params, roll_params, VISUALIZE=VISUALIZE)
    best_error = hover_error
    # Implement your code to use twiddle to tune the params and find the best_error
    while sum(dparams) > tolerance:
        for i in range(len(params)):
            params[i] += dparams[i]
            # Updating params -> slight deviation from lecture code
            # Testing the new Tau parameters and receiving the error
            thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
            roll_params = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
            hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                thrust_params, roll_params, VISUALIZE=VISUALIZE)

            if hover_error < best_error:
                best_error = hover_error
                dparams[i] *= 1.1
            else:
                params[i] -= 2.0 * dparams[i]
                # Testing the new Tau parameters and receiving the error
                thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}
                roll_params = {'tau_p': params[3], 'tau_d': params[4], 'tau_i': params[5]}
                hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
                    thrust_params, roll_params, VISUALIZE=VISUALIZE)
                if hover_error < best_error:
                    best_error = hover_error
                    dparams[i] *= 1.1
                else:
                    params[i] += dparams[i]
                    dparams[i] *= 0.9
    # Return the dict of gain values that give the best error.

    return thrust_params, roll_params

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith123).
    whoami = 'tcheng99'
    return whoami
