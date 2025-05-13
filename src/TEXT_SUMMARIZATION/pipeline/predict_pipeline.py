# from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
# from transformers import AutoTokenizer
# from transformers import pipeline

# class PredictionPipeline:
#     def __init__(self):
#         self.config = ConfigurationManager().get_model_trainer_config()

#     def predict(self,text):
#         tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
#         gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

#         pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

#         print("Dialogue:")
#         print(text)

#         output = pipe(text, **gen_kwargs)[0]["summary_text"]
#         print("\nModel Summary:")
#         print(output)

#         return output
from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_trainer_config()

    def predict(self, text: str) -> str:
        try:
            # Load the tokenizer
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            
            # Define generation parameters
            gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
            
            # Load the summarization pipeline
            summarization_pipeline = pipeline(
                "summarization", 
                model=self.config.model_path, 
                tokenizer=tokenizer
            )
            
            # Print input text
            print("Dialogue:")
            print(text)
            
            # Generate summary
            output = summarization_pipeline(text, **gen_kwargs)[0]["summary_text"]
            
            # Print summary
            print("\nModel Summary:")
            print(output)
            
            return output
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise e

    
