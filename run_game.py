import sys
import os

# Add src/main to Python's module search path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'main'))

# Launch the game logic
from GameLogic.toe import main

if __name__ == "__main__":
    main()
