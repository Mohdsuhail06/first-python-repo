# محطة A — أدوات الشغل (اليوم الأول، ~3 ساعات)

**المشروع:** `first-python-repo` — سكربت بيقرأ ملف مصاريف ويطبع ملخص، ومنشور على GitHub.
**رح تتعلم من المشروع نفسه:** Git، GitHub، venv، تشغيل Python من الـ terminal.

---

## الجزء 1 — فهم سريع (15 دقيقة)
| الكلمة | يعني ببساطة |
|---|---|
| **Git** | برنامج بيصوّر مشروعك كل فترة. كل صورة اسمها **commit**، وبتقدر ترجع لأي صورة. |
| **GitHub** | موقع بتحط فيه نسخة من مشروعك أونلاين — هو الـ CV تبعك قدام الشركات. |
| **repo** (repository) | مجلد المشروع اللي Git بيراقبه. |
| **venv** | صندوق معزول للمكتبات، كل مشروع إله صندوقه عشان ما تتخانق المكتبات. |
| **terminal** | الشاشة اللي بتكتب فيها أوامر بدل ما تكبس بالماوس. |

---

## الجزء 2 — جهّز المشروع (30 دقيقة)
افتح terminal بـ VS Code (`Ctrl + ~`) ونفّذ واحد واحد:

```bash
cd C:\Users\USER\projects\ml-journey\first-python-repo
```
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
✔️ لازم تشوف `(.venv)` بأول السطر — يعني إنت جوّا الصندوق.

---

## الجزء 3 — اكتب السكربت بإيدك (60–75 دقيقة)
اعمل ملف اسمه `summarize.py`. **المطلوب** (حاول لحالك أول، والتلميحات تحت):

1. اقرأ `expenses.csv`.
2. اطبع **مجموع** المصاريف.
3. اطبع **مجموع كل فئة** (food، transport، ...).
4. اطبع **أغلى** مصروف.

<details><summary>تلميح 1</summary>

استخدم المكتبة الجاهزة `csv` (موجودة مع Python، ما بدها تنزيل): `csv.DictReader` بيعطيك كل سطر كـ dictionary.
</details>

<details><summary>تلميح 2</summary>

الأرقام بتيجي كنص (`"23.50"`)، لازم تحوّلها بـ `float(...)`. ولمجموع كل فئة استخدم dictionary: `totals[category] = totals.get(category, 0) + amount`.
</details>

شغّله:
```bash
python summarize.py
```
**النتيجة الصحيحة** (عشان تتأكد): المجموع `49.75`، food = `25.75`، transport = `9.00`، internet = `15.00`، الأغلى = groceries `23.50`.

---

## الجزء 4 — Git و GitHub (45 دقيقة)
1. اعمل ملف `.gitignore` وفيه سطر واحد: `.venv/` (عشان الصندوق ما يطلع على GitHub).
2. اكتب `README.md` فيه: شو بيعمل المشروع + أوامر التشغيل + النتيجة.
3. الأوامر:
```bash
git init
```
```bash
git add .
```
```bash
git commit -m "Add expense summary script"
```
```bash
gh repo create first-python-repo --public --source . --push
```
4. عدّل إشي صغير (زي إنك تطبع **متوسط** المصروف)، وبعدين commit ثاني و push:
```bash
git add .
```
```bash
git commit -m "Print average expense"
```
```bash
git push
```
✔️ **خلصت المحطة A لما:** صفحة الـ repo على GitHub فيها commitين، والـ README بيشرح كيف تشغّله.

---

## الجزء 5 — شو تعلمت؟ (10 دقائق)
اكتبلي بـ 3 أسطر بالشات: شو هو الـ commit؟ ليش الـ venv؟ شو اللي صعب عليك؟
بعدها Codex بيراجع الـ repo، وبنعمل `my-ml-journey` (صفحة بتجمع كل مشاريعك).
