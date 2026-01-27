# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template='Hello, <name>!'):
    greeting=template.replace("<name>", name)
    return greeting
print(greet('Kazio', "What's up, <name>!"))

