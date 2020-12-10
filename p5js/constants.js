var directions = [
  [1,0],[1,1],
  [0,1],[-1,1],
  [-1,0],[-1,-1],
  [0,-1],[1,-1]
]

let numCols = 20
let numRows = 15
let cellSize = 20
let cells =[]

let MaxLineLength = 10;
let numWires = 4;
let W = numCols * cellSize;
let H =numRows * cellSize

let BOARD_COL = {'r':25, 'g':75, 'b':25}
let WIRE_COL = {'r':150, 'g':128, 'b':50}

