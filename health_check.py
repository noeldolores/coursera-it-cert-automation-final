#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import pathlib
import emails

def cpu_check(limit, interval): #80%
  cpu_percentage = psutil.cpu_percent(interval)
  if cpu_percentage > limit:
    print("CPU: " + str(cpu_percentage))
    return True    
  else:
    return False

def disk_chek(limit): #20%
  free_space = (shutil.disk_usage(pathlib.Path().absolute())[2] / shutil.disk_usage(pathlib.Path().absolute())[0]) * 100
  if free_space < limit:
    print("Disk: " + str(free_space))
    return True
  else:
    return False


def memory_check(limit): #500mb
  free_memory = psutil.virtual_memory()[4] / 1000000
  if free_memory < limit:
    print("Memory: " + str(free_memory) + "mb")
    return True
  else:
    return False
    

def socket_check(name, ip): #localhost, 127.0.0.1
  ip_address = socket.gethostbyname(name)
  if ip != ip_address:
    print("Name: " + name + " -> " + "ip: " + ip_address)
    return True
  else:
    return False

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
email_subject = ""
body = "Please check your system and resolve the issue as soon as possible."

if cpu_check(80, 4):
  email_subject = "Error - CPU usage is over 80%"
if disk_chek(20):
  email_subject = "Error - Available disk space is less than 20%"
if memory_check(500):
  email_subject = "Error - Available memory is less than 500MB"
if socket_check("localhost", "127.0.0.1"):
  email_subject = "Error - localhost cannot be resolved to 127.0.0.1"

if len(email_subject) > 0:
  message = emails.generate_error_report(sender, receiver, email_subject, body)
  emails.send_email(message)

