# Notes

## Shell Outline
// Main menu
    // Select map
    // Create map
    // Exit

// Draw grid outline

// Read from file

// Game loop
    // Check neighbors
    // Update grid
    // Draw grid
        // Will need to add size to keep number of cells
    // Add buttons
        // Add text and color
        // Center map button
        // Add action listeners
    // Listen for mouse
        // Zoom in and out
        // Drag map
    // Thread.sleep();

## Representing 2D array of bits as single hexadecimal number
Let m be the map number. Coordinates (r, c) correspond to (y, x)

### 2x2
1 0  
0 1  
m = 1001_2 = 9_10 = 9_16
Bits = 4
Digits required = 1

### 3x3
1 1 1  
0 0 1  
1 0 1  
m = 111001101_2 = 461_10 = 1CD_16
Bits = 9
Nibbles = 3

### 4x4
1 0 0 1  
0 1 0 0  
1 0 1 1  
0 1 0 1  
m = 1001010010110101_2 = 38069_10 = 94B5_16
Bits = 9
Nibbles = 4

### nxn
1 ... 0  
. .   .  
.  .  .  
.   . .  
0 ... 1  
m = 1...0 = ..._10 = ..._16
Bits = n^2
Nibbles required: 