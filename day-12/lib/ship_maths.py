from typing import List


def process_move(position: List[int], compass_point: str, distance: int) -> List[int]:
    x, y = position

    if compass_point == 'N':
        y += distance
    elif compass_point == 'S':
        y -= distance
    elif compass_point == 'E':
        x += distance
    elif compass_point == 'W':
        x -= distance

    return [x, y]


def get_compass_point_for_heading(heading: str) -> str:
    if heading == 0:
        return 'N'
    elif heading == 90:
        return 'E'
    elif heading == 180:
        return 'S'
    elif heading == 270:
        return 'W'
    else:
        raise RuntimeError('Bad')
