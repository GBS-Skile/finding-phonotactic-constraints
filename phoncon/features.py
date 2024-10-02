from dataclasses import dataclass
from itertools import chain
from typing import List, Optional

import pandas as pd

@dataclass
class FeatureSystem:
    _data: pd.DataFrame

    @staticmethod
    def load(path, *, word_boundary: Optional[str]=None):
        """
        :param word_boundary: If set, add special token for word_boundary.
        """
        df = pd.read_table(path, sep="\t", index_col=0, header=0)
        return FeatureSystem(df)

    def add_word_boundary(self, phoneme: str, feature: str) -> "FeatureSystem":
        return FeatureSystem(_add_word_boundary(self._data, phoneme, feature))

    def to_binary_feature(self) -> "FeatureSystem":
        df = self._data
        data = []
        for feature in df.columns:
            data.append((df.loc[:, feature] == "+").rename("+" + feature))
            data.append((df.loc[:, feature] == "-").rename("-" + feature))
        return FeatureSystem(pd.DataFrame(data).astype(int).T)

    def get_phonemes(self):
        return list(self._data.index)

    def get_features(self, phoneme: str):
        return self._data.loc[phoneme]

    def get_matrix(self, corpus: List[str]) -> pd.DataFrame:
        splitted = [word.split(" ") for word in corpus]
        max_token = max(len(tokens) for tokens in splitted)
        indice = list(chain(*(self._data.columns + str(i) for i in range(max_token))))

        data = []
        for tokens in splitted:
            row = list(chain(*(self._data.loc[phone] for phone in tokens)))
            row += [0] * (len(indice) - len(row))
            data.append(row)
        return pd.DataFrame(data, columns=indice, index=corpus)


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
