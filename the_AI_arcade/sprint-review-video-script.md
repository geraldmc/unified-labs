# AI Arcade — Sprint Review Video Script (~4:20)

**[0:00–0:15] Open**

I'm the lead AI engineer on RetroMind Studios' new project — bringing classic board games back to life with built-in AI. Today it's Mastermind and Peg Solitaire, both solved with classical AI.

## [0:15–1:20] Part 1 — The Detective Alibi (Mastermind)

**Mastermind** is a classic code-breaking game where players guess a hidden 4-color sequence and receive Black/White peg feedback to refine their guesses. We chose this game because it's a perfectly constrained logical puzzle. Our AI demonstration shows a live attempt to uncover the secret code. 

*[Show: heatmap animation]*

Each circle represents a possible color in a specific slot, with brightness indicating how many hypotheses support that choice. As options are ruled out, the circle color darkens.

After each guess, the AI checks all 1,296 possible codes against a question: if this were the correct answer, would it produce the same feedback? If not, that candidate is impossible and is eliminated. The potential pool shrinks with each turn because we systematically eliminate options rather than just guessing. This method ensures the process terminates.


## [1:20–1:55] Part 2 — Rule-Based AI vs. LLMs

Why solve this with rule-based logic instead of an LLM? Because Mastermind is fully constrained — every rule is precise, every outcome deterministic. An LLM functions as a statistical pattern-matcher. If you request it to monitor 1,296 hypotheses over six turns, it may hallucinate — misremembering eliminated codes or confidently suggesting guesses that contradict earlier feedback — because it predicts probable text rather than following a strict algorithm. For games with strict, precise rules, rigid logic is more effective.


## [1:55–4:15] Part 3 — The Custom Heuristic (A*)

Mastermind worked because feedback let us reason logically toward the answer. Peg Solitaire is different: pegs jump over each other until only one remains, with no feedback to say which move was 'right' — the only way to know if a sequence works is to seek it out. That makes this a pure search problem, not a deduction problem, and it needs different tools.

*[Show: nodes-expanded chart]*
Blind BFS found a 13-jump solution but had to explore 3,012 states to get there. DFS is far cheaper, just 490 states, but it's betting on a lucky branch with no guarantee.

*[Show: memory/frontier chart]*
Node count isn't the whole memory story — this chart splits frontier from visited set. BFS holds both at once, over 5,700 combined. DFS's frontier is tiny, just 26, but its footprint is still dominated by a 490-state visited set.

The A* algorithm scores every candidate as f(n) = g(n) + h(n) — cost so far plus estimated cost remaining — and always expands the most promising state first. My heuristic adds two penalties to the baseline "pegs remaining" count: isolated pegs, which can't jump without a neighbor, and dispersion, how spread out the remaining pegs are, since the goal is one consolidated peg. That drops the search to just 57 states and a footprint of 225 — a 98% reduction versus BFS.

A key caveat: an *admissible* heuristic never overestimates the true remaining cost, guaranteeing the optimal solution. Mine isn't admissible — it deliberately overestimates. Normally that's risky, but here every winning solution is exactly 13 jumps regardless of path, so there's no shorter solution to miss. So I trade that guarantee for speed, for free.

## [4:15–4:30] Close

Constraint Satisfaction for pure logical deduction, Informed Search for pure combinatorial search — two classical AI tools, each matched to the shape of its problem. Thanks.