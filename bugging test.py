def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Je kan iets niet door nul delen.")
    return None

print(divide(2,1))

# def fetch_user_snippets():
#     user = requests.get('https://run.mocky.io/v3/3b7fdcfc-53b9-43e7-9042-53d1870c8693').json() # fetch user
#     snippets = requests.get('https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json() # fetch snippets
#     snippets = [s['snippet'] for s in snippets if s['user_id'] == user['meta']['user_id']]
#     return snippets

def fetch_user_snippets():
    user = requests.get('https://run.mocky.io/v3/3b7fdcfc-53b9-43e7-9042-53d1870c8693').json()
    breakpoint() # halt execution and open a shell
    snippets = requests.get('https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()
    snippets = [s['snippet'] for s in snippets if s['user_id'] == user['meta']['user_id']]
    return snippets

if 1 == 1:
    pass
else:
    raise AssertionError

assert 1 == 3, "need a calculator"
