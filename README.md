# Automatically mining tags from PDF files

This is just a playground repository so far! :)

## How to run the scripts

1. Make sure you have pip installed (try typing pip). If not, install it
   with the command:
    
    sudo easy_install pip.

2. Install pdfminer

    sudo pip install pdfminer==20131113

3. Run the pdfreader.py:

    python pdfreader.py <path to PDF>

## What to do

A program that takes as input a PDF file and spits out a JSON formatted
document with suggested tags.

Steps:

- Convert a PDF to text
- Using different types of data from the AlchemyAPI

## Datas of interest

- Keywords
- Concepts
- Entities

## Questions

We need some sort of IT
