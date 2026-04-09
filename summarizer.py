from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def summarize_text(text, max_length=180):
    prompt = "summarize: " + text

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=80,
        num_beams=4,
        length_penalty=1.0,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


def summarize_chunks(chunks, limit=12):
    summaries = []

    for chunk in chunks[:limit]:
        summaries.append(summarize_text(chunk))

    return "\n\n".join(summaries)


def final_summary(text):
    # do NOT compress again
    return text
