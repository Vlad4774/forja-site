"""Generează paginile site-ului Forja (python build.py). Textele legale trebuie ținute la fel ca în aplicație (src/app/legal.tsx)."""

import html
import pathlib

CONTACT = "vladbaracut7@yahoo.com"
UPDATED = "November 2026"
OUT = pathlib.Path(__file__).parent

LOGO = (
    '<svg viewBox="0 0 512 512" width="34" height="34" aria-hidden="true"><path fill="currentColor" d="M104 160h48v192h-48a24 24 0 0 1-24-24V184a24 24 0 0 1 24-24zm304 0a24 24 0 0 1 24 24v144a24 24 0 0 1-24 24h-48V160zM168 128h40a16 16 0 0 1 16 16v224a16 16 0 0 1-16 16h-40a16 16 0 0 1-16-16V144a16 16 0 0 1 16-16zm136 0h40a16 16 0 0 1 16 16v224a16 16 0 0 1-16 16h-40a16 16 0 0 1-16-16V144a16 16 0 0 1 16-16zM224 232h64v48h-64zM32 224h48v64H32zm400 0h48v64h-48z"/></svg>'
)

CSS = """
:root{--bg:#08090A;--top:#1B1E24;--surface:#16181C;--border:#2A2D34;--text:#F5F6F8;--dim:#A0A4AD;--green:#3DD37E}
*{box-sizing:border-box}
body{margin:0;background:linear-gradient(#1B1E24,#08090A 420px) no-repeat,#08090A;color:var(--text);font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--green)}
.wrap{max-width:760px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:40px}
.brand{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:900;font-size:22px;letter-spacing:2px}
nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px}
nav a{color:var(--dim);text-decoration:none}
nav a:hover{color:var(--text)}
h1{font-size:40px;line-height:1.1;margin:0 0 12px;letter-spacing:-1px}
h2{font-size:20px;margin:32px 0 8px}
.lead{color:var(--dim);font-size:18px;margin:0 0 32px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:32px 0}
.card{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:18px}
.card b{display:block;margin-bottom:4px}
.card span{color:var(--dim);font-size:14px}
.muted{color:var(--dim);font-size:14px}
ol li,ul li{margin-bottom:6px}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--border);color:var(--dim);font-size:14px;display:flex;gap:16px;flex-wrap:wrap}
footer a{color:var(--dim)}
"""


def page(file, title, body, description):
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header>
  <a class="brand" href="./">{LOGO}FORJA</a>
  <nav><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="delete-account.html">Delete account</a></nav>
