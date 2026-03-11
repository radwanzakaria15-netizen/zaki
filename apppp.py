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
<h2>موقع حساب المعدل</h2>

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

معدلك هو {{mo3adal}}

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

        msg="مبروك نجحت" if mo3adal>=10 else "حاول أكثر"

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

        msg="مبروك نجحت" if mo3adal>=10 else "يمكنك التعويض"

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

    if mo3adal:
        return f"<h1 style='color:white'>المعدل السنوي: {mo3adal}</h1>"
    else:
        return "<h1 style='color:white'>املأ السداسيين أولاً</h1>"

# ------------------

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
