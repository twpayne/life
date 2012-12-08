package main

import "fmt"

type Cell struct {
	x, y int
}

type World map[Cell]int

func (c Cell) Neighbors() []Cell {
	return []Cell{
		Cell{c.x - 1, c.y - 1}, Cell{c.x, c.y - 1}, Cell{c.x + 1, c.y - 1},
		Cell{c.x - 1, c.y}, Cell{c.x + 1, c.y},
		Cell{c.x - 1, c.y + 1}, Cell{c.x, c.y + 1}, Cell{c.x + 1, c.y + 1},
	}
}

func (w *World) CountNeighbors(c Cell) int {
	count := 0
	for _, n := range c.Neighbors() {
		count += (*w)[n]
	}
	return count
}

func (w *World) Evolve() *World {
	next := make(World)
	for cell := range *w {
		if n := w.CountNeighbors(cell); n == 2 || n == 3 {
			next[cell] = 1
		}
		for _, neighbor := range cell.Neighbors() {
			if w.CountNeighbors(neighbor) == 3 {
				next[neighbor] = 1
			}
		}
	}
	return &next
}

func (w *World) String() string {
	result := ""
	for y := 0; y < 50; y++ {
		for x := 0; x < 200; x++ {
			if (*w)[Cell{x, y}] == 0 {
				result += "."
			} else {
				result += "X"
			}

		}
		result += "\n"
	}
	result += "\x1b[50A"
	return result
}

func NewR() *World {
	w := make(World)
	for _, c := range []Cell{
		Cell{25, 25},
		Cell{26, 25},
		Cell{24, 26},
		Cell{25, 26},
		Cell{25, 27},
	} {
		w[c] = 1
	}
	return &w
}

func (w *World) Animate() {
	for {
		fmt.Printf("%v", w)
		w = w.Evolve()
	}
}

func main() {
	NewR().Animate()
}
