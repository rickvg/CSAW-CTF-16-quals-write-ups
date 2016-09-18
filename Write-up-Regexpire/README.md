# Write-up Regexpire CSAW CTF 2016
In this section you will find the write-up of the Regexpire Misc challenge of CSAW CTF 2016 - 100 points.
This challenge requires you to connect to:

> nc misc.chal.csaw.io 8001

On the server, you will reach the Regexpire system, which works as follows:
* Multiple regular expressions are given;
* The response string must match the given regular expression, but may not contain newlines (\n);

I decided to solve this problem using an automated script, which can be found in this repository.

# Running the Python script
In order to run the Python script, it is required you use Python 2.7 due to some module incompatibilities in Python 3.x. The script can be started using the following command:

> python Regexpire.py

The script runs automatically, submitting all strings matching the regexes, and after ~1 minute, you will have the flag as result:
> flag{^regularly_express_yourself$}
