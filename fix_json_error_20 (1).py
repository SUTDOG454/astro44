import json

def main():
    with open('/home/ubuntu/cleaned_json_attempt.txt', 'r') as f:
        content = f.read()
    
    # Remove the markdown trailing text
    idx = content.find('```')
    if idx != -1:
        content = content[:idx]
    
    # Trim trailing spaces
    content = content.strip()
    
    # Fix the archetypal pairs by just making it an empty array for now
    start_ap = content.find('"major_archetype_pairs"')
    if start_ap != -1:
        end_ap = content.find('"advanced_points_and_bodies"', start_ap)
        if end_ap != -1:
            content = content[:start_ap] + '"major_archetype_pairs":[],' + content[end_ap:]

    # Fix midpoint
    content = content.replace('"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]', '"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"')

    try:
        data = json.loads(content)
        print("Success!")
        with open('/home/ubuntu/astrology_framework.json', 'w') as f:
            json.dump(data, f, indent=2)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        print(f"Context: {content[e.pos-50:e.pos+50]}")

if __name__ == "__main__":
    main()
