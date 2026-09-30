# Visual-to-Script Integration Map: Assignment 2 Sprint Review

Companion to `A2-sprint-review-script.md` (~4:45 at 128 wpm). Cells are named by
the banner comment on their first line, not by position — Colab shows execution
counts, not indices, and any inserted cell renumbers everything below it. Find a
cell with Ctrl+F on its banner text.

**The spine is the reproducibility finding.** Each row below should visibly
serve it: the Open states it, the Interlude demonstrates it, Part 2 contrasts
the architecture that never changes with the one that never repeats, Part 3
supplies the single constant, the Close lands it.

| Timestamp | Script Section | On-Screen Action / Focus | Cursor & Narration Cue | Prompt Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **0:00 – 0:30** | **Open — the finding** | Top of the notebook: title and "The Scenario". | Cursor rests on the title. Do not rush this — "almost nothing here reproduces" is the sentence the rest of the talk depends on. | Framing; sets the thesis. |
| **0:30 – 1:16** | **Part 1 — The Mathematical Nudge** | `# MILESTONE 1 — CODE`, scrolled to `gaussian_mutation`. | Highlight `chromosome[i] += random.gauss(0, sigma)`. Say "expected value is the weight it replaced" with the cursor on `gauss(0, sigma)` — the zero is the whole argument. | **Prompt 1:** Continuous Evolution. |
| **1:16 – 1:37** | **Interlude — a sample size of one** | `# MILESTONE 1 — HONEST RE-EVALUATION`, then the histogram under `# MILESTONE 1 — SCORE DISTRIBUTION PLOT`, then the GA sweep table in `# MILESTONE 2 — AUDIT NUMBER REGENERATION`. | Say "a sample size of one" while pointing at the harness line, then sweep down the 30-row GA table to show 0% next to 100%. This is the evidence for the Open's claim. | Thesis evidence; Milestone 1 result. |
| **1:37 – 2:48** | **Part 2 — Occam's Razor** | `# MILESTONE 3 TEST HARNESS`: let `fixed_agent.mp4` play, scroll to the fixed topology graph in the same output, then the NEAT graph under `# Call your NEAT topology graph here`. | Deliver "that clip is one of the runs where the GA works" **over** the video. Then sweep the 25-edge web on "identical every run", and cut to the NEAT graph on "never the same twice". | **Prompt 2:** Occam's Razor & hardware. |
| **2:48 – 4:04** | **Part 3 — Protection of Innovation** | `StdOutReporter` log under `# MILESTONE 2 TEST HARNESS`, then section 4 of `# MILESTONE 2 — AUDIT NUMBER REGENERATION`. | Point at the **Species** columns and the **Mean genetic distance** line by name. Then hold on `delta = 0.91667` for "the one number in this talk that never moves". | **Prompt 3:** Speciation & compatibility distance. |
| **4:04 – 4:45** | **Close** | The dot plot under `# MILESTONE 2 — RUN COMPARISON PLOT`. | Trace the dashed 100% line first — every run passed there — then drop to the two clusters. Land on "all sixty told the harness they were perfect". | Executive delivery; closes the thesis. |

---

### Screencast Setup Checklist

* **Run the whole notebook top to bottom first.** Execution counts should read
  1–19 on camera; a stale `In [ ]` beside a result invites the question of
  whether the number came from the code above it.
* **Renders confirmed.** Both `fixed_agent.mp4` and `neat_agent.mp4` play. The
  NEAT clip no longer has a dedicated slot — show it only if you are running
  ahead of schedule.
* **The GA clip is a lucky run, and you must say so over it.** It balanced all
  500 steps unseeded, but only 5 of 30 GA winners work in most episodes.
* **Figures verified against commit `f21e364` (execution 1-19).** Winner: 0
  hidden nodes, 4 connections, all four sensors wired, 5 parameters. Sweeps at
  n=30: fixed GA median 26% (5/30 above half), NEAT median 66% (21/30). NEAT
  hidden-node distribution 23/6/1 across 0, 1 and 3. Drift 0.65 wired vs 1.11
  dropped. `0.91667` and the 2.0 threshold do not move; nothing else does.
* **Three figures need refreshing if you re-execute:** the hidden-node
  distribution and the winner's counts in Part 2, and 21-of-30 / 5-of-30 in the
  Close. The medians are quoted as ranges across three sweeps and survive.
* **Pacing.** 4:20–5:04 across 140–120 wpm; 4:45 at the pace the AI Arcade
  script was actually delivered. The cap is hard and all three prompts are
  load-bearing — if you run long, shorten the Open's second half, not Part 3.
