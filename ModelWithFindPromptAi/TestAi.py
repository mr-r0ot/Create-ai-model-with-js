import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("data.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]


prompts = [item['prompt'] for item in dataset]


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(prompts)

def GenText(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, tfidf_matrix)[0]


    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score < 0.2:
        return "🤖 متوجه نشدم! لطفاً واضح‌تر بپرس."
    
    return dataset[best_index]['completion']


if __name__ == "__main__":
    print("🤖 هوش مصنوعی آماده پاسخگویی است. برای خروج Ctrl+C بزنید.\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        response = GenText(user_input)
        print("Bot:", response)
