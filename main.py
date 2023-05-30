import datetime as dt

print("Hello World")

def mostrar_data():
   Element('data').write(str(dt.date.today()))
   print(dt.date.today())

    
mostrar_data()


def write_to_page():
      manual_div = Element("manual-write")
      manual_div.element.innerHTML = "<p><b>Hello World</b></p>"
      