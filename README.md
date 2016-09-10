# Canonical
This program takes an equation and returns it in canonical form.  
The equation is a string in the following form:

P1 + P2 + ... = ... + PN

where P1..PN - summands, which look like: 

ax^k

where a - floating point value;
k - integer value;
x - variable (each summand can have many variables).
 
For example:
x^2 + 3.5xy + y = y^2 - xy + y

Should be transformed into:
x^2 - y^2 + 4.5xy = 0

The program has two modes, file and input. In file mode, an input file with a list of equations is taken, and an output file
with those equations in canonical form is given back. In input mode the user can enter equations and those equations are returned
in canonical form. This ends when the user presses ctrl+c
