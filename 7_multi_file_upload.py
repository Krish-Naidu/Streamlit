# Import required libraries
import streamlit as st
import pandas as pd
from PIL import Image  # Python Imaging Library for working with images
from PyPDF2 import PdfReader
import json

# Set up the page configuration
st.title("📁 Multi-File Upload and Display Demo")
st.markdown("Upload multiple files and see all their content displayed below!")

# Multi-file uploader widget - accepts multiple file types
uploaded_files = st.file_uploader(
    "Choose files to upload", 
    type=['txt', 'csv', 'json', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py', 'html', 'md'],
    accept_multiple_files=True  # This enables multiple file selection
)

# Function to display individual file content
def display_file_content(uploaded_file, file_number):
    """Display content for a single uploaded file"""
    
    # Create an expander for each file to keep the interface organized
    with st.expander(f"📄 File {file_number}: {uploaded_file.name}", expanded=True):
        
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
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        st.subheader("📄 File Content")
        
        try:
            if file_extension in ['txt', 'py', 'html', 'css', 'js', 'md']:
                # Display text-based files
                content = uploaded_file.read().decode('utf-8')
                st.text_area(f"Content of {uploaded_file.name}", content, height=300, key=f"text_{file_number}")
                
            elif file_extension == 'csv':
                # Display CSV files as dataframe
                df = pd.read_csv(uploaded_file)
                st.write("**CSV Data:**")
                st.dataframe(df, key=f"csv_{file_number}")
                st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
                
            elif file_extension == 'json':
                # Display JSON files
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
                # Handle PDF files with PyPDF2
                st.write("**PDF File Content:**")
                try:
                    pdf_reader = PdfReader(uploaded_file)
                    text = ""
                    for page_num, page in enumerate(pdf_reader.pages):
                        text += f"\n--- Page {page_num + 1} ---\n"
                        text += page.extract_text()
                    
                    st.text_area(f"PDF Content of {uploaded_file.name}", text, height=300, key=f"pdf_{file_number}")
                    st.info(f"📋 Total pages: {len(pdf_reader.pages)}")
                    
                except Exception as pdf_error:
                    st.error(f"❌ Error reading PDF: {str(pdf_error)}")
                
            else:
                # For other file types, show raw content
                st.write("**Raw File Content (first 1000 bytes):**")
                raw_content = uploaded_file.read()
                if len(raw_content) > 1000:
                    st.text(raw_content[:1000])
                    st.info(f"Showing first 1000 bytes of {len(raw_content)} total bytes")
                else:
                    st.text(raw_content)
                    
        except Exception as e:
            st.error(f"❌ Error reading file {uploaded_file.name}: {str(e)}")
            st.info("The file might be in a format that requires special handling or might be corrupted.")

# Process and display all uploaded files
if uploaded_files:
    # Display summary information
    st.success(f"🎉 Successfully uploaded {len(uploaded_files)} file(s)!")
    
    # Show summary statistics
    total_size = sum(file.size for file in uploaded_files)
    file_types = list(set(file.name.split('.')[-1].lower() for file in uploaded_files))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📁 Total Files", len(uploaded_files))
    with col2:
        st.metric("💾 Total Size", f"{total_size:,} bytes")
    with col3:
        st.metric("🔧 File Types", len(file_types))
    
    st.write(f"**File Types Found:** {', '.join(file_types)}")
    
    # Display each file's content
    st.subheader("📋 File Contents")
    
    for i, uploaded_file in enumerate(uploaded_files, 1):
        display_file_content(uploaded_file, i)
        
        # Reset file pointer for next read (important for multiple operations)
        uploaded_file.seek(0)

else:
    # Show instructions when no files are uploaded
    st.info("👆 Please upload one or more files using the file uploader above")
    st.markdown("### 💡 Tips:")
    st.markdown("- You can select **multiple files** at once by holding Ctrl (Windows) or Cmd (Mac)")
    st.markdown("- You can **drag and drop** multiple files directly onto the uploader")
    st.markdown("- Mix different file types - upload CSVs, images, PDFs, and text files together!")
    
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

