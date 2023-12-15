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

    sequence_to_classify = """ Lok Sabha expels Mahua Moitra amidst Opposition walkout. Though TMC had strongly argued to allow Ms. Moitra to speak on the floor of the House, Parliamentary Affairs Minister Prahlada Joshi quoted precedence to object. Speaker Om Birla put the resolution to vote without allowing her to speak. The Lok Sabha on December 8, 2023, expelled Trinamool Congress member Mahua Moitra over the "cash-for-query" allegation through a voice vote amid chaos. Union Parliamentary Affairs Minister Prahlada Joshi moved the motion to expel Ms. Moitra as per the recommendation of Ethics Committee report, which found her guilty of sharing her credentials with others, accepted gifts for favours from a businessman. Though Trinamool Congress had strongly argued to allow Mahua Moitra to speak on the floor of the House, Mr. Joshi quoted precedence to object. Speaker Om Birla put the resolution to vote without allowing her to speak. Opposition members walked out of the House even as the vote was being conducted. Earlier, Ethics Committee chairman Vinod Kumar Sonkar tabled the panel's first report when the House re-convened at noon after an adjournment during the Question Hour. Trinamool Congress members and some from the Congress trooped in the Well of the House raising slogans demanding a copy of the report. TMC fully supports Mahua Moitra: Mamata West Bengal Chief Minister Mamata Banerjee extended support to TMC leader Mahua Moira and expressed surprise that Ms. Moitra was not allowed to defend herself. She also thanked parties in INDIA alliance for backing Ms. Moitra. “Today I am really sad to see the attitude of BJP party. A 475 page report was submitted and after that they have half an hour time to go through it. I congratulate INDIA alliance that they supported her. Party fully supports Mahua Moitra. They didn’t allow Mahua to defend herself. It is betrayal of Constitutional rights. We have two third majority in Assembly does it mean we will expel someone,” said Ms. Banerjee. Mahua is a victim of circumstances and party is fully behind Mahua. I am shocked and it is sad day for Parliament. It is unacceptable and Mahua will win the battle. They will be defeated in next elections,” the TMC supremo added. Give at least 48 hours to study ethics panel report on Mahua Moitra: TMC Trinamool Congress MP Kalyan Banerjee had said the party has written to Lok Sabha Speaker Om Birla, urging him to give at least 48 hours to read the ethics panel report. However, the resolution was taken up for discussion after the House assembled after lunch. The Lok Sabha witnessed two adjournments on Friday over the report amid Opposition protests. Amid uproar, BJP member Rajendra Agrawal, who was in the chair, adjourned the proceedings till 2 p.m. Businessman Darshan Hiranandani, who allegedly paid Ms. Moitra to raise questions in Parliament about the Adani Group, had claimed in a signed affidavit that Mahua Moitra targeted industrialist Gautam Adani to "malign and embarrass" Prime Minister Narendra Modi. At a meeting on November 9, the Committee adopted its report recommending Ms. Moitra's expulsion from the Lok Sabha over the "cash-for-query" allegation. Six members of the panel, including suspended Congress member Preneet Kaur, voted in favour of the report. Four members of the panel belonging to opposition parties submitted dissent notes. The Opposition members termed the report a "fixed match" and said the complaint filed by BJP Lok Sabha member Nishikant Dubey, which the panel reviewed, was not supported by a "shred of evidence". Ms. Moitra can be expelled only if the House votes in favour of the panel's recommendation. Ethics panel report a political vendetta: TMC MP Sudip Bandyopadhyay Trinamool Congress leader in Lok Sabha Sudip Bandyopadhyay described the Ethics Committee’s recommendation to expel party MP Mahua Moitra in a “cash-for-query” allegation as “political vendetta” and claimed that it was aimed at stopping her from raising issues against the Adani Group. Mr. Bandyopadhyay said he had a one-on-one meeting with Lok Sabha Speaker Om Birla, who informed him that the report would be tabled along with a resolution. He told the Speaker that Ms. Moitra should be given time to make her speech on the floor of the House to which Mr. Birla replied that half an hour would be given for discussion on the matter. Mr. Bandyopadhyay asked why was the MP who alleged that Ms. Moitra was paid cash for asking questions not called to the Ethics Committee meeting. “The first meeting (of the ethics panel) ended in a short time and could not produce any result. Why was a second meeting not held? Why such a hurry?” he posed. Mr. Bandyopadhyay also asked why was the report being tabled on a Friday, which is dedicated to Private Members’ Business. “It could have been introduced on Monday... Everywhere we find there is some motivation. We can say it is absolute political vendetta,” he said. Mr. Bandyopadhyay claimed that the government was “unable to digest Ms. Moitra’s allegation against the Adani group. “They want her to be stopped.” “The whole country has seen how the first meeting started and ended. This projection of the outcome and result of the meeting cannot go to the extent that one Member of Parliament is expelled,” he added.
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

