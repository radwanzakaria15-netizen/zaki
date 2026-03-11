from flask import Flask, request, render_template_string  

app = Flask(__name__)  

html = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>حساب معدل السداسي </title>
<style>
body, html {
    margin:0;
    padding:0;
    font-family:'Segoe UI',sans-serif;
    min-height:100%;
    background: linear-gradient(-45deg, #1b1b2f, #4e54c8, #00c6ff, #0072ff);
    background-size: 400% 400%;
    animation: gradientMove 25s ease infinite;
    color:#fff;
}

@keyframes gradientMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.container{
    max-width:900px;
    width:95%;
    margin:30px auto;
    padding:30px;
    background: rgba(0,0,0,0.6);
    border-radius:25px;
    box-shadow:0 12px 35px rgba(0,0,0,0.6);
}

h2{
    text-align:center;
    color:#00ffff;
    text-shadow:0 0 12px #00ffff;
    margin-bottom:30px;
    font-size:28px;
}

/* === قسم المواد === */
.cards {
    display: flex;
    flex-wrap: wrap;
    gap:20px;
    justify-content: center;
}

.card {
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    width: 250px;
    text-align:center;
    box-shadow:0 4px 15px rgba(0,0,0,0.3);
    transition:0.3s;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow:0 8px 20px rgba(0,0,0,0.5);
}

.card h3{
    margin-bottom:15px;
    color:#ffd700;
}

/* === الحقول === */
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
    box-shadow:0 0 12px #00ffff;
    transform: scale(1.05);
    outline:none;
}

/* === زر الحساب === */
button{
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
button:hover{
    transform:scale(1.08);
    box-shadow:0 0 18px #00ffff;
}

/* === النتيجة === */
.result{
    margin-top:28px;
    font-size:28px;
    font-weight:bold;
    color:#ffdf00;
    text-shadow:0 0 14px #ffdf00;
    padding:18px;
    border-radius:20px;
    background: rgba(255,255,255,0.07);
    text-align:center;
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
    box-shadow:0 0 18px #00ffff;
}

.footer{
    margin-top:22px;
    color:#ccc;
    font-size:14px;
    text-align:center;
}

@media(max-width:768px){
    .cards { flex-direction: column; align-items:center;}
    .card { width:90%; }
    .card input { width:45%; }
}
</style>
</head>
<body>
<div class="container">
<h2>📊 حساب معدل السداسي </h2>
<form method="post">
<div class="cards">
<div class="card">
<h3>النحو</h3>
<input name="tdnaho" placeholder="TD" required>
<input name="examnaho" placeholder="Exam" required>
</div>

<div class="card">
<h3>الصرف</h3>
<input name="tdsrf" placeholder="TD" required>
<input name="examsrf" placeholder="Exam" required>
</div>

<div class="card">
<h3>الأدب</h3>
<input name="tdadab" placeholder="TD" required>
<input name="examadab" placeholder="Exam" required>
</div>

<div class="card">
<h3>الرياضيات</h3>
<input name="tdm" placeholder="TD" required>
<input name="examm" placeholder="Exam" required>
</div>

<div class="card">
<h3>الفيزياء</h3>
<input name="tdf" placeholder="TD" required>
<input name="examf" placeholder="Exam" required>
</div>

<div class="card">
<h3>الكيمياء</h3>
<input name="tdc" placeholder="TD" required>
<input name="examc" placeholder="Exam" required>
</div>

<div class="card">
<h3>الشريعة</h3>
<input name="examchari3a" placeholder="Exam" required>
</div>

<div class="card">
<h3>التكنولوجيا</h3>
<input name="tdticno" placeholder="TD" required>
<input name="examticno" placeholder="Exam" required>
</div>

<div class="card">
<h3>مواد أخرى</h3>
<input name="b" placeholder="البلاغة" required>
<input name="e" placeholder="الانجليزية" required>
<input name="i" placeholder="الإملاء" required>
<input name="y" placeholder="فنيات الكتابة" required>
</div>
</div>
<button type="submit">احسب المعدل</button>
</form>

{% if mo3adal %}
<div class="result">
🔥 معدلك هو: {{ mo3adal }} 🔥<br>{{ msg }}
</div>
<a href="/" class="reset-btn">🔄 إعادة الحساب</a>
{% endif %}

<div class="footer">© zaki</div>
</div>
</body>
</html>
'''

@app.route("/", methods=["GET","POST"])
def index():
    mo3adal = None
    msg = ""
    if request.method == "POST":
        tdnaho=float(request.form["tdnaho"])
        examnaho=float(request.form["examnaho"])
        notnaho=tdnaho*0.33+examnaho*0.67
        n=notnaho*2

        tdsrf=float(request.form["tdsrf"])
        examsrf=float(request.form["examsrf"])
        notsrf=tdsrf*0.33+examsrf*0.67
        s=notsrf*2

        tdadab=float(request.form["tdadab"])
        examadab=float(request.form["examadab"])
        notadab=tdadab*0.33+examadab*0.67
        a=notadab*2

        tdm=float(request.form["tdm"])
        examm=float(request.form["examm"])
        notm=tdm*0.33+examm*0.67
        m=notm*2

        tdf=float(request.form["tdf"])
        examf=float(request.form["examf"])
        notf=tdf*0.33+examf*0.67
        f=notf*2

        tdc=float(request.form["tdc"])
        examc=float(request.form["examc"])
        notc=tdc*0.33+examc*0.67
        c=notc*2

        examchari3a=float(request.form["examchari3a"])
        ch=examchari3a*2

        tdticno=float(request.form["tdticno"])
        examticno=float(request.form["examticno"])
        ticno=tdticno*0.33+examticno*0.67
        t=ticno

        b=float(request.form["b"])
        e=float(request.form["e"])
        i=float(request.form["i"])
        y=float(request.form["y"])

        majmo3=n+s+a+m+f+c+ch+t+b+e+i+y
        mo3adal=round(majmo3/19,2)

        if mo3adal >= 10:
            if mo3adal > 15:
                msg = "🎉 ألف مبروك، معدلك ممتاز!"
            else:
                msg = "✅ مبروك، راك نجحت!"
        else:
            msg = "❌ لا تقلق، مزال السداسي الثاني"

    return render_template_string(html, mo3adal=mo3adal, msg=msg)

app.run(host="0.0.0.0", port=5000)
