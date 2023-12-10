from transformers import pipeline

from summarizer import summarizer



def analyze_sentiment(sequence,classifier):

    sentiment_labels = ['positive', 'neutral', 'negative']

    sentiment_output = classifier(sequence, sentiment_labels, multi_label=True)

    print(sentiment_output)
    
    index_of_highest_sentiment_score = sentiment_output['scores'].index(max(sentiment_output['scores']))

    sentiment_label_with_highest_score = sentiment_output['labels'][index_of_highest_sentiment_score]
    
    return sentiment_label_with_highest_score


def classify_ministry(sequence,classifier):

    ministry_labels = ['Information and Broadcasting',
    'Agriculture',
    'Textiles',
    'Commerce & Industry','Defence',
    'Finance',
    'Health and Family Welfare',
    'Home Affairs',
    'Housing and Urban Affairs',
    'Education',
    'Petroleum & Natural Gas',
    'Power',
    'Railways',
    'Road Transport & Highways',
    'Rural Development',
    'Urban Development',
    'Water Resources',
    'Women & Child Development',
    'Youth Affairs and Sports',
    'Coal',
    'Personnel, Public Grievances & Pensions',
    'Law & Justice',
    'Parliamentary Affairs',
    'Science & Technology',
    'Culture',
    'Steel',
    'Labour & Employment',
    'Communications',
    'Civil Aviation',
    'New and Renewable Energy',
    'Tourism',
    'Consumer Affairs, Food & Public Distribution',
    'Food Processing Industries',
    'chemicals and fertilizers',
    'Environment, Forest and Climate Change',
    'Shipping',
    'Mines',
    'Tribal Affairs',
    'Social Justice & Empowerment',
    'Micro,Small & Medium Enterprises',
    'Heavy Industries & Public Enterprises',
    'Statistics & Programme Implementation',
    'Development of North-East Region',
    'Minority Affairs',
    'Corporate Affairs',
    'Earth Science',
    'Skill Development and Entrepreneurship',
    'Department of Space',
    'Election Commission']

    ministry_output = classifier(sequence, ministry_labels, multi_label=True)

    print(ministry_output)

    index_of_highest_ministry_score = ministry_output['scores'].index(max(ministry_output['scores']))

    ministry_label_with_highest_score = ministry_output['labels'][index_of_highest_ministry_score]

    return f"Ministry Of {ministry_label_with_highest_score}"


if __name__ == "__main__":

    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    sequence_to_classify = """ Adani Group setting up world's largest green energy park in Gujarat, will generate 30GW of power This Adani Group project is expected to add to India's green energy capacity, besides helping in reaching its climate action pledges it made at COP The Adani Group is setting up the world's largest green energy park in the Rann of Kutch desert in Gujarat, Gautam Adani said on Thursday. The chairman of the business conglomerate took to social media platform X and share pictures of the under-construction plant, stating that it will cover a vast 726 square kilometres land mass and generate 30 GW of power. "Proud to play a crucial role in India's impressive strides in renewable energy as we build the world's largest green energy park. This monumental project, covering 726 sq km in the challenging Rann desert, is visible even from space. We will generate 30GW to power over 20 million homes," Adani posted on X. “Also, just 150 km away, in our karmabhoomi Mundra, we are creating one of the globe's most extensive and integrated renewable energy manufacturing ecosystems for solar and wind. This marks a significant milestone in India's journey towards sustainable energy, underlining our commitment to the Solar Alliance and the Atmanirbhar Bharat initiative,” he added. This Adani Group project is expected to add to India's green energy capacity, besides helping in reaching its climate action pledges it made at COP. During the COP26 summit in 2021, Prime Minister Narendra Modi in his address had said that India would achieve net zero carbon emissions by 2070. He also spelt out the five ‘amrit tatva’ from India. “At this global brainstorming on climate change, I present 5 'amrit tatva' from India. I gift this 'panchamrit'. First, India will bring its non-fossil energy capacity to 500 GW by 2030. Second, by 2030 India will fulfill 50 per cent of its energy requirement through renewable energy," the prime minister said. “Third, India will cut down its net projected carbon emission by 1 billion tonne from now until 2030. Fourth, by 2030, India will bring down carbon intensity of its economy by more than 45%. Fifth, by 2070 India will achieve the target of 'net zero,” he added.
    """
    length_sequence = len(sequence_to_classify.split())

    if length_sequence>100:
        input_text = summarizer(sequence_to_classify)
        print(f"News Content : {input_text}")

        sentiment_result = analyze_sentiment(input_text,classifier)
        print("Sentiment:", sentiment_result)

        ministry_result = classify_ministry(input_text,classifier)
        print("Ministry:", ministry_result)
    
    else:
        print(f"News Content : {sequence_to_classify}")
        sentiment_result = analyze_sentiment(sequence_to_classify,classifier)
        print("Sentiment:", sentiment_result)

        ministry_result = classify_ministry(sequence_to_classify,classifier)
        print("Ministry:", ministry_result)

