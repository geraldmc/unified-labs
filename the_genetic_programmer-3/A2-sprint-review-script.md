# Assignment 2 — Sprint Review Video Script (~4:45)

Target 3:00–5:00. 608 spoken words. At 128 wpm — the pace the AI Arcade script
was actually delivered at — this runs 4:45. At 140 it is 4:20; at 120 it is 5:04,
so rehearse against a timer and do not ad-lib.

**The thesis is the reproducibility finding, not the architecture comparison.**
It is stated in the Open, demonstrated in the Interlude, threaded through both
topology graphs in Part 2, inverted in Part 3 (the one constant), and landed in
the Close. Every required prompt is answered inside that frame rather than
alongside it.

Audience: engineering directors **and** non-technical procurement executives.
All figures verified against commit `f21e364`, execution 1-19.

---

## [0:00–0:30] Open — the finding - (Control + Command + N).

> ON SCREEN — top of the notebook, title and "The Scenario".

As part of Synthetica’s Global Defense Initiative, I'm here to present a control system for our newest kinetic stabilization platform. As part of this research, we’ve built and tested two architectures: a fixed-weight genetic algorithm and an algorithm based on NEAT (NeuroEvolution of Augmenting Topologies). The second model evolves both the network's topology and its weights. As a practical note, every result reported here comes from hundreds of trials, not a single run.

---

## [0:30–1:16] Part 1 — Continuous Evolution (The Mathematical Nudge)

> ON SCREEN — the cell banner `# MILESTONE 1 — CODE`, at `gaussian_mutation`.
> Highlight `chromosome[i] += random.gauss(0, sigma)`.

In the drone lab, a mutation replaces one integer weight with a random number. This method works when genes are interpreted as labels. But weights can behave differently. First, as they're continuous values, nearby values mauy tend to act in a similar manner. Thus no single weight controls a specific rule; instead, behavior is distributed across all twenty-five weights.

Mutations add small random amounts to each weight, with the result that sometimes they go up and sometimes down. There’s no systematic bias in either direction. An upshot is that weights change, but they stay basically the same. An alternative approach is to discard a weight and create a new one, at random. The new weight bears no relation to the old. In other words, this “nudging” process provides variation from a known value. However, whatever that value came to represent - in terms of evolution - is now lost. 

---

## [1:16–1:37] Interlude — a sample size of one

> ON SCREEN — `# MILESTONE 1 — HONEST RE-EVALUATION`, then the histogram under
> `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`. Then scroll to the GA sweep table
> in `# MILESTONE 2 — AUDIT NUMBER REGENERATION` for the 0–100% range.

As an aside why does nothing seem to reproduce across runs? The “reproducibility gap” traces back to a specific measurement flaw: the test harness here evaluates every network on a single run. Each of 30 fixed-GA models posts a perfect 500 during training, yet in testing (over 200 iterations) they actually score anywhere between zero and 100%.

---

## [1:37–2:48] Part 2 — Occam's Razor & Hardware Deployment

> ON SCREEN — `# MILESTONE 3 TEST HARNESS`. Let `fixed_agent.mp4` play while you
> open, then scroll to the fixed topology graph in the same cell output, then to
> the NEAT graph under `# Call your NEAT topology graph here`.

This movie clip is one of the runs where the genetic algorithm works.  On the left, there are twenty-five connections, because I guessed five hidden nodes before training. 

On the right, is what NEAT evolves. Across thirty runs, twenty-three used no hidden layer, six used a single hidden layer. 

Occam's Razor in machine learning says take the smallest model that fits, because spare capacity gets spent memorising the training episodes rather than the task. NEAT searched across architectures; while the GA model can only search which a single one. F

---

## [2:48–4:04] Part 3 — The Protection of Innovation (Speciation)

> ON SCREEN — the `StdOutReporter` log under `# MILESTONE 2 TEST HARNESS`:
> the Species table and the "Mean genetic distance" line. Then section 4 of
> `# MILESTONE 2 — AUDIT NUMBER REGENERATION` for the 0.91667 figure.

But topology evolution has a built-in problem. If we add a node to a tuned network (where its new connections start off untrained) performance immediately drops while any payoff takes many subsequent generations. Any innovation is lost upon initial meeting with optimized rivals.

NEAT's answer is speciation — where  Mean Genetic Distance is the population's average pairwise separation. Every genome pair gets a compatibility distance. Below the threshold a newcomer joins an existing species; above the threshold, it founds its own and gets time to mature.


---

## [4:04–4:45] Close

> ON SCREEN — the dot plot under `# MILESTONE 2 — RUN COMPARISON PLOT`.

So what can you rely on? Not a single run. At 10 runs per architecture the ranking reverses itself between consecutive executions. At 30 it holds: three sweeps put NEAT's median between 51% and 66%, the GA's between 18 and 26, and they never overlap. In a recent run here, 21/30 NEAT runs work in most episodes against 5/30. Byb this margin NEAT is the better option by a wide margin. Thus, I recommend NEAT, along with an acceptance test that can measure more than a single run.

(Control + Command + Esc)