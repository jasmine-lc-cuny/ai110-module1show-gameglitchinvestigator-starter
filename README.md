# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

The game asks the player to guess a hidden number within the range for the
selected difficulty. I found bugs where the high/low hints were backwards, a
correct guess could fail when the secret was converted to a string, Hard mode
used an easier range than Normal mode, and score changes were inconsistent. I
fixed the game by moving reusable logic into `logic_utils.py`, keeping guesses
and secrets as numbers, correcting the hint text, resetting state cleanly, and
adding pytest coverage for the repaired behavior.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty, and the app creates a secret number between 1 and 100.
2. User enters `40` when the secret is `50`, and the game returns `Too Low` with the hint `Go HIGHER!`.
3. User enters `60`, and the game returns `Too High` with the hint `Go LOWER!`.
4. User enters `50`, and the game returns `Correct!`, marks the game as won, and shows the final score.
5. User clicks New Game, and the app resets the secret, attempts, score, status, and guess history.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.1.0, pluggy-1.6.0
rootdir: D:\codex\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 7 items

tests\test_game_logic.py .......                                         [100%]

============================== 7 passed in 0.03s ==============================
```

## 🚀 Stretch Features

- [x] Added Challenge 1-style edge-case tests for string secrets, decimal input, Hard difficulty range, and score behavior.
