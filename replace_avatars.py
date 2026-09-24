import re
import glob

replacements = {
    r'https://ui-avatars\.com/api/\?name=Anita\+Sharma[^"\' ]*': 'https://randomuser.me/api/portraits/women/24.jpg',
    r'https://ui-avatars\.com/api/\?name=Priya\+Reddy[^"\' ]*': 'https://randomuser.me/api/portraits/women/33.jpg',
    r'https://ui-avatars\.com/api/\?name=Rohan\+Das[^"\' ]*': 'https://randomuser.me/api/portraits/men/46.jpg',
    r'https://ui-avatars\.com/api/\?name=Bengali\+Bites[^"\' ]*': 'https://randomuser.me/api/portraits/men/45.jpg',
    r'https://ui-avatars\.com/api/\?name=Fit\+Macros[^"\' ]*': 'https://randomuser.me/api/portraits/men/22.jpg',
    r'https://ui-avatars\.com/api/\?name=Sara\+Khan[^"\' ]*': 'https://randomuser.me/api/portraits/women/12.jpg',
    r'https://ui-avatars\.com/api/\?name=Maa\+Ki\+Rasoi[^"\' ]*': 'https://randomuser.me/api/portraits/women/48.jpg',
    r'https://ui-avatars\.com/api/\?name=Kerala\+Kitchen[^"\' ]*': 'https://randomuser.me/api/portraits/men/12.jpg',
    r'https://ui-avatars\.com/api/\?name=Vegan\+Bites[^"\' ]*': 'https://randomuser.me/api/portraits/women/19.jpg'
}

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    for pattern, replacement in replacements.items():
        new_content = re.sub(pattern, replacement, new_content)
        
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Updated avatars in {count} files.")
