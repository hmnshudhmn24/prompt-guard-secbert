from src.inference.pipeline import load_pipeline

def predict(prompt, model_path="checkpoints"):
    pipe = load_pipeline(model_path)
    return pipe(prompt)
