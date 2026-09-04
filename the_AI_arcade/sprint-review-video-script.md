# AI Arcade — Sprint Review Video Script (4:00)

**[0:00–0:10] Open**

I'm the lead AI engineer on RetroMind Studios' new project — bringing classic board games back to life with built-in AI opponents. Today: Mastermind and Peg Solitaire, both solved with classical AI, not neural networks. No guessing — math that's provably correct.

## [0:10–1:00] Part 1 — The Detective Alibi (Mastermind)

*[Show: heatmap animation]*

**Mastermind** is a classic code-breaking game where players guess a hidden 4-color sequence and receive Black/White peg feedback to refine their guesses. We chose this game because it is a well-defined logical puzzle, showcasing where classical AI exceeds simple guessing. Our AI demonstration shows a live attempt to uncover the secret code. Each circle represents a possible color in a specific slot, with brightness indicating how many hypotheses support that choice. As options are ruled out, they darken immediately.

After each guess, the AI checks all 1,296 possible codes against one question: if this were the correct answer, would it produce the same feedback? If not, that candidate is impossible and is eliminated. The pool of potential codes shrinks with each turn because we systematically eliminate options rather than just guessing at random. This method ensures the process doesn’t continue endlessly.


## [1:00–1:50] Part 2 — Rule-Based AI vs. LLMs

Why solve this with rule-based logic instead of an LLM? Because Mastermind is fully constrained — every rule is precise, every outcome deterministic. A modern LLM only approximates an answer; our Constraint Satisfaction approach proves one.

An LLM functions as a statistical pattern-matcher. If you request it to monitor 1,296 hypotheses over six turns, it may hallucinate — misremembering eliminated codes or confidently suggesting guesses that contradict earlier feedback — because it predicts probable text rather than following a strict algorithm. For games with strict, precise rules, rigid logic is more effective.


## [1:50–3:40] Part 3 — The Custom Heuristic (A*)

*[Show: both bar charts]*

Mastermind worked because feedback let us reason logically toward the answer. Peg Solitaire is different: jump pegs over each other until only one remains, with no feedback signal telling you if a move was 'right' — the only way to know if a sequence works is to search it out directly. That makes this a pure search problem, not a deduction problem, and it needs different tools.

Peg Solitaire presents a more challenging search problem. Blind BFS discovered a solution with 13 jumps but required exploring 3,012 states, keeping its entire frontier and visited set in memory—totaling over 5,700 states. DFS is less resource-intensive, examining only 490 states, but it relies on a fortunate branch without any certainty.

The A* algorithm utilizes an informed score, $f(n)=g(n)+h(n)$, combining actual costs and estimated remaining costs, prioritizing the expansion of the most promising state. My heuristic incorporates two additional penalties beyond the standard "pegs remaining" count: one for isolated pegs that cannot jump without neighboring pegs, and another for dispersion, which measures how dispersed the pegs are to encourage consolidation into a single peg. This approach reduces the search space to 57 states, representing a 98% decrease compared to BFS.

A key caveat: an *admissible* heuristic never overestimates the actual remaining cost, ensuring the optimal solution. My heuristic isn't admissible — it intentionally overestimates. Typically, this is risky. However, in this case, every winning solution must be exactly 13 jumps, no matter the path, so there's no risk of missing a shorter solution. This allows me to sacrifice that guarantee without penalty and instead focus on improving speed.

## [3:40–4:00] Close

Constraint Satisfaction for pure logical deduction, Informed Search for pure combinatorial search — two classical AI tools, each matched to the shape of its problem. Thanks."