from flask import Flask, request, render_template_string, redirect, url_for  

app = Flask(__name__)  

# ----------------------------- CSS -----------------------------
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
    justify-content:flex-start
    align-items:center;  
    overflow-x: hidden;  
    overflow-y: auto;  
}  

@keyframes gradientMove{  
0%{background-position:0% 50%;}  
50%{background-position:100% 50%;}  
100%{background-position:0% 50%;}  
}  

header{text-align:center;margin-bottom:50px;}  
header h1{font-size:60px;color:#00ffff;}  
header h2{font-size:28px;color:#ffffff;}  

.buttons{display:flex;justify-content:center;gap:30px;flex-wrap:wrap;}  
.buttons a{text-decoration:none;}  

.buttons a button{  
    padding:25px 50px;  
    font-size:22px;  
    font-weight:bold;  
    border:none;  
    border-radius:30px;  
    cursor:pointer;  
    background: linear-gradient(90deg,#00ffff,#0072ff);  
    color:#1b1b2f;  
    transition:0.2s;  
}  

.buttons a button:hover{transform:scale(1.05);}  

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
    overflow-y:auto; 
}  

h2.result-title{text-align:center;color:#00ffff;margin-bottom:30px;font-size:28px;}  

.cards{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;}  

.card{  
    background: rgba(255,255,255,0.05);  
    padding:20px;  
    border-radius:20px;  
    width:250px;  
    text-align:center;  
    transition:0.3s;  
}  

.card:hover{transform: translateY(-6px);}  

.card h3{margin-bottom:15px;color:#ffd700;}  

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
    transition:0.2s;  
}  

.card input:focus{  
    background: rgba(0,255,255,0.2);  
    outline:none;  
}  

button.calc{  /* زر حساب المعدل مع التوهج والموجة */
button.calc {
    padding: 16px 36px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    color: #1b1b2f;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    box-shadow: 0 4px 15px rgba(0,255,255,0.4), 0 0 8px rgba(0,255,255,0.3);
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    animation: pulseGlow 2s infinite;
}

/* تأثير التوهج عند المرور */
button.calc:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 25px rgba(0,255,255,0.7), 0 0 20px rgba(0,200,255,0.9);
}

/* تأثير الضغط */
button.calc:active {
    transform: translateY(1px) scale(0.98);
    box-shadow: 0 4px 10px rgba(0,255,255,0.5), 0 0 10px rgba(0,200,255,0.7);
}

/* حركة التوهج المستمرة */
@keyframes pulseGlow {
    0% { box-shadow: 0 4px 15px rgba(0,255,255,0.4), 0 0 8px rgba(0,255,255,0.3); }
    50% { box-shadow: 0 4px 25px rgba(0,255,255,0.6), 0 0 18px rgba(0,255,255,0.5); }
    100% { box-shadow: 0 4px 15px rgba(0,255,255,0.4), 0 0 8px rgba(0,255,255,0.3); }
}

/* تأثير الموجة عند النقر */
button.calc::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0,255,255,0.2);
    top: 0;
    left: -100%;
    transform: skewX(-20deg);
    transition: all 0.5s ease;
}

button.calc:active::after {
    left: 100%;
    transition: all 0.5s ease;
}
    display:block;  
    padding:14px 28px;  
    border:none;  
    border-radius:22px;  
    font-weight:bold;  
    background: linear-gradient(90deg,#00ffff,#0072ff);  
    color:#1b1b2f;  
    font-size:16px;  
    cursor:pointer;  
    transition:0.2s;  
}  

button.calc:hover{transform:scale(1.05);}  

/* ------------------ أزرار جانبية سريعة الاستجابة ------------------ */
/* تأثير موجة ضوئية للأزرار */
a.back-btn, a.reset-btn, a.home-btn, .buttons a button {
    display: inline-block;
    padding: 14px 28px;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color: #1b1b2f;
    border-radius: 22px;
    font-weight: bold;
    text-decoration: none;
    overflow: hidden;
    position: relative;
    z-index: 0;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

/* إضافة عنصر موجة ضوئية */
a.back-btn::before, a.reset-btn::before, a.home-btn::before, .buttons a button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -75%;
    width: 50%;
    height: 100%;
    background: rgba(255,255,255,0.3);
    transform: skewX(-25deg);
    transition: all 0.5s ease;
    z-index: 1;
}

/* حركة الموجة عند المرور */
a.back-btn:hover::before, a.reset-btn:hover::before, a.home-btn:hover::before, .buttons a button:hover::before {
    left: 125%;
}

/* تكبير بسيط عند المرور */
a.back-btn:hover, a.reset-btn:hover, a.home-btn:hover, .buttons a button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0,255,255,0.5);
}

