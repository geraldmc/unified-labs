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

## [0:00–0:30] Open — the finding

> ON SCREEN — top of the notebook, title and "The Scenario".

The control system for the kinetic stabilization platform. Two architectures: a fixed-weight genetic algorithm, and NEAT, which evolves the network's shape as well as its weights. One finding first, because it governs everything else: almost nothing here reproduces. Run it again, you get a different network and a different success rate. The number that repeats perfectly every time is the one the acceptance test prints.

---

## [0:30–1:16] Part 1 — Continuous Evolution (The Mathematical Nudge)

> ON SCREEN — the cell banner `# MILESTONE 1 — CODE`, at `gaussian_mutation`.
> Highlight `chromosome[i] += random.gauss(0, sigma)`.

In the drone lab, mutation replaced an integer with a fresh random one. That works when genes are labels — column three is no nearer column four than column seven. Weights are different: they sit on a continuous scale, and no single weight holds a rule.

So mutation here adds Gaussian noise centred on zero. A mutated weight's expected value is the weight it replaced. Replacement's expected value is zero whatever the parent was — it doesn't perturb what the network learned, it deletes it. Nudging keeps the child a variation on its parent; replacement makes it a stranger.

---

## [1:16–1:37] Interlude — a sample size of one

> ON SCREEN — `# MILESTONE 1 — HONEST RE-EVALUATION`, then the histogram under
> `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`. Then scroll to the GA sweep table
> in `# MILESTONE 2 — AUDIT NUMBER REGENERATION` for the 0–100% range.

Here is why nothing reproduces. The harness scores a controller on one episode — a sample size of one. All thirty fixed-GA runs passed it with a perfect five hundred. Re-evaluated over two hundred episodes, those same winners range from zero percent to a hundred.

---

## [1:37–2:48] Part 2 — Occam's Razor & Hardware Deployment

> ON SCREEN — `# MILESTONE 3 TEST HARNESS`. Let `fixed_agent.mp4` play while you
> open, then scroll to the fixed topology graph in the same cell output, then to
> the NEAT graph under `# Call your NEAT topology graph here`.

That clip is one of the runs where the GA works. The same split shows up in the architectures. On the left, the one I was handed: twenty-five connections, because I guessed five hidden nodes before training. A weight can reach zero but never be removed, so this picture is identical every run — reproducible, and reproducibly the wrong size.

On the right, what NEAT evolved, never the same twice. Across thirty runs, twenty-three used no hidden layer, six used one, one grew three. Today: four connections, five parameters.

Occam's Razor in machine learning says take the smallest model that fits, because spare capacity gets spent memorising the training episodes rather than the task. NEAT searched across architectures; the GA could only search inside one. For your platform: five parameters instead of twenty-five, four multiply-accumulates per step. On a battery, that is the case — though smaller is cheaper, not safer.

---

## [2:48–4:04] Part 3 — The Protection of Innovation (Speciation)

> ON SCREEN — the `StdOutReporter` log under `# MILESTONE 2 TEST HARNESS`:
> the Species table and the "Mean genetic distance" line. Then section 4 of
> `# MILESTONE 2 — AUDIT NUMBER REGENERATION` for the 0.91667 figure.

Topology evolution has a built-in problem. Add a node to a tuned network and its new connections start untrained, so performance drops at once while the payoff takes generations. The innovation is weakest exactly when it first meets optimised rivals.

NEAT's answer is speciation — these are the Species columns, and this line, Mean genetic distance, is the population's average pairwise separation. Every genome pair gets a compatibility distance: structural differences counted and normalised, plus weight and bias differences scaled by a half. Below the threshold, two point zero here, a newcomer joins an existing species; above it, it founds its own and gets time to mature.

And here is the one number in this talk that never moves. An added node contributes exactly zero point nine one seven — never reaching two point zero alone. So in this configuration structural innovation cannot found a species by itself; what splits these populations is bias divergence. The mechanism is real, and mostly dormant.

---

## [4:04–4:45] Close

> ON SCREEN — the dot plot under `# MILESTONE 2 — RUN COMPARISON PLOT`.

So what can you rely on? Not one run. At ten per architecture the ranking reversed between consecutive executions. At thirty it holds: three sweeps put NEAT's median between fifty-one and sixty-six percent, the GA's between eighteen and twenty-six, never overlapping. Today, twenty-one of thirty NEAT runs work in most episodes against five of thirty. NEAT is the better bet by a wide margin — and all sixty told the harness they were perfect. Recommend NEAT, and an acceptance test that measures more than one episode.

---

## Notes

**Why the clips lost their own slot.** An earlier draft gave the two videos a
dedicated beat. Featuring the reproducibility thesis cost about forty words and
the clips were the only section not answering a required prompt, so the GA video
now plays under Part 2's opening — it sits in the same cell output as the fixed
topology graph, so it costs no extra time. The line "that clip is one of the runs
where the GA works" still has to be said, because the audience is watching a
flawless GA balance shortly before the close says five of thirty work.

**The 0.91667 is the rhetorical anchor.** It is the only figure identical on
every execution, because it involves no environment. Part 3 says so out loud,
which is what makes the variability claim land rather than sound like an excuse.

**Three figures track the current run** and need refreshing if it is executed
again: the hidden-node distribution and the winner's counts in Part 2, and the
21-of-30 / 5-of-30 in the Close. The medians are quoted as ranges across three
sweeps, so they survive.

**Part 2 ends on "smaller is cheaper, not safer."** The prompt asks why NEAT is
"vastly superior" for edge hardware. On parameter count that is true. On
reliability the spread says be careful, and a procurement audience evaluating
hardware for physical deployment is the worst one to oversell to.
