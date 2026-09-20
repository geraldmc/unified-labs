# Assignment 2 — Sprint Review Video Script (~4:38)

Target 3:00–5:00. Word counts below are real; timings assume 128 wpm, the pace
of the AI Arcade script. At 120 wpm this runs 4:57, at 140 wpm 4:15 — inside the
cap either way, though only two seconds of margin survive at 120 wpm — the AI Arcade
script was actually delivered at 128, where this lands at 4:39.

Audience: engineering directors **and** non-technical procurement executives.
Every claim below is measured in the notebook; none is asserted from theory.
All figures verified against the committed run (`b683aec`, execution 1-19).

---

## [0:00–0:21] Open

> ON SCREEN — top of the notebook, title and "The Scenario".

I'm presenting the control system for the kinetic stabilization platform. Two architectures: a fixed-weight genetic algorithm, and NEAT, which evolves the network's shape as well as its weights. One warning — every result here is a distribution over thirty runs, because single runs do not repeat.

---

## [0:21–1:13] Part 1 — Continuous Evolution (The Mathematical Nudge)

> ON SCREEN — Milestone 1 code cell (banner `# MILESTONE 1 — CODE`), `gaussian_mutation`.
> Highlight `chromosome[i] += random.gauss(0, sigma)`.

In the drone lab, mutation replaced an integer with a brand-new random one. That works when genes are labels — column three is no nearer column four than column seven. Weights are different: they sit on a continuous scale where nearby values behave alike, and no single weight holds a rule.

So mutation here adds Gaussian noise centred on zero. The expected value of a mutated weight is the weight it replaced. Replacement has an expected value of zero regardless of the parent — it doesn't perturb what the network learned, it deletes it and redraws. Nudging keeps the child a variation on its parent; replacement makes it a stranger.

---

## [1:13–1:32] Interlude — What the harness actually measured

> ON SCREEN — the re-evaluation output (banner `# MILESTONE 1 — HONEST RE-EVALUATION`), then the episode-score
> histogram from `plot_score_distribution` (banner `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`).

Start with measurement; it changes how you read everything after. The harness scores one episode. All thirty fixed-GA runs passed it with a perfect five hundred. Re-evaluated over two hundred fresh episodes, those same winners range from two percent to a hundred.

---

## [1:32–2:37] Part 2 — Occam's Razor & Hardware Deployment

> ON SCREEN — the two topology graphs, fixed (banner `# MILESTONE 3 TEST HARNESS`) then NEAT
> (banner `# Call your NEAT topology graph here`). Trace the dashed disabled
> edge, then the two-hop path through the new hidden node.

On the left, the architecture I was given: four inputs, five hidden nodes, twenty-five connections, because I guessed five hidden nodes before training. A weight can go to zero but never be removed, so this picture is identical every run.

On the right, what NEAT evolved — never the same twice. Across thirty runs, twenty-four used no hidden layer, five used one, one outlier grew four. Today: four connections, five parameters against twenty-five.

Occam's Razor in machine learning says take the smallest model that fits, because spare capacity gets spent memorising the training episodes instead of learning the task. NEAT searched across architectures; the fixed GA could only search inside one. For your platform that is five parameters instead of twenty-five, four multiply-accumulates per control step. On a battery, that is the case.

Smaller is cheaper, though, not safer.

---

## [2:37–3:55] Part 3 — The Protection of Innovation (Speciation)

> ON SCREEN — the `StdOutReporter` log (banner `# MILESTONE 2 TEST HARNESS`): Species table and
> "Mean genetic distance". Then section 4 of the regeneration cell
> (banner `# MILESTONE 2 — AUDIT NUMBER REGENERATION`) for the 0.91667 figure.

Topology evolution has a built-in problem. Add a node to a tuned network and its new connections start untrained, so performance drops at once while the payoff takes generations. The innovation is weakest when it first meets optimized rivals.

NEAT's answer is speciation — these are the Species columns, and this line, Mean genetic distance, is the population's average pairwise separation. Every pair of genomes gets a compatibility distance: structural differences counted and normalised, plus weight and bias differences scaled by a half. Below the threshold — two point zero here — a newcomer joins an existing species; above it, it founds its own, with sheltered time to mature.

And here is the one number in this talk that never moves. One added node contributes exactly zero point nine one seven — never reaching two point zero alone. Structural innovation here cannot found a species by itself; what splits these populations is bias divergence. The mechanism is real, and at this genome size mostly dormant.

---

## [3:55–4:04] Behavioural evidence

> ON SCREEN — play `fixed_agent.mp4` (banner `# MILESTONE 3 TEST HARNESS`), then `neat_agent.mp4`
> (banner `--- 2. NEAT GA VISUALIZATION ---`). Both ran 500 steps unseeded.

Both controllers, balancing. Neither can idle, so both vibrate. And that first clip is a run where the GA worked.

---

## [4:04–4:38] Close

> ON SCREEN — the GA-vs-NEAT dot plot (banner `# MILESTONE 2 — RUN COMPARISON PLOT`).

All sixty runs reported a perfect five hundred. Measured properly: four of thirty GA runs and eighteen of thirty NEAT runs work in most episodes — median nineteen against sixty-six percent. NEAT is the better bet by a wide margin, though both columns reach from near zero to a hundred. The only figure that reproduced across all sixty runs is the harness's, and it means nothing. Recommend NEAT, plus a multi-episode acceptance test.

---

## Notes on the framing

**Every claim is about a distribution, not a run.** Earlier drafts quoted one
winner's topology and one sweep's median, and both moved every time the
notebook was executed — at one point the GA/NEAT ranking reversed between two
consecutive runs. The talk now states what survives repetition and says
explicitly that the rest varies. Three numbers still come from the current
execution and need refreshing if it is run again: the winner's connection and
parameter count in Part 2, and the two medians in the close. The hidden-node
distribution, the ranges, and the sixty-out-of-sixty harness result are stable
in shape even when the digits shift.

**The 0.91667 is the rhetorical anchor.** It is the only figure in the talk
identical on every execution, because it involves no environment — pure
arithmetic over the compatibility distance. Part 3 says so out loud, which
turns a dry constant into the contrast that makes the variability point land.

**The close inverts the expected ending.** Rather than "NEAT wins," it observes
that the single perfectly reproducible number across all sixty runs is the
harness's 500, and that it is the one number that means nothing. NEAT is still
recommended, on a wide margin and on cost — but the reliability claim is framed
as a better bet, not a guarantee.

**Part 2 ends on "smaller is cheaper, not safer."** The prompt asks why NEAT is
"vastly superior" for edge hardware. On parameter count that is true. On
reliability the spread says be careful, and a procurement audience evaluating
hardware for physical deployment is the worst possible audience to oversell to.

**The GA clip is a lucky run, and the script says so over the footage.** The
unseeded render balanced all 500 steps, but only four of thirty GA winners work
in most episodes. Saying it while the clip plays beats letting the close
contradict what the audience just watched.
