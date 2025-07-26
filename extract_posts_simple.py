#!/usr/bin/env python3
"""
Simple version of post extraction that doesn't require markdown library.
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Any
import json

def extract_frontmatter_and_content(file_path: str) -> Dict[str, Any]:
    """Extract YAML frontmatter and markdown content from a Jekyll post."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            content_text = parts[2].strip()
        else:
            frontmatter_text = ""
            content_text = content
    else:
        frontmatter_text = ""
        content_text = content
    
    # Parse frontmatter
    frontmatter = {}
    if frontmatter_text:
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError:
            pass
    
    return {
        'frontmatter': frontmatter,
        'content': content_text
    }

def simple_markdown_to_text(markdown_content: str) -> str:
    """Convert markdown to plain text using simple regex (no markdown library)."""
    content = markdown_content
    
    # Remove Jekyll liquid tags (like {% include amazon.html %})
    content = re.sub(r'{%.*?%}', '', content)
    
    # Remove markdown links [text](url) -> text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove markdown images ![alt](url) -> alt
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', content)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove markdown headers
    content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)
    
    # Remove markdown emphasis
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # bold
    content = re.sub(r'\*([^*]+)\*', r'\1', content)      # italic
    content = re.sub(r'`([^`]+)`', r'\1', content)        # code
    
    # Remove markdown lists
    content = re.sub(r'^\s*[-*+]\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*\d+\.\s+', '', content, flags=re.MULTILINE)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = re.sub(r' +', ' ', content)
    
    return content.strip()

def extract_all_posts(posts_dir: str) -> List[Dict[str, Any]]:
    """Extract all blog posts from the _posts directory."""
    posts = []
    posts_path = Path(posts_dir)
    
    for file_path in posts_path.glob('*.md'):
        try:
            post_data = extract_frontmatter_and_content(str(file_path))
            
            # Extract metadata
            frontmatter = post_data['frontmatter']
            title = frontmatter.get('title', file_path.stem)
            date = frontmatter.get('date', '')
            categories = frontmatter.get('categories', [])
            if isinstance(categories, str):
                categories = [categories]
            
            # Convert markdown content to plain text
            text_content = simple_markdown_to_text(post_data['content'])
            
            # Skip if content is too short
            if len(text_content.strip()) < 50:
                continue
            
            post = {
                'id': file_path.stem,
                'title': title,
                'date': str(date),
                'categories': categories,
                'file_path': str(file_path),
                'content': text_content,
                'url': f"/{file_path.stem}/"
            }
            
            posts.append(post)
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    return posts

def main():
    """Extract all posts and save to JSON for indexing."""
    posts_dir = "_posts"
    output_file = "posts_data.json"
    
    if not os.path.exists(posts_dir):
        print(f"Posts directory '{posts_dir}' not found!")
        return
    
    print("Extracting blog posts...")
    posts = extract_all_posts(posts_dir)
    
    print(f"Extracted {len(posts)} posts")
    
    # Save to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print(f"Posts data saved to {output_file}")
    
    # Print some statistics
    total_chars = sum(len(post['content']) for post in posts)
    print(f"Total content: {total_chars:,} characters")
    
    # Show sample
    if posts:
        print(f"\nSample post:")
        sample = posts[0]
        print(f"Title: {sample['title']}")
        print(f"Date: {sample['date']}")
        print(f"Categories: {sample['categories']}")
        print(f"Content preview: {sample['content'][:200]}...")

if __name__ == "__main__":
    main()