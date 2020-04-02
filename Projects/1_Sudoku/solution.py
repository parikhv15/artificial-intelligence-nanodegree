
from utils import *


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units

# Fetch list of left and right diagonal units
diagonal_units = [dot(rows, cols)] + [dot(rows, cols[::-1])]

unitlist = unitlist + diagonal_units


# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    The naked twins strategy says that if you have two or more unallocated boxes
    in a unit and there are only two digits that can go in those two boxes, then
    those two digits can be eliminated from the possible assignments of all other
    boxes in the same unit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).

    See Also
    --------
    Pseudocode for this algorithm on github:
    https://github.com/udacity/artificial-intelligence/blob/master/Projects/1_Sudoku/pseudocode.md
    """
    
    new_values = values.copy()
    for units in unitlist:
        # Build an inverted list of values.
        inverted_values = dict()
        for box in units:
            value = values[box]
            if len(value) == 2 and (value not in inverted_values or len(inverted_values[value]) == 1):
                inverted_values.setdefault(value, list()).append(box)

        # Create a list of unsolved boxes in that unit
        unit_values = [values[box] for box in units]
        unit_dict = dict(zip(units, unit_values))
        unsolved_boxes = [key for key in unit_dict.keys() if len(unit_dict[key]) > 1]

        for twin_value, twin_boxes in inverted_values.items():
            if len(twin_boxes) != 2: continue

            for unsolved_box in unsolved_boxes:
                if unsolved_box in twin_boxes: continue

                for digit in twin_value:
                    new_values[unsolved_box] = new_values[unsolved_box].replace(digit, '')

    return new_values


def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    solved_boxes = [box for box in values.keys() if len(values[box]) == 1]

    for box in solved_boxes:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')

    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """

    # Iterate through each unit and for each unit loop through each digit from 1 to 9
    # If this digit is present in only one box, then this is the only only_choice
    # We replace that box's value with the only choice value
    for unit in unitlist:
        digits = '123456789'
        for digit in digits:
            digit_containing_boxes = [box for box in unit if digit in values[box]]
            if len(digit_containing_boxes) == 1:
                values[digit_containing_boxes[0]] = digit

    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable
    """
    is_same = False

    while not is_same:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = only_choice(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

        is_same = solved_values_before == solved_values_after

        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values


def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """

    values = reduce_puzzle(values)

    if values is False:
        return False

    if all(len(values[b]) == 1 for b in boxes):
        return values

    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    for v in values[s]:
        new_values = values.copy()
        new_values[s] = v
        output = search(new_values)
        if output:
            return output
    # TODO: Copy your code from the classroom to complete this function
    return False


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
