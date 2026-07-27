"""
src/experiments/logger.py

Experiment logging utilities.

Responsible for:

- creating reproducible experiment directories
- saving configurations
- logging per-episode metrics
- writing experiment summaries
"""

from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class ExperimentLogger:

    def __init__(
        self,
        experiment_name: str,
        output_root: str = "results",
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        self.run_dir = (
            Path(output_root)
            / experiment_name
            / f"run_{timestamp}"
        )

        self.run_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.metrics: List[Dict[str, Any]] = []



    @property
    def path(self):

        return self.run_dir



    def save_config(
        self,
        config_path: str,
    ):

        """
        Stores the configuration used
        for this experiment.
        """

        destination = (
            self.run_dir
            / "config.yaml"
        )

        shutil.copyfile(
            config_path,
            destination,
        )



    def log(
        self,
        episode: int,
        metrics: Dict[str, Any],
    ):

        """
        Append one episode of metrics.
        """

        row = {
            "episode": episode,
            **metrics,
        }

        self.metrics.append(row)



    def save_metrics(self):

        """
        Saves metrics.csv
        """

        if not self.metrics:

            return

        file = (
            self.run_dir
            / "metrics.csv"
        )

        fieldnames = list(
            self.metrics[0].keys()
        )

        with open(
            file,
            "w",
            newline="",
            encoding="utf-8",
        ) as csvfile:

            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            writer.writerows(
                self.metrics
            )



    def save_history(self):

        """
        Saves history.json.

        Contains the complete episode log.
        """

        file = (
            self.run_dir
            / "history.json"
        )

        with open(
            file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                self.metrics,
                f,
                indent=4,
            )



    def save_summary(
        self,
        summary: Dict[str, Any],
    ):

        """
        Saves summary.json.
        """

        file = (
            self.run_dir
            / "summary.json"
        )

        with open(
            file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                summary,
                f,
                indent=4,
            )



    def finalize(
        self,
        summary: Dict[str, Any],
    ):

        """
        Save every artifact.
        """

        self.save_metrics()

        self.save_history()

        self.save_summary(
            summary
        )
