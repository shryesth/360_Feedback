# from transformers import BartForConditionalGeneration, BartTokenizer
# import torch

# def load_bart_model(model_name="facebook/bart-large-cnn"):
#     tokenizer = BartTokenizer.from_pretrained(model_name)
#     model = BartForConditionalGeneration.from_pretrained(model_name)
#     return model, tokenizer

# def summarize_news(model, tokenizer, content_string):
#     total_words = len(content_string.split())
#     print(f"\n Total words {total_words} \n")

#     # Determine the max and min length for summary

#     new_max_length = total_words
#     new_min_length = 100

    
#     print(f"Max Length:{new_max_length}, Minimum Length:{new_min_length}")

#     # Determine the number of beams and length penalty
#     if total_words >= 200:
#         num_beams = 5
#         length_penalty = 2.0
#     elif total_words >= 150:
#         num_beams = 4
#         length_penalty = 2.0
#     elif total_words >= 100:
#         num_beams = 3
#         length_penalty = 1.2
#     else:
#         num_beams = 2
#         length_penalty = 1.0

#     print(length_penalty,num_beams)
#     # Encode the content using the tokenizer
#     inputs = tokenizer(
#         content_string, return_tensors="pt", max_length=1024, truncation=True
#     )

#     # Generate the summary
#     summary_ids = model.generate(
#         inputs["input_ids"],
#         max_length=int(new_max_length),
#         min_length=int(new_min_length),
#         num_beams=num_beams,
#         length_penalty=length_penalty,
#         early_stopping=False,
#     )

#     # Decode and return the summary
#     summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)


#     return summary_text


# def summarizer(content):
#     model, tokenizer = load_bart_model()

#     summary = summarize_news(model, tokenizer, content)

#     return summary


# if __name__ == "__main__":
#     # Example usage:
#     content = """ Adani Group setting up world's largest green energy park in Gujarat, will generate 30GW of power This Adani Group project is expected to add to India's green energy capacity, besides helping in reaching its climate action pledges it made at COP The Adani Group is setting up the world's largest green energy park in the Rann of Kutch desert in Gujarat, Gautam Adani said on Thursday. The chairman of the business conglomerate took to social media platform X and share pictures of the under-construction plant, stating that it will cover a vast 726 square kilometres land mass and generate 30 GW of power. "Proud to play a crucial role in India's impressive strides in renewable energy as we build the world's largest green energy park. This monumental project, covering 726 sq km in the challenging Rann desert, is visible even from space. We will generate 30GW to power over 20 million homes," Adani posted on X. “Also, just 150 km away, in our karmabhoomi Mundra, we are creating one of the globe's most extensive and integrated renewable energy manufacturing ecosystems for solar and wind. This marks a significant milestone in India's journey towards sustainable energy, underlining our commitment to the Solar Alliance and the Atmanirbhar Bharat initiative,” he added. This Adani Group project is expected to add to India's green energy capacity, besides helping in reaching its climate action pledges it made at COP. During the COP26 summit in 2021, Prime Minister Narendra Modi in his address had said that India would achieve net zero carbon emissions by 2070. He also spelt out the five ‘amrit tatva’ from India. “At this global brainstorming on climate change, I present 5 'amrit tatva' from India. I gift this 'panchamrit'. First, India will bring its non-fossil energy capacity to 500 GW by 2030. Second, by 2030 India will fulfill 50 per cent of its energy requirement through renewable energy," the prime minister said. “Third, India will cut down its net projected carbon emission by 1 billion tonne from now until 2030. Fourth, by 2030, India will bring down carbon intensity of its economy by more than 45%. Fifth, by 2070 India will achieve the target of 'net zero,” he added.
#     """

#     print(f"Original Content :\n{content}")
#     summary= summarizer(content)
  
#     print(f"Summary Text:\n{summary}")



#**********************************************************************Sdosdsx****************************************************************************

from transformers import BartForConditionalGeneration, BartTokenizer
import torch

def load_bart_model(model_name="facebook/bart-large-cnn"):
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

def summarize_news(model, tokenizer, content_string, device):
    total_words = len(content_string.split())

    print(f"\n {total_words} \n")

    # Determine the max and min length for summary
    if total_words>200:
        new_max_length = total_words
        new_min_length = 180
    
    else:
        new_max_length = total_words
        new_min_length = total_words // 2

    print(f"Max Length:{new_max_length}, Minimum Length:{new_min_length}")

    # Determine the number of beams and length penalty
    if total_words >= 200:
        num_beams = 5
        length_penalty = 4.0
    elif total_words >= 150:
        num_beams = 4
        length_penalty = 2.0
    elif total_words >= 100:
        num_beams = 3
        length_penalty = 1.2
    else:
        num_beams = 2
        length_penalty = 1.0

    print(length_penalty, num_beams)

    # Move model and inputs to GPU
    model.to(device)
    inputs = tokenizer(content_string, return_tensors="pt", max_length=1024, truncation=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Perform inference on GPU
    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=int(new_max_length),
            min_length=int(new_min_length),
            num_beams=num_beams,
            length_penalty=length_penalty,
            early_stopping=True,
        )

    # Move output back to CPU if needed
    summary_ids = summary_ids.to("cpu")
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary_text

def summarizer(content):
    model, tokenizer = load_bart_model()

    # Check GPU availability
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("No GPU available, using CPU.")

    summary = summarize_news(model, tokenizer, content, device)

    return summary

if __name__ == "__main__":
    
    # Example usage:
    content = """ Shifting to election gear | Baghel blows the bugle The Chhattisgarh chief minister works towards a second term by sinking differences and using a mix of farm sector initiatives, soft Hindutva, cow and caste politics to get the voters on his side It's poll season in Chhattisgarh and Chief Minister Bhupesh Baghel is out to win friends and influence people. So when the Congress central leadership elevated his bete noire, health minister T.S. Singh Deo, as the deputy chief minister, Baghel welcomed the move.

    """

    print(f"Original Content : \n {content}")

    summary= summarizer(content)

    print(f"Summary Text:\n{summary}")
