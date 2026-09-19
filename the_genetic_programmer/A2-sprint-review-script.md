# Assignment 2 — Sprint Review Video Script (~4:30)

Target 3:00–5:00. Word counts below are real; timings assume 128 wpm, the pace
of the AI Arcade script. At 120 wpm this runs 4:49, at 140 wpm 4:07 — inside the
cap either way, though the slow end leaves only eleven seconds of margin.

Audience: engineering directors **and** non-technical procurement executives.
Every claim below is measured in the notebook; none is asserted from theory.
All figures verified against the committed run (`5dbaefd`, execution 1-18).

---

## [0:00–0:21] Open

> ON SCREEN — top of the notebook, title and "The Scenario".

I'm presenting the control system for the kinetic stabilization platform. Two architectures were built and tested: a fixed-weight genetic algorithm, and NEAT, which evolves the network's shape as well as its weights. Every number you'll see is measured over two hundred episodes, not one demonstration run.

---

## [0:21–1:16] Part 1 — Continuous Evolution (The Mathematical Nudge)

> ON SCREEN — Milestone 1 code cell (banner `# MILESTONE 1 — CODE`), `gaussian_mutation`.
> Highlight `chromosome[i] += random.gauss(0, sigma)`.

In the drone lab, mutation replaced an integer with a brand-new random one. That works when genes are labels — column three is no nearer column four than column seven. Weights are different. They sit on a continuous scale where nearby values behave alike, and no single weight holds a rule — behaviour is spread across all twenty-five.

So mutation here adds Gaussian noise centred on zero. The expected value of a mutated weight is the weight it replaced. Replacement has an expected value of zero regardless of the parent — it doesn't perturb what the network learned, it deletes it and redraws. Nudging keeps the child a variation on its parent. Replacement makes it a stranger.

---

## [1:16–1:29] Interlude — What the harness actually measured

> ON SCREEN — the re-evaluation output (banner `# MILESTONE 1 — HONEST RE-EVALUATION`), then the episode-score
> histogram from `plot_score_distribution` (banner `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`).

One thing about measurement first. The harness scored this controller a perfect five hundred. Re-evaluated on two hundred fresh episodes it succeeds thirty-eight percent of the time.

---

## [1:29–2:41] Part 2 — Occam's Razor & Hardware Deployment

> ON SCREEN — the two topology graphs, fixed (banner `# MILESTONE 3 TEST HARNESS`) then NEAT
> (banner `# Call your NEAT topology graph here`). Point at the hollow node.

Here are the two brains. On the left, the architecture I was given: four inputs, five hidden nodes, twenty-five connections. Every connection exists because I guessed five hidden nodes before training began. The algorithm can drive a weight toward zero but cannot remove it, so this picture is identical for every solution it will ever find.

On the right, what NEAT evolved: zero hidden nodes, three connections. It declined one sensor outright — the hollow circle.

Occam's Razor in machine learning says take the smallest model that fits, because spare capacity gets spent memorising the training episodes instead of learning the task. And the point isn't tidiness — NEAT searched across architectures; the fixed GA could only search inside one. For your platform: four parameters instead of twenty-five, three multiply-accumulates per control step instead of twenty-five. On a battery, that's the case.

One caveat you should hear from me. Smaller is cheaper, not safer.

---

## [2:41–3:59] Part 3 — The Protection of Innovation (Speciation)

> ON SCREEN — the `StdOutReporter` log (banner `# MILESTONE 2 TEST HARNESS`): Species table and
> "Mean genetic distance". Then section 4 of the regeneration cell
> (banner `# MILESTONE 2 — AUDIT NUMBER REGENERATION`) for the 0.91667 figure.

Topology evolution has a built-in problem. Add a node to a tuned network and its new connections start untrained, so performance drops at once while the payoff takes generations. The innovation is weakest exactly when it first meets optimized rivals.

NEAT's answer is speciation — these are the Species columns, and this line, Mean genetic distance, is the population's average pairwise separation. Every pair of genomes gets a compatibility distance: structural differences counted and normalised, plus weight and bias differences scaled by a half. Below the threshold — two point zero here — a newcomer joins an existing species; above it, it founds its own and gets sheltered time to mature.

Here is what I measured. One added node contributes exactly zero point nine one seven, and never reaches two point zero alone. Structural innovation here cannot found a species by itself; what splits these populations is bias divergence, and most runs never split at all. The mechanism is real, and at this genome size mostly dormant.

---

## [3:59–4:11] Behavioural evidence

> ON SCREEN — play `fixed_agent.mp4` (banner `# MILESTONE 3 TEST HARNESS`), then `neat_agent.mp4`
> (banner `--- 2. NEAT GA VISUALIZATION ---`). Both ran 500 steps unseeded.

Both controllers, balancing. There is no "do nothing" action, so anything that solves this vibrates. And that first clip is a run where the GA worked.

---

## [4:11–4:30] Close

> ON SCREEN — the GA-vs-NEAT dot plot (banner `# MILESTONE 2 — RUN COMPARISON PLOT`).

Both architectures report a perfect five hundred, every run. Across two hundred fresh episodes, two of ten fixed-GA runs and seven of ten NEAT runs actually work. I recommend NEAT for the hardware, and a multi-episode acceptance test before anything flies.

---

## Notes on four deliberate choices

**The interlude exists so Milestone 1 has a result on screen, not just code.**
Without it the video shows the mutation operator and no evidence that any of
the measurement work happened. It also front-loads the standard of proof, so
Part 2's caveat and the close both land against a premise already established
rather than one introduced at 4:11.

**Part 2 ends on "smaller is cheaper, not safer."** The prompt asks why NEAT is
"vastly superior" for edge hardware. On parameter count that is true and worth
saying plainly — 4 against 25. On reliability the measurement says otherwise,
and a procurement audience evaluating hardware for physical deployment is the
worst possible audience to oversell to.

**Part 3 contradicts the prompt's premise, with arithmetic.** The prompt assumes
the compatibility threshold shelters structural innovation. Here it measurably
does not: one added node is worth exactly 0.91667 against a threshold of 2.0, so
it can never found a species alone. Explain the mechanism as designed, then give
the measurement.

**The GA clip is a lucky run, and the script says so over the footage.** The
unseeded render balanced all 500 steps, but that winner works in 2 of 10 runs.
Saying it while the clip plays is better than letting the close contradict what
the audience just watched.
