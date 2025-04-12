import subprocess
import sys
import unittest

class TestRunGameScript(unittest.TestCase):
    def test_game_declares_laura_as_winner(self):
        """Runs run_game.py and checks that 'Winners: laura' is printed at the end."""
        result = subprocess.run(
            [
                sys.executable,
                "run_game.py",
                "--players", "pedro:pacifist,laura:aggressive",
                "--ui-turn-delay", "0.1",
                "--width", "10",
                "--height", "10",
                "--no-ui"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Ensure script ran successfully
        self.assertEqual(result.returncode, 0, msg=f"Script failed with error:\n{result.stderr}")

        # Capture the last printed line and validate winner
        lines = result.stdout.strip().splitlines()
        last_line = lines[-1].strip() if lines else ""
        self.assertEqual(last_line, "Winners: laura", msg="Expected 'Winners: laura' at the end of output.")

if __name__ == "__main__":
    unittest.main()
