import random
from typing import Iterable

import pandas as pd


class LearningData:
    def __init__(self, path, *, prefix: str="", suffix: str=""):
        self._data = pd.read_table(path, sep="\t", names=["word", "freq"])
        self._data["word"] = prefix + self._data["word"] + suffix

    def sample(self, n: int=1) -> pd.Series:
        return self._data["word"].sample(
            n=n, weights=self._data["freq"], replace=True, ignore_index=True
        )


def slice_word(corpus: Iterable[str], window: int):
    for word in corpus:
        tokens = word.split(" ")
        if len(tokens) < window:
            continue

        for i in range(len(tokens) - window + 1):
            yield " ".join(tokens[i:i+window])


def randomize_word(corpus: Iterable[str], phonemes):
    for word in corpus:
        replaced = []
        for token in word.split(" "):
            if token == "#":
                replaced.append("#")
                continue

            replaced.append(random.choice(phonemes))
        yield " ".join(replaced)
