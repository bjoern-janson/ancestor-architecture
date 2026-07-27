from pathlib import Path
from typing import Any, Dict

import yaml



class ConfigLoader:
    """
    Loads and manages experiment configuration files.

    Configurations define:
    - experiment parameters
    - agent settings
    - model parameters
    - reward weights
    - evaluation metrics
    """

    def __init__(self, config_path: str):

        self.path = Path(config_path)

        if not self.path.exists():

            raise FileNotFoundError(
                f"Configuration file not found: {self.path}"
            )

        self.config = self._load()



    def _load(self) -> Dict[str, Any]:

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as file:

            return yaml.safe_load(file)



    def get(
        self,
        key: str,
        default=None,
    ):

        """
        Access top-level configuration values.
        """

        return self.config.get(
            key,
            default,
        )



    def get_nested(
        self,
        path: str,
        default=None,
    ):

        """
        Access nested values using dot notation.

        Example:

        config.get_nested(
            "reward.dependency_penalty"
        )
        """

        keys = path.split(".")

        value = self.config


        for key in keys:

            if not isinstance(
                value,
                dict,
            ):

                return default


            value = value.get(
                key,
                default,
            )


        return value



    def all(self) -> Dict[str, Any]:

        """
        Return complete configuration.
        """

        return self.config



def load_config(
    path: str = "configs/default.yaml",
) -> ConfigLoader:

    """
    Convenience function.
    """

    return ConfigLoader(path)
