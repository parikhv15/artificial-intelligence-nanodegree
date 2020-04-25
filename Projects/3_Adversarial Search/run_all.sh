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

echo "-DEFENSIVE TO OFFENSIVE STRATEGY------------------------------------"
echo "[HEURISTIC 4] Custom Player v/s MINIMAX"
python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 4

echo "[HEURISTIC 4] Custom Player v/s GREEDY"
python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 4

echo "[HEURISTIC 4] Custom Player v/s RANDOM"
python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 4

echo "[HEURISTIC 4] Custom Player v/s SELF"
python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 4

echo "-BLANK SPACES STRATEGY---------------------------------------------"
echo "[HEURISTIC 5] Custom Player v/s MINIMAX"
python run_match.py -r 20 -o MINIMAX -t 150 -p 4 -f -s 5

echo "[HEURISTIC 5] Custom Player v/s GREEDY"
python run_match.py -r 20 -o GREEDY -t 150 -p 4 -f -s 5

echo "[HEURISTIC 5] Custom Player v/s RANDOM"
python run_match.py -r 20 -o RANDOM -t 150 -p 4 -f -s 5

echo "[HEURISTIC 5] Custom Player v/s SELF"
python run_match.py -r 20 -o SELF -t 150 -p 4 -f -q 6 -s 5
