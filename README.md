# LLM Training and Inference

This repository contains examples for training and serving LLMs in single-GPU and multi-GPU environments, with support for offline (HPC/cluster) setups.

---

## Files

* `Qwen3_4B_SFT_Math.ipynb`
  Example notebook for fine-tuning a math-focused LLM.

* `TrainingLLM-SFT-Example.ipynb`
  General training pipeline for LLMs. Supports both single GPU and distributed multi-GPU training.

* `download_model.py`
  Downloads model weights to the Hugging Face cache (`.cache/huggingface`).

* `download_data.py`
  Downloads datasets to local cache.

* `.env`
  Stores model name, model path/URL, and other configuration values.

* `inference.ipynb`
  Notebook to test model inference using a served endpoint.

---

## Usage

### 1. (Optional) Prepare offline resources

Run on a machine with internet:

```bash
python download_model.py
python download_data.py
```

* Downloads are stored in `.cache/huggingface`
* Useful for HPC/cluster environments without internet
* Not required when using platforms like Kaggle

---

### 2. Train the model

Use either notebook:

* Supports single GPU and multi-GPU
* Can be run on Kaggle or local setups

---

### 3. Serve the model

Using vLLM:

```bash
vllm serve <model_path>
```

Using Ollama:

```bash
ollama serve
```

Set model name and path/URL in `.env`.

---

### 4. Run inference

Open `inference.ipynb` and test the model via the configured endpoint.

---

## Notes

* PPT : [click here](https://docs.google.com/presentation/d/1e8Zsh73Ok0mo6gJ9zqVg5KdlFuPPMRL7/edit?usp=sharing&ouid=100241248115510035377&rtpof=true&sd=true)
* Blog : [click here](https://medium.com/@ankushsonawane36/from-words-to-understanding-how-the-attention-mechanism-powers-modern-ai-c3e6e49de69e)

---
