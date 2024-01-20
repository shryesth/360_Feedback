from transformers import pipeline
from summarize import summarizer


def analyze_sentiment(sequence, classifier):
    sentiment_labels = ["positive", "neutral", "negative"]
    sentiment_output = classifier(sequence, sentiment_labels)
    index_of_highest_sentiment_score = sentiment_output["scores"].index(
        max(sentiment_output["scores"])
    )
    sentiment_label_with_highest_score = sentiment_output["labels"][
        index_of_highest_sentiment_score
    ]
    return sentiment_label_with_highest_score


def classify_ministry(sequence, classifier):
    ministry_labels = [
        "Information and Broadcasting",
        "Agriculture",
        "Textiles",
        "Commerce & Industry",
        "Defence",
        "Finance",
        "Health and Family Welfare",
        "Home Affairs",
        "Housing and Urban Affairs",
        "Education",
        "Petroleum & Natural Gas",
        "Power",
        "Railways",
        "Road Transport & Highways",
        "Rural Development",
        "Urban Development",
        "Water Resources",
        "Women & Child Development",
        "Youth Affairs and Sports",
        "Coal",
        "Personnel, Public Grievances & Pensions",
        "Law & Justice",
        "Parliamentary Affairs",
        "Science & Technology",
        "Culture",
        "Steel",
        "Labour & Employment",
        "Communications",
        "Civil Aviation",
        "New and Renewable Energy",
        "Tourism",
        "Consumer Affairs, Food & Public Distribution",
        "Food Processing Industries",
        "chemicals and fertilizers",
        "Environment, Forest and Climate Change",
        "Shipping",
        "Mines",
        "Tribal Affairs",
        "Social Justice & Empowerment",
        "Micro,Small & Medium Enterprises",
        "Heavy Industries & Public Enterprises",
        "Statistics & Programme Implementation",
        "Development of North-East Region",
        "Minority Affairs",
        "Corporate Affairs",
        "Earth Science",
        "Skill Development and Entrepreneurship",
        "Department of Space",
        "Election Commission",
    ]

    ministry_output = classifier(sequence, ministry_labels)
    index_of_highest_ministry_score = ministry_output["scores"].index(
        max(ministry_output["scores"])
    )
    ministry_label_with_highest_score = ministry_output["labels"][
        index_of_highest_ministry_score
    ]
    return f"Ministry Of {ministry_label_with_highest_score}"


def print_results(input_text, sentiment_result, ministry_result):
    print(f"News Content : {input_text}")
    print("Sentiment:", sentiment_result)
    print("Ministry:", ministry_result)


