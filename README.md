# DFA MINIMIZATION ALGORITHM

## Team
* Juan José Escobar Saldarriaga
* Samuel Llano Madrigal
* Class Code: 7308

## Development environment
* Operating System: Windows 11
* Programming Language: Python 3.12.2
* Tools: IDE's and editors such as Visual Studio Code and Replit

## Algorithm Description
* This program allows the user to enter one or several Deterministic Finite Automata (DFA) and apply a minimization algorithm to find the equivalent states. DFAs can be entered manually or read from a file.

## Explanation and Structure of the Minimization Algorithm
* There is a main menu with three options:
    1. Enter DFA manually 
    2. Read DFA from a file
    3. Exit the program

* With option '1', the function “read_dfa_from_file()” is called, where the complete name of the text file to be read is requested. This is opened and each line is checked for correct formatting. Then, all the DFA information is obtained in order and each of them is returned, represented as a tuple with the attributes “(num_states, alphabet, final_states, transitions)”. 
* For case '2', the function “leer_entrada()” is called, which acts similarly to the function mentioned above. The data of each DFA is requested in order and following the designated format. At the end, a list of the entered DFA is obtained with the structure: “(num_states, alphabet, final_states, transitions)”.
* And, for case '3', that simply exits the program and no result is saved.
* Then, we have the core of the algorithm, which is in charge of returning the equivalent data through the function “find_equivalent_states()”. To do this, a two-dimensional Boolean matrix is created, where the states are stored in pairs and initially assigned the value True (they are distinguishable) to those in which one state is final and the other is not. 
* Then, iterations are performed as long as there are changes in the table, and at each iteration, the pairs (i, j) not marked as distinguishable are checked. For each alphabet symbol, the states that i and j lead to are checked. If those target states were already marked as distinguishable, then i and j must be distinguishable as well. When this happens, the pair is marked as not equivalent and the variable changes = “True” is set.
* If in one iteration no new pair was marked as distinguishable, it means that no more changes are possible, at which point the changes variable is set to False and the loop terminates.
* At the end, this function extracts and returns those ordered pairs of states that are equivalent.

## Instructions for Running
1. Make sure you have a compatible version of Python installed (No need to download additional libraries).
2. Download the file “dfa_reader.py”.
3. If you want a file to be read by the code, download “dfa_file.txt” or create your own text file. Then, place it in the same address as the python script.
4. The file to be read or the manually entered data corresponding to the DFA must follow the following format:
   * A line with a number 𝑐 > 0 indicating how many cases you will receive.
   * For each case, in a single line a number 𝑛 > 0 denoting of states of 𝑀.
   * Then, a single line with the alphabet of 𝑀. Symbols are separated by blank spaces.
   * Then, the final states of 𝑀 separated by blank spaces.
   * Finally, 𝑛 lines, one for each state. Each line is a row of the table that represents 𝑀.
   
   Otherwise, an error message will be displayed.
5. Run the python file from the terminal or your IDE of choice.
