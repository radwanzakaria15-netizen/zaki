from flask import Flask, request, render_template_string  

app = Flask(__name__)  

style = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body {
    margin:0;
    padding:0;
    font-family:'Cairo',sans-serif;
    width:100%;
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
    margin-bottom:10px;
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
a.reset-btn:hover{
    transform:scale(1.08);
}

footer{
    text-align:center;
    font-size:18px;
    color:#00ffff;
    margin-top:30px;
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
<title>حساب معدل (ملمح ابتدائي لغة عربية)</title>
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
<a href="https://t.me/zakariazakii" target="_blank">Telegram</a>
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
<div class="card"><h3>النحو</h3><input name="tdnaho" placeholder="TD" required><input name="examnaho" placeholder="Exam" required></div>
<div class="card"><h3>الصرف</h3><input name="tdsrf" placeholder="TD" required><input name="examsrf" placeholder="Exam" required></div>
<div class="card"><h3>الأدب</h3><input name="tdadab" placeholder="TD" required><input name="examadab" placeholder="Exam" required></div>
<div class="card"><h3>الرياضيات</h3><input name="tdm" placeholder="TD" required><input name="examm" placeholder="Exam" required></div>
<div class="card"><h3>الفيزياء</h3><input name="tdf" placeholder="TD" required><input name="examf" placeholder="Exam" required></div>
<div class="card"><h3>الكيمياء</h3><input name="tdc" placeholder="TD" required><input name="examc" placeholder="Exam" required></div>
<div class="card"><h3>الشريعة</h3><input name="examchari3a" placeholder="Exam" required></div>
<div class="card"><h3>{{tech_name}}</h3><input name="tdtech" placeholder="TD" required><input name="examtech" placeholder="Exam" required></div>
<div class="card"><h3>مواد أخرى</h3><input name="b" placeholder="البلاغة" required><input name="e" placeholder="الانجليزية" required><input name="i" placeholder="{{other_name}}" required><input name="y" placeholder="فنيات الكتابة" required></div>
</div>
<button type="submit" class="calc">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
معدلك هو: {{ mo3adal }}<br>{{ msg }}
</div>
<a href="/" class="reset-btn">🔄 إعادة الحساب</a>
{% endif %}
</div>
</body>
</html>
'''

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
معدلك السنوي هو: {{ mo3adal }}<br>
{% if mo3adal >= 10 %}🎉 ألف مبروك، معدلك ممتاز!{% else %}❌ المعدل أقل من المطلوب{% endif %}
</div>
<a href="/" class="reset-btn">🔄 إعادة الحساب</a>
{% else %}
<div class="result">
يجب أن تملأ علامات السداسي الأول والثاني حتى تستطيع حساب المعدل السنوي
</div>
<a href="/" class="reset-btn">🔄 العودة للرئيسية</a>
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
            msg="لا تقلق، راك خادم في السداسي الاول أو استعد للاستدراكي حسب التعويض"
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg)

@app.route("/year", methods=["GET","POST"])
def year():
    mo3adal=None
    return render_template_string(year_template, mo3adal=mo3adal)

app.run(host="0.0.0.0", port=5000)
