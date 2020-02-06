# Big_Data_and_Analytics


## --------------------------------------------------------
##   Lab1:   Mine Sweeper program
## --------------------------------------------------------
Input The first line contains two integers N and M, 1 ≤ N, M ≤ 1000,
corresponding to the the height and width of the map respectively.
The next N lines contain M space-separated characters.
Each character is either an x if this cell contains a mine,
or o to represent an empty cell.

Output The output consists of N lines of M space-separated characters. Each
character either encodes for the number of adjacent cells containing mines,
or the character ’x’ if the cell itself contains a mine.

## EX:
Sample Input 1:   
3 5                 
o x o x o              
o o o x x             
o o o o o  

Sample Output 1:  
1 x 3 x 3  
1 1 3 x x    
0 0 1 2 2 . 
