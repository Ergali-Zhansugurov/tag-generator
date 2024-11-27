from flask import Flask, request, jsonify
from internal.core.usecases.gen_tags import GenerateTags
app = Flask(__name__)
tag_generator = GenerateTags()

@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    data = request.get_json()
    review_text = data.get('review_text')
    book_id = data.get('book_id')

    tags = tag_generator.generate_tags(review_text)
    save_tags_to_db(book_id, tags) # type: ignore

    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(debug=True)