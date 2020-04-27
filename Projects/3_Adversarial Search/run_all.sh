#!/bin/bash

# echo "-DEFENSIVE STRATEGY------------------------------------------------"
# echo "[HEURISTIC 0] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 0
#
# echo "[HEURISTIC 0] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 0
#
# echo "[HEURISTIC 0] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 0
#
# echo "[HEURISTIC 0] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 0
#
# echo "-OFFENSIVE STRATEGY------------------------------------------------"
# echo "[HEURISTIC 1] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 1
#
# echo "[HEURISTIC 1] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 1
#
# echo "[HEURISTIC 1] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 1
#
# echo "[HEURISTIC 1] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 1
#
# echo "-MOVES TO BOARD STRATEGY-------------------------------------------"
# echo "[HEURISTIC 2] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 2
#
# echo "[HEURISTIC 2] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 2
#
# echo "[HEURISTIC 2] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 2
#
# echo "[HEURISTIC 2] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 2
#
# echo "-OFFENSIVE TO DEFENSIVE STRATEGY------------------------------------"
# echo "[HEURISTIC 3] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 3
#
# echo "[HEURISTIC 3] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 3
#
# echo "[HEURISTIC 3] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 3
#
# echo "[HEURISTIC 3] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 3
#
# echo "-DEFENSIVE TO OFFENSIVE STRATEGY------------------------------------"
# echo "[HEURISTIC 4] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 4
#
# echo "[HEURISTIC 4] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 4
#
# echo "[HEURISTIC 4] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 4
#
# echo "[HEURISTIC 4] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 4
#
# echo "-BLANK SPACES STRATEGY---------------------------------------------"
# echo "[HEURISTIC 5] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 5
#
# echo "[HEURISTIC 5] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 5
#
# echo "[HEURISTIC 5] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 5
#
# echo "[HEURISTIC 5] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 5
#
# echo "-BLANK SPACES STRATEGY---------------------------------------------"
# echo "[HEURISTIC 5] Custom Player v/s MINIMAX"
# python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 6
#
# echo "[HEURISTIC 5] Custom Player v/s GREEDY"
# python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 6
#
# echo "[HEURISTIC 5] Custom Player v/s RANDOM"
# python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 6
#
# echo "[HEURISTIC 5] Custom Player v/s SELF"
# python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 6

python run_match.py -o GREEDY -s 4 -t 50 -r 20
python run_match.py -o GREEDY -s 4 -t 100 -r 20
python run_match.py -o GREEDY -s 4 -t 150 -r 20
python run_match.py -o GREEDY -s 4 -t 200 -r 20
python run_match.py -o GREEDY -s 4 -t 250 -r 20
# python run_match.py -o MINIMAX -s 2 -t 300 -r 20
# python run_match.py -o MINIMAX -s 2 -t 120 -r 20
# python run_match.py -o MINIMAX -s 2 -t 140 -r 20
# python run_match.py -o MINIMAX -s 2 -t 160 -r 20
# python run_match.py -o MINIMAX -s 2 -t 180 -r 20
