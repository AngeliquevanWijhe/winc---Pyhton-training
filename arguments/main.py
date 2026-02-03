# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template='Hello, <name>!'):
    greeting=template.replace("<name>", name)
    return greeting
print(greet('Kazio', "What's up, <name>!"))

def force(mass, body='earth'):
    
    data ={
        "sun":274,
        "mercury":3.7,
        "venus":8.87,
        "earth":9.798,
        "mars":3.71,
        "jupiter":24.92,
        "saturn":10.44,
        "uranus":8.87,
        "neptune":11.15,
        "pluto":0.58,
        "moon":1.62
        }

    gravity= round(data[body],1)
    print(gravity)
    return (mass*gravity)
print(force(2,'neptune'))


def pull(m1,m2,d):
    G=6.674*10**-11
    return (G*((m1*m2))/d**2)
print(pull(0.1,5.972*10**24,6.371*10**6))
