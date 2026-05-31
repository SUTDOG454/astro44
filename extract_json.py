import json
import re
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

def main():
    pdf_path = "/home/ubuntu/upload/BasedontheprovidedJSONfiles,I'vecreatedaunifiedastrologyframeworkthatsynthesizesallthecontentintoacomprehensivestructure.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    # The PDF text has double spaces and other artifacts
    # Let's try to find the JSON by looking for the key with flexible spacing
    pattern = r'\{\s*"\s*unified_astrological_framework\s*"\s*:'
    match = re.search(pattern, text)
    
    if match:
        start_index = match.start()
        brace_count = 0
        json_chars = []
        for i in range(start_index, len(text)):
            char = text[i]
            json_chars.append(char)
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    break
        
        json_str = "".join(json_chars)
        
        # Clean up the JSON string: 
        # 1. Remove extra spaces between characters in keys/values
        # This is tricky. Let's try to normalize it.
        
        # Actually, let's try to just parse it after removing newlines and multiple spaces
        normalized_json = re.sub(r'\s+', ' ', json_str)
        # Fix common issues like " t i t l e " -> "title"
        # This is hard to do perfectly without knowing the keys.
        # Let's try a simpler approach: remove spaces if they are between letters in what should be a word
        
        # Try to parse the normalized one first
        try:
            data = json.loads(normalized_json)
            with open("/home/ubuntu/astrology_framework.json", "w") as f:
                json.dump(data, f, indent=2)
            print("Successfully extracted JSON!")
            return
        except json.JSONDecodeError as e:
            print(f"Initial parse failed: {e}")
            # Save for manual inspection or further processing
            with open("/home/ubuntu/raw_json_extract.txt", "w") as f:
                f.write(json_str)
            
            # Try to fix the "spaced out" words
            # Example: " t i t l e " -> "title"
            # We can use a regex to find sequences of single letters separated by spaces
            def fix_spaced_words(match):
                return match.group(0).replace(" ", "")
            
            fixed_json = re.sub(r'(?:[a-zA-Z]\s){2,}[a-zA-Z]', fix_spaced_words, json_str)
            # Also fix double spaces
            fixed_json = re.sub(r'\s+', ' ', fixed_json)
            
            try:
                data = json.loads(fixed_json)
                with open("/home/ubuntu/astrology_framework.json", "w") as f:
                    json.dump(data, f, indent=2)
                print("Successfully extracted JSON after fixing spaced words!")
                return
            except json.JSONDecodeError as e:
                print(f"Second parse failed: {e}")
                with open("/home/ubuntu/fixed_json_attempt.txt", "w") as f:
                    f.write(fixed_json)

    print("Could not find the start of the JSON framework.")

if __name__ == "__main__":
    main()
