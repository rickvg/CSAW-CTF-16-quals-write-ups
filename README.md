# Write-up Coinslot CSAW CTF 2016
In this section you will find the write-up of the Coinslot Misc challenge of CSAW CTF 2016 - 25 points.
This challenge requires you to connect to:

> nc misc.chal.csaw.io 8000

On the server, you will reach the Coinslot system, which works as follows:
* Amount of money is shown that needs to be inserted into the Coinslot system;
* Next message is: $10,000 bills. This requires the user to calculate how many $10,000 bills fit in the amount of money described at step 1;
* After sending the first response with the number of $10,000 dollar bills fit in the amount of specified money, the second request from the server appears, asking the user the number of $5,000 dollar bills fitting in the amount of specified money. This continues for the money values of: $1,000, $500, $100, $50, $20, $10, $5, $1, 50c, 25c, 10c, 5c, 1c.

There are several rules while inputting a value into the system:
* No strings/other characters than positive or negative integers or the system crashes;
* The highest fitting value of money must be chosen first. If it is required multiple times and there is no higher fitting value available, it must be chosen multiple times before another coin/bill can be used.

I decided to solve this challenge by solving all problems issued by the Coinslot system using a script. It was predictable, a lot of problems would be given by the coinslot system. The Python script can be found in this repository and contains the required pieces of description of the code. It took 10 minutes to solve all problems using the Python script.

# Running the Python script
In order to run the Python script, it is required you use Python 2.7 due to some module incompatibilities in Python 3.x. The script can be started using the following command:

> python CoinSlot.py

The script runs automatically and after ~10 minutes, you will have the flag as result:
> flag{started-from-the-bottom-now-my-whole-team-fucking-here}
