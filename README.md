# Transcrevendo uma Imagem em Texto com AWS Textract

![AWS Textract](img/aws-textract-logo.png)  
*Extração de texto de imagens usando serviços AWS.*

## 📝 Visão Geral
Este projeto demonstra como usar o **AWS Textract** para extrair texto de uma imagem e convertê-lo em formato editável. Ideal para digitalização de documentos, reconhecimento de caracteres (OCR) e automação de processos.

## 🛠 Pré-requisitos
- Conta na AWS ([criar aqui](https://aws.amazon.com/pt/)).
- AWS CLI instalado ([guia de instalação](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)).
- Python 3.8+ e biblioteca Boto3 (`pip install boto3`).
- Uma imagem com texto (ex: `nota_fiscal.jpg`).

## 🔑 Configuração da AWS
1. **Crie um usuário IAM**:
   - Acesse o **Console da AWS > IAM**.
   - Crie um usuário com permissão `AmazonTextractFullAccess`.
   - Gere as chaves de acesso (**Access Key ID** e **Secret Access Key**).

2. **Configure a AWS CLI**:
   ```bash
   aws configure
