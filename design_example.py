# from juji_python_sdk.design import JujiDesign
import dotenv
import os

from juji_python_sdk import JujiDesign

dotenv.load_dotenv()

JUJI_PLATFORM_URL = os.getenv("JUJI_PLATFORM_URL", "https://juji.ai")

JUJI_API_KEY = os.getenv("JUJI_API_KEY", "your juji api key")
if JUJI_API_KEY == "your juji api key":
    raise ValueError("JUJI_API_KEY is not set. Please set it in your environment variables.")

design = JujiDesign(JUJI_API_KEY, JUJI_PLATFORM_URL)

engagement_id = "67bac9c2-71eb-4a73-ae2e-3135f75ac3df"

# Set the browser key
browser_key_response = design.set_browser_key(engagement_id)
browser_key = browser_key_response["browser_key"]

# Get all brands
brands = design.get_brands()
print(brands)

# Add a FAQ to the chatbot
resp = design.add_faq(["Where can I buy some tomatoes?"], 
                      ["We have the best tomatoes in the world!"], 
                      engagement_id, 
                      browser_key)
print(resp)
