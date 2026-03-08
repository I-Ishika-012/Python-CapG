'''
Prog.9
Description
Password Strength Validator
Problem Description
A website checks the strength of passwords. A password is considered strong if it satisfies the following rules:

Length must be at least 8 characters

Must contain at least one uppercase letter

Must contain at least one digit

Must contain at least one special character (@, #, $)

Given a list of passwords, return a list containing only strong passwords.
'''

class Solution:
    def strong_passwords(self, passwords):
        strong = []
        spl="!@#$%^&*()-=?_+,<>/\"'\\`~[]{}"
        for password in passwords:
            if len(password)<8:
                continue
            upper = any(c.isupper() for c in password)
            digit = any(c.isdigit() for c in password)
            special = any(c in spl for c in password)

            if upper and digit and special:
                strong.append(password)
            
       
        return strong