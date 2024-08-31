import openai

class BackgroundCreator:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def create_background(self, id, job_title, hobby, favorit_food):
        # Directly create the prompt for DALL-E
        prompt = f"Create a background for the photo, on the background I will photograph a person. The background should have elements according to the person's favorite things. His profession is {job_title}, his hobby is {hobby} and his favorite food is {favorit_food}"

        try:
            # Generate an image using DALL-E via OpenAI API
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            return image_url

        except Exception as e:
            print(f"Error generating image: {e}")
            return None