</header>
{body}
<footer><span>© 2026 Forja</span><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="delete-account.html">Delete your account</a><a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</div>
</body>
</html>
"""
    (OUT / file).write_text(doc, encoding="utf-8")


def sections(items):
    out = []
    for h, ps in items:
        out.append(f"<h2>{html.escape(h)}</h2>")
        out.extend(f"<p>{html.escape(p)}</p>" for p in ps)
    return "\n".join(out)


TERMS = [
    ("Who we are", [f"Forja is a workout logging app made by an individual developer based in Romania. Contact: {CONTACT}."]),
    ("Your account", [
        "You need an account to use Forja. You can create one with your email and a password, or sign in with Google. Keep your password private; you are responsible for activity on your account.",
        "You can delete your account at any time from Profile → Account → Delete account.",
    ]),
    ("Free version and Premium", [
        "Forja is free to use and shows ads. Workout logging, programs, the recommended plan and your full history are free. Forja Premium is an optional subscription that removes the ads and unlocks progress charts, strength ranks, the muscle map and muscle recovery.",
        "Every new account gets Premium free for its first 30 days. No payment details are needed and nothing is charged; afterwards the app simply continues as the free version. The price of the subscription and any free trial are shown in Google Play, in your own currency, before you subscribe. The subscription renews automatically until you cancel.",
        "Payments, renewals and refunds are handled by Google Play. Cancel at least 24 hours before the trial or period ends to avoid the next charge: Google Play → Payments & subscriptions → Subscriptions.",
    ]),
    ("Health", ["Forja gives general training suggestions (programs, weights, recovery estimates). It is not medical advice. Check with a doctor before starting a new exercise program, and stop if you feel pain."]),
    ("Acceptable use", ["Do not misuse the service: no attempts to access other people’s data, overload the servers or reverse-engineer the subscription."]),
    ("Liability", ["The app is provided “as is”. To the extent allowed by law, we are not liable for injuries or for loss of data. Your workouts are saved to your account; you can also download a copy at any time (Profile → Account → Download my data)."]),
    ("Changes", ["We may update these terms. Important changes will be announced in the app."]),
]

PRIVACY = [
    ("What we collect", [
        "Account: your email address and a securely hashed password. If you sign in with Google, we receive your name, email address and profile picture from Google instead of a password.",
        "Training data you enter: workouts, sets, programs, body weight and measurements, and the answers from the setup questions (goal, experience, injuries you choose to tell us about).",
        "Subscription status from Google Play (through RevenueCat). We never see your card details.",
        "In the free version: ads are shown by Google AdMob and its advertising partners (listed in the consent form). They use device identifiers (such as the advertising ID), your location (approximate from the IP address, or more precise only if you allow it in the consent form) and how you interact with ads. Personalised ads are shown only if you agree in the consent form; you can change your choice at any time in Profile → Ad choices.",
    ]),
    ("Why", ["To run the app (log you in, back up and sync your data between your phones, unlock Premium) and, in the free version, to show ads through Google AdMob. Your training data is never shared with advertisers and never sold."]),
    ("Sharing you choose", [
        "Ranking (optional): if you join the ranking, other Forja users see the username you choose, an optional short description, your monthly and yearly workout count and volume, your ranks, level and ranking badges. Never your email. You can leave the ranking at any time.",
        "Coaches (optional): if you accept an invitation from a personal trainer who uses Forja, that trainer can see your synced training data (workouts and sets, history, programs and routines, body weight and measurements, settings) and can send you routines and programs. Progress photos are never shared. You can stop sharing at any time in Profile → Coaching; the trainer loses access immediately.",
    ]),
    ("Where it is stored", [
        "On your phone, and in your account on Supabase servers in the EU (Ireland). Data is sent over encrypted connections and each account can only read its own data, except what you choose to share (see above).",
        "Service providers: Supabase (database and login), Google (Sign in with Google), RevenueCat and Google Play (subscription), Google AdMob (ads in the free version), and an email provider for the verification codes.",
    ]),
    ("Permissions", ["Notifications (optional): only to show your running workout and rest timer in the notification bar. Files: only when you download your data yourself."]),
    ("Your rights (GDPR)", [
        "You can see your data in the app, download a copy (Profile → Account → Download my data), correct it in the app, and delete your account and all its data permanently (Profile → Account → Delete account).",
        f"For any other request, write to {CONTACT}. You can also complain to the Romanian data protection authority (ANSPDCP).",
    ]),
    ("Retention", ["We keep your data while your account exists. Deleting the account removes it from our servers."]),
]

page(
    "index.html",
    "Forja – workout log",
    """<h1>Log every set.<br>See every gain.</h1>
<p class="lead">Forja is a simple workout log for the gym: track your sets in seconds, follow a program and watch your strength go up.</p>
<div class="grid">
  <div class="card"><b>Fast logging</b><span>Weights and reps pre-filled from last time. One tap per set.</span></div>
  <div class="card"><b>Programs</b><span>Ready-made plans or your own routines, with a smart next workout.</span></div>
  <div class="card"><b>Progress</b><span>Records, estimated 1RM, streaks and a muscle map of your week.</span></div>
  <div class="card"><b>Works offline</b><span>Your data lives on your phone and syncs to your account.</span></div>
</div>
<p class="muted">Forja is free with ads, programs included. New accounts get a free month of Premium, which removes the ads and unlocks advanced stats.</p>
<p class="muted">Questions? Write to <a href="mailto:""" + CONTACT + """">""" + CONTACT + """</a>.</p>""",
    "Forja is a simple workout log: track sets, follow programs and see your progress.",
)

page(
    "privacy.html",
    "Privacy Policy – Forja",
    f'<h1>Privacy Policy</h1><p class="muted">Last updated: {UPDATED}</p>\n' + sections(PRIVACY),
    "How Forja collects, uses and protects your data.",
)

page(
    "terms.html",
    "Terms of Service – Forja",
    f'<h1>Terms of Service</h1><p class="muted">Last updated: {UPDATED}</p>\n' + sections(TERMS),
    "The terms for using the Forja app.",
)

page(
    "delete-account.html",
    "Delete your account – Forja",
    f"""<h1>Delete your Forja account</h1>
<p class="lead">You can permanently delete your account and all its data at any time.</p>
<h2>In the app</h2>
<ol>
  <li>Open Forja and go to <b>Profile → Account</b>.</li>
  <li>Tap <b>Delete account</b>, type <b>DELETE</b> to confirm.</li>
</ol>
<p>Optional: before deleting, tap <b>Download my data</b> on the same screen to keep a copy of your workouts.</p>
<h2>By email</h2>
<p>If you can’t open the app, write to <a href="mailto:{CONTACT}?subject=Delete%20my%20Forja%20account">{CONTACT}</a> from the email address of your account and ask for it to be deleted. We do it within 30 days.</p>
<h2>What gets deleted</h2>
<p>Your account, workouts, routines, programs, body weight and measurements, and your settings are removed permanently from our servers. Nothing is kept. A Google Play subscription must be cancelled separately in Google Play.</p>""",
    "How to delete your Forja account and data.",
)
print("built")
