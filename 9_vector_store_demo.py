import streamlit as st
import chromadb
from chromadb.config import Settings
import os
import tempfile
from typing import List, Dict, Any

# Configure Streamlit page
st.set_page_config(
    page_title="ChromaDB Vector Store Demo",
    page_icon="🔍",
    layout="wide"
)

# Initialize ChromaDB persistent client
@st.cache_resource
def init_chromadb_client():
    """Initialize ChromaDB persistent client with krish_demo_db"""
    # Create a persistent directory for the database
    db_path = os.path.join(os.getcwd(), "krish_demo_db")
    
    # Create the directory if it doesn't exist
    os.makedirs(db_path, exist_ok=True)
    
    # Initialize persistent client
    client = chromadb.PersistentClient(path=db_path)
    return client

def main():
    st.title("🔍 ChromaDB Vector Store Demo")
    st.markdown("### Persistent ChromaDB Client with krish_demo_db")
    
    # Initialize ChromaDB client
    try:
        client = init_chromadb_client()
        st.success(f"✅ ChromaDB persistent client initialized successfully!")
        st.info(f"📁 Database path: {os.path.join(os.getcwd(), 'krish_demo_db')}")
    except Exception as e:
        st.error(f"❌ Error initializing ChromaDB client: {str(e)}")
        return
    
    # Sidebar for collection management
    st.sidebar.title("Collection Management")
    
    # Create or get collection
    collection_name = st.sidebar.text_input("Collection Name", value="krish_collection")
    
    if st.sidebar.button("Create/Get Collection"):
        try:
            collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"description": "Demo collection for Krish's vector store"}
            )
            st.session_state.collection = collection
            st.sidebar.success(f"✅ Collection '{collection_name}' ready!")
        except Exception as e:
            st.sidebar.error(f"❌ Error: {str(e)}")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Add Documents")
        
        # Document input
        doc_text = st.text_area("Document Text", height=100, placeholder="Enter your document text here...")
        doc_id = st.text_input("Document ID", placeholder="unique_doc_id")
        
        # Metadata input
        st.write("**Metadata (optional):**")
        metadata_source = st.text_input("Source", placeholder="e.g., website, book, etc.")
        metadata_author = st.text_input("Author", placeholder="e.g., John Doe")
        metadata_category = st.text_input("Category", placeholder="e.g., technology, science")
        
        if st.button("Add Document", type="primary"):
            if doc_text and doc_id and hasattr(st.session_state, 'collection'):
                try:
                    # Prepare metadata
                    metadata = {}
                    if metadata_source:
                        metadata["source"] = metadata_source
                    if metadata_author:
                        metadata["author"] = metadata_author
                    if metadata_category:
                        metadata["category"] = metadata_category
                    
                    # Add document to collection
                    st.session_state.collection.add(
                        documents=[doc_text],
                        ids=[doc_id],
                        metadatas=[metadata] if metadata else None
                    )
                    st.success(f"✅ Document '{doc_id}' added successfully!")
                    
                    # Clear inputs
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error adding document: {str(e)}")
            else:
                if not hasattr(st.session_state, 'collection'):
                    st.warning("⚠️ Please create/select a collection first!")
                else:
                    st.warning("⚠️ Please fill in both document text and ID!")
    
    with col2:
        st.subheader("🔍 Search Documents")
        
        # Search functionality
        query_text = st.text_area("Search Query", height=100, placeholder="Enter your search query here...")
        n_results = st.slider("Number of Results", min_value=1, max_value=10, value=3)
        
        if st.button("Search", type="primary"):
            if query_text and hasattr(st.session_state, 'collection'):
                try:
                    # Perform similarity search
                    results = st.session_state.collection.query(
                        query_texts=[query_text],
                        n_results=n_results
                    )
                    
                    st.write("**Search Results:**")
                    
                    if results['documents'][0]:
                        for i, (doc, distance, doc_id, metadata) in enumerate(zip(
                            results['documents'][0],
                            results['distances'][0],
                            results['ids'][0],
                            results['metadatas'][0] or [{}] * len(results['documents'][0])
                        )):
                            with st.expander(f"Result {i+1} - ID: {doc_id} (Distance: {distance:.4f})"):
                                st.write("**Document:**")
                                st.write(doc)
                                if metadata:
                                    st.write("**Metadata:**")
                                    st.json(metadata)
                    else:
                        st.info("No results found for your query.")
                        
                except Exception as e:
                    st.error(f"❌ Error searching: {str(e)}")
            else:
                if not hasattr(st.session_state, 'collection'):
                    st.warning("⚠️ Please create/select a collection first!")
                else:
                    st.warning("⚠️ Please enter a search query!")
    
    # Collection information
    if hasattr(st.session_state, 'collection'):
        st.subheader("📊 Collection Information")
        
        try:
            # Get collection count
            count = st.session_state.collection.count()
            st.metric("Total Documents", count)
            
            if count > 0:
                # Show all documents
                if st.button("Show All Documents"):
                    all_docs = st.session_state.collection.get()
                    
                    st.write("**All Documents in Collection:**")
                    for i, (doc_id, doc, metadata) in enumerate(zip(
                        all_docs['ids'],
                        all_docs['documents'],
                        all_docs['metadatas'] or [{}] * len(all_docs['ids'])
                    )):
                        with st.expander(f"Document {i+1}: {doc_id}"):
                            st.write("**Content:**")
                            st.write(doc)
                            if metadata:
                                st.write("**Metadata:**")
                                st.json(metadata)
                
                # Delete functionality
                st.subheader("🗑️ Delete Documents")
                doc_to_delete = st.text_input("Document ID to Delete")
                if st.button("Delete Document", type="secondary"):
                    if doc_to_delete:
                        try:
                            st.session_state.collection.delete(ids=[doc_to_delete])
                            st.success(f"✅ Document '{doc_to_delete}' deleted!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error deleting document: {str(e)}")
        
        except Exception as e:
            st.error(f"❌ Error getting collection info: {str(e)}")
    
    # Database information
    st.subheader("💾 Database Information")
    db_path = os.path.join(os.getcwd(), "krish_demo_db")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Database Path:** `{db_path}`")
        st.write(f"**Database Exists:** {'✅ Yes' if os.path.exists(db_path) else '❌ No'}")
    
    with col2:
        if os.path.exists(db_path):
            try:
                # List collections
                collections = client.list_collections()
                st.write(f"**Collections:** {len(collections)}")
                for collection in collections:
                    st.write(f"- {collection.name}")
            except Exception as e:
                st.write(f"Error listing collections: {str(e)}")

if __name__ == "__main__":
    main()