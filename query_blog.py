#!/usr/bin/env python3
"""
Query the blog archive using RAG (Retrieval-Augmented Generation).
"""

import os
import sys
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, load_index_from_storage, StorageContext, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.response_synthesizers import get_response_synthesizer

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
        # Get timeout from environment variable with default
        local_llm_timeout = float(os.getenv("LOCAL_LLM_TIMEOUT", "120.0"))
        print(f"Timeout: {local_llm_timeout}s")
        
        llm = OpenAILike(
            model=local_llm_model,
            api_base=local_llm_url + "/v1",
            api_key="dummy",  # local server doesn't need real API key
            is_chat_model=True,
            timeout=local_llm_timeout,
            temperature=0.1,
            max_retries=1  # Reduce retries for faster failure
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

def load_index(storage_dir: str) -> VectorStoreIndex:
    """Load the pre-built vector index."""
    storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
    index = load_index_from_storage(storage_context)
    return index

def create_query_engine(index: VectorStoreIndex, top_k: int = 5):
    """Create a query engine for RAG search."""
    # Create retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=top_k
    )
    
    # Create response synthesizer
    response_synthesizer = get_response_synthesizer(
        response_mode="tree_summarize"
    )
    
    # Create query engine
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer
    )
    
    return query_engine

def format_sources(response):
    """Format the source information from the response."""
    sources = []
    if hasattr(response, 'source_nodes'):
        for node in response.source_nodes:
            metadata = node.metadata
            source_info = {
                'title': metadata.get('title', 'Unknown'),
                'date': metadata.get('date', 'Unknown'),
                'url': metadata.get('url', ''),
                'score': getattr(node, 'score', 0.0),
                'categories': metadata.get('categories', [])
            }
            sources.append(source_info)
    return sources

def interactive_mode(query_engine):
    """Run interactive query mode."""
    print("🔍 kiyokaのブログアーカイブ RAG検索")
    print("=" * 50)
    print("質問を入力してください（'quit'で終了）:")
    print()
    
    while True:
        try:
            query = input("質問: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q', '終了']:
                print("検索を終了します。")
                break
            
            if not query:
                continue
            
            print("\n🤔 検索中...")
            
            # Query the index
            response = query_engine.query(query)
            
            print(f"\n💡 回答:")
            print("-" * 30)
            print(response.response)
            
            # Show sources
            sources = format_sources(response)
            if sources:
                print(f"\n📚 参考記事:")
                print("-" * 30)
                for i, source in enumerate(sources[:3], 1):  # Show top 3 sources
                    print(f"{i}. {source['title']}")
                    print(f"   日付: {source['date']}")
                    if source['categories']:
                        print(f"   カテゴリ: {', '.join(source['categories'])}")
                    if source['url']:
                        print(f"   URL: https://kiyoka.github.io/blog-archive{source['url']}")
                    print(f"   関連度: {source['score']:.3f}")
                    print()
            
            print("=" * 50)
            
        except KeyboardInterrupt:
            print("\n\n検索を終了します。")
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")

def single_query_mode(query: str, query_engine):
    """Run a single query and exit."""
    print(f"質問: {query}")
    print()
    
    response = query_engine.query(query)
    
    print("回答:")
    print("-" * 30)
    print(response.response)
    
    # Show sources
    sources = format_sources(response)
    if sources:
        print(f"\n参考記事:")
        print("-" * 30)
        for i, source in enumerate(sources[:5], 1):
            print(f"{i}. {source['title']} ({source['date']})")
            if source['categories']:
                print(f"   カテゴリ: {', '.join(source['categories'])}")
            if source['url']:
                print(f"   URL: https://kiyoka.github.io/blog-archive{source['url']}")
            print()

def main():
    """Main function."""
    storage_dir = "./storage"
    
    # Check if LLM configuration is set
    local_llm_url = os.getenv("LOCAL_LLM_URL")
    local_llm_model = os.getenv("LOCAL_LLM_MODEL")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not (local_llm_url and local_llm_model) and not openai_api_key:
        print("Error: Either LOCAL_LLM_URL & LOCAL_LLM_MODEL or OPENAI_API_KEY must be set!")
        print("For local LLM, set LOCAL_LLM_URL and LOCAL_LLM_MODEL in .env")
        print("For OpenAI, set OPENAI_API_KEY in .env")
        return
    
    # Check if index exists
    if not os.path.exists(storage_dir):
        print(f"Error: Index storage directory '{storage_dir}' not found!")
        print("Please run build_index.py first to build the search index.")
        return
    
    # Setup llama-index
    setup_llama_index()
    
    # Load index
    print("Loading search index...")
    try:
        index = load_index(storage_dir)
        print("Index loaded successfully!")
    except Exception as e:
        print(f"Error loading index: {e}")
        return
    
    # Create query engine
    query_engine = create_query_engine(index)
    
    # Check if query was provided as command line argument
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        single_query_mode(query, query_engine)
    else:
        interactive_mode(query_engine)

if __name__ == "__main__":
    main()