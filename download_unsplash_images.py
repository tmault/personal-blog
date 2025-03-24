import os
import re
import requests
from urllib.parse import urlparse
import hashlib
from pathlib import Path

def download_image(url, save_path):
    """Download an image from a URL and save it to the specified path."""
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    return False

def get_photo_id(url):
    """Extract the photo ID from an Unsplash URL."""
    if 'source.unsplash.com' in url:
        # For source.unsplash.com URLs, use the last part as the ID
        return url.split('/')[-1].split('?')[0]
    else:
        # For images.unsplash.com URLs, extract the photo ID
        match = re.search(r'photo-([^?]+)', url)
        if match:
            return match.group(1)
    return None

def process_markdown_file(file_path):
    """Process a markdown file to find and download Unsplash images."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all featured_image fields that contain Unsplash URLs
    patterns = [
        r'featured_image:\s*"/assets/images/(https://images\.unsplash\.com/[^"]+)"',
        r'featured_image:\s*"(https://images\.unsplash\.com/[^"]+)"',
        r'image:\s*"(https://images\.unsplash\.com/[^"]+)"',
        r'image:\s*"(https://source\.unsplash\.com/[^"]+)"'
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            full_url = match.group(1)
            # Extract the photo ID from the URL
            photo_id = get_photo_id(full_url)
            if not photo_id:
                print(f"Could not extract photo ID from URL: {full_url}")
                continue
            
            # Create a local path for the image
            local_path = f"assets/images/unsplash/{photo_id}.jpg"
            
            # Download the image
            if download_image(full_url, local_path):
                print(f"Downloaded: {local_path}")
                
                # Update the markdown file to use the local path
                if pattern.startswith(r'featured_image:\s*"/assets/images/'):
                    new_content = content.replace(
                        f'featured_image: "/assets/images/{full_url}"',
                        f'featured_image: "/{local_path}"'
                    )
                else:
                    new_content = content.replace(
                        f'"{full_url}"',
                        f'"/{local_path}"'
                    )
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")

def main():
    # Process all markdown files in the collections/_posts directory
    posts_dir = Path("collections/_posts")
    for file_path in posts_dir.glob("*.markdown"):
        print(f"\nProcessing: {file_path}")
        process_markdown_file(str(file_path))
    
    # Also process the about.md file
    about_file = Path("about.md")
    if about_file.exists():
        print(f"\nProcessing: {about_file}")
        process_markdown_file(str(about_file))

if __name__ == "__main__":
    main() 