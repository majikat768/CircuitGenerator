Number.prototype.mod = function(n) {
      return ((this%n)+n)%n;
};

function Wire(start) {
  this.cells = [];
  this.start = start;
  this.start.open = false;
  this.cells.push(start);

  this.draw_vias = function() {
    strokeWeight(cellSize/6);
    stroke(WIRE_COL['r'],WIRE_COL['g'],WIRE_COL['b']);
    fill(0)
    start = this.cells[0];
    end = this.cells[this.cells.length-1];

    rad = cellSize/2;
    circle(
      start.x * cellSize + cellSize/2,
      start.y * cellSize + cellSize/2,
      rad);
    circle(
      end.x * cellSize + cellSize/2,
      end.y * cellSize + cellSize/2,
      rad);
  }

  this.find_open_direction = function() {
    let dirs = [...directions].sort(function(){return 0.5-Math.random();});

    for(let i = 0; i < dirs.length; i += 1) {
      let d = dirs[i];
      let c = get_cell(start.x + d[0], start.y + d[1]);
      if(c != null && c.open) {
        return d;
      }
    }
    return null;
  }

  this.current_direction = this.find_open_direction();

  this.create_wire = function() {
    while(this.cells.length < MaxLineLength) {
      let next_cell = this.find_next_cell();
      if(next_cell == null) {
        break;
      }
      this.cells.push(next_cell);
      next_cell.open = false;
    }
  }

  this.find_next_cell = function() {
    if(this.current_direction == undefined) return undefined;
    let current_cell = this.cells[this.cells.length-1];
    let possible_directions = [
      this.current_direction,
      directions[(directions.indexOf(this.current_direction) - 1).mod(directions.length)],
      directions[(directions.indexOf(this.current_direction) + 1).mod(directions.length)]
    ];

    if(Math.random() > 0.5) {
      possible_directions.sort(function(){return 0.5-Math.random();});
    }
    for(let i = 0; i < possible_directions.length; i += 1) {
      let d = possible_directions[i];
      let next_cell = get_cell(current_cell.x + d[0], current_cell.y + d[1]);
      if(next_cell != null && next_cell.open) {
        this.current_direction = d;
        return next_cell;
      }
    }
    return null;
  }

  this.draw_wire = function() {
    strokeWeight(lineWidth)
    stroke(WIRE_COL['r'],WIRE_COL['g'],WIRE_COL['b']);
    for(let i = 0; i < this.cells.length-1; i += 1) {
      let c1 = this.cells[i];
      let c2 = this.cells[i+1]
      line(c1.x*cellSize+cellSize/2,c1.y*cellSize+cellSize/2,c2.x*cellSize+cellSize/2,c2.y*cellSize+cellSize/2);
    }
  }
}

