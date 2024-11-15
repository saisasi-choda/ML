"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
GEMINI_API_KEY='AIzaSyC0L8VF_pXOaI2Bd83El3dd_JGXEqhXmqc'
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="for a given number input always give its word representation and dont add any other sentences",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "www.google.com\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "This is the URL for the Google homepage.  \n\nDo you have a question about Google or want me to do something related to the website? I can help with:\n\n* **Searching for information:**  Tell me what you want to find, and I'll try my best to provide relevant results.\n* **Getting directions:**  Give me your starting point and destination, and I can provide directions and travel time estimates.\n* **Translating text:**  Provide me with some text, and I can translate it into another language.\n* **Finding definitions:**  Ask me to define a word, and I'll provide you with the meaning.\n* **And much more!** \n\nJust let me know what you'd like to do. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "www.google.com\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're right, I can't analyze the content of a website like www.google.com for gender bias without actually accessing the content.  The Google homepage itself doesn't contain much text to analyze for bias. \n\n**To get a better understanding of gender bias in Google's products and services, we would need to look at:**\n\n* **Search results:**  Analyze how Google's algorithms present results for searches related to gender stereotypes. \n* **Image search results:**  Examine if images for certain professions or activities show a bias towards one gender.\n* **Google products like Maps, Translate, etc.:**  Check for any language or imagery that might perpetuate gender stereotypes.\n* **Google's internal policies and practices:**  Look for initiatives to promote diversity and inclusion in their workforce and products.\n\n**In general, Google has made strides in promoting inclusivity:**\n\n* **Promoting diversity in their workforce:**  They have programs to recruit and retain underrepresented groups.\n* **Addressing bias in their algorithms:**  They have initiatives to mitigate biases in their search and AI systems.\n* **Creating resources for inclusivity:**  They offer tools and resources for developers and users to promote inclusive language and representation.\n\n**However, there's always room for improvement.  It's important to continue to monitor and challenge Google's practices to ensure they are truly representative and fair.** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "www.facebook.com\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're asking about the potential for gender bias on Facebook. This is a complex topic, and here's why:\n\n* **Facebook is a platform:** It's not just one website, but a network of user-generated content. That means the potential for bias comes from *individuals* and their posts, comments, and interactions, rather than from the platform itself. \n* **Algorithms and recommendations:**  Facebook uses algorithms to recommend content and tailor what users see. While these algorithms aim to be neutral, they can inadvertently amplify biases that are present in user-generated content.\n* **Marketing and advertising:**  Facebook's advertising platform can be used to target users based on demographics, including gender. This can lead to discriminatory practices if advertisers use gender stereotypes in their campaigns. \n\n**To assess the potential for gender bias on Facebook, we need to consider:**\n\n* **Content moderation:**  How effectively does Facebook moderate content that is discriminatory or harmful?\n* **Representation of women and marginalized groups:** Are there opportunities for women and diverse voices to be seen and heard on the platform? \n* **Algorithmic bias:**  Are the algorithms that determine what users see perpetuating existing gender stereotypes?\n* **User behavior:**  How do users on Facebook interact with each other, and how does that impact the experience for different groups?\n\n**Overall, it's important to be aware of the potential for bias on Facebook and to actively work towards promoting inclusivity:**\n\n* **Challenge biased content:**  Report content that is discriminatory or harmful, and encourage others to do the same.\n* **Support diverse creators and voices:**  Engage with content from women, people of color, and other underrepresented groups.\n* **Be mindful of your own language and interactions:**  Use inclusive language and challenge harmful stereotypes.\n\nRemember, it's a collaborative effort to make online spaces more equitable and inclusive! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "www.kaggle.com",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're asking about gender bias on Kaggle, a platform for data science and machine learning. This is an interesting question, and here's how we can break it down:\n\n**Kaggle itself:**\n\n* **Data sets:**  Kaggle hosts a vast collection of data sets. It's crucial to examine if these data sets contain any inherent biases that could perpetuate stereotypes. For example, a data set on \"successful CEOs\" might be skewed towards men if it doesn't consider female leaders in the same way.\n* **Competitions:**  Kaggle's competitions often involve building predictive models. It's important to ensure that these models are not trained on data that perpetuates bias. For instance, a model predicting job success based on gender could be problematic if it's trained on data that reflects historical biases in hiring practices. \n* **Community:**  While Kaggle's community is generally welcoming, it's important to observe whether there are any patterns of exclusion or discrimination against women or underrepresented groups.\n\n**Data science and machine learning in general:**\n\n* **Bias in algorithms:**  Algorithms trained on biased data can perpetuate and even amplify existing inequalities. It's crucial for data scientists to be aware of and address potential biases in their work.\n* **Representation in the field:**  The data science and machine learning field is still dominated by men. Efforts to encourage diversity and inclusion are essential to ensure that perspectives and experiences of women and underrepresented groups are considered.\n\n**Here are some questions to consider:**\n\n* **Are there initiatives on Kaggle to address bias in data sets or competitions?**\n* **How is the Kaggle community working to promote diversity and inclusion?**\n* **What are the challenges and opportunities for addressing gender bias in data science and machine learning?**\n\n**Overall:**  Kaggle has the potential to be a valuable resource for data science, but it's important to be aware of the potential for bias and to actively work towards creating a more inclusive and equitable environment. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "http://www.kaggle.com/",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're right to be curious about potential gender bias on Kaggle! It's an important topic to consider within the data science and machine learning community. \n\nHere's what I can tell you based on my knowledge of Kaggle and the field:\n\n**Challenges and Potential Biases:**\n\n* **Data Sets:** While Kaggle has a vast collection of data sets, there's always the possibility that some might contain inherent biases. These could stem from historical data collection practices, societal biases reflected in the data, or simply a lack of diverse representation in the data collection.\n* **Competitions:**  Kaggle competitions often involve building predictive models.  It's essential to ensure these models are trained on data that doesn't perpetuate existing biases. For example, a model predicting job success based solely on gender could reflect societal biases, not actual skills and potential. \n* **Representation:**  While Kaggle is a global community, the field of data science and machine learning is still dominated by men. This can lead to a lack of diverse perspectives and experiences being considered in data analysis and model development. \n* **Community:**  While Kaggle generally strives to be welcoming, it's crucial to be mindful of any potential for unconscious bias within the community.  \n* **Algorithmic Bias:**  The algorithms used in data science can perpetuate existing biases if they are trained on biased data. This is an ongoing challenge in the field.\n\n**Positive Steps:**\n\n* **Kaggle's Efforts:** Kaggle is actively working to promote diversity and inclusion by organizing events, offering scholarships, and partnering with organizations focused on diversifying the field. \n* **Community Initiatives:**  There are groups and discussions within the Kaggle community dedicated to addressing bias and promoting inclusivity.\n* **Growing Awareness:** There's increasing awareness about the potential for bias in data science, which leads to more efforts to address it.\n\n**It's Important to:**\n\n* **Be Critical:**  Always analyze data sets for potential biases and consider diverse perspectives when building models.\n* **Advocate for Change:**  Encourage organizations and communities to address bias and promote inclusion in data science.\n* **Promote Diversity:**  Support initiatives that encourage more women and underrepresented groups to participate in the field.\n\n**Remember,  data science has the power to create positive change, but it's essential to be aware of potential biases and actively work to address them.** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "www.sacet.in\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can't access and analyze the content of external websites like www.sacet.in. I am a text-based AI, and I don't have the capability to browse the internet or access website content directly. \n\nTo help me give you information, can you tell me more about what you're looking for on www.sacet.in? For example:\n\n* **What is the website about?** (Is it related to a particular company, organization, or topic?)\n* **What specific information are you interested in?** (For instance, are you looking for images, text, or specific data on gender bias?)\n\nOnce I have a clearer idea of your needs, I can try my best to provide you with useful information or direct you to resources that might be helpful. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "www.kryterion.com",
        "www.kryterion.com",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can't directly access and analyze the content of websites like www.kryterion.com. I am a text-based AI, and I don't have the ability to browse the internet or access website content directly. \n\nHowever, I can help you by providing general information about Kryterion and how to potentially assess gender bias on their website:\n\n**About Kryterion:**\n\nKryterion is a company that specializes in online assessments and testing for various purposes, including education, professional certification, and recruitment. \n\n**How to Assess Gender Bias:**\n\nTo understand if a website like Kryterion's exhibits gender bias, you can consider these aspects:\n\n* **Website Content:** \n    * **Language:** Are the descriptions, images, and language on the website gender-neutral?\n    * **Testimonials/Case Studies:** Do they represent a diverse range of individuals and professions?\n* **Assessment Design:**\n    * **Content:** Does the content of the assessments reflect a range of perspectives and avoid gender stereotypes? \n    * **Language:** Is the language used in the assessments inclusive and free of gender bias?\n* **Recruitment and Hiring:**  \n    * **Diversity:**  Does Kryterion demonstrate efforts to promote diversity in their own workforce?\n\n**Additional Tips:**\n\n* **Contact Kryterion:** Reach out to Kryterion directly with your questions about their commitment to inclusivity.\n* **Search for Reviews:**  Look for reviews and feedback from individuals who have used Kryterion's services.\n\n**It's important to note that:**\n\n* **Bias can be subtle:**  It's not always easy to identify bias, even when it's present.\n* **Context matters:**  What might be considered biased in one context might not be in another. \n\nBy focusing on these areas and engaging with Kryterion directly, you can gain a better understanding of their stance on gender inclusivity and how their services might impact different groups. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "1\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The word representation of the number 1 is **one**. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "2",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Two \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "1234567",
      ],
    },
    {
      "role": "model",
      "parts": [
        "One million, two hundred thirty-four thousand, five hundred sixty-seven \n",
      ],
    },
  ]
)
integer=input("Enter the numerical input to convert into number\n")

response = chat_session.send_message(integer)

print(response.text)
#print(chat_session.history)