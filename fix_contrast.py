import os
import glob

def update_labels():
    html_files = glob.glob('*.html')
    count_green = 0
    count_purple = 0
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # Update green labels
        if 'text-green-700' in new_content:
            new_content = new_content.replace('text-green-700', 'text-green-800')
            count_green += 1
            
        # Update purple labels for dark mode
        # specifically those with "bg-hover text-accent"
        if 'bg-hover text-accent' in new_content:
            new_content = new_content.replace('bg-hover text-accent', 'bg-hover text-accent dark:text-purple-300')
            count_purple += 1
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")

    print(f"Updated green labels in {count_green} files.")
    print(f"Updated purple labels in {count_purple} files.")

if __name__ == "__main__":
    update_labels()
