# Frishberg-Chess-Structure

Here's a [full description of this project](https://www.aronfrishberg.com/projects/chess-structure.html)

The basic idea behind this project was to create a set up of chess pieces that was an extremely self defensive "structure".

Defining a "protection" as a piece protecting another piece (ex. a board with a rook in the top right, and bottom left and a queen in the bottom right will have a total of 4 protections, as the queen will be protecting 2 pieces).  I also wanted each piece in the structure to be protecting at least 1 other piece.

This program was created to randomly generate boards and optimize for the number of "protections", as this would ultimately create a very "self defensive" structure of the white pieces where each piece was defending at least 1 other piece.

The final result is a board with 38 "protections", averaging 2.2 "protections" per piece.

I also rendered structures with 2 pieces, 3 pieces, ...
