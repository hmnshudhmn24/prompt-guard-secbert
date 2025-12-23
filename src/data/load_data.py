from datasets import load_dataset

def load_prompt_dataset(train, val, test):
    return load_dataset(
        "json",
        data_files={
            "train": train,
            "validation": val,
            "test": test
        }
    )
