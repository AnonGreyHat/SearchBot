try:

    from mechanize import Browser

except:

    os. system("pip install mechanize")

try:

    import pyfiglet

except:

    os. system("pip install pyfiglet")

R="\033[1;31m" 

G="\033[1;32m" 

Y="\033[1;33m" 

res = pyfiglet.figlet_format(" SEARCH  \n       BOT      ",font="banner3-D")

print(Y+res)

print(G+'Search what ever you want on the internet using this  tools\nif you want to make a search you have to start with \"cb"\ne.g cb http://www.google.com or cd what is hacking\n\n')

def result():

    chat =(input (G+"Search"+R+" ==>"+Y+" " ))

    if chat.startswith("cb"):

        print(G+"Processing Results")

        browser = Browser()

        response = browser. open(chat)

        print(response.code)

    else: print('Not Me use \"cb" to start your search')

    result()

result()
