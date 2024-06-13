from flask import Flask, redirect, url_for, render_template, request, flash
import openai
import api_key
from PIL import Image
import io
import google.generativeai as genai
GOOGLE_API_KEY='AIzaSyDrllDFKLnI5q8dF361nvdzuL3h6O0JxmM'
genai.configure(api_key=GOOGLE_API_KEY)
model2 = genai.GenerativeModel('gemini-pro-vision')






app = Flask(__name__)
openai.api_key = api_key.val_api_key

#code for normal text model openai
@app.route('/',methods=["POST", "GET"])
def index():

    return render_template('index.html')

@app.route('/founder',methods=["POST", "GET"])
def founder():

    return render_template('founder.html')

@app.route('/services',methods=["POST", "GET"])
def services():

    return render_template('services.html')


#just trying openai here, calculating time complexity of a function
@app.route('/tc',methods=['POST','GET'])
def tc():
    if request.method=="POST":
        code=request.form['code']
        print(code)
        response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="{}\nThe time complexity of this function is".format(code),
    temperature=0.1,
    max_tokens=128,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
        #ans=response['choices'][0]['text']
        ans=response.choices[0].text
        print(ans)
        list = ans.split('\n')
        list = filter(None, list)
        tagline=" Time Complexity of the given code:-"
        return render_template('output.html',tagline=tagline, list=list)
        #return render_template('output.html',value=ans)
    else:
        heading="Calculate timeComplexity of code:"
        return render_template('pg2.html',heading=heading)

@app.route('/sql',methods=['POST','GET'])
def sql():
    if request.method=="POST":
        code=request.form['code']
        print(code)
        response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="{}".format(code),
  temperature=0,
  max_tokens=128,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
        ans=response.choices[0].text
        print(ans)
        list = ans.split('\n')
        list = filter(None, list)
        tagline="SQL queries:-"
        return render_template('outputsql.html',tagline=tagline, list=list)
    else:
        heading="Generate SQL queries for projects"
        return render_template('pg2.html',heading=heading)


@app.route('/explain',methods=['POST','GET'])
def explain():
    if request.method=="POST":
        code=request.form['code']
        lang=request.form.get('lang')
        print(code)
        print(lang)
        response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="{}\nHere's what the {} above code is doing: \n".format(code,lang),
  temperature=0,
  max_tokens=300,
  stop='</code>',
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
        ans=response.choices[0].text
        print(ans)
        list = ans.split('\n')
        list = filter(None, list)
        tagline="Ai explanation:-"
        return render_template('outputsql.html',tagline=tagline, list=list)
    else:
        heading="Paste your code , our AI will provide you an explanation."
        return render_template('explain-ip.html',heading=heading)


@app.route('/convert',methods=['POST','GET'])
def convert():
    if request.method=="POST":
        code=request.form['code']
        From=request.form['from']
        to=request.form['to']
        str1="#Convert this from {} to {}\n#{} version".format(From,to,From)
        print(code)
        print(str1)
        response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="{}\n{}\n#end\n\n {} version".format(str1,code,to),
  temperature=0,
  max_tokens=512,
  top_p=1,
  stop='#end',
  frequency_penalty=0,
  presence_penalty=0
)
        ans=response.choices[0].text
        print(ans)
        list = ans.split('\n')
        list = filter(None, list)
        heading="converted code:-"
        return render_template('outputsql.html',heading=heading, list=list)
    else:
        heading="Convert code from one language to another."
        return render_template('inputconvert.html',heading=heading)


@app.route('/create',methods=['POST','GET'])
def create():
    if request.method=="POST":
        code=request.form['code']
        lang=request.form.get('lang')
        print(code)
        print(lang)
        response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="{} \n language:{}\n".format(code,lang),
  temperature=0,
  max_tokens=300,
  stop='</code>',
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
        ans=response.choices[0].text
        print(ans)
        list = ans.split('\n')
        list = filter(None, list)
        tagline="A.I coded this for you"
        return render_template('outputsql.html',tagline=tagline, list=list)
    else:
        heading="Write your task,our A.I will write the code for you."
        return render_template('inputcreate.html',heading=heading)

@app.route('/purva',methods=["POST", "GET"])
def purva():
    if request.method=='POST':
        code=request.form['code']
        print(code)
        response=openai.Image.create(
        prompt=code,
        n=4,
        size="512x512"
        )
        img_list=[]
        for val in response['data']:
            img_list.append(val['url'])


        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a tagline for {code}",
        max_tokens=25,
        temperature=0
        )
        tagline=response2['choices'][0]['text']

        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a name for {code}",
        max_tokens=25,
        temperature=0
        )
        title=response2['choices'][0]['text']

        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write product description about {code} in less than 50 words",
        max_tokens=90,
        temperature=0
        )
        description=response2['choices'][0]['text']


        return render_template('dummy.html',tagline=tagline,list=img_list,title=title ,description=description)

    else:
        return render_template('inputbizz.html')




app.debug = True

app.run(debug=True,port=5500)
