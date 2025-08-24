# 🕹️ Game of Life – Python Console Version  

This is a console-based version of Conway's Game of Life in Python.  
The game simulates the evolution of cells on a grid according to simple rules:
- 🌱 Cells can live or die in each generation  
- 🔄 The board is toroidal (torus topology) – edges wrap around (cells on the edges have neighbors on the opposite side)  
- 🖥️ Display uses the console: `#` represents a live cell, `.` represents a dead cell  

---------------------------------------------------------------------

## ⚙️ Features

- 📐 Create a square grid of any size entered by user  
- 🎲 Randomly generate a specified number of living cells  
- ⏩ Simulate multiple generations with automatic display  
- 🖤 Simple console visualization  
- 🔄 Torus topology: edge cells interact with opposite edges  

---------------------------------------------------------------------

## 📜 Game Rules

1. ⚫ **Underpopulation:** A live cell with fewer than 2 neighbors dies  
2. ✅ **Survival:** A live cell with 2 or 3 neighbors survives  
3. 🌱 **Reproduction:** A dead cell with exactly 3 neighbors becomes alive  
4. 💀 **Overpopulation:** A live cell with more than 3 neighbors dies  

---------------------------------------------------------------------

## 🖥️ Example usage

What size board do you want to create? 5  
How many living cells do you want to create? 3  
How many life cycles do you want to see? 3  

Generation at the start:  
. . . . .  
. . . . .  
. # # # .  
. . . . .  
. . . . .  

Generation 1:  
. . . . .  
. . # . .  
. . # . .  
. . # . .  
. . . . .  

Generation 2:  
. . . . .  
. . . . .  
. # # # .  
. . . . .  
. . . . .  

Generation 3:  
. . . . .  
. . # . .  
. . # . .  
. . # . .  
. . . . .  
