"""
Game tasks for training reasoning capabilities:
- Board games
- Puzzle games
- Strategy games
- Simulation games
"""

from .countdown import CountdownConfig, CountdownDataset
from .emoji_mystery import EmojiMysteryConfig, EmojiMysteryDataset
from .game_of_life import GameOfLifeConfig, GameOfLifeDataset
from .knight_swap import KnightSwapConfig, KnightSwapDataset
from .maze import MazeConfig, MazeDataset
from .mini_sudoku import MiniSudokuConfig, MiniSudokuDataset
from .n_queens import NQueensDataset
from .sokoban import SokobanConfig, SokobanDataset
from .sudoku import SudokuConfig, SudokuDataset
from .tower_of_hanoi import HanoiConfig, HanoiDataset
from .tsumego import TsumegoConfig, TsumegoDataset

__all__ = [
    "CountdownConfig",
    "CountdownDataset",
    "EmojiMysteryConfig",
    "EmojiMysteryDataset",
    "MiniSudokuConfig",
    "MiniSudokuDataset",
    "SudokuConfig",
    "SudokuDataset",
    "SokobanConfig",
    "SokobanDataset",
    "MazeConfig",
    "MazeDataset",
    "GameOfLifeConfig",
    "GameOfLifeDataset",
    "HanoiConfig",
    "HanoiDataset",
    "NQueensDataset",
    "TsumegoConfig",
    "TsumegoDataset",
    "KnightSwapConfig",
    "KnightSwapDataset",
]
