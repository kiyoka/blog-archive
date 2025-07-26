#!/usr/bin/env python3
"""
Build a vector index from blog posts using llama-index.
"""

import os
import json
from dotenv import load_dotenv
from llama_index.core import Document, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai_like import OpenAILike
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

def setup_llama_index():
    """Configure llama-index with local LLM or OpenAI models."""
    # Check if local LLM should be used
    local_llm_url = os.getenv("LOCAL_LLM_URL")
    local_llm_model = os.getenv("LOCAL_LLM_MODEL")
    
    if local_llm_url and local_llm_model:
        # Set up local LLM
        print(f"Using local LLM: {local_llm_model} at {local_llm_url}")
        llm = OpenAILike(
            model=local_llm_model,
            api_base=local_llm_url + "/v1",
            api_key="dummy",  # local server doesn't need real API key
            is_chat_model=True,
            timeout=30.0,
            temperature=0.1
        )
    else:
        # Set up OpenAI LLM (fallback)
        llm = OpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    # Set up embeddings
    openai_api_key = os.getenv("OPENAI_API_KEY")
    use_local_embeddings = os.getenv("USE_LOCAL_EMBEDDINGS", "false").lower() == "true"
    
    if use_local_embeddings or not openai_api_key or openai_api_key == "your_openai_api_key_here":
        # Use local embeddings
        print("Using local embeddings (HuggingFace)")
        embed_model = HuggingFaceEmbedding(
            model_name="intfloat/multilingual-e5-small"
        )
    else:
        # Use OpenAI embeddings
        embed_model = OpenAIEmbedding(
            model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002"),
            api_key=openai_api_key
        )
    
    # Configure global settings
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = 1024
    Settings.chunk_overlap = 200

def load_posts_data(file_path: str) -> List[Dict[str, Any]]:
    """Load extracted posts data from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_documents(posts: List[Dict[str, Any]]) -> List[Document]:
    """Convert posts to llama-index Document objects."""
    documents = []
    
    for post in posts:
        # Create document content
        content = f"タイトル: {post['title']}\n"
        content += f"日付: {post['date']}\n"
        if post['categories']:
            content += f"カテゴリ: {', '.join(post['categories'])}\n"
        content += f"\n{post['content']}"
        
        # Create metadata
        metadata = {
            'title': post['title'],
            'date': post['date'],
            'categories': post['categories'],
            'file_path': post['file_path'],
            'url': post['url'],
            'post_id': post['id']
        }
        
        doc = Document(
            text=content,
            metadata=metadata,
            doc_id=post['id']
        )
        
        documents.append(doc)
    
    return documents

def build_index(documents: List[Document]) -> VectorStoreIndex:
    """Build vector index from documents."""
    print("Building vector index...")
    
    # Create node parser for chunking
    parser = SentenceSplitter(
        chunk_size=1024,
        chunk_overlap=200
    )
    
    # Build index
    index = VectorStoreIndex.from_documents(
        documents,
        transformations=[parser],
        show_progress=True
    )
    
    return index

def main():
    """Main function to build the index."""
    posts_data_file = "posts_data.json"
    index_storage_dir = "./storage"
    
    # Check if embeddings configuration is set (OpenAI API key still needed for embeddings)
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set!")
        print("OpenAI API key is required for text embeddings even when using local LLM.")
        print("Please copy .env.example to .env and set your OpenAI API key.")
        return
    
    # Check if posts data exists
    if not os.path.exists(posts_data_file):
        print(f"Error: {posts_data_file} not found!")
        print("Please run extract_posts.py first to extract blog post data.")
        return
    
    # Setup llama-index
    setup_llama_index()
    
    # Load posts data
    print("Loading posts data...")
    posts = load_posts_data(posts_data_file)
    print(f"Loaded {len(posts)} posts")
    
    # Create documents
    print("Creating documents...")
    documents = create_documents(posts)
    print(f"Created {len(documents)} documents")
    
    # Build index
    index = build_index(documents)
    
    # Save index
    print(f"Saving index to {index_storage_dir}...")
    index.storage_context.persist(persist_dir=index_storage_dir)
    
    print("Index built and saved successfully!")
    print(f"Storage directory: {index_storage_dir}")
    print("\nYou can now use query_blog.py to search the blog archive.")

if __name__ == "__main__":
    main()