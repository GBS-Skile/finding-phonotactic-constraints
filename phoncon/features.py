import csv
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class FeatureSystem:
    _features: List[str]
    _phonemes: Dict[str, List[str]]

    def get_phonemes(self):
        return list(self._phonemes.keys())


def load_feature_system(fp) -> FeatureSystem:
    reader = csv.reader(fp, delimiter='\t')

    features = next(reader)[1:]  # skip first column
    phonemes = {}
    for row in reader:
        phonemes[row[0]] = row[1:]

    return FeatureSystem(features, phonemes)


if __name__ == "__main__":
    with open("data/englishonset/EnglishFeatures.txt") as f:
        fs = load_feature_system(f)

        # TODO: add segment feature
