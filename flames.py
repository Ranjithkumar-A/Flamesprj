import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template,url_for
from collections import Counter
from flask import *
app = Flask(__name__)
relation={'f':'Friendship','l':'Love','a':'Affection','m':'Marriage','e':'Enemy','s':'Siblings'}
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])  
def predict():
    from collections import Counter
    k=0;d=0;flag=1;rel="flames"
    uname=request.form['first'].replace(" ","")
    passwrd=request.form['last'].replace(" ","")
    if(uname.isalpha() and passwrd.isalpha()):
        a=Counter(uname.upper())
        b=Counter(passwrd.upper())
        for i in a:
            if i in b:
                n=min(a[i],b[i])
                a[i]=abs(a[i]-n)
                b[i]=abs(b[i]-n)
        k=sum(a.values())+sum(b.values())
        flag=1
        while(flag):
            f=k%len(rel)-1
            if(len(rel)>1):
                if(f!=-1):
                    rel=rel[f+1:]+rel[:f]
                elif(f==-1):
                    rel=rel[:-1]
            else:
                flag=0
        return render_template('content.html',name=uname,i=passwrd,relation=relation[rel])
    else:
        return render_template('index.html',msg="Sorry!! Please type the names in alphabets, no special characters are allowed")
   
if __name__ == '__main__':  
   app.run()
