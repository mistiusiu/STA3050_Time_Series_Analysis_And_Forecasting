import shutil
import os
import re
from pathlib import Path

def transform_latex(content):
    """
    Identifies all $$ math $$ blocks (single or multi-line)
    and wraps them in a div + \[ \] for MkDocs compatibility.
    """
    # Pattern looks for $$ followed by anything (including newlines) 
    # until it hits the next $$
    block_math_pattern = r'\$\$(.*?)\$\$'
    
    def replace_with_latex_brackets(match):
        math_content = match.group(1).strip()
        # We add newlines inside the div to ensure Markdown doesn't 
        # try to parse the <div> tag and the math as a single line.
        return f'\n<div class="arithmatex">\n\\[\n{math_content}\n\\]\n</div>\n'

    # Using re.DOTALL is critical so that (.*?) matches across newlines
    return re.sub(block_math_pattern, replace_with_latex_brackets, content, flags=re.DOTALL)

def sync_vault(vault_path, mkdocs_docs_path):
    vault = Path(vault_path).expanduser().resolve()
    dest = Path(mkdocs_docs_path).expanduser().resolve()

    if not vault.exists():
        print(f"Error: Vault path {vault} does not exist.")
        return

    dest.mkdir(parents=True, exist_ok=True)
    print(f"Syncing and transforming: {vault} -> {dest}")

    for item in vault.rglob("*"):
        if any(part.startswith('.') for part in item.parts):
            continue
            
        relative_path = item.relative_to(vault)
        target_path = dest / relative_path

        if item.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            continue

        if item.is_file():
            # Protect your custom index.md
            if target_path.name.lower() == "index.md" and target_path.exists():
                continue
            
            # If it's a markdown file, transform the LaTeX during copy
            if item.suffix == ".md":
                with open(item, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = transform_latex(content)
                
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            else:
                # For images/attachments, just do a straight copy
                shutil.copy2(item, target_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python sync_obsidian.py <vault_path> <mkdocs_docs_path>")
    else:
        sync_vault(sys.argv[1], sys.argv[2])