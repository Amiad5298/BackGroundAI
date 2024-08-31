import pandas as pd
from BackgroundCreator import BackgroundCreator

class ExcelManager:
    def __init__(self, file_path, openai_api_key):
        self.file_path = file_path
        self.background_creator = BackgroundCreator(openai_api_key)
    
    def process_excel(self):
        try:
            # Read the Excel file
            df = pd.read_excel(self.file_path)

            # Extract data from specific columns
            data = df[['FirstName', 'LastName', 'PhoneNumber', 'Id', 'JobTitle', 'Hobby', 'FavoritFood']].to_dict(orient='records')

            # Generate background (description or image URL) for each row
            for row in data:
                background = self.background_creator.create_background(
                    row['Id'],
                    row['JobTitle'],
                    row['Hobby'],
                    row['FavoritFood']
                )
                row['Background'] = background  # Store the generated background (description or URL) in the data

            return data
        except Exception as e:
            print(f"Error processing Excel file: {e}")
            return None
