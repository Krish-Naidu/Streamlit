# Import required libraries
import streamlit as st
import pandas as pd
from PIL import Image #Python Imaging Library. library for working with images in Python.
from PyPDF2 import PdfReader

# Set up the page configuration
st.title("📁 File Upload and Display Demo")
st.markdown("Upload a file and see its content displayed below!")

# File uploader widget - accepts multiple file types
uploaded_file = st.file_uploader(
    "Choose a file to upload", 
    type=['txt', 'csv', 'json', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py', 'html', 'md']
)

# Process and display the uploaded file
if uploaded_file is not None:
    # Display file information
    st.success(f"✅ File uploaded successfully!")
    
    # Show file details
    file_details = {
        "Filename": uploaded_file.name,
        "File Type": uploaded_file.type,
        "File Size": f"{uploaded_file.size} bytes"
    }
    
    st.subheader("📊 File Information")
    for key, value in file_details.items():
        st.write(f"**{key}:** {value}")
    
    # Get file extension to determine how to display content
    # Splits the filename at every dot (.) into a list
    # .lower() - Converts the extension to lowercase
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    st.subheader("📄 File Content")
     
    try:
        if file_extension in ['txt', 'py', 'html', 'css', 'js', 'md']:
            # Display text-based files
            content = uploaded_file.read().decode('utf-8')
            st.text_area("File Content", content, height=400)
            
        elif file_extension == 'csv':
            # Display CSV files as dataframe
            df = pd.read_csv(uploaded_file)
            st.write("**CSV Data:**")
            st.dataframe(df)
            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
            
        elif file_extension == 'json':
            # Display JSON files
            import json
            content = uploaded_file.read().decode('utf-8')
            json_data = json.loads(content)
            st.write("**JSON Content:**")
            st.json(json_data)
            
        elif file_extension in ['png', 'jpg', 'jpeg', 'gif']:
            # Display image files
            image = Image.open(uploaded_file)
            st.write("**Image Preview:**")
            st.image(image, caption=f"Uploaded Image: {uploaded_file.name}")
            st.write(f"**Image Size:** {image.size[0]} × {image.size[1]} pixels")
            
        elif file_extension == 'pdf':
            # For PDF files, show that it's uploaded but would need PyPDF2 for content
            st.write("**PDF File Detected**")
            st.info("📋 PDF content extraction requires PyPDF2. File uploaded successfully but content preview not available in this demo.")
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            st.text_area("PDF Content", text, height=400)

        else:
            # For other file types, show raw content or hex dump
            st.write("**Raw File Content (first 1000 bytes):**")
            raw_content = uploaded_file.read()
            if len(raw_content) > 1000:
                st.text(raw_content[:1000])
                st.info(f"Showing first 1000 bytes of {len(raw_content)} total bytes")
            else:
                st.text(raw_content)
                
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.info("The file might be in a format that requires special handling or might be corrupted.")

else:
    # Show instructions when no file is uploaded
    st.info("👆 Please upload a file using the file uploader above")
    
    # Show supported file types
    st.subheader("📋 Supported File Types")
    supported_types = {
        "Text Files": "txt, py, html, css, js, md",
        "Data Files": "csv, json",
        "Image Files": "png, jpg, jpeg, gif", 
        "Document Files": "pdf",
        "Other": "Any file type (raw content display)"
    }
    
    for category, types in supported_types.items():
        st.write(f"**{category}:** {types}")

# # Add a download section for demonstration
# st.subheader("💾 Download Sample Files")
# st.markdown("You can download these sample files to test the upload functionality:")

# # Create sample content for download
# sample_txt = "Hello World!\nThis is a sample text file.\nYou can upload this to test the file reader."
# sample_csv = "Name,Age,City\nJohn,25,New York\nJane,30,London\nBob,35,Paris"
# sample_json = '{"name": "Sample Data", "version": "1.0", "items": ["apple", "banana", "orange"]}'

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.download_button(
#         label="📄 Download Sample TXT",
#         data=sample_txt,
#         file_name="sample.txt",
#         mime="text/plain"
#     )

# with col2:
#     st.download_button(
#         label="📊 Download Sample CSV", 
#         data=sample_csv,
#         file_name="sample.csv",
#         mime="text/csv"
#     )

# with col3:
#     st.download_button(
#         label="🔧 Download Sample JSON",
#         data=sample_json,
#         file_name="sample.json",
#         mime="application/json"
#     )
