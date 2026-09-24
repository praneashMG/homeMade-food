import re

files = ['menu.html', 'plans.html', 'contact.html', 'works.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the first <section> after <!-- 1. HERO... -->
    # and replace its class.
    
    # We will just replace py-16 sm:py-24 or similar with the new layout
    # works.html has: <section class="relative bg-custom-gradient overflow-hidden py-20 lg:py-28">
    # contact.html has: <section class="bg-custom-gradient py-16 sm:py-20 lg:py-24 relative overflow-hidden">
    # menu.html has: <section class="relative bg-custom-gradient py-16 sm:py-24 overflow-hidden">
    # plans.html has: <section class="relative bg-custom-gradient py-16 sm:py-24 overflow-hidden">
    
    new_content = content
    if file in ['menu.html', 'plans.html']:
        new_content = new_content.replace(
            '<section class="relative bg-custom-gradient py-16 sm:py-24 overflow-hidden">',
            '<section class="relative bg-custom-gradient py-16 overflow-hidden min-h-[60vh] flex items-center">'
        )
    elif file == 'contact.html':
        new_content = new_content.replace(
            '<section class="bg-custom-gradient py-16 sm:py-20 lg:py-24 relative overflow-hidden">',
            '<section class="bg-custom-gradient py-16 relative overflow-hidden min-h-[60vh] flex items-center">'
        )
    elif file == 'works.html':
        new_content = new_content.replace(
            '<section class="relative bg-custom-gradient overflow-hidden py-20 lg:py-28">',
            '<section class="relative bg-custom-gradient overflow-hidden py-16 min-h-[60vh] flex items-center">'
        )

    # We also need to add w-full to the container inside the hero so it spans correctly under flex.
    # The container usually looks like: <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
    # We can just replace '<div class="container mx-auto px-4 sm:px-6 lg:px-8' with '<div class="container mx-auto px-4 sm:px-6 lg:px-8 w-full'
    # but only for the first occurrence (the hero container).
    
    # Find first container
    idx = new_content.find('<div class="container mx-auto')
    if idx != -1:
        prefix = new_content[:idx]
        suffix = new_content[idx:]
        suffix = suffix.replace('container mx-auto', 'container mx-auto w-full', 1)
        new_content = prefix + suffix

    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")

