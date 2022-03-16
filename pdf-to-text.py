import time
import os
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


class extract_text_from_pdf:
    def __init__(self, pdf_file_name, target_file_name):
        """Extracts PDF file into text file. 
        Args:
            file_name (string): PDF file name to extrat text from (including extension). 
            target_file_name (string): File name where text will be written as txt. 
        """
        self.pdf_file_name = pdf_file_name
        self.target_file_name = target_file_name

    def extract(self):
        """Start extract
        """
        print(
            f"Extrating '{self.pdf_file_name}' to '{self.target_file_name}'.")

        # Start measuring time it takes to extract text from PDF
        start = time.time()
        pdf_words = []

        # Create text file writer.
        writer = open(self.target_file_name, 'w', encoding="utf-8", newline="")
        # Extract pages from PDF
        for page_layout in extract_pages(self.pdf_file_name):
            # Retrieve PDF layout elements from a page.
            for element in page_layout:
                # Only look at text containers
                if isinstance(element, LTTextContainer):
                    # Get text from layout
                    layout_text = element.get_text()
                    # Remove 'newline' symbol
                    layout_text = layout_text.replace('\n', '')
                    # Split text into list of words
                    layout_words = layout_text.split()
                    # For ech word in the layout
                    for layout_word in layout_words:
                        # Remove leading and tailing white spaces
                        layout_word = layout_word.strip()
                        # Process words that are words and not empty strings
                        if layout_word != '':
                            pdf_words.append(layout_word)
        writer.write(' '.join(pdf_words))
        end = time.time()
        print(
            f"Extrating '{self.pdf_file_name}' took {end-start} seconds and extracted {len(pdf_words)} words")


# START our program here
folder = 'pdf_files'
files = os.listdir(folder)
for file in files:
    if file.endswith('.pdf'):
        target_file_name = os.path.splitext(file)[0]+'.txt'
        extractor = extract_text_from_pdf(os.path.join(
            folder, file), os.path.join(folder, target_file_name))
        extractor.extract()
