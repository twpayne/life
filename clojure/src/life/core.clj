(ns life.core
  (:use quil.core)
  (:require [clojure.set :as set])
  (:require [clojure.string :as string]))


;; the game of life

(defn neighbors [[x y]]
  #{[(dec x) (dec y)] [(dec x) y] [(dec x) (inc y)]
    [     x  (dec y)]             [     x  (inc y)]
    [(inc x) (dec y)] [(inc x) y] [(inc x) (inc y)]})

(defn count-neighbors [world cell]
  (count (set/intersection (neighbors cell) world)))

(def rules #{[true 2] [true 3] [false 3]})

(defn live [world cell]
  (contains? rules [(contains? world cell) (count-neighbors world cell)]))

(defn evolve [world]
  (into #{} (filter #(live world %) (reduce set/union (map neighbors world)))))


;; pre-defined worlds

(def r-pentomino #{[0 0] [1 0] [-1 1] [0 1] [0 2]})

(def glider #{[1 0] [2 1] [0 2] [1 2] [2 2]})

(def blse #{[1 1] [1 2] [1 3] [1 5] [2 1] [3 4] [3 5] [4 2] [4 3] [4 5] [5 1] [5 3] [5 5]})


;; text-based animation

(defn dump [world]
  (string/join "\n"
    (map
      (fn [y] (string/join
                (map #(if (world [% y]) "X" ".")
                     (range 0 200))))
      (range 0 40))))

(defn animate [world]
  (println (dump world))
  (if (= (read-line) "")
    (animate (evolve world))
    world))


;; quil-based animation

(def world blse)

(defn setup []
  (smooth)
  (frame-rate 60))

(defn draw []
  (background 255)
  (stroke-weight 0)
  (fill 255)
  (doseq [[x y] world]
    (ellipse (+ (* 2 x) 512) (+ (* 2 y) 512) 3 3))
  (def world (evolve world)))

(defsketch life
  :setup setup
  :draw draw
  :size [1024 1024])
