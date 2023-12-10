from transformers import pipeline

from summarizer import summarizer



def analyze_sentiment(sequence,classifier):

    sentiment_labels = ['positive', 'neutral', 'negative']

    sentiment_output = classifier(sequence, sentiment_labels)
    
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

    ministry_output = classifier(sequence, ministry_labels)

    index_of_highest_ministry_score = ministry_output['scores'].index(max(ministry_output['scores']))

    ministry_label_with_highest_score = ministry_output['labels'][index_of_highest_ministry_score]

    return f"Ministry Of {ministry_label_with_highest_score}"


if __name__ == "__main__":

    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    sequence_to_classify = """ Kolkata High Court's Advice To Girls For Controlling Sexual Desire Irks Supreme Court The court appointed advocate Madhavi Diwan as Amicus Curiae and sought clarification from the state government if they intend to file an appeal against the High Court's decision. The court appointed advocate Madhavi Diwan as Amicus Curiae and sought clarification from the state government if they intend to file an appeal against the High Court's decision. Trending Photos Reporter: Arvind Singh The Supreme Court has expressed displeasure over the Kolkata High Court's advice to girls suggesting them to control their desire for sex. The SC emphasized that courts should refrain from offering personal opinions or advice while delivering judgments and stated that the High Court's comments were highly objectionable and unnecessary, constituting a violation of fundamental rights under Article 21. The court appointed advocate Madhavi Diwan as Amicus Curiae and sought clarification from the state government if they intend to file an appeal against the High Court's decision. The government's counsel is directed to inform the court about their stance. Previously, the Kolkata High Court, in a ruling regarding a case of sexual harassment with a minor, had stated that girls should control their desire for sex and not focus on fleeting pleasures, which the Supreme Court found objectionable. Additionally, the court had advised boys to respect the dignity of girls. The accused boy, after making statements acknowledging consensual sexual relations with the girl, was acquitted of charges related to the POCSO Act. The High Court had underscored the importance of parental guidance for teenagers and advocated for comprehensive sex education. It stressed the inclusion of topics such as reproductive health, hygiene, and related aspects as essential components in the curriculum of every school. The Supreme Court has expressed displeasure over the Kolkata High Court's advice to girls suggesting them to control their desire for sex. The SC emphasized that courts should refrain from offering personal opinions or advice while delivering judgments and stated that the High Court's comments were highly objectionable and unnecessary, constituting a violation of fundamental rights under Article 21. The court appointed advocate Madhavi Diwan as Amicus Curiae and sought clarification from the state government if they intend to file an appeal against the High Court's decision. The government's counsel is directed to inform the court about their stance. Previously, the Kolkata High Court, in a ruling regarding a case of sexual harassment with a minor, had stated that girls should control their desire for sex and not focus on fleeting pleasures, which the Supreme Court found objectionable. Additionally, the court had advised boys to respect the dignity of girls. The accused boy, after making statements acknowledging consensual sexual relations with the girl, was acquitted of charges related to the POCSO Act. The High Court had underscored the importance of parental guidance for teenagers and advocated for comprehensive sex education. It stressed the inclusion of topics such as reproductive health, hygiene, and related aspects as essential components in the curriculum of every school. The court appointed advocate Madhavi Diwan as Amicus Curiae and sought clarification from the state government if they intend to file an appeal against the High Court's decision. The government's counsel is directed to inform the court about their stance. Previously, the Kolkata High Court, in a ruling regarding a case of sexual harassment with a minor, had stated that girls should control their desire for sex and not focus on fleeting pleasures, which the Supreme Court found objectionable. Additionally, the court had advised boys to respect the dignity of girls. The accused boy, after making statements acknowledging consensual sexual relations with the girl, was acquitted of charges related to the POCSO Act. The High Court had underscored the importance of parental guidance for teenagers and advocated for comprehensive sex education. It stressed the inclusion of topics such as reproductive health, hygiene, and related aspects as essential components in the curriculum of every school. Previously, the Kolkata High Court, in a ruling regarding a case of sexual harassment with a minor, had stated that girls should control their desire for sex and not focus on fleeting pleasures, which the Supreme Court found objectionable. Additionally, the court had advised boys to respect the dignity of girls. The accused boy, after making statements acknowledging consensual sexual relations with the girl, was acquitted of charges related to the POCSO Act. The High Court had underscored the importance of parental guidance for teenagers and advocated for comprehensive sex education. It stressed the inclusion of topics such as reproductive health, hygiene, and related aspects as essential components in the curriculum of every school. The High Court had underscored the importance of parental guidance for teenagers and advocated for comprehensive sex education. It stressed the inclusion of topics such as reproductive health, hygiene, and related aspects as essential components in the curriculum of every school. Live Tv Thank you By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. By clicking “Accept All Cookies”, you agree to the storing of cookies on your device and the processing of information obtained via those cookies (including about your preferences, device and online activity) by us and our commercial partners to enhance site navigation, personalise ads, analyze site usage, and assist in our marketing efforts. More information can be found in our Cookies and Privacy Policy. You can amend your cookie settings to reject non-essential cookies by clicking Cookie Settings below. Accept All Cookies Manage Consent Preferences These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work or you may not be able to login. These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly. These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They are also used to limit the number of times you see an advert as well as help measure the effectiveness of an advertising campaign. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we may not know when you have visited our site, and may not be able to monitor its performance.
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

