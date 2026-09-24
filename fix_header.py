import os
import glob

def update_files():
    html_files = glob.glob('*.html')
    
    # Text to find (Desktop Header Right Actions)
    search_desktop = """            <!-- Right Actions -->
            <div class="flex-1 flex justify-end items-center">
                <div class="hidden xl:flex items-center space-x-4">
                    <button id="theme-toggle" class="icon-btn text-primary-text hover:text-accent p-1.5 rounded-full transition duration-200">
                        <svg class="w-6 h-6 light-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg class="w-6 h-6 dark-icon hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </button>
                    <button id="lang-icon" class="text-primary-text hover:text-accent p-1.5 rounded-full transition duration-200">
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7.5 21 3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5" />
</svg>                    </button>
                    <div class="flex items-center gap-3 ml-3">
                        <a href="login.html" class="btn-outline px-6 py-2 rounded-xl font-bold shadow-md">Login</a>
                        <a href="signup.html" class="book-btn px-6 py-2.5 rounded-xl font-bold shadow-md whitespace-nowrap">Sign Up</a>
                    </div>
                </div>"""

    replace_desktop = """            <!-- Right Actions -->
            <div class="flex-1 flex justify-end items-center">
                <div class="hidden xl:flex items-center space-x-4 pl-12 lg:pl-16">
                    <button id="theme-toggle" class="icon-btn text-primary-text hover:text-accent p-1.5 rounded-full transition duration-200">
                        <svg class="w-6 h-6 light-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg class="w-6 h-6 dark-icon hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </button>
                    <button id="lang-icon" class="text-primary-text hover:text-accent p-1.5 rounded-full transition duration-200">
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7.5 21 3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5" />
</svg>                    </button>
                    <div class="flex items-center ml-4">
                        <a href="signup.html" class="book-btn px-6 py-2.5 rounded-xl font-bold shadow-md whitespace-nowrap">Sign Up</a>
                    </div>
                </div>"""

    search_mobile = """            <div class="flex mt-5 gap-5 w-full">
                <a href="login.html" class="flex-1 btn-outline text-center py-1.5 rounded-xl font-bold text-sm shadow-md">Login</a>
                <a href="signup.html" class="flex-1 book-btn text-center py-2 rounded-xl font-bold text-sm shadow-md">Sign Up</a>
            </div>"""
            
    replace_mobile = """            <div class="flex mt-5 w-full">
                <a href="signup.html" class="flex-1 book-btn text-center py-3 rounded-xl font-bold text-sm shadow-md">Sign Up</a>
            </div>"""

    count = 0
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace(search_desktop, replace_desktop)
        new_content = new_content.replace(search_mobile, replace_mobile)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {file}")

    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_files()
