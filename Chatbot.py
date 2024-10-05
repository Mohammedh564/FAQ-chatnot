import spacy 
import streamlit as st
nlp=spacy.load("en_core_web_sm")
FAQS = {
    "What is your return policy?": "Our return policy lasts 30 days.",
    "How do I track my order?": "You can track your order using the tracking number sent to your email.",
    "Do you ship internationally?": "Yes, we ship internationally to over 50 countries.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and more."
}
def faq_detct(userInput):
    user_doc=nlp(userInput)
    maxSimilarety=0
    for ques in FAQS.keys():
        faqQues=nlp(ques)
        similarety= user_doc.similarity(faqQues)
        if similarety>maxSimilarety :
            maxSimilarety=similarety
            bestQues=ques
    if bestQues:
        return FAQS[bestQues]
    else:
        return "Sorry, I couldn't find an answer to your question."
st.title("FAQ chatbot")
st.write("What is your question ? ")
user_input=st.text_area("Type your question here:")
if st.button("ASK"):
    st.write(faq_detct(user_input))