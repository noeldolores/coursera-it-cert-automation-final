#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

def process_descriptions(path):
  pdf_paragraph = ""
  for files in os.listdir(description_path):
    with open(description_path + files) as f:
      _ = f.read().splitlines()
      pdf_paragraph += "name: " + _[0] + "\n"
      pdf_paragraph += "weight: " + _[1] + "\n\n"
  return pdf_paragraph

if __name__ == "__main__":
  description_path = "supplier-data/descriptions/"
  today = date.today()
  _date = today.strftime("%B %d, %Y")
  pdf_title = "Processed Update on " + _date
  pdf_paragraph = process_descriptions(description_path)
  reports.generate_report('/tmp/processed.pdf',pdf_title,pdf_paragraph)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)