def main():
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    sequence_to_classify = """ DNA Exclusive: Analysis Of Modi Government's New Guidelines For Coaching Centres In today's DNA, Zee News' analysed the new guidelines floated by government of India for coaching centres that prepare students for competitive exams. In today's DNA, Zee News' analysed the new guidelines floated by government of India for coaching centres that prepare students for competitive exams. Trending Photos The government has also admitted that coaching centres across the country, including Kota, that prepare students for various competitive exams like Neet, IIT and others, are violating the government’s rules and regulations. That is why the Ministry of Education has issued guidelines for coaching institutes across the country. In today's DNA, Zee News' analysed the new guidelines floated by government of India for coaching centres that prepare students for competitive exams. These guidelines are made for coaching centres that prepare students for competitive exams. Here are the big and important points from the news guidelies: DNA : 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस. दसवीं से पहले प्रतियोगी परीक्षाओं की कोचिंग बैन, नई गाइडलाइंस के बाद कितना बदलेगी कोचिंग इंडस्ट्री?#DNA #DNAWithSourabh #CoachingCentre @saurabhraajjain @vishalpandeyk pic.twitter.com/BlEhvMbdyV — Zee News (@ZeeNews) January 19, 2024 Coaching centres that prepare students for competitive exams will not give admission to students below 16 years of age. Now, students will be able to take admission in coaching centres only after passing their secondary exam, i.e. tenth class. Coaching centres cannot guarantee good marks and ranks. Teachers teaching in coaching centres should be at least graduates. No pressure will be put on children for good performance. Coaching classes should not be held during school hours. Coaching classes should not be more than five hours a day. Every coaching centre will have to take a day off in a week. No test will be taken on the next day of the weekly holiday. The results of the students’ tests will not be made public. The government says that the purpose of the new guidelines is to restrict the coaching centres that consider coaching as a business and are not afraid to do anything to increase their business. But after the implementation of the new guidelines the coaching centres will not be able to make misleading promises and claims of guaranteeing good marks. Watch Today's DNA For A Detailed Analysis On New Guidelines For Coaching Centres In India: स्थापित होने से पहले प्रतिमा के 'वर्चुअल दर्शन' 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस देखिए #DNA LIVE Sourabh Raaj Jain के साथ#ZeeLive #ZeeNews #DNAWithSourabh #RamMandir #Ayodhya #CoachingCentre @saurabhraajjain https://t.co/81OfjVcZGo — Zee News (@ZeeNews) January 19, 2024 In today's DNA, Zee News' analysed the new guidelines floated by government of India for coaching centres that prepare students for competitive exams. These guidelines are made for coaching centres that prepare students for competitive exams. Here are the big and important points from the news guidelies: DNA : 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस. दसवीं से पहले प्रतियोगी परीक्षाओं की कोचिंग बैन, नई गाइडलाइंस के बाद कितना बदलेगी कोचिंग इंडस्ट्री?#DNA #DNAWithSourabh #CoachingCentre @saurabhraajjain @vishalpandeyk pic.twitter.com/BlEhvMbdyV — Zee News (@ZeeNews) January 19, 2024 Coaching centres that prepare students for competitive exams will not give admission to students below 16 years of age. Now, students will be able to take admission in coaching centres only after passing their secondary exam, i.e. tenth class. Coaching centres cannot guarantee good marks and ranks. Teachers teaching in coaching centres should be at least graduates. No pressure will be put on children for good performance. Coaching classes should not be held during school hours. Coaching classes should not be more than five hours a day. Every coaching centre will have to take a day off in a week. No test will be taken on the next day of the weekly holiday. The results of the students’ tests will not be made public. The government says that the purpose of the new guidelines is to restrict the coaching centres that consider coaching as a business and are not afraid to do anything to increase their business. But after the implementation of the new guidelines the coaching centres will not be able to make misleading promises and claims of guaranteeing good marks. Watch Today's DNA For A Detailed Analysis On New Guidelines For Coaching Centres In India: स्थापित होने से पहले प्रतिमा के 'वर्चुअल दर्शन' 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस देखिए #DNA LIVE Sourabh Raaj Jain के साथ#ZeeLive #ZeeNews #DNAWithSourabh #RamMandir #Ayodhya #CoachingCentre @saurabhraajjain https://t.co/81OfjVcZGo — Zee News (@ZeeNews) January 19, 2024 DNA : 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस. दसवीं से पहले प्रतियोगी परीक्षाओं की कोचिंग बैन, नई गाइडलाइंस के बाद कितना बदलेगी कोचिंग इंडस्ट्री?#DNA #DNAWithSourabh #CoachingCentre @saurabhraajjain @vishalpandeyk pic.twitter.com/BlEhvMbdyV — Zee News (@ZeeNews) January 19, 2024 The government says that the purpose of the new guidelines is to restrict the coaching centres that consider coaching as a business and are not afraid to do anything to increase their business. But after the implementation of the new guidelines the coaching centres will not be able to make misleading promises and claims of guaranteeing good marks. Watch Today's DNA For A Detailed Analysis On New Guidelines For Coaching Centres In India: स्थापित होने से पहले प्रतिमा के 'वर्चुअल दर्शन' 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस देखिए #DNA LIVE Sourabh Raaj Jain के साथ#ZeeLive #ZeeNews #DNAWithSourabh #RamMandir #Ayodhya #CoachingCentre @saurabhraajjain https://t.co/81OfjVcZGo — Zee News (@ZeeNews) January 19, 2024 स्थापित होने से पहले प्रतिमा के 'वर्चुअल दर्शन' 'रियल कोटा फैक्ट्री' के लिए नई गाइडलाइंस देखिए #DNA LIVE Sourabh Raaj Jain के साथ#ZeeLive #ZeeNews #DNAWithSourabh #RamMandir #Ayodhya #CoachingCentre @saurabhraajjain https://t.co/81OfjVcZGo — Zee News (@ZeeNews) January 19, 2024 Live Tv Thank you By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. By clicking “Accept All Cookies”, you agree to the storing of cookies on your device and the processing of information obtained via those cookies (including about your preferences, device and online activity) by us and our commercial partners to enhance site navigation, personalise ads, analyze site usage, and assist in our marketing efforts. More information can be found in our Cookies and Privacy Policy. You can amend your cookie settings to reject non-essential cookies by clicking Cookie Settings below. Accept All Cookies Manage Consent Preferences These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work or you may not be able to login. These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly. These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They are also used to limit the number of times you see an advert as well as help measure the effectiveness of an advertising campaign. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we may not know when you have visited our site, and may not be able to monitor its performance. """
    analyze_and_classify(sequence_to_classify, classifier)


def analyze_and_classify(sequence, classifier):
    length_sequence = len(sequence.split())
    if length_sequence > 100:
        input_text = summarizer(sequence)
    else:
        input_text = sequence

    sentiment_result = analyze_sentiment(input_text, classifier)
    ministry_result = classify_ministry(input_text, classifier)

    print_results(input_text, sentiment_result, ministry_result)


if __name__ == "__main__":
    main()
