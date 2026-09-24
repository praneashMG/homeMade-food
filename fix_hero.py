import re

files = ['menu.html', 'plans.html', 'contact.html', 'works.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, let's remove the erroneous w-full from the header if it was added
    # Header container looks like: <div class="container mx-auto w-full px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between h-[70px]">
    content = content.replace('container mx-auto w-full px-4 sm:px-6 lg:px-8 py-3', 'container mx-auto px-4 sm:px-6 lg:px-8 py-3')
    
    # Now, find the hero section
    hero_idx = content.find('HERO')
    if hero_idx != -1:
        # Find the first container mx-auto AFTER the hero_idx
        container_idx = content.find('container mx-auto', hero_idx)
        if container_idx != -1:
            prefix = content[:container_idx]
            suffix = content[container_idx:]
            
            # Make sure it doesn't already have w-full
            if not suffix.startswith('container mx-auto w-full'):
                suffix = suffix.replace('container mx-auto', 'container mx-auto w-full', 1)
            
            content = prefix + suffix

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {file}")
