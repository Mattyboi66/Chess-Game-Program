from stockfish import Stockfish

class stockfish():
    
    stockfish = Stockfish(path=r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\stockfish.exe")
    
    def __init__(self) -> None:
        pass
        {
            "Debug Log File": "",
            "Contempt": 0,
            "Min Split Depth": 0,
            "Threads": 1, # More threads will make the engine stronger, but should be kept at less than the number of logical processors on your computer.
            "Ponder": "false",
            "Hash": 16, # Default size is 16 MB. It's recommended that you increase this value, but keep it as some power of 2. E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
            "MultiPV": 1,
            "Skill Level": 20,
            "Move Overhead": 10,
            "Minimum Thinking Time": 20,
            "Slow Mover": 100,
            "UCI_Chess960": "false",
            "UCI_LimitStrength": "false",
            "UCI_Elo": 1350
        }
    


