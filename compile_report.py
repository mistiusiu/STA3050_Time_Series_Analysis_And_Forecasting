import subprocess
import os
import re
import argparse

def clean_obsidian_links(text):
    """
    Advanced Obsidian cleaner:
    1. Removes file references from [[File#Header|Alias]]
    2. Converts headers to Pandoc-compatible kebab-case IDs (#header-name)
    3. Cleans percent-encoded spaces and LaTeX symbols from links
    """
    def slugify(match):
        full_link = match.group(0)
        
        # Split by pipe for alias
        if '|' in full_link:
            path_part, alias = full_link.strip('[]').split('|', 1)
        else:
            path_part = full_link.strip('[]')
            alias = None

        # Split by # for header
        if '#' in path_part:
            _, header = path_part.split('#', 1)
        else:
            header = path_part
            if not alias: alias = header

        if not alias: alias = header

        # Create Pandoc-style ID
        clean_id = header.lower()
        clean_id = re.sub(r'%20', ' ', clean_id)
        clean_id = re.sub(r'[^a-z0-9\s-]', '', clean_id)
        clean_id = re.sub(r'\s+', '-', clean_id).strip('-')
        
        return f"[{alias}](#{clean_id})"

    cleaned_text = re.compile(r'\[\[([^\]]+)\]\]').sub(slugify, text)
    cleaned_text = re.sub(r'\$\$(.*?)\$\$', r'\n\n$$\1$$\n\n', cleaned_text, flags=re.DOTALL)
    
    return cleaned_text

def knit_obsidian_project(docs_dir):
    base_path = os.path.abspath(os.getcwd())
    # Report will still be saved relative to where the script is run (e.g. your MkDocs root)
    output_dir = os.path.join(base_path, "docs", "reports")
    output_file = os.path.join(output_dir, "Time_Series_Analysis_Report.pdf")
    temp_combined_md = os.path.join(base_path, "temp_combined_report.md")
    
    ordered_files = [
        "AR Model.md", "MA Model.md", "ARMA Model.md",
        "ARIMA Model.md", "Seasonal ARIMA Model.md", "References.md", 
        "Mathematical Proofs.md"
    ]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(temp_combined_md, "w", encoding="utf-8") as outfile:
            for filename in ordered_files:
                file_path = os.path.join(docs_dir, filename)
                if os.path.exists(file_path):
                    title = filename.replace(".md", "")
                    outfile.write(f"\n\n# {title}\n\n")
                    
                    with open(file_path, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        cleaned_content = clean_obsidian_links(content)
                        outfile.write(cleaned_content)
                else:
                    print(f"Warning: {filename} not found in {docs_dir}")

        pandoc_command = [
            "pandoc",
            temp_combined_md,
            "--pdf-engine=xelatex",
            f"--resource-path={docs_dir}",
            "-V", "mainfont=Times New Roman",
            "-V", "geometry:margin=1in",
            "-V", "linestretch=1.5",
            "-V", "fontsize=12pt",
            "-V", "indent=true",
            "--toc",
            "--number-sections",
            "-o", output_file
        ]

        print(f"Processing Obsidian syntax from: {docs_dir}")
        print("Knitting PDF...")
        subprocess.run(pandoc_command, check=True)
        print(f"Success! Report generated at: {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error during Pandoc execution: {e}")
    finally:
        if os.path.exists(temp_combined_md):
            os.remove(temp_combined_md)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Knit Obsidian Markdown files to a formatted PDF.")
    parser.add_argument("docs_dir", help="The absolute path to your Obsidian vault directory containing the .md files.")
    
    args = parser.parse_args()
    
    # Run the knitter with the provided directory
    knit_obsidian_project(args.docs_dir)
