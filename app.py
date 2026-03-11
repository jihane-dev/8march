import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# === PAGE CONFIG ===
st.set_page_config(page_title="8 Mars", page_icon="👩‍🏫", layout="wide")


# === LOAD LOGO ===
logo = Image.open("assets/logo.jpg")

# Display logo normally first
col_logo, col_title = st.columns([1,8])

with col_logo:
    st.image(logo, width=60)

with col_title:
    st.markdown(
    '<div class="event-title">J.I des droits des femmes 💜</div>',
    unsafe_allow_html=True
)

# === LOAD LOTTIE FUNCTION ===
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_intro = load_lottie("assets/woman.json")  # intro Lottie


# === SESSION STATE ===
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "messages" not in st.session_state:
    st.session_state.messages = []

# === CSS ===
st.markdown("""
<style>
.event-title{
font-size:32px;
font-family:"Papyrus", cursive;
color:#8e44ad;
margin-top:5px;
margin-bottom:10px;
}

/* === PAGE GENERALE === */
.stApp{
    font-size: 12px;          
    padding: 0 20px;          /* réduit le padding horizontal */
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

/* === PAGE 1 : INTRODUCTION === */
.page-intro {

background:white;

padding:40px;

border-radius:25px;

box-shadow:0 0 20px 5px rgba(155,89,182,0.7);


min-height:100vh;

border:4px solid;

display:flex;

flex-direction:column;

justify-content:flex-start;

}

.logo-fixed {
    position: fixed;
    left: 10px;
    z-index: 100;
}

/* bouton intro */
.button-click{
    background-color:#9b59b6;
    color:white;
    padding:10px 20px;
    border-radius:10px;
    font-size:16px;   
    cursor:pointer;
}

/* === PAGE 2 : MUR DE MESSAGES === */
.form-card{
    background: #fff;
    padding: 30px 20px;
    border-radius: 25px;
    box-shadow: 0 0 20px 5px rgba(155,89,182,0.7);
    width: 100%;
    min-height: 100vh;           /* prend toute la hauteur de la page */
    font-size: 14px;
    border: 4px solid;
    border-image-slice: 1;
    border-image-source: linear-gradient(90deg, #ff66cc, #8e44ad);
    animation: borderGlow 2s infinite alternate;
    display: flex;
    flex-direction: column;
    justify-content: flex-start; /* lève le contenu en haut */
}

/* animation border glow (rose <-> violet) */
@keyframes borderGlow {
    0% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
    50% { border-color: #8e44ad; box-shadow: 0 0 25px 10px #8e44ad; }
    100% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
}

/* cadre scintillant pour messages */
.message-bubble{
    background:white;
    padding:12px 18px;
    border-radius:25px;
    margin:10px 0;
    display:inline-block;
    box-shadow:0 0 15px 3px rgba(155,89,182,0.6);
    border-left:6px solid #9b59b6;
    animation: glow 2s infinite alternate;
    max-width:500px;
    font-size: 14px; 
}

/* animation glow */
@keyframes glow{
    from{box-shadow:0 0 10px 2px rgba(155,89,182,0.6);}
    to{box-shadow:0 0 20px 5px rgba(155,89,182,1);}
}

/* Container padding */
.block-container {
    padding-top: 0rem !important;
}
</style>
""", unsafe_allow_html=True)

