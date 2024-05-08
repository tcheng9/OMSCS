def find_parameters_thrust(run_callback, tune='thrust', DEBUG=False, VISUALIZE=False):


    # Initialize a list to contain your gain values that you want to tune
    params = [0, 0, 0]

    # Create dicts to pass the parameters to run_callback
    thrust_params = {'tau_p': params[0], 'tau_d': params[1], 'tau_i': params[2]}

    # If tuning roll, then also initialize gain values for roll PID controller
    roll_params = {'tau_p': 0, 'tau_d': 0, 'tau_i': 0}

    # Call run_callback, passing in the dicts of thrust and roll gain values
    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
        thrust_params, roll_params, VISUALIZE=VISUALIZE)

    # Calculate best_error from above returned values
    best_error = None

    # Implement your code to use twiddle to tune the params and find the best_error
    '''
    I think you only have to start coding from ehre
    '''
    tolerance = 0.0001

    dparams = [1.0, 1.0, 1.0]

    # default setup for error

    hover_error, max_allowed_velocity, drone_max_velocity, max_allowed_oscillations, total_oscillations = run_callback(
        thrust_params, roll_params, VISUALIZE=VISUALIZE)
    best_error = hover_error

    # end of default setup for error
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