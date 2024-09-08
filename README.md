# Paddle

Paddle is a simple Pong-like game written in Python using Pygame. In the game, you play against an AI with the goal of hitting the ball past them to score. The first to get 5 points wins the game. You can move using the Up/Down arrow keys or the W/S keys.

## Requirements

To run Paddle, you need to install the latest versions of [Python](https://www.python.org/downloads/), *[Pip](https://pip.pypa.io/en/stable/installation/), and [Git](https://git-scm.com/downloads).

*Pip should be installed if you installed Python from python.org

## Running Paddle

To run Paddle:

1. Open a terminal (Command Prompt on Windows)
2. Clone this repo with `git clone https://github.com/DamareonC/paddle.git`
3. Go into the directory with `cd paddle`
4. Install the required dependencies with `pip install -r requirements.txt`
5. Start Paddle with `python ./src/Main.py`

## Running in a virtual environment

Alternatively, if you want to use a virtual environment, run these commands between steps 3 and 4 from above:

1. `python -m venv .venv` to create a virtual environment
2. `.\.venv\Scripts\activate` (Windows) or `source ./.venv/bin/activate` (Mac/Linux) to start the virtual environment

To turn off the virtual environment, run the `deactivate` command