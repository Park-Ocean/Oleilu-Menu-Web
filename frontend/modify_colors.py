import os
import glob

FRONTEND_DIR = r"c:\Programacion\Git\CoffeBeansWeb\Coffe-Beans-Menu\frontend\src"

COLOR_MAP = {
    "#6B2D3E": "#50768C",
    "#522231": "#3B596A",
    "#8B4A5C": "#E09F7D",
    "#B8907A": "#8D7A6A",
    "#F2E0E5": "#FAEBE3",
    "#E0C5CE": "#F0CDBA",
    "#EBD3DA": "#F2D8C9",
    "#E8D9CB": "#DBCBB4",
    "#D9C4B1": "#CBB69C",
    "#3A3530": "#423838",
    "#4A3040": "#423838",
    "#FAF5EF": "#F5EBE1",
    "#F0E6D8": "#EBDCCA",
    "?murta-menu?": "coffee-beans-menu",
}

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply color mapping
    for old, new in COLOR_MAP.items():
        # Case insensitive replace for hex colors
        content = content.replace(old, new)
        content = content.replace(old.lower(), new)
        content = content.replace(old.upper(), new)

    # Word replacements
    content = content.replace("Murta Menu", "Coffee Beans")
    content = content.replace("Murta", "Coffee Beans")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Recursively find all js, jsx, css files
    search_pattern = os.path.join(FRONTEND_DIR, '**', '*.js*')
    for filepath in glob.glob(search_pattern, recursive=True):
        print(f"Modifying {filepath}")
        replace_in_file(filepath)
    
    # Also do index.css
    css_pattern = os.path.join(FRONTEND_DIR, '**', '*.css')
    for filepath in glob.glob(css_pattern, recursive=True):
        print(f"Modifying {filepath}")
        replace_in_file(filepath)

if __name__ == '__main__':
    main()
