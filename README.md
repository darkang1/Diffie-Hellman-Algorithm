# Diffie-Hellman-Algorithm
Simple Python implementation of two-parties Diffie-Hellman algorithm.

## Functional description of the application
This application has **two different modes** for testing of algorithm.

First is the **manual mode** where the user manually inputs prime numbers for each
of two clients **public** and **private** keys with later possibility to encode and decode
input message with obtained **full** key.

Second mode is **automatic testing** where the user inputs the desired number of
tests to run and application automatically randomly generates prime numbers,
uses them as **public** and **private** keys of two clients and verifies if obtained **full**
key of first client matches **full** key of second client.

## Important Remarks

I want to clarify some important points regarding the implemented Diffie-Hellman algorithm. In the real world, much larger prime numbers would be used
(**1024-bit** and **2048-bit** numbers) in order to provide high security for generated keys.

By default, this application using prime numbers in range from 1 to 1000 for simplicity and less computation time during their generation. 

However, it is always possible to increase the desired range in the code of the program.
