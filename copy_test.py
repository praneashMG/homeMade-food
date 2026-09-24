import os

with open('home2.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

testimonials = "".join(lines[429:486])  # lines 430 to 486 (inclusive)
# Let's adjust the comment from "<!-- 6. BOTTOM CTA... -->" to "<!-- 6. TESTIMONIALS -->"
testimonials = "<!-- 5.5. TESTIMONIALS -->\n" + testimonials + "\n"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = "<!-- 6. CALL TO ACTION (CHEF SIGNUP) -->"
new_content = content.replace(target, testimonials + target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added testimonials to index.html")
