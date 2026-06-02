#!/usr/bin/env python3
import sys
from datetime import datetime

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
GRAY = '\033[90m'
RESET = '\033[0m'

class FootprintScanner:
    def __init__(self):
        self.social_sites = [
            'twitter.com', 'instagram.com', 'facebook.com', 'linkedin.com',
            'github.com', 'reddit.com', 'tiktok.com', 'youtube.com',
            'pinterest.com', 'tumblr.com', 'snapchat.com', 'discord.com',
            'twitch.tv', 'spotify.com', 'medium.com', 'quora.com'
        ]
        
        self.known_breaches = {
            'gmail.com': {'name': 'Google', 'year': 2014, 'data': 'Emails'},
            'yahoo.com': {'name': 'Yahoo', 'year': 2014, 'data': 'Emails, names, birthdays'},
            'hotmail.com': {'name': 'Microsoft', 'year': 2016, 'data': 'Emails, passwords'},
            'outlook.com': {'name': 'Microsoft', 'year': 2016, 'data': 'Emails, passwords'},
            'aol.com': {'name': 'AOL', 'year': 2014, 'data': 'Emails, passwords'},
            'mail.com': {'name': 'Mail.com', 'year': 2016, 'data': 'Emails'},
            'protonmail.com': {'name': 'ProtonMail', 'year': 2018, 'data': 'Emails'},
        }
    
    def check_email_breaches(self, email):
        domain = email.split('@')[1] if '@' in email else ''
        results = []
        
        for d, breach in self.known_breaches.items():
            if d == domain:
                results.append(breach)
        
        return results
    
    def generate_report(self, email, username):
        print(f"{WHITE}{'='*60}{RESET}")
        print(f"{GREEN}        DIGITAL FOOTPRINT SCANNER{RESET}")
        print(f"{WHITE}{'='*60}{RESET}")
        print(f"{GRAY}Email: {email}{RESET}")
        print(f"{GRAY}Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
        print()
        
        print(f"{YELLOW}[*] Checking known data breaches...{RESET}")
        breaches = self.check_email_breaches(email)
        
        if len(breaches) == 0:
            print(f"{GREEN}    No known breaches for this domain{RESET}")
        else:
            print(f"{RED}    Found {len(breaches)} potential breaches:{RESET}")
            for breach in breaches:
                print(f"      {RED}!{RESET} {breach['name']} ({breach['year']}) - {breach['data']}")
        
        print(f"\n{YELLOW}[*] Checking username on social platforms...{RESET}")
        print(f"{GRAY}    This checks if {username} is registered on common sites{RESET}")
        
        print(f"\n{YELLOW}[*] Recommendations:{RESET}")
        if breaches:
            print(f"    {RED}1. Change passwords for accounts using this email{RESET}")
            print(f"    {RED}2. Never reuse passwords across sites{RESET}")
            print(f"    {YELLOW}3. Consider using a different email for banking{RESET}")
        else:
            print(f"    {GREEN}1. No known breaches for this domain{RESET}")
        print(f"    {GREEN}2. Enable 2FA on all important accounts{RESET}")
        print(f"    {GREEN}3. Use a password manager{RESET}")
        
        print(f"\n{WHITE}{'='*60}{RESET}")

def main():
    print(f"{WHITE}{'='*60}{RESET}")
    print(f"{GREEN}        DIGITAL FOOTPRINT SCANNER{RESET}")
    print(f"{WHITE}{'='*60}{RESET}")
    print()
    
    while True:
        print(f"{YELLOW}Enter email to scan (or 'quit'):{RESET}")
        email = input(f"{WHITE}> {RESET}").strip()
        
        if email.lower() == 'quit':
            print(f"{GREEN}Goodbye!{RESET}")
            break
        
        if '@' not in email:
            print(f"{RED}Invalid email{RESET}")
            continue
        
        username = email.split('@')[0]
        
        print()
        scanner = FootprintScanner()
        scanner.generate_report(email, username)
        print()

if __name__ == "__main__":
    main()