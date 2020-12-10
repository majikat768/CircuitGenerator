let directions = [
  [1,0],[1,1],
  [0,1],[-1,1],
  [-1,0],[-1,-1],
  [0,-1],[1,-1]
]

let numRows = 20 
let numCols = 40
let cellSize = 20
let cells = []
let wires = []

let MaxLineLength = 80;
let numWires = 80;
let lineWidth = cellSize/4;
let W = numCols * cellSize;
let H = numRows * cellSize

let BOARD_COL = {'r':25, 'g':75, 'b':25}
let WIRE_COL = {'r':150, 'g':128, 'b':50}


for(let i = 0; i < numCols; i += 1) {
  for(let j = 0; j < numRows; j += 1) {
    cells.push(new cell(i,j));
  }
}

for(let i = 0; i < numWires; i += 1) {
  var w = new Wire(cells[Math.floor(Math.random() * cells.length)]);
  w.create_wire();
  wires.push(w);
}

function setup() {
  createCanvas(W,H);
  background(color(BOARD_COL['r'],BOARD_COL['g'],BOARD_COL['b']));
}

function draw() {
  background(color(BOARD_COL['r'],BOARD_COL['g'],BOARD_COL['b']));
  //draw_grid();
  fill(255);
  for(let i = 0; i < wires.length; i += 1) {
    wires[i].draw_wire();
    wires[i].draw_vias();
  }
}

function get_cell(x,y) {
  for(let i = 0; i < cells.length; i += 1) {
    if(cells[i].x == x && cells[i].y == y) {
      return cells[i];
    }
  }
}

function draw_grid() {
  for(let i = 0; i < numCols; i += 1) {
    line(i*cellSize,0,i*cellSize,numRows*cellSize);
    stroke(255,64);
  }

  for(let j = 0; j < numRows; j += 1) {
    line(0,j*cellSize,numCols*cellSize,j*cellSize);
    stroke(255,64);
  }
}

Number.prototype.mod = function(n) {
      return ((this%n)+n)%n;
};
