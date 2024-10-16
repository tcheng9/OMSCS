""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt

  		  	   		 	   		  		  		    	 		 		   		 		  
def author():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return "tcheng99"  # replace tb34 with your Georgia Tech username.
  		  	   		 	   		  		  		    	 		 		   		 		  
def study_group():
    return "tcheng99"

def gtid():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return 903967530  # replace with your GT ID number
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	   		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    result = False  		  	   		 	   		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	   		  		  		    	 		 		   		 		  
        result = True  		  	   		 	   		  		  		    	 		 		   		 		  

    return result


def test_code():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	   		  		  		    	 		 		   		 		  
    """



    win_prob = 18/38  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once



    '''
    Experiment 1
    '''
    total_results = np.zeros((10, 1001))
    episode_winnings = 0
    count = 0


    for i in range(10):

        episode_winnings = 0
        bets = 0


        while episode_winnings < 80 and bets < 1000:
            won = False
            bet_amount = 1
            while not won:
                bets += 1
                won = get_spin_result(win_prob)
                if won == True:

                    episode_winnings += bet_amount
                else:
                    episode_winnings -= bet_amount
                    bet_amount *= 2
                total_results[i][bets] = episode_winnings

        ##forward fill algo
        for j in range(bets+1, 1000):
            total_results[i, j] = total_results[i, j-1]



    for i in range(0,10):
        plt.plot(total_results[i,:], label = 'line' + str(i))
    plt.legend()
    plt.title('Figure1')
    plt.xlabel('Bet number')
    plt.ylabel('Earnings')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    #
    plt.savefig('Figure1.png')
    plt.close()



    # '''
    # Figure 2 and 3
    # '''

    total_results = np.zeros((1000, 1001))
    mean_per_round = np.zeros((1, 1001))
    std_per_round_pos = np.zeros((1,1001))
    std_per_round_neg = np.zeros((1, 1001))
    mean_plus_std = np.zeros((1,1001))
    episode_winnings = 0
    count = 0

    for i in range(1000):

        episode_winnings = 0
        bets = 0

        while episode_winnings < 80 and bets < 1000:
            won = False
            bet_amount = 1
            while not won and bets < 1000:
                bets += 1
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings += bet_amount
                else:
                    episode_winnings -= bet_amount
                    bet_amount *= 2
                total_results[i][bets] = episode_winnings

    ##forward fill algo
        for j in range(bets + 1, 1001):
            total_results[i, j] = total_results[i, j - 1]



    '''
    Figure 2
    '''


    mean_per_round = np.mean(total_results, axis = 0)
    std_per_round = np.std(total_results, axis = 0)
    mean_std_per_round_pos = mean_per_round + std_per_round
    mean_std_per_round_neg = mean_per_round - std_per_round


    plt.plot(mean_per_round, label = "mean per iteration")
    plt.plot(mean_std_per_round_pos, label = "positive st. deviation")
    plt.plot(mean_std_per_round_neg, label = "negative st. deviation")
    plt.title('Figure2')
    plt.xlabel('Bet number')
    plt.ylabel('Earnings')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend()
    plt.savefig('Figure2.png')
    plt.close()
    #
    # '''
    # Figure 3
    # '''
    median_per_round = np.median(total_results, axis=0)
    std_per_round = np.std(total_results, axis=0)
    median_std_per_round_pos = median_per_round + std_per_round
    median_std_per_round_neg = median_per_round - std_per_round

    plt.plot(median_per_round, label="median per iteration")
    plt.plot(median_std_per_round_pos, label="positive st. deviation")
    plt.plot(median_std_per_round_neg, label="negative st. deviation")

    plt.title('Figure3')
    plt.legend()
    plt.xlabel('Bet number')
    plt.ylabel('Earnings')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.savefig('Figure3.png')
    plt.close()



    '''
    Experiment 2
    '''
    total_results = np.zeros((1000, 1001))

    mean_per_round = np.zeros((1, 1001))

    std_per_round_pos = np.zeros((1, 1001))
    std_per_round_neg = np.zeros((1, 1001))
    episode_winnings = 0
    count = 0
    bankroll = 256


    for i in range(1000):

        episode_winnings = 0
        bets = 0


        while episode_winnings < 80 and episode_winnings > -256 and bets < 1000:
            won = False
            bet_amount = 1
            while not won:
                bets += 1

                won = get_spin_result(win_prob)
                if won == True:

                    episode_winnings += bet_amount
                    bankroll += bet_amount
                else:
                    #you lost so now double your bet amount, unless bet_amount is greater than money u have
                    episode_winnings -= bet_amount
                    bet_amount *= 2

                    if episode_winnings + 256 < bet_amount:
                        bet_amount = episode_winnings+256
                total_results[i][bets] = episode_winnings
            ##forward fill algo
            for j in range(bets + 1, 1001):
                total_results[i, j] = total_results[i, j - 1]



    '''
    Figure 4
    '''

    mean_per_round = np.mean(total_results, axis = 0)

    std_per_round = np.std(total_results, axis = 0)
    mean_std_per_round_pos = mean_per_round + std_per_round
    mean_std_per_round_neg = mean_per_round - std_per_round

    plt.title('Figure 4')
    plt.plot(mean_per_round, label = 'mean')
    plt.plot(mean_std_per_round_pos, label = "positive st. deviation")
    plt.plot(mean_std_per_round_neg, label = "negative standard deviation")
    plt.legend()
    plt.xlabel('Bet number')
    plt.ylabel('Earnings')
    plt.xlim(0, 1000)
    plt.ylim(-256, 100)
    plt.savefig('Figure4.png')
    plt.close()



    '''
    Figure 5
    '''
    median_per_round = np.median(total_results, axis=0)
    std_per_round = np.std(total_results, axis=0)
    median_std_per_round_pos = median_per_round + std_per_round
    median_std_per_round_neg = median_per_round - std_per_round


    # plt.figure('figure 5')
    plt.plot(median_per_round, label = 'median')
    plt.plot(median_std_per_round_pos, label = 'positive st. deviation')
    plt.plot(median_std_per_round_neg, label = 'negative st. deviation')
    plt.title('Figure 5')
    plt.xlabel('Bet number')
    plt.ylabel('Earnings')
    plt.legend()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.savefig('Figure5.png')
    plt.close()






  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	   		  		  		    	 		 		   		 		  
