""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Tommy Cheng (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tcheng99 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 903967530 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import random as rand  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
class QLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This is a Q learner object.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param num_states: The number of states to consider.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type num_states: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param num_actions: The number of actions available..  		  	   		 	   		  		  		    	 		 		   		 		  
    :type num_actions: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type alpha: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type gamma: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type rar: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type radr: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type dyna: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    def __init__(  		  	   		 	   		  		  		    	 		 		   		 		  
        self,  		  	   		 	   		  		  		    	 		 		   		 		  
        num_states=100,  		  	   		 	   		  		  		    	 		 		   		 		  
        num_actions=4,  		  	   		 	   		  		  		    	 		 		   		 		  
        alpha=0.2,  		  	   		 	   		  		  		    	 		 		   		 		  
        gamma=0.9,  		  	   		 	   		  		  		    	 		 		   		 		  
        rar=0.5,  		  	   		 	   		  		  		    	 		 		   		 		  
        radr=0.99,  		  	   		 	   		  		  		    	 		 		   		 		  
        dyna=0,  		  	   		 	   		  		  		    	 		 		   		 		  
        verbose=False,  		  	   		 	   		  		  		    	 		 		   		 		  
    ):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Constructor method  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        self.verbose = verbose  		  	   		 	   		  		  		    	 		 		   		 		  
        self.num_actions = num_actions  		  	   		 	   		  		  		    	 		 		   		 		  
        self.s = 0  		  	   		 	   		  		  		    	 		 		   		 		  
        self.a = 0

        self.num_states = num_states
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna

        self.prev_s = None
        self.prev_a = None
        self.q_table = np.zeros((self.num_states, self.num_actions))
        self.t_c = np.zeros((self.num_states, self.num_actions))
        self.r_table = np.zeros((self.num_states, self.num_actions))
        self.past_states = np.array([])
  		  	   		 	   		  		  		    	 		 		   		 		  
    def querysetstate(self, s):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Update the state without updating the Q-table  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param s: The new state  		  	   		 	   		  		  		    	 		 		   		 		  
        :type s: int  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        self.s = s
        self.prev_s = s

        '''
        Non random action
        '''
        max_index = np.argmax(self.q_table[s, :])
        action = self.q_table[s, max_index]
        action = int(max_index)






        '''
        Random action check
        '''
        rand_check = rand.random()

        if rand_check < self.rar:
            action = rand.randint(0, self.num_actions-1)
            self.rar = self.rar * self.radr



        self.prev_s = s
        self.prev_a = action
        self.past_states = np.append(self.past_states, s)
        # if self.verbose:
        #     print(f"s = {s}, a = {action}")

        return action  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    def query(self, s_prime, r):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Update the Q table and return an action  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param s_prime: The new state  		  	   		 	   		  		  		    	 		 		   		 		  
        :type s_prime: int  		  	   		 	   		  		  		    	 		 		   		 		  
        :param r: The immediate reward  		  	   		 	   		  		  		    	 		 		   		 		  
        :type r: float  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
        """

        '''
        Non random action
        Implementing update rule
        '''
        q_table = self.q_table
        prev_s = self.prev_s
        prev_a = self.prev_a
        alpha = self.alpha
        gamma = self.gamma

        piece1 = ((1 - alpha) * q_table[prev_s, prev_a])
        best_action_index = np.argmax(q_table[s_prime, :])
        action = int(best_action_index)  # NOTE:action is actually best action
        piece2 = alpha * (r + gamma * q_table[s_prime, action])
        q_table[prev_s, prev_a] = piece1 + piece2


        '''
        Attempt 1 - updating T_C and R
        '''
        # print('here')
        t_c = self.t_c
        r_table = self.r_table
        past_states = self.past_states
        np.append(past_states, s_prime) #or is it s?
        t_c[s_prime, best_action_index] += 1
        r_table[s_prime, best_action_index] = ((1-alpha) * r_table[prev_s, prev_a]) + (alpha * r)

        for i in range(10): #swap 10 to dyna later
            rand_previous_state = rand.choice(past_states)
            # print(rand_previous_state)
            rand_action = rand.randint(0, self.num_actions-1)
            rand_action = int(rand_action)
            rand_previous_state = int(rand_previous_state)

            t_c[rand_previous_state, rand_action] += 1

            r = r_table[rand_previous_state, rand_action]

            piece1 = ((1 - alpha) * q_table[rand_previous_state, rand_action])
            best_action_index = np.argmax(q_table[rand_previous_state, :])
            action = int(best_action_index)  # NOTE:action is actually best action
            piece2 = alpha * (r + gamma * q_table[rand_previous_state, action])
            q_table[rand_previous_state, rand_action] = piece1 + piece2

        '''
        Random action check
        '''
        rand_check = rand.random()

        if rand_check < self.rar:
            action = rand.randint(0, self.num_actions - 1)
            self.rar = self.rar * self.radr





        #output updates and misc
        # if self.verbose:
        #     print(f"s = {s_prime}, a = {action}, r={r}")
        self.prev_s = s_prime
        self.prev_a = action
        self.q_table = q_table
        self.t_c = t_c




        return action

    # def personal(self, s):
    #     # print(self.q_table)
    #     # arr = [[1,2,3,4]]
    #     arr = np.array([[5, 1,2,3,4], [1,2,3, 5,6]])
    #     val = np.argmax(arr[1])
    #     print(arr[int(1.0)])
    def author(self,):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "tcheng99"  # replace tb34 with your Georgia Tech username.


    def study_group(self,):
        return "tcheng99"

if __name__ == "__main__":
    print("Remember Q from Star Trek? Well, this isn't him")
    learner = QLearner(verbose = True)
    # learner.query(1, 1)
    # learner.personal(1)
    s = 1
    learner.query(1, .5)