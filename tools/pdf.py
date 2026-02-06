import pymupdf
import pymupdf.layout
import pymupdf4llm

def get_table_of_contents(pdf_path):
    pymupdf.TOOLS.mupdf_display_errors(False)
    try:
        with pymupdf.open(pdf_path) as document:
            table_of_contents = document.get_toc(simple=True)

            if (table_of_contents):
                print("Table of contents read successfully.")
                return table_of_contents
            else:
                md_text = pymupdf4llm.to_markdown(pdf_path, pages=list(range(0, 24)))
                print("First 25 pages read successfully.")
                return md_text
    except Exception as e:
        print("Error: " + str(e))

print(get_table_of_contents("bucket/textbooks/David H McIntyre_ Corinne A Manogue_ Janet Tate_ Oregon State Un - Quantum mechanics _ a paradigms approach (2012, Pearson ).pdf"))