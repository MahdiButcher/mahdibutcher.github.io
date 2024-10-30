import os

def create_fa_md_files(content_folder):
    for root, _, files in os.walk(content_folder):
        for filename in files:
            if filename.endswith(".md") and not filename.endswith(".fa.md"):
                base_name = os.path.splitext(filename)[0]
                fa_md_filename = f"{base_name}.fa.md"
                fa_md_filepath = os.path.join(root, fa_md_filename)
                
                if not os.path.exists(fa_md_filepath):
                    with open(fa_md_filepath, 'w') as fa_md_file:
                        fa_md_file.write(f"# {base_name}\n\n")
                        fa_md_file.write(f"This is the Persian translation of {base_name}.\n")

if __name__ == "__main__":
    content_folder = "/workspaces/mahdibutcher.github.io/content"
    create_fa_md_files(content_folder)
