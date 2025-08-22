from PyPDF2 import PdfReader

file_path = "C:\\Users\\krish\\OneDrive\\Documents\\A_Levels\\Computer_Science\\CPU.pdf"
reader = PdfReader(file_path)
number_of_pages = len(reader.pages)

# Read all pages and combine the text
all_text = ""
for page_num in range(number_of_pages):
    page = reader.pages[page_num]
    page_text = page.extract_text()
    all_text += f"\n--- Page {page_num + 1} ---\n"
    all_text += page_text + "\n"

print(f"Total pages: {number_of_pages}")
print(all_text)