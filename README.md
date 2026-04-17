# Algorithm Visualizer

An interactive GUI application designed to visualize common sorting algorithms in real-time using **Python** and **Pygame**. This project is built to demonstrate understanding of data structures, algorithmic complexity, and GUI development principles.



## Features

* **Real-time Visualization**: Watch bars rearrange as algorithms execute.
* **Multiple Algorithms**: Switch between different sorting techniques instantly.
* **Performance Metrics**: Track the number of swaps and comparisons per algorithm.
* **Interactive Controls**: Restart or change algorithms without closing the application.

## Implemented Algorithms

| Algorithm | Key | Time Complexity (Avg) |
| :--- | :--- | :--- |
| **Insertion Sort** | `1` | $O(n^2)$ |
| **Bubble Sort** | `2` | $O(n^2)$ |
| **Selection Sort** | `3` | $O(n^2)$ |
| **Quicksort** | `4` | $O(n \log n)$ |

## How to Run

### Prerequisites
* Python 3.x
* Pygame library

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/HugoLennartsson/AlgorithmVisualizer.git
    cd AlgorithmVisualizer
    ```

2.  **Install Pygame**:
    ```bash
    pip install pygame
    ```

3.  **Run the application**:
    ```bash
    python main.py
    ```

## Controls

* **`1`**: Switch to Insertion Sort
* **`2`**: Switch to Bubble Sort
* **`3`**: Switch to Selection Sort
* **`4`**: Switch to Quicksort
* **`R`**: Restart current algorithm with new random data
