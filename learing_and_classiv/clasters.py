from sklearn.cluster import KMeans

def cluster_reviews(reviews, num_clusters=3):
    embeddings = model.encode(reviews)
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(embeddings)
    return clusters

# Пример использования
for book in books:
    clusters = cluster_reviews(book["reviews"])
    book["clustered_reviews"] = {}
    for i, cluster in enumerate(clusters):
        if cluster not in book["clustered_reviews"]:
            book["clustered_reviews"][cluster] = []
        book["clustered_reviews"][cluster].append(book["reviews"][i])

def summarize_clustered_reviews(clustered_reviews):
    summaries = {}
    for cluster, reviews in clustered_reviews.items():
        text = " ".join(reviews)
        summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
        summaries[cluster] = summary[0]["summary_text"]
    return summaries

# Пример использования
for book in books:
    book["summarized_reviews"] = summarize_clustered_reviews(book["clustered_reviews"])

from sklearn.feature_extraction.text import TfidfVectorizer

def generate_tags(descriptions, top_n=5):
    vectorizer = TfidfVectorizer(max_features=100)
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    feature_names = vectorizer.get_feature_names_out()
    tags = []
    for i in range(len(descriptions)):
        tfidf_scores = tfidf_matrix[i].toarray().flatten()
        top_indices = tfidf_scores.argsort()[-top_n:][::-1]
        tags.append([feature_names[idx] for idx in top_indices])
    return tags

# Пример использования
descriptions = [book["description"] + " " + " ".join(book["reviews"]) for book in books]
tags = generate_tags(descriptions)
for i, book in enumerate(books):
    book["tags"] = tags[i]

def analyze_sentiment(reviews):
    sentiments = sentiment_analyzer(reviews)
    positive_count = sum(1 for s in sentiments if s['label'] == 'POSITIVE')
    negative_count = sum(1 for s in sentiments if s['label'] == 'NEGATIVE')
    return positive_count, negative_count

# Пример использования
for book in books:
    positive, negative = analyze_sentiment(book["reviews"])
    book["sentiment"] = {"positive": positive, "negative": negative}