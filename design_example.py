from juji_python_sdk import design

# from juji_python_sdk import design

engagement_id = "67bac9c2-71eb-4a73-ae2e-3135f75ac3df"

# Set the browser key
browser_key_response = design.set_browser_key(engagement_id)
browser_key = browser_key_response["browser_key"]

# Get all brands
brands = design.get_brands()
print(brands)

# Add a FAQ to the chatbot
resp = design.add_faq(["Where can I find some ice cream?",
                       "Where can I buy some ice cream?"], 
                      ["We have the best ice cream in the world!"], 
                      engagement_id, 
                      browser_key)
print(resp)
