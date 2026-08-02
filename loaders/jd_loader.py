from pathlib import Path

def load_jd(file_path:str)->str:
    
    with open(file_path, "r", encoding="utf-8") as f:
            jd_text = f.read() 
            
    return jd_text