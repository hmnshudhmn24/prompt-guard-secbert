from src.data.label_mapper import LABEL_MAP

def preprocess(example):
    example["label"] = LABEL_MAP[example["label"]]
    return example
