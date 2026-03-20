from huggingface_hub import snapshot_download
import os

model_name = "unsloth/Qwen3-4B"

print(f"[INFO] Starting download for model: {model_name}")
print(f"[INFO] Files will be saved to HuggingFace cache (~/.cache/huggingface/hub)")

download_path = snapshot_download(
    repo_id=model_name,
    repo_type="model",
)
print(f"[INFO] Download completed. Model files are located at: {download_path}")