from typing import Optional

import pandas as pd

class FeatureSystem:
    def __init__(self, path, *, word_boundary: Optional[str]=None):
        """
        :param word_boundary: If set, add special token for word_boundary.
        """
        self._data = pd.read_table(path, sep="\t", index_col=0, header=0)
        if word_boundary:
            self._data = _add_word_boundary(self._data, word_boundary, "word_boundary")

    def get_phonemes(self):
        return list(self._data.index)


def _add_word_boundary(df: pd.DataFrame, phoneme: str, feature: str) -> pd.DataFrame:
    wb_row = pd.Series(
        ["0"] * len(df.columns) + ["+"],
        index=list(df.columns) + [feature],
        name=phoneme
    )
    wb_column = pd.Series(["-"] * len(df.index), index=df.index, name=feature)
    return pd.concat(
        [
            pd.concat([df, wb_column], axis=1),
            wb_row.to_frame().T
        ],
        axis=0
    )