# === PAGE 1 : INTRODUCTION ===
if st.session_state.page == "intro":
    rain(emoji="💮", font_size=15, falling_speed=5, animation_length="infinite")  
    st.markdown("""
    <style>
    
/* enlever fond gris streamlit */
[data-testid="stAppViewContainer"]{
background: transparent;
}

/* enlever fond header */
[data-testid="stHeader"]{
background: transparent;
}

/* enlever fond toolbar */
[data-testid="stToolbar"]{
right: 2rem;
}

/* page prend toute la largeur */
.block-container{
padding-top:0rem !important;
padding-left:3rem;
padding-right:3rem;
max-width:100%;
}

/* background global rose */
body{
background: linear-gradient(135deg,#ffe0f0,#f5d0ff);
}


    .stApp {
        background: #fff;
        border-radius: 0px;
        box-shadow: 0 0 25px 10px rgba(155,89,182,0.7);
        border: 5px solid;
        border-image-slice: 1;
        border-image-source: linear-gradient(90deg, #ff66cc, #8e44ad);
        animation: borderGlow 2s infinite alternate;
        min-height: 100vh;
        width: 100%;
        padding: 20px 30px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* lève le contenu */
        font-size: 14px;
    }

    @keyframes borderGlow {
        0% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
        50% { border-color: #8e44ad; box-shadow: 0 0 25px 10px #8e44ad; }
        100% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
    }
    div[data-testid="stLottie"]{
background: transparent !important;
}
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])
    with col1:
      
        st.write(" **Pour s’inspirer:**")
        st.write(" **🌸La femme est force et lumière**")
        st.write(" **🌸Chaque femme est une source d’inspiration**")
        st.write(" **🌸Célébrons les femmes qui changent le monde**")

        if st.button("💌 Cliquez ici pour envoyer un message"):
            st.session_state.page = "messages"

    with col2:
        st_lottie(lottie_intro, speed=1, loop=True, height=200, key="lottie",)
    


# === PAGE 2 : MUR DE MESSAGES ===
elif st.session_state.page == "messages":
    rain(emoji="💌", font_size=15, falling_speed=5, animation_length="40s")
    # Appliquer le style full-page directement à stApp
    st.markdown("""
    <style>
    
/* enlever fond gris streamlit */
[data-testid="stAppViewContainer"]{
background: transparent;
}

/* enlever fond header */
[data-testid="stHeader"]{
background: transparent;
}

/* enlever fond toolbar */
[data-testid="stToolbar"]{
right: 2rem;
}

/* page prend toute la largeur */
.block-container{
padding-top:0rem !important;
padding-left:3rem;
padding-right:3rem;
max-width:100%;
}

/* background global rose */
body{
background: linear-gradient(135deg,#ffe0f0,#f5d0ff);
}


    .stApp {
        background: #fff;
        border-radius: 0px;
        box-shadow: 0 0 25px 10px rgba(155,89,182,0.7);
        border: 5px solid;
        border-image-slice: 1;
        border-image-source: linear-gradient(90deg, #ff66cc, #8e44ad);
        animation: borderGlow 2s infinite alternate;
        min-height: 100vh;
        width: 100%;
        padding: 20px 30px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* lève le contenu */
        font-size: 14px;
    }

    @keyframes borderGlow {
        0% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
        50% { border-color: #8e44ad; box-shadow: 0 0 25px 10px #8e44ad; }
        100% { border-color: #ff66cc; box-shadow: 0 0 25px 10px #ff66cc; }
    }
    body, p, div, span, label, input, textarea, button{
font-family: "Times New Roman", Times, serif;
}
.wall-title{
text-align:center;
color:#ff66cc;              /* rose foncé */
font-family:"Papyrus", cursive;
font-size:36px;
margin-top:-65px;
margin-bottom:10px;
border-bottom:3px solid #8e44ad;
}
.msg {
    color: #8e44ad;
    font-family : "Papyrus", cursive;
    font-size: 15px;
    margin-bottom: 2px;
}
    </style>
    """, unsafe_allow_html=True)

    # Contenu de la page 2
    st.markdown(
'<div class="wall-title"> Mur de messages – Journée du 8 mars</div>',
unsafe_allow_html=True
)
    st.markdown(
'<div class="msg"> Laissez un message pour une femme qui vous inspire</div>',
unsafe_allow_html=True
)
    

    # Formulaire
    nom = st.text_input("Votre nom")
    role = st.selectbox("Vous êtes :", ["Élève", "Professeur"])
    message = st.text_area("Votre message")

    if st.button("Publier mon message"):
        if nom and message:
            st.session_state.messages.append({
                "nom": nom,
                "role": role,
                "message": message
            })
            st.success("Merci ! Votre message a été publié.")
        else:
            st.warning("Veuillez remplir le nom et le message.")

    # Affichage des messages
    st.markdown("### 💬 Messages publiés aujourd'hui")
    st.metric(label="Nombre de messages", value=len(st.session_state.messages))
    st.markdown("#### 💌 Messages des participants")

    st.markdown('<div class="bubble-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        st.markdown(f"""
        <div class="message-bubble">
            <div class="message-name">
            💬 {msg['nom']} ({msg['role']})
            </div>
            <div>{msg['message']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # === FOOTER ===
st.markdown("""
<hr>
Partagé par [Professeure de SVT : J.Jait 🌹]

© all rights reserved - 2026
""", unsafe_allow_html=True)
