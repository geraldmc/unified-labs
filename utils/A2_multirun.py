# =====================================================================
# NEW CELL — add after the Milestone 1 re-evaluation cell
# =====================================================================
# One winner is an anecdote. This runs the GA several times and asks
# whether a harness score of 500 predicts anything about the controller.
#
# Results are written to ga_runs.json after every run, and the cell
# resumes from that file, so a Colab disconnect costs one run instead
# of all of them. Delete ga_runs.json to start fresh.

"""Multi-run experiment: does a harness score of 500 predict anything?

Runs the GA N times, re-evaluates each winner on fresh seeded episodes,
and persists results after every run so a runtime disconnect costs one
run rather than all of them.
"""

import json
import os
import random
import statistics

RESULTS_PATH = "ga_runs.json"


def load_results(path: str = RESULTS_PATH) -> list:
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return []


def save_results(results: list, path: str = RESULTS_PATH) -> None:
    with open(path, "w") as f:
        json.dump(results, f)


def run_experiment(n_runs: int = 8,
                   episodes: int = 200,
                   eval_seed: int = 1000,
                   path: str = RESULTS_PATH) -> list:
    """Run the GA n_runs times. Resumes from whatever is already on disk."""
    results = load_results(path)
    done = {r["run"] for r in results}

    for run in range(n_runs):
        if run in done:
            print(f"run {run}: already on disk, skipping")
            continue

        try:
            best, harness_fitness = run_fixed_ga(
                pop_size=15, generations=30, mutation_rate=0.1,
                rng=random.Random(run), verbose=False,
            )
            scores = evaluate(best, episodes=episodes, seed=eval_seed)
            hits = sum(1 for s in scores if s >= 500)

            results.append({
                "run": run,
                "harness_fitness": harness_fitness,
                "chromosome": list(best),
                "scores": scores,
                "success_rate": 100 * hits / len(scores),
                "mean": statistics.mean(scores),
            })
            save_results(results, path)   # persist immediately

            print(f"run {run}: harness {harness_fitness:5.1f}   "
                  f"true success {100 * hits / len(scores):5.1f}%   "
                  f"mean {statistics.mean(scores):5.1f}")

        except Exception as exc:
            print(f"run {run} FAILED: {type(exc).__name__}: {exc}")
            continue

    return sorted(results, key=lambda r: r["run"])


# ---------------------------------------------------------------- plotting
def plot_experiment(results: list):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_theme(style="whitegrid", context="notebook")

    rows = [{"run": r["run"], "score": s, "success_rate": r["success_rate"]}
            for r in results for s in r["scores"]]
    df = pd.DataFrame(rows)

    order = [r["run"] for r in results]
    labels = [f"run {r['run']}\n{r['success_rate']:.0f}%" for r in results]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.stripplot(data=df, x="run", y="score", order=order, ax=ax,
                  size=3, alpha=0.25, jitter=0.3, color="#c1442e",
                  legend=False)

    # what the harness reported for every single run
    ax.axhline(500, color="#2a7f62", linestyle="--", linewidth=2)
    ax.text(len(order) - 0.4, 500, "  harness score,\n  every run",
            color="#2a7f62", fontsize=10, va="center")

    # what each controller actually averages
    means = [r["mean"] for r in results]
    ax.plot(range(len(order)), means, "o-", color="black",
            markersize=7, linewidth=1.5, label="true mean over episodes")

    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 540)
    ax.set_xlabel("")
    ax.set_ylabel("steps balanced in one episode")
    ax.set_title("Every run passed the harness at 500.\n"
                 "Each column is 200 fresh episodes from that run's winner.",
                 fontsize=13, loc="left")
    ax.legend(loc="lower left", frameon=True)

    fig.tight_layout()
    return fig


# --- execute -----------------------------------------------------------
results = run_experiment(n_runs=8, episodes=200)

rates = [r["success_rate"] for r in results]
print(f"\nsuccess rate across runs: min {min(rates):.0f}%  "
      f"max {max(rates):.0f}%  median {statistics.median(rates):.0f}%")

plot_experiment(results)
import matplotlib.pyplot as plt
plt.show()
