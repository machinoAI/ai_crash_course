"""
RAG Document Parsing

1. Excel / CSV
   - XLSX → openpyxl
   - CSV → pandas
   - Preserve sheet, headers, rows, tables as metadata

2. PDF
   - Text → PyMuPDF
   - Tables → pdfplumber / Camelot
   - Scanned PDF → PaddleOCR / Tesseract
   - Preserve page number + sections

3. DOCX
   - python-docx
   - Extract paragraphs, headings, tables
   - Preserve document hierarchy

4. PPT / PPTX
   - python-pptx
   - Extract slide title, text, bullets, tables, notes
   - Preserve slide number + title

5. TXT / Markdown
   - TXT → Python file handling
   - Markdown → markdown
   - Preserve headings, paragraphs, sections

6. HTML / Web
   - BeautifulSoup / trafilatura
   - Remove navigation, scripts, boilerplate
   - Preserve title, headings, URL

7. Images / Scanned Documents
   - OCR → PaddleOCR / Tesseract
   - Complex images/charts → Vision LLM
   - Convert to text + metadata

8. Architecture:
    PDF
 ↓
Extract text + tables + images
 ↓
 ├── Normal text → Text parser
 ├── Tables      → Table parser
 └── Images
      ↓
      ├── Simple text image → OCR
      └── Chart / Diagram / Infographic
             ↓
          Vision LLM
             ↓
      Text + relationships
             ↓
          Chunking
             ↓
        Embeddings
             ↓
         Vector DB

9. To convert the images to embedding, multi-modal embedding modal is required like:
    - CLIP — classic image ↔ text embedding; good for visual similarity/search.
    - Cohere Embed v4 — multimodal text/image embeddings.
    - Voyage Multimodal 3.5 — multimodal embeddings.
    - Google Gemini Embedding 2 — text, image, PDF and audio embeddings.
    - ImageBind — image + text + several other modalitie

Common Flow:
Parser → Normalize → Chunk → Embed → Vector DB

10. Weaviate or PineCone is the right choice for multi-modal embeddings.


11. When we are retrieving the images from vectorDB, we must use multi-modal llm.

                    ┌── Text ──→ Text Embedding ──┐
PDF                 │                              │
                    ├── Tables → Text/Embedding ──┤
                    │                              ├→ Vector DB
                    ├── Images → Image Embedding ─┤
                    │                              │
                    └── Images → Vision LLM → Text ┘
                                                   ↓
                                              Retrieval
                                                   ↓
                                     ┌─────────────┴─────────────┐
                                     ↓                           ↓
                              Text/Metadata                  Images
                                     ↓                           ↓
                              Text LLM                  Multimodal LLM




"""

""""
How to identify number of images ?

import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    total_images = sum(len(page.images) for page in pdf.pages)

print(total_images)

"""