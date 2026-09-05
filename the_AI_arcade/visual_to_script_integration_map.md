# Visual-to-Script Integration Map: AI Arcade Sprint Review

| Timestamp | Script Section | On-Screen Action / Focus | Cursor & Narration Cue | Rubric Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **0:00 – 0:15** | **Open** | Display top of Colab notebook: title & "The Scenario" markdown header. | Cursor rests on title. Establish professional context as Lead AI Engineer at RetroMind Studios. | Executive Delivery (clear framing). |
| **0:15 – 1:20** | **Part 1: The Detective Alibi** | Run/replay `MastermindEngine` test harness cell with `time.sleep(0.8)`. | Hover over **Turn 1 header** (`Hypotheses Remaining: 625`). Trace the bottom heatmap matrix as circles fade and red **"X"** marks appear over invalidated colors. Match narration of the consistency check to the elimination. | Data & Visuals: Direct continuous evidence of monotonic pruning. |
| **1:20 – 1:55** | **Part 2: Rule-Based AI vs. LLMs** | Scroll down to the `MastermindAI` class code block. | Highlight `process_feedback()` and the `simulate_feedback()` logic. Contrast this deterministic boolean filter with statistical token generation. | Technical Concept: Concrete justification of CSP over LLMs. |
| **1:55 – 2:30** | **Part 3A: Search vs. Deduction & Nodes** | Display the newly styled Seaborn chart: **"Milestone 3: The Pathfinder \| Search Space & Memory Scaling"**. | Point directly to the **3,012** (BFS) and **490** (DFS) bars to visually illustrate search explosion versus lucky branch diving. | Data & Visuals: Anchoring comparative claims in plotted data. |
| **2:30 – 3:05** | **Part 3B: Memory & Frontier Trade-offs** | Pan to the memory/frontier breakdown figure or tabular metrics cell. | Trace the BFS footprint (Frontier + Visited > 5,700) versus DFS (tiny frontier of 26, visited = 490). | Technical Concept: Nuanced distinction between queue storage and visited tracking. |
| **3:05 – 3:45** | **Part 3C: The A\* Heuristic Formula** | Scroll to the `heuristic(state)` code block and point back to the **57 states** bar on the chart. | Highlight the Python return line: `pegs_remaining + 2*isolated_pegs + 3*dispersion`. Point out the badge reading **"98.1% compute reduction vs. BFS"**. | Technical Concept: Mathematical deconstruction of penalties ($g(n) + h(n)$). |
| **3:45 – 4:15** | **Part 3D: Admissibility Trade-off** | Keep the `heuristic(state)` code and `a_star_solve()` test harness in frame. | Highlight the test assertions confirming `len(astar_path) == 13`. Explain why overestimating $h^*(n)$ does not forfeit path optimality when all solutions are length 13. | Technical Concept: Formal mathematical justification of inadmissibility. |
| **4:15 – 4:30** | **Close** | Run/display the `animate_solution_path()` Peg Board playback. | Let the final pegs resolve down to 1 peg in the center as you deliver the concluding takeaway. | Executive Delivery: Clean, polished wrap-up well under the 5:00 mark. |

---

### Screencast Setup Checklist

* **Chart Check:** Verify that the Seaborn plot is generated with the title *"Milestone 3: The Pathfinder | Search Space & Memory Scaling"*.
* **Animation Speed:** Confirm that `time.sleep(0.8)` is set inside `MastermindEngine.render_frame()` so the visual executes concurrently with Part 1.
* **Pacing Buffer:** Keep the total spoken delivery between 4:05 and 4:25 to maintain an executive pace and satisfy the strict < 5:00 rubric constraint.