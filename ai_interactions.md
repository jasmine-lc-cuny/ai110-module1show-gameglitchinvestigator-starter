# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I used three AI tools: Perplexity AI (Comet), GitHub Copilot, and Codex. I used Perplexity AI to help me navigate the setup steps, open the repo and Codespace, review the `app.py` code, and identify the first three bugs. I asked GitHub Copilot inside the Codespace to analyze the `check_guess` function and explain the hint direction bug. I then asked Codex to inspect the GitHub repo, compare the documentation against the actual code, finish the logic refactor, add stronger pytest coverage, verify the app, and push the completed changes.

**What did the agent do?**
Copilot read through the `check_guess` function and correctly identified that the hint messages were swapped - the `Too High` branch returned `Go HIGHER!` and the `Too Low` branch returned `Go LOWER!`, which is backwards. It also traced through the even-attempt string conversion issue where `secret = str(st.session_state.secret)` caused integer-to-string comparison failures, explaining that `42 != "42"` in Python. Codex later checked the repository state, found that `logic_utils.py` still contained placeholder `NotImplementedError` functions, completed the refactor, and expanded the pytest suite.

**What did you have to verify or fix manually?**
I had to manually compare the three difficulty range values (`Easy: 1-20`, `Normal: 1-100`, `Hard: 1-50`) to catch that Hard mode was actually easier than Normal mode. I also had to verify AI-generated documentation against the actual test output, because one saved version of `test_results.txt` showed that all tests were still failing before the final repair.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Guess exactly equals secret when secret is passed as a string | "Write a pytest test for check_guess where the guess equals the secret but secret is passed as a string instead of an integer" | `assert check_guess(42, "42")[0] == "Win"` | Yes | This verifies the fix converts inputs consistently before comparing them |
| Guess is higher than secret | "Write a test to check that when guess is greater than secret, the hint tells the player to go lower" | `assert check_guess(60, 42)[1] == "Go LOWER!"` | Yes | This proves the hint now tells the player the correct next direction |
| Hard difficulty range is harder than Normal | "Write a test that verifies get_range_for_difficulty returns a wider range for Hard than for Normal" | `assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]` | Yes | Hard mode now uses a wider range than Normal, making it meaningfully harder |
| Decimal input | "Add an edge-case test for decimal input in parse_guess" | `assert parse_guess("42.5")[0] is False` | Yes | The game now asks for whole-number guesses instead of silently truncating decimals |
| Wrong guesses and score | "Add a test that proves wrong guesses do not increase the score" | `assert update_score(0, "Too High", 1) == 0` | Yes | This prevents the previous score behavior where some wrong guesses added points |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**
```
Review this Python code for style issues, unused variables, and any PEP8 violations. Suggest improvements to make it cleaner and more Pythonic.
```

**Linting output before:**
```
W0611: Unused import (random imported but used only in one branch)
C0301: Line too long (83 > 79 characters) in check_guess function
R1705: Unnecessary elif after return in get_range_for_difficulty
W0612: Unused variable 'g' assigned but only used in one branch of except block
```

**Changes applied:**
Copilot suggested replacing the chained `if/elif` in `get_range_for_difficulty` with a dictionary lookup for cleaner code. It also suggested combining the `try/except` branches in `check_guess` into a single comparison using `int()` conversion upfront rather than catching `TypeError` after the fact. I reviewed both suggestions and agreed the dictionary approach was cleaner, but kept the try/except for now since changing it could introduce new bugs.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:** "Look at this Python function `check_guess(guess, secret)`. The hints are backwards - when guess is too high it says Go HIGHER, and when guess is too low it says Go LOWER. Explain why this is happening and suggest a fix."

| | Model A | Model B |
|---|---|---|
| **Model name** | GitHub Copilot (GPT-4o) | Perplexity AI - Comet |
| **Response summary** | Immediately identified that the return values in the `if guess > secret` and `else` branches were swapped. Provided a corrected version of the function with the messages switched and explained that `Too High` should tell the player to go lower, not higher. | Helped me move through the GitHub/Codespace workflow, review the source code, identify all 3 bugs at once (hints, string conversion, Hard difficulty range), and organize documentation notes. |
| **More Pythonic?** | Yes - suggested using a match/case statement (Python 3.10+) for cleaner branching | Did not suggest code changes - focused on bug identification and documentation |
| **Clearer explanation?** | Yes - concise before/after code block for the specific function | Yes - explained all bugs in plain English and documented them in a structured table format |

**Which did you prefer and why?**
I preferred Perplexity AI (Comet) overall for early setup and research because it helped me move through the GitHub and Codespace workflow, review code directly, identify multiple bugs at once, and organize documentation. GitHub Copilot was better for inline code suggestions and quick one-line fixes inside the editor. The ideal workflow is using both together: Perplexity AI for research, setup, and documentation, and GitHub Copilot for in-editor code completions and refactoring.
