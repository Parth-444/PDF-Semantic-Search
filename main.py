import json
from search_engine.pdf_processor import PDFProcessor
from search_engine.search_service import SearchService

def main():
    """Main function to run the CLI-based semantic search system."""
    pdf_path = input("Enter you pdf path here: ").strip()
    print("Processing the PDF file...")

    # Extract text from PDF
    pdf_text = PDFProcessor.extract_text(pdf_path)

    # Initialize search service
    search_service = SearchService(pdf_text)

    while True:
        query = input("\nEnter your search query (or type 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            print("Exiting program.")
            break

        results = search_service.search(query)
        print("\nSearch Results (JSON Format):")
        print(json.dumps({"query": query, "results": results}, indent=4))

if __name__ == "__main__":
    main()
