from flask import Flask, request, render_template_string  
  
app = Flask(__name__)  
  
html = '''  
<!DOCTYPE html>  
<html>  
<head>  
<meta charset="UTF-8">  
<title>حساب معدل السداسي (ملمح ابتدائي)</title>  
<style>  
body, html {  
    margin:0;  
    padding:0;  
    font-family:'Segoe UI',sans-serif;  
    height:100%;  
    color:#fff;  
    overflow-x:hidden;  

    /* الخلفية المتحركة الأصلية */  
    background: linear-gradient(135deg, #4a00e0, #8e2de2, #00c6ff, #0072ff);  
    background-size: 400% 400%;  
    animation: gradientMove 30s ease infinite;  
}  

@keyframes gradientMove {  
    0%{background-position:0% 50%;}  
    50%{background-position:100% 50%;}  
    100%{background-position:0% 50%;}  
}  

.container{  
    max-width:700px;  
    width:90%;  
    margin:50px auto;  
    padding:30px;  
    background: rgba(0,0,0,0.6);  
    border-radius:25px;  
    box-shadow:0 10px 30px rgba(0,0,0,0.5);  
    text-align:center;  
}  

h2{  
    color:#00ffff;  
    margin-bottom:25px;  
    text-shadow:0 0 10px #00ffff;  
}  
h3{margin:15px 0 5px;}  

input{  
    width:45%;  
    padding:12px;  
    margin:6px 2%;  
    border-radius:12px;  
    border:none;  
    background:rgba(255,255,255,0.1);  
    color:#fff;  
    text-align:center;  
    transition:0.2s;  
}  
input:focus{  
    background:rgba(0,255,255,0.15);  
    box-shadow:0 0 10px #00ffff;  
    transform:scale(1.02);  
    outline:none;  
}  

button{  
    padding:12px 25px;  
    margin-top:20px;  
    border:none;  
    border-radius:18px;  
    font-weight:bold;  
    background: linear-gradient(90deg,#00ffff,#0072ff);  
    color:#1b1b2f;  
    cursor:pointer;  
    transition:0.3s;  
}  
button:hover{  
    transform:scale(1.05);  
    box-shadow:0 0 15px #00ffff;  
}  

.result{  
    margin-top:25px;  
    font-size:26px;  
    font-weight:bold;  
    color:#ffdf00;  
    text-shadow:0 0 12px #ffdf00;  
    padding:15px;  
    border-radius:18px;  
    background: rgba(255,255,255,0.05);  
}  

a.reset-btn{  
    display:inline-block;  
    margin-top:15px;  
    padding:12px 25px;  
    background: linear-gradient(90deg,#0072ff,#00ffff);  
    color:#1b1b2f;  
    border-radius:15px;  
    font-weight:bold;  
    text-decoration:none;  
    transition:0.3s;  
}  
a.reset-btn:hover{  
    transform:scale(1.05);  
    box-shadow:0 0 15px #00ffff;  
}  

.footer{margin-top:20px;color:#ccc;font-size:14px;}  
</style>  
</head>  
<body>  
<div class="container">  
<h2>📊 حساب معدل السداسي (ملمح ابتدائي)</h2>  
<form method="post">  
<h3>النحو</h3><input name="tdnaho" placeholder="TD" required><input name="examnaho" placeholder="Exam" required>  
<h3>الصرف</h3><input name="tdsrf" placeholder="TD" required><input name="examsrf" placeholder="Exam" required>  
<h3>الأدب</h3><input name="tdadab" placeholder="TD" required><input name="examadab" placeholder="Exam" required>  
<h3>الرياضيات</h3><input name="tdm" placeholder="TD" required><input name="examm" placeholder="Exam" required>  
<h3>الفيزياء</h3><input name="tdf" placeholder="TD" required><input name="examf" placeholder="Exam" required>  
<h3>الكيمياء</h3><input name="tdc" placeholder="TD" required><input name="examc" placeholder="Exam" required>  
<h3>الشريعة</h3><input name="examchari3a" placeholder="Exam" required>  
<h3>التكنولوجيا</h3><input name="tdticno" placeholder="TD" required><input name="examticno" placeholder="Exam" required>  
<h3>مواد أخرى</h3>  
<input name="b" placeholder="البلاغة" required>  
<input name="e" placeholder="الانجليزية" required>  
<input name="i" placeholder="الإملاء" required>  
<input name="y" placeholder="فنيات الكتابة" required>  
<br><br>  
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
