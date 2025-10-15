#!/usr/bin/env python3
"""
Easy Blog Post Creator
Run this script to create a new blog post without coding!
"""

import os
import sys
from datetime import datetime
import subprocess

def create_new_post():
    print("=" * 50)
    print("📝 Blog Post Creator")
    print("=" * 50)
    
    # Get post title
    title = input("\nEnter post title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        return
    
    # Get categories (optional)
    categories = input("Enter categories (comma-separated, or press Enter to skip): ").strip()
    if not categories:
        categories = "blog"
    
    # Get tags (optional)
    tags_input = input("Enter tags (comma-separated, or press Enter to skip): ").strip()
    tags = []
    if tags_input:
        tags = [tag.strip() for tag in tags_input.split(",")]
    
    # Get content
    print("\n📄 Enter your post content (type 'END' on a new line when done):")
    content_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            content_lines.append(line)
        except EOFError:
            break
    
    content = "\n".join(content_lines)
    
    if not content.strip():
        print("❌ Content cannot be empty!")
        return
    
    # Generate filename
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S +0900")
    
    # Create URL-friendly filename
    filename_title = title.lower()
    filename_title = filename_title.replace(" ", "-")
    # Remove special characters
    filename_title = "".join(c for c in filename_title if c.isalnum() or c == "-")
    filename = f"{date_str}-{filename_title}.md"
    
    # Create post content with frontmatter
    tags_yaml = ""
    if tags:
        tags_str = ", ".join([f'"{tag}"' for tag in tags])
        tags_yaml = f"tags: [{tags_str}]"
    
    post_content = f"""---
layout: post
title: "{title}"
date: {date_str} {time_str}
categories: {categories}
{tags_yaml}
---

{content}
"""
    
    # Write file
    filepath = os.path.join("_posts", filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(post_content)
        print(f"\n✅ Post created successfully: {filepath}")
    except Exception as e:
        print(f"\n❌ Error creating post: {e}")
        return
    
    # Ask if user wants to publish (commit and push)
    publish = input("\n🚀 Do you want to publish this post now? (y/n): ").strip().lower()
    
    if publish == "y":
        try:
            print("\n📤 Publishing post...")
            
            # Git add
            subprocess.run(["git", "add", filepath], check=True)
            
            # Git commit
            commit_msg = f'Add new post: "{title}"'
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            
            # Git push
            subprocess.run(["git", "push", "origin", "main"], check=True)
            
            print("✅ Post published successfully!")
            print("🌐 Your blog will be updated in a few minutes at https://Sungheyn.github.io")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error publishing post: {e}")
            print("You can manually publish later with: git add . && git commit -m 'Add post' && git push")
    else:
        print("\n💾 Post saved locally. To publish later, run:")
        print(f"   git add {filepath}")
        print(f'   git commit -m "Add new post"')
        print("   git push origin main")

if __name__ == "__main__":
    try:
        create_new_post()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
        sys.exit(1)
