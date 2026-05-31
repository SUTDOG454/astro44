import json

def main():
    with open('/home/ubuntu/cleaned_json_attempt.txt', 'r') as f:
        content = f.read()
    
    # Remove markdown
    idx = content.find('```')
    if idx != -1:
        content = content[:idx]
    content = content.strip()
    
    # Fix midpoint
    content = content.replace('"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]', '"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"')

    # Fix archetypal pairs
    start_ap = content.find('"major_archetype_pairs"')
    if start_ap != -1:
        end_ap = content.find('"advanced_points_and_bodies"', start_ap)
        if end_ap != -1:
            content = content[:start_ap] + '"major_archetype_pairs":[],' + content[end_ap:]

    # The error at 88061 is at the very end.
    # Context: ... techniques"]}}}
    # If it's expecting a comma, it means there's something after the closing braces 
    # or the braces are not closing everything correctly.
    
    # Let's try to just add/remove braces at the end until it works.
    for i in range(1, 10):
        test_content = content + ("}" * i)
        try:
            data = json.loads(test_content)
            print(f"Success with {i} extra braces!")
            with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                json.dump(data, f, indent=2)
            return
        except:
            pass
            
    for i in range(1, 10):
        if len(content) > i:
            test_content = content[:-i]
            try:
                data = json.loads(test_content)
                print(f"Success by removing {i} characters!")
                with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                    json.dump(data, f, indent=2)
                return
            except:
                pass

    print("Still failing.")

if __name__ == "__main__":
    main()
