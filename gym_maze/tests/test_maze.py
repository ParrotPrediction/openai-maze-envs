import gym
import pytest

import gym_maze  # noqa: F401


class TestMaze:
    @pytest.mark.parametrize("_env_name, _goal", [
        ('Maze4-v0', (1, 6)),
        ('Maze5-v0', (1, 7)),
        ('Maze6-v0', (1, 7)),
        ('MazeF1-v0', (1, 2))
    ])
    def test_should_return_reward_state(self, _env_name, _goal):
        maze = gym.make(_env_name)
        assert maze.env.maze._goal == _goal

    @pytest.mark.parametrize("_env_name, _xy, _goal_state", [
        ('Maze4-v0', (1, 5), list('11110001')),
        ('Maze4-v0', (2, 5), list('11110001')),
        ('Maze4-v0', (2, 6), list('11110001')),
        ('Maze5-v0', (1, 6), list('11110101')),
        ('Maze5-v0', (2, 7), list('11110101')),
        ('MazeF1-v0', (1, 1), list('11111001'))
    ])
    def test_should_return_goal_state(self, _env_name, _xy, _goal_state):
        maze = gym.make(_env_name)
        maze.env.maze.insert_agent(_xy)

        assert maze.env.maze.get_goal_state() == _goal_state
