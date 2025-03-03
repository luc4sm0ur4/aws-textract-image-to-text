import boto3
import argparse

def extract_text_from_image(image_path):
    client = boto3.client('textract')
    with open(image_path, 'rb') as file:
        image_bytes = bytearray(file.read())
    
    response = client.detect_document_text(Document={'Bytes': image_bytes})
    
    extracted_text = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text.append(block['Text'])
    
    return '\n'.join(extracted_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=True, help='Caminho da imagem (ex: img/nota_fiscal.jpg)')
    args = parser.parse_args()
    
    text = extract_text_from_image(args.image)
    print("Texto extraído:\n")
    print(text)
