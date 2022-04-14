"""Тесты для модуля maze"""
import pytest
from pytest_mock import MockerFixture
from maze import Maze


@pytest.mark.parametrize(
    argnames=[
        "height",
        "width",
        "initial",  # your step in your algorithm
        "right_bottom",  # your step in your algorithm
        "way",
    ],
    argvalues=[
    [
        3,
        3,
        [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "1", "1", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
        ],
        [
            [
                ["0", "0", "0", "0", "0", "0", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "1", "1", "1", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"],
            ],
            [
                ["0", "0", "0", "0", "0", "0", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"],
            ],
            [
                ["0", "0", "0", "0", "0", "0", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "1", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"],
            ],
        ],
        [
            [1, 1],
            [2, 1],
            [3, 1],
            [4, 1],
            [5, 1],
            [5, 2],
            [5, 3],
            [5, 4],
            [5, 5],
        ],
    ],  # pylint: disable=too-many-arguments
    [
        1,
        1,
        [
            ["0", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "0"],
        ],
        [
            [
                ["0", "0", "0"],
                ["0", "1", "0"],
                ["0", "0", "0"],
            ],
        ],
        [
            [1, 1],
        ],  # pylint: disable=too-many-arguments
    ],
])
def test_maze(
    mocker: MockerFixture,
    height: int,
    width: int,
    initial: list,
    right_bottom: list,
    way: list,
) -> None:
    """Тест генерации и решения лабиринта."""
    mocker.patch(
        "maze.Maze.init_base_data",  # name function, which result we need faked
        side_effect=initial,
    )
    mocker.patch(
        "maze.Maze.build_right_walls",  # name function, which result we need faked
        side_effect=right_bottom,
    )
    mocker.patch(
        "maze.Maze.build_bottom_walls",  # name function, which result we need faked
        side_effect=right_bottom,
    )
    mocker.patch(
        "maze.Maze.check_walls", # name function, which result we need faked
        side_effect=right_bottom,
    )
    maze = Maze(height=height, width=width)  # your initial maze
    maze.solve_maze()
    assert all([right_bottom[-1] == maze.list_maze, way == maze.list_way])
