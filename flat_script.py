# -*- coding: utf-8 -*-
import os
import re

docs_dir = r"e:\All\BlockMaster\docs"
html_files = [f for f in os.listdir(docs_dir) if f.endswith(".html")]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Typography plugin
    content = content.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com?plugins=typography"></script>'
    )
    
    # 2. Responsive layout
    content = content.replace(
        '<aside class="fixed left-0 top-0 h-screen w-64 bg-slate-900 overflow-y-auto z-20 flex flex-col">',
        '<aside class="lg:fixed lg:left-0 lg:top-0 lg:h-screen lg:w-64 bg-slate-900 lg:overflow-y-auto z-20 flex flex-col relative w-full h-auto">'
    )
    content = content.replace(
        '<main class="ml-64 min-h-screen">',
        '<main class="lg:ml-64 min-h-screen pt-4 lg:pt-0">'
    )
    
    # 3. Remove Emojis
    emojis = ['?? ', '?? ', '?? ', '?? ', '? ', '?? ', '? ', '? ']
    for e in emojis:
        content = content.replace(e, '')
        
    # 4. Remove borders and shadows
    classes_to_remove = [
        'border', 'border-slate-200', 'border-slate-700', 'border-b', 'border-t',
        'border-l-4', 'border-l-emerald-500', 'border-l-indigo-500', 'border-l-amber-500',
        'border-l-violet-500', 'border-l-red-500', 'border-red-200', 'border-emerald-200',
        'border-emerald-300', 'border-indigo-300',
        'hover:border-indigo-300', 'hover:shadow-md', 'shadow-md', 'shadow-lg',
        'prose-pre:shadow-lg'
    ]
    
    for c in classes_to_remove:
        content = re.sub(r'\b' + re.escape(c) + r'\b', '', content)

    # 5. Flat Backgrounds
    color_bgs = ['bg-indigo-50', 'bg-amber-50', 'bg-red-50', 'bg-emerald-50', 'bg-violet-50', 'bg-orange-50']
    for b in color_bgs:
        content = content.replace(b, 'bg-slate-100')
        
    content = content.replace('bg-white', 'bg-slate-100')
    content = content.replace('rounded-xl', 'rounded-none')
    content = content.replace('rounded-2xl', 'rounded-none')
    content = content.replace('rounded-lg', 'rounded-none')
    content = content.replace('rounded-md', 'rounded-none')

    # Remove repeated spaces
    content = re.sub(r' +', ' ', content)
    content = content.replace('class=" "', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for h in html_files:
    process_file(os.path.join(docs_dir, h))

print("Script execute avec succes.")
