# Visual-to-Script Integration Map: Assignment 2 Sprint Review

Companion to `A2-sprint-review-script.md` (~4:26 at 128 wpm). Cell numbers are
zero-indexed positions in `Assignment-2.ipynb`.

| Timestamp | Script Section | On-Screen Action / Focus | Cursor & Narration Cue | Prompt Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **0:00 – 0:22** | **Open** | Top of the notebook: title and "The Scenario" markdown. | Cursor rests on the title. Establish the two architectures and the 200-episode standard of evidence before any result appears. | Executive framing. |
| **0:22 – 1:19** | **Part 1 — The Mathematical Nudge** | Milestone 1 code cell (**cell 7**), scrolled to `gaussian_mutation`. | Highlight `chromosome[i] += random.gauss(0, sigma)`. Say "expected value of a mutated weight is the weight it replaced" while the cursor sits on `gauss(0, sigma)` — the zero is the whole argument. | **Prompt 1:** Continuous Evolution. |
| **1:19 – 2:26** | **Part 2 — Occam's Razor** | Milestone 3 harness output: the fixed topology graph (**cell 32**), then the NEAT graph (**cell 34**). | Sweep the cursor across the 25-edge web while saying "identical for every solution it will ever find." Then cut to the NEAT graph and rest on the **hollow node** for the "declined one sensor" line. | **Prompt 2:** Occam's Razor & hardware. |
| **2:26 – 3:41** | **Part 3 — Protection of Innovation** | `StdOutReporter` log in the Milestone 2 harness output (**cell 21**), then section 4 of the regeneration cell (**cell 22**). | Point at the **Species** table and the **Mean genetic distance** line as you describe the mechanism. Then scroll to `one add-node mutation ... delta = 0.91667` and hold there for the measurement. | **Prompt 3:** Speciation & compatibility distance. |
| **3:41 – 3:59** | **Behavioural evidence** | Play `fixed_agent.mp4` (**cell 32**), then `neat_agent.mp4` (**cell 33**). | Let both clips run without narrating over the physics. Deliver the "that is a run where the fixed GA worked" line *over the first clip*, not after it — the audience is watching a flawless GA balance while the close is about to say it fails most of the time. | Milestone 3 behavioural renders. |
| **3:59 – 4:26** | **Close** | The GA-vs-NEAT dot plot (**cell 23**). | Trace the dashed 100% line first — "every run passed here" — then drop to the two clusters. Land on "2 of 10 and 7 of 10." | Executive delivery; ties back to Prompt 2's reliability caveat. |

---

### Screencast Setup Checklist

* **Run the whole notebook top to bottom first.** Execution counts should be
  monotone on camera; a stale `In [ ]` next to a result invites the question of
  whether the number on screen came from the code above it.
* **Renders confirmed.** Cells 32–34 ran in Colab under commit `5dbaefd`; both
  `fixed_agent.mp4` and `neat_agent.mp4` play, each 500 steps, unseeded.
* **The GA clip got lucky, and that needs saying out loud.** The unseeded render
  happened to balance all 500 steps, but that winner succeeds in only 2 of 10
  runs. A flawless GA video followed by "it works twice in ten" reads as a
  contradiction unless you name it while the clip is playing. The alternative is
  to re-render with a seed that crashes, which matches the argument but looks
  like stacking the deck. Naming it is the better option.
* **Figures verified against commit `5dbaefd`.** Winner: 0 hidden nodes, 3
  connections, `cart position` never wired. Sweeps: fixed GA median 29%
  (range 0–81%), NEAT median 58% (range 2–100%); above a 50% bar that is
  **2 of 10 and 7 of 10**. Re-verify only if you re-run the notebook — these
  move. `0.91667` and the 2.0 threshold do not.
* **The dropped sensor is `cart position`.** Confirmed in the committed run's
  graph subtitle, so the "declined one sensor" line stands as written.
* **Pacing buffer.** Script runs 4:02–4:42 across 140–120 wpm. The hard cap is
  5:00 and the three prompts are all load-bearing, so there is nothing safe to
  cut live — if you are running long, trim the Open and the second clip, not
  Part 3.
