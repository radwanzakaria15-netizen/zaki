from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# تخزين البيانات
stored_data = {
    "s1": {},
    "s2": {}
}

# ------------------ CSS ------------------

style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

body{
font-family:'Cairo',sans-serif;
margin:0;
background:linear-gradient(-45deg,#1b1b2f,#4e54c8,#00c6ff,#0072ff);
background-size:400% 400%;
animation:gradientMove 25s ease infinite;
color:white;
display:flex;
flex-direction:column;
align-items:center;
}

@keyframes gradientMove{
0%{background-position:0% 50%}
50%{background-position:100% 50%}
100%{background-position:0% 50%}
}

.container{
max-width:900px;
width:95%;
background:rgba(0,0,0,0.6);
padding:30px;
border-radius:25px;
margin-top:40px;
}

.cards{
display:flex;
flex-wrap:wrap;
gap:20px;
justify-content:center;
}

.card{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:20px;
width:230px;
text-align:center;
}

.card input{
width:40%;
padding:10px;
margin:5px;
border:none;
border-radius:10px;
text-align:center;
background:rgba(255,255,255,0.15);
color:white;
}

button{
padding:12px 25px;
border:none;
border-radius:20px;
background:linear-gradient(90deg,#00ffff,#0072ff);
cursor:pointer;
font-weight:bold;
}

.result{
margin-top:25px;
font-size:26px;
text-align:center;
}
</style>
"""

# ------------------ الصفحة الرئيسية ------------------

home = """
<html>
<head>
<meta charset="UTF-8">
<title>Zaki</title>
""" + style + """
</head>

<body>

<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>

<br>

<a href="/s1"><button>السداسي الأول</button></a>
<a href="/s2"><button>السداسي الثاني</button></a>
<a href="/year"><button>المعدل السنوي</button></a>

</body>
</html>
"""

# ------------------ قالب السداسي ------------------

s_template = """
<html>
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
""" + style + """
</head>

<body>

<div class="container">

<h2>{{title}}</h2>

<form method="post">

<div class="cards">

<div class="card">
<h3>النحو</h3>
<input type="number" name="tdnaho" placeholder="TD" value="{{data.get('tdnaho','')}}">
<input type="number" name="examnaho" placeholder="Exam" value="{{data.get('examnaho','')}}">
</div>

<div class="card">
<h3>الصرف</h3>
<input type="number" name="tdsrf" placeholder="TD" value="{{data.get('tdsrf','')}}">
<input type="number" name="examsrf" placeholder="Exam" value="{{data.get('examsrf','')}}">
</div>

<div class="card">
<h3>الأدب</h3>
<input type="number" name="tdadab" placeholder="TD" value="{{data.get('tdadab','')}}">
<input type="number" name="examadab" placeholder="Exam" value="{{data.get('examadab','')}}">
</div>

<div class="card">
<h3>الرياضيات</h3>
<input type="number" name="tdm" placeholder="TD" value="{{data.get('tdm','')}}">
<input type="number" name="examm" placeholder="Exam" value="{{data.get('examm','')}}">
</div>

<div class="card">
<h3>الفيزياء</h3>
<input type="number" name="tdf" placeholder="TD" value="{{data.get('tdf','')}}">
<input type="number" name="examf" placeholder="Exam" value="{{data.get('examf','')}}">
</div>

<div class="card">
<h3>الكيمياء</h3>
<input type="number" name="tdc" placeholder="TD" value="{{data.get('tdc','')}}">
<input type="number" name="examc" placeholder="Exam" value="{{data.get('examc','')}}">
</div>

</div>

<br>

<button type="submit">احسب المعدل</button>

</form>

{% if mo3adal %}
<div class="result">

🔥 معدلك هو {{mo3adal}}

<br>

{{msg}}

<br><br>

<a href="/reset/{{sem}}"><button>إعادة الحساب</button></a>
<a href="/"><button>الرئيسية</button></a>

</div>
{% endif %}

</div>

</body>
</html>
"""

# ------------------ حساب المعدل ------------------

def calc_s(data):

naho=(float(data["tdnaho"])*0.33+float(data["examnaho"])*0.67)*2
srf=(float(data["tdsrf"])*0.33+float(data["examsrf"])*0.67)*2
adab=(float(data["tdadab"])*0.33+float(data["examadab"])*0.67)*2
math=(float(data["tdm"])*0.33+float(data["examm"])*0.67)*2
phys=(float(data["tdf"])*0.33+float(data["examf"])*0.67)*2
chem=(float(data["tdc"])*0.33+float(data["examc"])*0.67)*2

return {
"n":naho,
"s":srf,
"a":adab,
"m":math,
"f":phys,
"c":chem
}

# ------------------ الصفحة الرئيسية ------------------

@app.route("/")
def index():
    return render_template_string(home)

# ------------------ إعادة الحساب ------------------

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem]={}
    return redirect(url_for(sem))

# ------------------ السداسي الأول ------------------

@app.route("/s1",methods=["GET","POST"])
def s1():

mo3adal=None
msg=""

if request.method=="POST":

stored_data["s1"]=request.form.to_dict()

res=calc_s(stored_data["s1"])

mo3adal=round(sum(res.values())/12,2)

msg="🎉 مبروك نجحت" if mo3adal>=10 else "❌ حاول أكثر"

return render_template_string(
s_template,
title="السداسي الأول",
data=stored_data["s1"],
mo3adal=mo3adal,
msg=msg,
sem="s1"
)

# ------------------ السداسي الثاني ------------------

@app.route("/s2",methods=["GET","POST"])
def s2():

mo3adal=None
msg=""

if request.method=="POST":

stored_data["s2"]=request.form.to_dict()

res=calc_s(stored_data["s2"])

mo3adal=round(sum(res.values())/12,2)

msg="🎉 مبروك نجحت" if mo3adal>=10 else "❌ يمكنك التعويض"

return render_template_string(
s_template,
title="السداسي الثاني",
data=stored_data["s2"],
mo3adal=mo3adal,
msg=msg,
sem="s2"
)

# ------------------ المعدل السنوي ------------------

@app.route("/year")
def year():

mo3adal=None

if stored_data["s1"] and stored_data["s2"]:

r1=calc_s(stored_data["s1"])
r2=calc_s(stored_data["s2"])

mo3adal=round((sum(r1.values())+sum(r2.values()))/24,2)

return f"<h1 style='color:white'>المعدل السنوي: {mo3adal}</h1>" if mo3adal else "<h1 style='color:white'>املأ السداسيين أولاً</h1>"

# ------------------

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

# تخزين البيانات لكل سداسي
stored_data = {'s1': {}, 's2': {}}

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdnaho','')}}">
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examnaho','')}}">
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdsrf','')}}">
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examsrf','')}}">
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdadab','')}}">
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examadab','')}}">
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdm','')}}">
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examm','')}}">
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdf','')}}">
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examf','')}}">
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdc','')}}">
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examc','')}}">
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examchari3a','')}}">
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required value="{{data.get('tdtech','')}}">
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required value="{{data.get('examtech','')}}">
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required value="{{data.get('b','')}}">
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required value="{{data.get('e','')}}">
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required value="{{data.get('i','')}}">
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required value="{{data.get('y','')}}">
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة الحساب</a>
<a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/reset/<sem>")
def reset(sem):
    stored_data[sem] = {}  # مسح البيانات
    return redirect(url_for(sem))

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s1'] = request.form.to_dict()
        res=calc_s(stored_data['s1'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال السداسي الثاني")
    data = stored_data['s1']
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1")

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        stored_data['s2'] = request.form.to_dict()
        res=calc_s(stored_data['s2'])
        mo3adal=round(sum(res.values())/19,2)
        msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else ("✅ مبروك، راك نجحت!" if mo3adal>=10 else "❌ لا تقلق، مزال الاستدراكي أو السداسي الأول")
    data = stored_data['s2']
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2")

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    if stored_data['s1'] and stored_data['s2']:
        res1=calc_s(stored_data['s1'])
        res2=calc_s(stored_data['s2'])
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)
    year_template = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="UTF-8">
    <title>المعدل السنوي</title>
    ''' + style + '''
    </head>
    <body>
    <div class="container">
    <h2 class="result-title">حساب المعدل السنوي</h2>
    {% if mo3adal %}
    <div class="result">
    🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
    {% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
    </div>
    {% else %}
    <div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
    {% endif %}
    <a href="/" class="home-btn">🏠 الصفحة الرئيسية</a>
    </div>
    </body>
    </html>
    '''
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    width:100%;
    height:100%;
    background: linear-gradient(-45deg, #1b1b2f, #4e54c8, #00c6ff, #0072ff);
    background-size: 400% 400%;
    animation: gradientMove 25s ease infinite;
    color:white;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

@keyframes gradientMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

header{
    text-align:center;
    margin-bottom:50px;
}

header h1{
    font-size:60px;
    color:#00ffff;
}

header h2{
    font-size:28px;
    color:#ffffff;
}

.buttons{
    display:flex;
    justify-content:center;
    gap:30px;
    flex-wrap:wrap;
}

.buttons a{
    text-decoration:none;
}

.buttons a button{
    padding:25px 50px;
    font-size:22px;
    font-weight:bold;
    border:none;
    border-radius:30px;
    cursor:pointer;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color:#1b1b2f;
    transition:0.3s;
}

.buttons a button:hover{
    transform:scale(1.08);
}

.container{
    max-width:900px;
    width:95%;
    margin:30px auto;
    padding:30px;
    background: rgba(0,0,0,0.6);
    border-radius:25px;
    display:flex;
    flex-direction:column;
    align-items:center;
}

h2.result-title{
    text-align:center;
    color:#00ffff;
    margin-bottom:30px;
    font-size:28px;
}

.cards{
    display:flex;
    flex-wrap:wrap;
    gap:20px;
    justify-content:center;
}

.card{
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    width: 250px;
    text-align:center;
    transition:0.3s;
}
.card:hover{
    transform: translateY(-6px);
}

.card h3{
    margin-bottom:15px;
    color:#ffd700;
}

.card input{
    width:40%;
    padding:10px;
    margin:5px 3%;
    border-radius:12px;
    border:none;
    background: rgba(255,255,255,0.12);
    color:#fff;
    font-weight:bold;
    text-align:center;
    transition:0.25s;
}

.card input:focus{
    background: rgba(0,255,255,0.2);
    transform: scale(1.05);
    outline:none;
}

button.calc{
    display:block;
    margin:25px auto 0 auto;
    padding:14px 28px;
    border:none;
    border-radius:22px;
    font-weight:bold;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color:#1b1b2f;
    font-size:16px;
    cursor:pointer;
    transition:0.3s;
}
button.calc:hover{
    transform:scale(1.08);
}

.result{
    margin-top:28px;
    font-size:28px;
    font-weight:bold;
    text-align:center;
    padding:18px;
    border-radius:20px;
    background: rgba(255,255,255,0.07);
}

a.reset-btn{
    display:inline-block;
    margin-top:18px;
    padding:14px 28px;
    background: linear-gradient(90deg,#0072ff,#00ffff);
    color:#1b1b2f;
    border-radius:18px;
    font-weight:bold;
    text-decoration:none;
    transition:0.3s;
}

footer{
    text-align:center;
    font-size:18px;
    color:#00ffff;
    margin-top:30px;
}
footer a{
    color:#00ffff;
    text-decoration:none;
    transition:0.3s;
    margin-left:10px;
}

@media(max-width:768px){
    .cards { flex-direction: column; align-items:center;}
    .card { width:90%; }
    .card input { width:45%; }
    .buttons a button { width:90%; padding:20px 0; }
}
</style>
'''

home = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
''' + style + '''
</head>
<body>
<header>
<h1>Zaki</h1>
<h2>📊 موقع حساب المعدل</h2>
</header>

<div class="buttons">
<a href="/s1"><button>حساب معدل السداسي الأول</button></a>
<a href="/s2"><button>حساب معدل السداسي الثاني</button></a>
<a href="/year"><button>حساب المعدل السنوي</button></a>
</div>

<footer>
<a href="https://t.me/zakariazakii" target="_blank"><i class="fab fa-telegram fa-2x"></i></a>
</footer>
</body>
</html>
'''

s_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>{{title}}</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">{{title}}</h2>
<form method="post">
<div class="cards">
<div class="card"><h3>النحو</h3>
  <input type="number" name="tdnaho" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examnaho" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الصرف</h3>
  <input type="number" name="tdsrf" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examsrf" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الأدب</h3>
  <input type="number" name="tdadab" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examadab" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الرياضيات</h3>
  <input type="number" name="tdm" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examm" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الفيزياء</h3>
  <input type="number" name="tdf" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examf" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الكيمياء</h3>
  <input type="number" name="tdc" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examc" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>الشريعة</h3>
  <input type="number" name="examchari3a" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>{{tech_name}}</h3>
  <input type="number" name="tdtech" placeholder="TD" min="0" max="20" step="0.01" required>
  <input type="number" name="examtech" placeholder="Exam" min="0" max="20" step="0.01" required>
</div>
<div class="card"><h3>مواد أخرى</h3>
  <input type="number" name="b" placeholder="البلاغة" min="0" max="20" step="0.01" required>
  <input type="number" name="e" placeholder="الانجليزية" min="0" max="20" step="0.01" required>
  <input type="number" name="i" placeholder="{{other_name}}" min="0" max="20" step="0.01" required>
  <input type="number" name="y" placeholder="فنيات الكتابة" min="0" max="20" step="0.01" required>
</div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/" class="reset-btn">🔄 إعادة الحساب</a>
{% endif %}

</div>
</body>
</html>
'''

def calc_s(s):
    n=(float(s["tdnaho"])*0.33+float(s["examnaho"])*0.67)*2
    srf=(float(s["tdsrf"])*0.33+float(s["examsrf"])*0.67)*2
    a=(float(s["tdadab"])*0.33+float(s["examadab"])*0.67)*2
    m=(float(s["tdm"])*0.33+float(s["examm"])*0.67)*2
    f=(float(s["tdf"])*0.33+float(s["examf"])*0.67)*2
    c=(float(s["tdc"])*0.33+float(s["examc"])*0.67)*2
    ch=float(s["examchari3a"])*2
    t=(float(s["tdtech"])*0.33+float(s["examtech"])*0.67)
    b=float(s["b"]); e=float(s["e"]); i=float(s["i"]); y=float(s["y"])
    return {'n':n,'s':srf,'a':a,'m':m,'f':f,'c':c,'ch':ch,'t':t,'b':b,'e':e,'i':i,'y':y}

@app.route("/")
def index():
    return render_template_string(home)

@app.route("/s1", methods=["GET","POST"])
def s1():
    mo3adal=None; msg=""
    if request.method=="POST":
        data=request.form.to_dict()
        res=calc_s(data)
        mo3adal=round(sum(res.values())/19,2)
        if mo3adal >= 10:
            msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else "✅ مبروك، راك نجحت!"
        else:
            msg="❌ لا تقلق، مزال السداسي الثاني"
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg)

@app.route("/s2", methods=["GET","POST"])
def s2():
    mo3adal=None; msg=""
    if request.method=="POST":
        data=request.form.to_dict()
        res=calc_s(data)
        mo3adal=round(sum(res.values())/19,2)
        if mo3adal >= 10:
            msg="🎉 ألف مبروك، معدلك ممتاز!" if mo3adal>15 else "✅ مبروك، راك نجحت!"
        else:
            msg="❌ لا تقلق، مزال الاستدراكي أو السداسي الأول"
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg)

year_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>المعدل السنوي</title>
''' + style + '''
</head>
<body>
<div class="container">
<h2 class="result-title">حساب المعدل السنوي</h2>
{% if mo3adal %}
<div class="result">
🔥 معدلك السنوي هو: {{ mo3adal }} 🔥<br>
{% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
</div>
<a href="/" class="reset-btn">🔄 إعادة الحساب</a>
{% else %}
<div class="result" style="color:#ff5555;">يجب أن تملأ علامات السداسي الأول والثاني</div>
<a href="/" class="reset-btn">🔄 العودة للرئيسية</a>
{% endif %}
</div>
</body>
</html>
'''

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    return render_template_string(year_template, mo3adal=mo3adal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
