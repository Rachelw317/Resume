from core.model import get_deepseek
from schemas.resumeTemplate import Resume

model = get_deepseek()

response = model.invoke(
    "你是一个资深HR，擅长简历优化."
)

print(response.content)