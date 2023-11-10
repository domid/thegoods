import argparse
import pdfkit

def main():
    parser = argparse.ArgumentParser(description="Convert URLs to PDF")
    parser.add_argument("file", help="Text file containing URLs, each on a new line")
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        urls = file.read().splitlines()

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8"
    }

    output_filename = "output.pdf"
    pdfkit.from_url(urls, output_filename, options=options)
    print(f"PDF saved as {output_filename}")

if __name__ == "__main__":
    main()
