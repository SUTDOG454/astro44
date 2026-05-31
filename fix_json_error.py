import json

def main():
    with open('/home/ubuntu/cleaned_json_attempt.txt', 'r') as f:
        content = f.read()
    
    # The error was around char 37478
    # Context: ..."midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"],"integration_theme":"Cosmic dance of destruction...
    # It looks like a missing quote or comma.
    
    # Let's try to find this specific part
    target = '"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]'
    if target in content:
        print("Found target!")
        # It should probably be "midpoint":["Pluto/Saturn","Mars/Uranus","Moon/Neptune"]
        # or "midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune" (if it's a string)
        # But there's a closing bracket ']' after it, which suggests it was meant to be an array or part of one.
        
        # Let's look at the context more broadly
        idx = content.find(target)
        print(f"Context: {content[idx-50:idx+100]}")
        
        # If it's "midpoint":"...", it shouldn't have a ']' unless it's in an array.
        # If it's in an array, it should be ["midpoint":"..."] which is invalid JSON (should be {"midpoint":"..."})
        
        # Let's try to replace it with something valid and see if it helps
        # Maybe it was meant to be an array of strings?
        fixed = content.replace('"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]', '"midpoint":["Pluto/Saturn","Mars/Uranus","Moon/Neptune"]')
        
        try:
            json.loads(fixed)
            print("Fixed!")
            with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                json.dump(json.loads(fixed), f, indent=2)
            return
        except json.JSONDecodeError as e:
            print(f"Still failing: {e}")
            # Try another fix - maybe it's just a string and the bracket is extra
            fixed2 = content.replace('"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]', '"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"')
            try:
                json.loads(fixed2)
                print("Fixed with second method!")
                with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                    json.dump(json.loads(fixed2), f, indent=2)
                return
            except json.JSONDecodeError as e2:
                print(f"Still failing: {e2}")
                # Show context for the new error
                print(f"New context: {fixed2[e2.pos-50:e2.pos+50]}")

if __name__ == "__main__":
    main()
