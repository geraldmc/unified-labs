# Visual-to-Script Integration Map: Assignment 2 Sprint Review

Companion to `A2-sprint-review-script.md` (~4:38 at 128 wpm). Cells are named by the banner comment on their
first line, not by position — Colab shows execution counts, not indices, and
any inserted cell renumbers everything below it. Find a cell with Ctrl+F on
its banner text.

| Timestamp | Script Section | On-Screen Action / Focus | Cursor & Narration Cue | Prompt Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **0:00 – 0:21** | **Open** | Top of the notebook: title and "The Scenario" markdown. | Cursor rests on the title. Establish the two architectures and the 200-episode standard of evidence before any result appears. | Executive framing. |
| **0:21 – 1:13** | **Part 1 — The Mathematical Nudge** | Milestone 1 code cell (banner `# MILESTONE 1 — CODE`), scrolled to `gaussian_mutation`. | Highlight `chromosome[i] += random.gauss(0, sigma)`. Say "expected value of a mutated weight is the weight it replaced" while the cursor sits on `gauss(0, sigma)` — the zero is the whole argument. | **Prompt 1:** Continuous Evolution. |
| **1:13 – 1:32** | **Interlude — what the harness measured** | Re-evaluation output (banner `# MILESTONE 1 — HONEST RE-EVALUATION`), then the `plot_score_distribution` histogram (banner `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`). | Read "episodes at 500: 75/200 (38%)" off that output, then let the histogram's own title carry the rest — it already says the harness reported 500 from one episode. Rest on the gap where the mean sits. | Milestone 1 evidence; sets the standard of proof for Parts 2 and 3. |
| **1:32 – 2:37** | **Part 2 — Occam's Razor** | Milestone 3 harness output: the fixed topology graph (banner `# MILESTONE 3 TEST HARNESS`), then the NEAT graph (banner `# Call your NEAT topology graph here`). | Sweep the cursor across the 25-edge web while saying "identical for every solution it will ever find." Then cut to the NEAT graph and trace the two-hop path: the dashed **disabled** edge, then cart position going through the new hidden node instead. | **Prompt 2:** Occam's Razor & hardware. |
| **2:37 – 3:55** | **Part 3 — Protection of Innovation** | `StdOutReporter` log in the Milestone 2 harness output (banner `# MILESTONE 2 TEST HARNESS`), then section 4 of the regeneration cell (banner `# MILESTONE 2 — AUDIT NUMBER REGENERATION`). | Point at the **Species** table and the **Mean genetic distance** line as you describe the mechanism. Then scroll to `one add-node mutation ... delta = 0.91667` and hold there for the measurement. | **Prompt 3:** Speciation & compatibility distance. |
| **3:55 – 4:04** | **Behavioural evidence** | Play `fixed_agent.mp4` (banner `# MILESTONE 3 TEST HARNESS`), then `neat_agent.mp4` (banner `--- 2. NEAT GA VISUALIZATION ---`). | Let both clips run without narrating over the physics. Deliver the "that is a run where the fixed GA worked" line *over the first clip*, not after it — the audience is watching a flawless GA balance while the close is about to say it fails most of the time. | Milestone 3 behavioural renders. |
| **4:04 – 4:38** | **Close** | The GA-vs-NEAT dot plot (banner `# MILESTONE 2 — RUN COMPARISON PLOT`). | Trace the dashed 100% line first — "every run passed here" — then drop to the two clusters. Land on "2 of 10 and 7 of 10." | Executive delivery; ties back to Prompt 2's reliability caveat. |

---

### Screencast Setup Checklist

* **Run the whole notebook top to bottom first.** Execution counts should be
  monotone on camera; a stale `In [ ]` next to a result invites the question of
  whether the number on screen came from the code above it.
* **Renders confirmed.** The Milestone 3 harness cells ran in Colab under commit `5dbaefd`; both
  `fixed_agent.mp4` and `neat_agent.mp4` play, each 500 steps, unseeded.
* **The GA clip got lucky, and that needs saying out loud.** The unseeded render
  happened to balance all 500 steps, but that winner succeeds in only 2 of 10
  runs. A flawless GA video followed by "it works twice in ten" reads as a
  contradiction unless you name it while the clip is playing. The alternative is
  to re-render with a seed that crashes, which matches the argument but looks
  like stacking the deck. Naming it is the better option.
* **Figures verified against commit `b683aec` (execution 1-19).** Winner: 0
  hidden nodes, 4 connections, all four sensors wired, 5 parameters. Sweeps at
  n=30: fixed GA median 19% (4/30 above half), NEAT median 66% (18/30). NEAT
  hidden-node distribution 24/5/1 across 0, 1 and 4. Drift: 0.89 wired vs 0.98
  dropped. `0.91667` and the 2.0 threshold do not move — nothing else here is
  stable, which is now the talk's argument rather than a caveat.
* **No sensor was dropped this run.** All four inputs are wired, so there is no
  hollow node. Part 2 describes the distribution across thirty runs and labels
  the current winner as one draw, so it survives a re-roll either way.
* **Pacing buffer.** Script runs 4:15–4:57 across 140–120 wpm. At 128 — the pace the AI
  Arcade script was actually delivered at — it is 4:38, so do not ad-lib. The three prompts are
  load-bearing; if you are running long, drop the second video clip and shorten
  the interlude to the 38% figure alone. Do not cut Part 3.
