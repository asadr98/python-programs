"""This program is designed to parse through emails.
"""
import re
import sys
from argparse import ArgumentParser


class Server:
    """This class stores the data for all emails found in the dataset.
    Attr:
    emails (list):Emails
    individ_emails (list): Each individual email.
    message_id (str): Message id of email
    date (str): Date of email
    subject (str): Subject of email
    sender (str): Sender of email
    reciever (str): Reciever of email 
    body (str): Body of email
    """
    def __init__(self, path):
        self.emails = []
        self.individ_emails = []
        
        with open(path, "r", encoding = "utf-8") as f:
            text = f.read()
            individ_emails = text.split('End Email"')
            individ_emails.pop()
            #print(len(individ_emails))
            for each_email in individ_emails:
                #emails.append(individ_emails)
            
                #print(each_email)
                message_id = re.compile(r'Message-ID:\s\S(\w.+)\S').search(each_email).group(1)
                print("This is message ID: ", message_id) 
                date = re.compile(r'Date:\s(.+)').search(each_email).group(1)
                print("This is the date: ", date)
                sender = re.compile(r'From:\s(.+)').search(each_email).group(1)
                print("This is the sender: ", sender)
                reciever = re.compile(r'To:(.+)').search(each_email).group(1)
                print("This is the reciever: ", reciever)
                subject = re.compile(r'Subject:(.+)').search(each_email).group(1)
                print("this is the subject: ", subject)
                body = re.compile(r'X-FileName:\s.+\s+(.+)').search(each_email).group(1)
                print("This is the body: ", body)
                self.emails.append(Email(message_id, date, sender, reciever, subject, body))
                
        
               

class Email:
    """This class stores the data related to individual email messages.
    Attr:
    message_id (str): The message-id that is unique to each email message
    date (str):  The date associated with each email message.
    subject (str): The subject of each email message.
    sender (str): The sender of each email message.
    reciever (str): The reciever of each email message.
    body (str): The body message of each email message.
    """
    def __init__(self, message_id, date, sender, reciever, subject, body):
        self.message_id = message_id
        self.date = date
        self.sender = sender
        self.reciever = reciever
        self.subject = subject
        self.body = body
        

def main(f):
    """Calls other functions.
    Parameters:
    Path (str): the path of the text file that will be parsed.
    
    Returns:
    len(dfr.emails): (int) The length of the emails attribute of that instance
    """
    dfr = Server(f)
    return len(dfr.emails)
    

def parse_args(arglist):
    """ Parse command-line arguments. 
    Attr:
    parser
    parser.add_argument
    Returns:
    arglist"""
    parser = ArgumentParser(arglist)
    parser.add_argument("path")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    """Runs function.
    Attr:
    args
    Prints:
    Main function
    """
    pass
    args = parse_args(sys.argv[1:])
    print(main(args.path))