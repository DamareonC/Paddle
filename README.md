# Paddle

Paddle is a simple [Pong-like](https://en.wikipedia.org/wiki/Pong) game written in [Python](https://www.python.org/) using [Pygame](https://www.pygame.org/). In the game, you play against a CPU with the goal of hitting the ball past them to score. The first to get 5 points wins the game. You can move using the Up/Down arrow keys or the W/S keys.

## Prerequisites

To run Paddle, you need to install the latest versions of [Python](https://www.python.org/downloads/), [Pip](https://pip.pypa.io/en/stable/installation/)*, and [Git](https://git-scm.com/downloads).

*Pip should be installed if you installed Python from python.org

## Running Paddle

It is recommended to use a virtual environment to avoid multiple Python projects requiring different versions of the same package. If you, however, do not want to use a virtual environment, ignore steps 4 and 5.

To run Paddle:

1. Open a terminal (on Windows, either Command Prompt or PowerShell will work, though PowerShell may require the right [ExecutionPolicy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) to be set in order to run scripts, so Command Prompt is recommended)
2. Clone this repo with `git clone https://github.com/DamareonC/Paddle.git`
3. Go into the directory with `cd Paddle`
4. Create a virtual environment with `python -m venv venv`
5. Start the virtual environment with `.\venv\Scripts\activate` (Windows) or `. venv/bin/activate` (Mac/Linux)
6. Install the required dependencies with `pip install -r requirements.txt`*
7. Start Paddle with `python ./src/Main.py`

To turn off the virtual environment, run the `deactivate` command.

*The latest version of Pygame may need to be installed, which can be done with `pip install -U pygame` after installing Pygame (step 6).