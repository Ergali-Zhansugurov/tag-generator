import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
from internal.db.postgres import tagrepo


class GenerateTags:
    def __init__(self, model_name: str = 'google/mt5-small', repo: tagrepo = None, threshold: float = 0.7):
        self.model = MT5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = MT5Tokenizer.from_pretrained(model_name)
        self.repo = repo
        self.threshold = threshold  

    def execute(self, reviews: list[str]):
        combined_reviews = " ".join(reviews)
        input_text = f"generate tags: {combined_reviews}"
        inputs = self.tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

        outputs = self.model.generate(
            inputs['input_ids'], 
            max_length=50, 
            num_beams=5, 
            return_dict_in_generate=True, 
            output_scores=True
        )

        scores = torch.exp(outputs.sequences_scores)  
        tags = [self.tokenizer.decode(output, skip_special_tokens=True).strip() for output in outputs.sequences]

        filtered_tags = [tag for tag, score in zip(tags, scores) if score >= self.threshold]

        self.repo.save_tags(filtered_tags)
        self.repo.save_book_tags(filtered_tags)
        print(filtered_tags)
        return filtered_tags