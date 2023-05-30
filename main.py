import datetime as dt

print("Hello World")

def mostrar_data():
    Element('data').write(str(dt.date.today()))
    print(dt.date.today())

    
mostrar_data()