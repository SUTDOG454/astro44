import json
import re

def main():
    with open('/home/ubuntu/cleaned_json_attempt.txt', 'r') as f:
        content = f.read()
    
    # Fix midpoint
    content = content.replace('"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"]', '"midpoint":"Pluto/Saturn,Mars/Uranus,Moon/Neptune"')
    
    # Fix the Isis object
    content = content.replace('"astrological_correspondences":["isis":', '"astrological_correspondences":{"isis":')
    # Fix the closing bracket for Isis
    content = re.sub(r'("isis":[^\]]+)\]', r'\1}', content)

    # Wrap the pairs in an array
    content = content.replace('"major_archetype_pairs":{', '"major_archetype_pairs":[')
    
    # The error was at 35454, which is the second '}' in "lost"}}.
    # If it's an array of objects, it should be { ... } , { ... }
    # If there are TWO braces, it means the first one closed an inner object, 
    # and the second one closed the pair object.
    # So it should be: ... lost"} } , { "pair" ...
    # This is valid.
    
    # Wait! If I changed the parent to an array [, then the closing brace of the parent 
    # should also be changed to a bracket ].
    # But I haven't done that yet.
    
    # Let's try to just remove the archetypal_pairs section to see if the rest is okay.
    # This will confirm if the rest of the JSON is valid.
    
    start_ap = content.find('"major_archetype_pairs"')
    if start_ap != -1:
        # Find the end of this section - let's say the next major key
        end_ap = content.find('"advanced_points_and_bodies"', start_ap)
        if end_ap != -1:
            new_content = content[:start_ap] + '"major_archetype_pairs":[],' + content[end_ap:]
            try:
                data = json.loads(new_content)
                print("Success with empty archetypal pairs!")
                with open('/home/ubuntu/astrology_framework.json', 'w') as f:
                    json.dump(data, f, indent=2)
                return
            except json.JSONDecodeError as e:
                print(f"Still failing: {e}")
                print(f"Context: {new_content[e.pos-50:e.pos+50]}")

if __name__ == "__main__":
    main()
