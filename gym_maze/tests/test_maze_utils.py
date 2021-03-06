import pytest
import numpy as np

from gym_maze.common.maze_utils import get_possible_insertion_coordinates, \
    get_reward_xy, adjacent_cell_values


class TestMazeUtils:

    @pytest.fixture
    def matrix(self):
        return np.asarray([
            [1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 9, 0, 1],
            [1, 1, 1, 1, 1],
        ])

    def test_should_get_insertion_coordinates(self, matrix):
        # when
        cords = get_possible_insertion_coordinates(matrix)

        # then
        assert len(cords) == 7
        assert sorted(cords) == \
               sorted(((1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 3)))

    def test_should_return_reward_xy(self, matrix):
        assert get_reward_xy(matrix) == (3, 2)

    @pytest.mark.parametrize('_cords, _p', [
        # Corners
        ((0, 0), (None, None, 1, 1, 1, None, None, None)),
        ((0, 4), (None, None, None, None, 1, 0, 1, None)),
        ((4, 0), (1, 0, 1, None, None, None, None, None)),
        ((4, 4), (1, None, None, None, None, None, 1, 0)),

        # Regular points
        ((1, 2), (1, 1, 0, 0, 0, 0, 1, 1)),
        ((3, 3), (0, 1, 1, 1, 1, 1, 9, 0)),
    ])
    def test_should_get_perception(self, _cords, _p, matrix):
        assert adjacent_cell_values(matrix, *_cords) == _p
