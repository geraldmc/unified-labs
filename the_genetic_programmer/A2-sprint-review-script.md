# Assignment 2 — Sprint Review Video Script (~4:26)

Target 3:00–5:00. Word counts below are real; timings assume 128 wpm, the pace
of the AI Arcade script. At 120 wpm this runs 4:43, at 140 wpm 4:03 — inside the
cap either way, with room to pause on the visuals.

Audience: engineering directors **and** non-technical procurement executives.
Every claim below is measured in the notebook; none is asserted from theory.
All figures verified against the committed run (`5dbaefd`, execution 1-18).

---

## [0:00–0:22] Open

> ON SCREEN — top of the notebook, title and "The Scenario".

I'm presenting the control system for the kinetic stabilization platform. Two architectures were built and tested: a fixed-weight genetic algorithm, and NEAT, which evolves the network's shape as well as its weights. Every number you'll see is measured over two hundred episodes, not one demonstration run.

---

## [0:22–1:19] Part 1 — Continuous Evolution (The Mathematical Nudge)

> ON SCREEN — Milestone 1 code cell, `gaussian_mutation`. Highlight
> `chromosome[i] += random.gauss(0, sigma)`.

In the drone lab, mutation replaced an integer with a brand-new random one. That works when genes are labels — column three is no closer to column four than to column seven. Weights are different. They sit on a continuous scale where nearby values behave alike, and no single weight holds a rule; the behaviour is spread across all twenty-five.

So mutation here adds Gaussian noise centred on zero. The expected value of a mutated weight is the weight it replaced. Replacement has an expected value of zero no matter what the parent was — it doesn't perturb what the network learned, it deletes it and redraws. Nudging keeps the child a variation on its parent. Replacement makes it a stranger.

---

## [1:19–2:26] Part 2 — Occam's Razor & Hardware Deployment

> ON SCREEN — the two topology graphs from Milestone 3, side by side.
> Fixed first, then NEAT. Point at the hollow node.

Here are the two brains. On the left, the architecture I was given: four inputs, five hidden nodes, twenty-five connections. Every connection exists because I guessed five hidden nodes before training began. The algorithm can drive a weight toward zero but cannot remove it, so this picture is identical for every solution it will ever find.

On the right, what NEAT evolved: zero hidden nodes, three connections. It declined one sensor outright — the hollow circle.

Occam's Razor says take the smallest hypothesis that fits. The point isn't that the right picture is tidier; it's that NEAT searched across architectures while the fixed GA could only search inside one. For your platform: four parameters instead of twenty-five, three multiply-accumulates per control step instead of twenty-five. On a battery, that's the case.

One caveat you should hear from me. Smaller is cheaper, not safer.

---

## [2:26–3:41] Part 3 — The Protection of Innovation (Speciation)

> ON SCREEN — the `StdOutReporter` log from the Milestone 2 harness: the
> Species table and the "Mean genetic distance" line. Then scroll to
> section 4 of the regeneration cell for the 0.91667 figure.

Topology evolution has a built-in problem. Add a node to a tuned network and its new connections start untrained, so performance drops at once — while the payoff, if any, takes generations. The innovation is weakest exactly when it first competes against optimized rivals.

NEAT's answer is speciation. Every pair of genomes gets a compatibility distance: structural differences counted and normalised, plus weight and bias differences scaled by a half. Below the threshold — two point zero here — a newcomer joins an existing species. Above it, it founds its own and gets sheltered time to mature.

Here is what I measured. One added node contributes exactly zero point nine one seven to that distance, and never reaches two point zero alone. Structural innovation in this configuration cannot found a species by itself; what splits these populations is bias divergence, and most runs never split at all. The mechanism is real, and at this genome size it is mostly dormant.

---

## [3:41–3:59] Behavioural evidence

> ON SCREEN — play `fixed_agent.mp4` (**cell 32**), then `neat_agent.mp4`
> (**cell 33**). Both ran 500 steps unseeded.

Both controllers, balancing. They look alike, and they are: there is no "do nothing" action, so anything that solves this vibrates. One caveat on the first clip — that is a run where the fixed GA worked.

---

## [3:59–4:26] Close

> ON SCREEN — the GA-vs-NEAT dot plot.

Which brings me to the number that matters for deployment. Both architectures report a perfect five hundred on the test harness — every run. Measured across two hundred fresh episodes, two of ten fixed-GA runs and seven of ten NEAT runs actually work. I recommend NEAT for the hardware, and a multi-episode acceptance test before anything flies.

---

## Notes on three deliberate choices

**Part 2 ends on "smaller is cheaper, not safer."** The assignment prompt asks
why NEAT is "vastly superior" for edge hardware. On parameter count that is
true and worth saying plainly — 4 against 25. On reliability the measurement
says otherwise, and a procurement audience evaluating hardware for physical
deployment is the worst possible audience to oversell to. The line costs four
seconds and it is what makes the close land.

**Part 3 contradicts the prompt's premise, with arithmetic.** The prompt assumes
the compatibility threshold is what shelters structural innovation. In this
configuration it measurably is not: one added node is worth exactly 0.91667 and
the threshold is 2.0, so a new node can never found a species on its own.
Explain the mechanism as designed, then give the measurement. Reporting a
number that overturns the expected answer is a stronger result than reciting
the expected answer.

**The close leads with the harness failure, not the win.** Both architectures
score a perfect 500 on the provided harness. That is the finding — the harness
cannot tell a good controller from a lucky one — and it reframes everything
before it.
