import json
import re

def clean_json_string(s):
    # Remove newlines and other control characters
    s = re.sub(r'[\n\r\t]', ' ', s)
    
    # Replace multiple spaces with a single space
    s = re.sub(r' +', ' ', s)
    
    # Fix spaced out words
    def fix_spaced(match):
        return match.group(0).replace(" ", "")
    
    # This is aggressive but might be needed for this specific PDF
    s = re.compile(r'(?:[a-zA-Z] ){2,}[a-zA-Z]').sub(fix_spaced, s)
    
    # Remove spaces around structural characters
    s = re.sub(r'\s*([\{\}\[\]\:,])\s*', r'\1', s)
    
    # Final trim
    s = s.strip()
    
    return s

def main():
    try:
        with open('/home/ubuntu/raw_json_extract.txt', 'r') as f:
            raw = f.read()
        
        cleaned = clean_json_string(raw)
        
        try:
            data = json.loads(cleaned)
            with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                json.dump(data, f, indent=2)
            print("Successfully cleaned and parsed JSON!")
        except json.JSONDecodeError as e:
            print(f"Cleaned parse failed: {e}")
            with open('/home/ubuntu/cleaned_json_attempt.txt', 'w') as f:
                f.write(cleaned)
            start = max(0, e.pos - 50)
            end = min(len(cleaned), e.pos + 50)
            print(f"Context: ...{cleaned[start:end]}...")
            
    except FileNotFoundError:
        print("raw_json_extract.txt not found.")

if __name__ == "__main__":
    main()
