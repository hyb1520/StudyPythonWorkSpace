import re

remail = re.compile(r'^(\w+.*)(@\w+\.com)$')
m = 'someone@!@gmail.com'
print(remail.match(m).groups())



M=['someone@gmail.com','bill.gates@microsoft.com']
re_mail=re.compile(r'^(\w{1}\S+)@(\w+).{1}(com|org)$')

for m in M:
    print (re_mail.match(m).groups())