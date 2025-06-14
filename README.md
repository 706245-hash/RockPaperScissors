# Rock Paper Scissors Game

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

![ToDo CLI Screenshot](todopic.PNG) 

A colourful, terminal-based Rock Paper scissoirs game with statistics tracking and best-of-three mode.

### Features
- 🎨 Colorful ASCII art for each choice (rock, paper, scissors)
- 📊 Statistics tracking (wins, losses, ties, rounds played)
- 🏆 Best-of-three competitive mode
- 📝 Command-based interface with helpful prompts
- 🎮 Simple menu system for easy navigation

### How to Play
1. Run the game by executing game.py with Python 3
2. Follow the on-screen instructions:
    - Type rock, paper, or scissors to make your choice
    - Type stats to view current game statistics
    - Type best to enter best-of-three mode
    - Type quit to exit the game
  

### Game rules
- ✊ Rock crushes ✌️ Scissors
- ✌️ Scissors cut ✋ Paper
- ✋ Paper covers ✊ Rock

### Requirements
- Python 3.x
- `colorama` package (install with `pip install colorama`)


### Installation
1. Clone this repository or download the `game.py` file
2. Install dependencies:
   ```bash
   pip install colorama
   ```
3. Run the game:
   ```bash
   python game.py
   ```

### logic
```mermaid
flowchart TD
    A([Start]) --> B[Display Welcome Message]
    B --> C{Main Menu}
    C -->|1. Single Round| D[Play Round]
    C -->|2. Best of Three| E[Play Best of Three]
    C -->|3. Quit| F([End Game])
    
    D --> G[Get User Input]
    G -->|rock/paper/scissors| H[Computer Random Choice]
    G -->|stats| I[Display Statistics]
    G -->|quit| C
    I --> G
    H --> J[Determine Winner]
    J --> K[Update Scores]
    K --> L[Display Choices & Result]
    L --> C
    
    E --> M[Reset Scores for Best of 3]
    M --> N{Play Round}
    N -->|Continue| N
    N -->|Quit| O[Restore Original Scores]
    O --> C
    N -->|Max 2 wins or 5 rounds| P[Display Final Result]
    P --> Q[Display Statistics]
    Q --> O

```

Enjoy the game! For any issues or feature requests, please open up an issue on GitHub.


