from datasets import load_dataset

gataset = load_dataset("mlabonne/FineTome-100k", split="train")
gataset = load_dataset("openai/gsm8k", "main", split="train")