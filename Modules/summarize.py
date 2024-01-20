from transformers import BartForConditionalGeneration, BartTokenizer
import torch

def load_bart_model(model_name="facebook/bart-large-cnn"):
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

def summarize_news(model, tokenizer, content_string, num_beams, length_penalty):
    total_words = len(content_string.split())

    new_max_length = total_words
    new_min_length = max(100, total_words // 2)

    inputs = tokenizer(content_string, return_tensors="pt", max_length=1024, truncation=True)

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=int(new_max_length),
            min_length=int(new_min_length),
            num_beams=num_beams,
            length_penalty=length_penalty,
            early_stopping=True,
        )

    summary_ids = summary_ids.to("cpu")
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary_text


def summarizer(content):
    model, tokenizer = load_bart_model() 

    summary = summarize_news(model, tokenizer, content, num_beams=4, length_penalty=2.0)

    return summary


if __name__ == "__main__":
    

    content = """ Shifting to election gear | Baghel blows the bugle The Chhattisgarh chief minister works towards a second term by sinking differences and using a mix of farm sector initiatives, soft Hindutva, cow and caste politics to get the voters on his side It's poll season in Chhattisgarh and Chief Minister Bhupesh Baghel is out to win friends and influence people. So when the Congress central leadership elevated his bete noire, health minister T.S. Singh Deo, as the deputy chief minister, Baghel welcomed the move.
    """

    print(f"Original Content :\n{content}")
    summary = summarizer(content)

    print(f"Summary Text:\n{summary}")
