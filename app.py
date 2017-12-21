from flask import Flask, url_for, request, render_template, redirect
import url_shortner
from db_query import get_short2_url, get_original_url
from urllib.parse import urlparse
from url_shortner import toBase62, toBase10


app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/',methods=['GET','POST'])

def index():
    if request.method=='GET':
        return render_template('main.html')

@app.route('/get_short_url',methods=['POST'])
def get_short_url():
    url = request.data.decode("UTF-8")
    url = url[1:len(url)-1]
    if not urlparse(url).scheme:
        url = "http://{}".format(url)
        print(url)
    req = get_short2_url(url)
    short = toBase62(req,62)
    print(short)
    return short

@app.route('/<st_url>')
def st_url(st_url):
     id = toBase10(st_url,62)   
     try:
         org_url = get_original_url(id)
         return redirect(org_url)
     except:
         return "invalid request"
if __name__ == '__main__':
    app.run(debug=True, port=6100)



