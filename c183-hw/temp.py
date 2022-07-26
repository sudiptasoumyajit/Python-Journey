from tkinter import *
import requests
import json

root=Tk()
root.geometry('350x350')

city_name_label=Label(root,text='Capital City Name')
city_name_label.pack(relx=0.4,rely=0.25,anchor=CENTER)

city_entry=Entry(root)
city_entry.pack(relx=0.24,rely=0.25,anchor=CENTER)

country_name=:abel(root,text='Country:')
country_name.pack()

region=Label(root,text='Language:')
region.pack()

population=Label(root,text='Population:')
population.pack()

area=Label(root,text='Area:')
area.pack()

search_btn=Button(root,text='City Details:',command=city_details)
search_btn.pack()

def city_details():
    api_request=requests.get('https://restcountries.com/v3.1/capital/'+city_entry.get())
    api_output_json=json.loads(api_request.content)

    country=api_output_json[0]['name']['common']
    print(country)
    country_name['text']=country

    reg=api_output_json[0]['region']
    print(reg)
    region['text']=reg

    lang=api_output_json[0]['language']['fra']
    print(lang)
    country_name['text']=country

    popn=api_output_json[0]['population']
    print(popn)
    country_name['text']=country

    ca=api_output_json[0]['area']
    print(ca)
    country_name['text']=country

root.mainloop()