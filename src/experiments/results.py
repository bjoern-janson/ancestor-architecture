"""
src/experiments/results.py

Utilities for loading, querying, comparing, and summarizing
experiment results.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd


class ExperimentResults:
    """
    Represents a single experiment run.
    """

    def __init__(self, run_directory: str):

        self.run_path = Path(run_directory)

        if not self.run_path.exists():

            raise FileNotFoundError(
                f"Run not found: {self.run_path}"
            )

        self.metrics = self._load_metrics()
        self.summary = self._load_summary()
        self.history = self._load_history()



    def _load_metrics(self):

        file = self.run_path / "metrics.csv"

        if file.exists():

            return pd.read_csv(file)

        return pd.DataFrame()



    def _load_summary(self):

        file = self.run_path / "summary.json"

        if file.exists():

            with open(
                file,
                "r",
                encoding="utf-8",
            ) as f:

                return json.load(f)

        return {}



    def _load_history(self):

        file = self.run_path / "history.json"

        if file.exists():

            with open(
                file,
                "r",
                encoding="utf-8",
            ) as f:

                return json.load(f)

        return []



    def metric_names(self):

        return list(
            self.metrics.columns
        )



    def final_metrics(self):

        if len(self.metrics) == 0:

            return {}

        return (
            self.metrics.iloc[-1]
            .to_dict()
        )



    def best(
        self,
        metric: str,
        maximize: bool = True,
    ):

        if metric not in self.metrics:

            return None

        if maximize:

            idx = (
                self.metrics[metric]
                .idxmax()
            )

        else:

            idx = (
                self.metrics[metric]
                .idxmin()
            )

        return (
            self.metrics
            .iloc[idx]
            .to_dict()
        )



    def describe(self):

        if len(self.metrics) == 0:

            return pd.DataFrame()

        return (
            self.metrics
            .describe()
        )



class ExperimentCollection:
    """
    Represents all runs for
    one experiment.
    """

    def __init__(
        self,
        experiment_directory: str,
    ):

        self.path = Path(
            experiment_directory
        )

        self.runs = self._discover_runs()



    def _discover_runs(self):

        runs = []

        if not self.path.exists():

            return runs

        for directory in sorted(
            self.path.iterdir()
        ):

            if directory.is_dir():

                runs.append(
                    ExperimentResults(
                        str(directory)
                    )
                )

        return runs



    def __len__(self):

        return len(self.runs)



    def latest(self):

        if not self.runs:

            return None

        return self.runs[-1]



    def summaries(self):

        rows = []

        for run in self.runs:

            rows.append(
                run.summary
            )

        return pd.DataFrame(
            rows
        )



    def compare(
        self,
        metric: str,
    ):

        rows = []

        for run in self.runs:

            final = (
                run.final_metrics()
            )

            rows.append(
                {
                    "run":
                        run.run_path.name,

                    metric:
                        final.get(
                            metric
                        ),
                }
            )

        return pd.DataFrame(
            rows
        )



    def best_run(
        self,
        metric: str,
        maximize: bool = True,
    ):

        best = None
        value = None

        for run in self.runs:

            final = (
                run.final_metrics()
            )

            score = final.get(
                metric
            )

            if score is None:

                continue

            if best is None:

                best = run
                value = score

                continue

            if maximize:

                if score > value:

                    best = run
                    value = score

            else:

                if score < value:

                    best = run
                    value = score

        return best



def load_results(
    path: str,
):

    """
    Load a single run or
    an entire experiment.

    Examples
    --------

    load_results(
        "results/agency_transfer"
    )

    load_results(
        "results/agency_transfer/run_20260727_140501"
    )
    """

    p = Path(path)

    if not p.exists():

        raise FileNotFoundError(path)

    metrics = p / "metrics.csv"

    if metrics.exists():

        return ExperimentResults(
            str(p)
        )

    return ExperimentCollection(
        str(p)
    )
