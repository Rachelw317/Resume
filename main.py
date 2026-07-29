from dotenv import load_dotenv
from Model import get_DeepSeek
from Message import messages

load_dotenv()

model = get_DeepSeek()
response = model.invoke(messages)
print(response)