/* تأثير الضغط عند النقر */
a.back-btn:active, a.reset-btn:active, a.home-btn:active, .buttons a button:active {
    transform: scale(0.97);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* أزرار جانبية ثابتة */
.side-buttons {
    position: fixed;
    top: 50%;
    right: 15px;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999;
    /* تأثير توهج عصري للأزرار */
a.back-btn, a.reset-btn, a.home-btn, .buttons a button {
    display: inline-block;
    padding: 14px 28px;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color: #1b1b2f;
    border-radius: 22px;
    font-weight: bold;
    text-decoration: none;
    transition: all 0.25s ease-in-out; /* حركة سلسة */
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    position: relative;
}

/* تأثير المرور مع توهج وخفة الحركة */
a.back-btn:hover, a.reset-btn:hover, a.home-btn:hover, .buttons a button:hover {
    transform: scale(1.08) translateY(-2px); /* تكبير بسيط ورفع خفيف */
    box-shadow: 0 8px 20px rgba(0,255,255,0.6), 0 0 12px rgba(0,255,255,0.5);
}

/* توهج متحرك على الزر */
a.back-btn::after, a.reset-btn::after, a.home-btn::after, .buttons a button::after {
    content: '';
    position: absolute;
    top: -5px; left: -5px;
    width: calc(100% + 10px);
    height: calc(100% + 10px);
    border-radius: 25px;
    background: linear-gradient(45deg, #00ffff, #0072ff, #00e5ff, #005de0);
    opacity: 0;
    transition: opacity 0.25s ease-in-out;
    filter: blur(10px);
    z-index: -1;
}

/* إظهار التوهج عند المرور */
a.back-btn:hover::after, a.reset-btn:hover::after, a.home-btn:hover::after, .buttons a button:hover::after {
    opacity: 0.6;
}

/* ضغط الزر عند النقر */
a.back-btn:active, a.reset-btn:active, a.home-btn:active, .buttons a button:active {
    transform: scale(0.97); 
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* أزرار جانبية ثابتة */
.side-buttons {
    position: fixed;
    top: 50%;
    right: 15px; 
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999;
}/* تأثير توهج عصري للأزرار */
a.back-btn, a.reset-btn, a.home-btn, .buttons a button {
    display: inline-block;
    padding: 14px 28px;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color: #1b1b2f;
    border-radius: 22px;
    font-weight: bold;
    text-decoration: none;
    transition: all 0.2s ease-in-out; /* حركة سلسة */
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    position: relative;
}

/* أزرار رئيسية وجانبية فخمة مع موجة ضوئية */
.buttons a button, a.back-btn, a.reset-btn, a.home-btn {
    display: inline-block;
    padding: 14px 28px;
    background: linear-gradient(90deg,#00ffff,#0072ff);
    color: #1b1b2f;
    border-radius: 22px;
    font-weight: bold;
    text-decoration: none;
    overflow: hidden;
    position: relative;
    transition: all 0.4s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* تأثير الموجة الضوئية عند المرور */
.buttons a button::before, a.back-btn::before, a.reset-btn::before, a.home-btn::before {
    content: '';
    position: absolute;
    top:0;
    left:-100%;
    width:100%;
    height:100%;
    background: rgba(255,255,255,0.2);
    transform: skewX(-20deg);
    transition: 0.7s;
}

.buttons a button:hover::before, a.back-btn:hover::before, a.reset-btn:hover::before, a.home-btn:hover::before {
    left: 200%;
}

/* تغيير اللون عند المرور */
.buttons a button:hover, a.back-btn:hover, a.reset-btn:hover, a.home-btn:hover {
    background: linear-gradient(90deg,#00e5ff,#005de0);
    color:#fff;
}

/* أزرار جانبية ثابتة على الحافة */
.side-buttons {
    position: fixed;
    top: 50%;
    right: 15px; /* مسافة عن الحافة */
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999;
}

}

/* توهج متحرك على الزر */
a.back-btn::after, a.reset-btn::after, a.home-btn::after, .buttons a button::after {
    content: '';
    position: absolute;
    top: -5px; left: -5px;
    width: calc(100% + 10px);
    height: calc(100% + 10px);
    border-radius: 25px;
    background: linear-gradient(45deg, #00ffff, #0072ff, #00e5ff, #005de0);
    opacity: 0;
    transition: opacity 0.25s ease-in-out;
    filter: blur(10px);
    z-index: -1;
}

/* إظهار التوهج عند المرور */
a.back-btn:hover::after, a.reset-btn:hover::after, a.home-btn:hover::after, .buttons a button:hover::after {
    opacity: 0.6;
}

/* ضغط الزر عند النقر */
a.back-btn:active, a.reset-btn:active, a.home-btn:active, .buttons a button:active {
    transform: scale(0.97); 
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* أزرار جانبية ثابتة */
.side-buttons {
    position: fixed;
    top: 50%;
    right: 15px; 
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999;
}
}
}

/* حاوية الأزرار الجانبية */
.side-buttons {
    position: fixed;
    top: 50%;
    right: 15px; /* مسافة عن الحافة */
    transform: translateY(-60%);
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999;
}

/* ------------------ نتيجة الحساب ------------------ */
.result{  
    margin-top:28px;  
    font-size:28px;  
    font-weight:bold;  
    text-align:center;  
    padding:18px;  
    border-radius:20px;  
    background: rgba(255,255,255,0.07);  
}  

footer{text-align:center;font-size:18px;color:#00ffff;margin-top:30px;}  
footer a{/* زر تيليغرام */
footer a.telegram-btn {
    display: inline-block;
    padding: 10px;
    border-radius: 50%;
    background: #0088cc; /* لون تيليغرام الرسمي */
    color: white;
    font-size: 24px;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
}

/* تأثير التوهج عند المرور */
footer a.telegram-btn:hover {
    box-shadow: 0 0 20px #00cfff, 0 0 30px #00cfff, 0 0 40px #00cfff;
    transform: scale(1.15) rotate(5deg);
}

/* حركة نبض خفيفة بشكل مستمر */
footer a.telegram-btn.pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 12px rgba(0, 207, 255, 0.5); }
    50% { transform: scale(1.05); box-shadow: 0 0 20px rgba(0, 207, 255, 0.7); }
    100% { transform: scale(1); box-shadow: 0 0 12px rgba(0, 207, 255, 0.5); }
}
color:#00ffff;text-decoration:none;}  

@media(max-width:768px){  
    .cards { flex-direction: column; align-items:center;}  
    .card { width:90%; }  
    .card input { width:45%; }  
    .buttons a button { width:90%; padding:20px 0; }  
    .side-buttons { right:10px; gap:10px;}  
}  
</style>  
'''  

# ----------------------------- الصفحة الرئيسية -----------------------------
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
<a href="https://t.me/zakariazakii" target="_blank">  
<i class="fab fa-telegram fa-2x"></i>  
</a>  
</footer>  
</body>  
</html>  
'''  

stored_data = {'s1': {}, 's2': {}}  

# ----------------------------- نموذج السداسي -----------------------------
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
<!-- المواد -->  
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

<!-- زر حساب المعدل في الوسط -->
<div style="display:flex; justify-content:center; align-items:center; margin-top:20px; width:100%;">  
  <button type="submit" class="calc">احسب المعدل</button>  
</div>

<!-- أزرار جانبية ثابتة -->
<div class="side-buttons">
    <a href="/reset/{{sem}}" class="reset-btn">🔄 إعادة</a>
    <a href="javascript:history.back()" class="back-btn">← رجوع</a>
    <a href="/" class="home-btn">🏠 الرئيسية</a>
</div>

{% if mo3adal %}  
<div class="result" style="color: {{ color }};">  
 معدلك هو: {{ mo3adal }} <br>{{ msg }}  
</div>  
{% endif %}  

</div>  
</body>  
</html>  
'''  

# ----------------------------- حساب المعدل -----------------------------
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

# ----------------------------- Routes -----------------------------
@app.route("/")  
def index():  
    return render_template_string(home)  

@app.route("/reset/<sem>")  
def reset(sem):  
    stored_data[sem] = {}  
    return redirect(url_for(sem))  

@app.route("/s1", methods=["GET","POST"])  
def s1():  
    mo3adal=None; msg=""; color=""  
    if request.method=="POST":  
        stored_data['s1'] = request.form.to_dict()  
        res=calc_s(stored_data['s1'])  
        mo3adal=round(sum(res.values())/19,2)  
        if mo3adal>15: color="#FFD700"; msg="🎉 ألف مبروك، معدلك ممتاز!"  
        elif mo3adal>=10: color="#00FF00"; msg="✅ مبروك، لقد نجحت!"  
        else: color="#FF5555"; msg="❌ لديك فرصة ثانية في السداسي الثاني"  
    data = stored_data['s1']  
    return render_template_string(s_template, title="حساب معدل السداسي الأول", tech_name="التكنولوجيا", other_name="الإملاء", mo3adal=mo3adal, msg=msg, data=data, sem="s1", color=color)  

@app.route("/s2", methods=["GET","POST"])  
def s2():  
    mo3adal=None; msg=""; color=""  
    total_mo3adal = None
    if request.method=="POST":  
        stored_data['s2'] = request.form.to_dict()  
        res=calc_s(stored_data['s2'])  
        mo3adal=round(sum(res.values())/19,2)  

        if stored_data['s1']:
            res1=calc_s(stored_data['s1'])
            total_mo3adal = round((sum(res1.values()) + sum(res.values()))/38,2)

        if mo3adal>15: color="#FFD700"; msg="🎉 ألف مبروك، معدلك ممتاز!"  
        elif mo3adal>=10: color="#00FF00"; msg="✅ مبروك، راك نجحت!"  
        else:  
            color="#FF5555"
            if total_mo3adal is not None:
                if total_mo3adal < 10:
                    msg="❌ لا يزال أمامك الامتحان الاستدراكي"
                else:
                    msg="✔️ لا بأس، فقد أنقذك اجتهادك في السداسي الأول"
            else:
                msg="❌ لديك فرصة ثانية في السداسي الثاني"

    data = stored_data['s2']  
    return render_template_string(s_template, title="حساب معدل السداسي الثاني", tech_name="الإعلام الآلي", other_name="الخط العربي", mo3adal=mo3adal, msg=msg, data=data, sem="s2", color=color)  

@app.route("/year", methods=["GET"])  
def year():  
    mo3adal=None; msg=""; color=""  
    if stored_data['s1'] and stored_data['s2']:  
        res1=calc_s(stored_data['s1'])  
        res2=calc_s(stored_data['s2'])  
        mo3adal=round((sum(res1.values())+sum(res2.values()))/38,2)  

        if mo3adal >= 15: 
            color="#FFD700"; msg="🎉 ألف مبروك، معدلك ممتاز!"
        elif mo3adal >= 12: 
            color="#00FF00"; msg="✅ مبروك، معدلك جيد!"
        elif mo3adal >= 10: 
            color="#00BFFF"; msg="☑️ معدلك مقبول!"
        else: 
            color="#FF5555"; msg="❌ للأسف، معدلك راسب"  

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
<div class="result" style="color: {{color }};">  
 معدلك السنويهو: {{ mo3adal }} <br>{{ msg }}
</div>  
{% else %}  
<div class="result" style="color:#FF5555;">  
يجب أن تملأ علامات السداسي الأول والثاني  
</div>  
{% endif %}  

<!-- زر الصفحة الرئيسية ثابت على الجانب الأيمن -->
<div class="side-buttons">
    <a href="/" class="home-btn">🏠 الرئيسية</a>
</div>

</div>  
</body>  
</html>  
'''  

    return render_template_string(year_template, mo3adal=mo3adal, msg=msg, color=color)  

# ----------------------------- تشغيل التطبيق -----------------------------
if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)#
