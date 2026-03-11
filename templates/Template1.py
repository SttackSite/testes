import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- CSS RADICAL (PLUNDER + DOCKYARD + QUDRIX) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');

    :root {
        --accent: #7b2cbf;
        --gold: #d4af37;
        --dark: #050505;
        --glass: rgba(255, 255, 255, 0.03);
    }

    .stApp {
        background-color: var(--dark);
        color: #ffffff;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    h1, h2 {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -3px;
        line-height: 0.85;
    }

    .serif-heavy {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        text-transform: none;
        letter-spacing: -1px;
    }

    .navbar-elite {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25px 8%;
        background: rgba(5, 5, 5, 0.5);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        width: 100%;
        box-sizing: border-box;
    }
    
    .logo-elite {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        font-family: 'Inter', sans-serif;
        color: var(--gold);
        text-transform: uppercase;
    }

    .nav-links-container {
        display: flex;
        gap: 45px;
        align-items: center;
    }

    .nav-link-elite {
        color: #ffffff !important;
        text-decoration: none !important;
        font-size: 12px;
        letter-spacing: 1px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        cursor: pointer;
        text-transform: uppercase;
    }

    .nav-link-elite:hover {
        color: var(--gold) !important;
        text-decoration: none !important;
    }

    .nav-link-elite:visited {
        color: #ffffff !important;
        text-decoration: none !important;
    }

    .hero-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 8%;
        background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .hero-h1 { font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }
    .hero-sub { 
        font-size: 24px; 
        max-width: 600px; 
        line-height: 1.4; 
        color: rgba(255,255,255,0.7);
        border-left: 4px solid var(--accent);
        padding-left: 20px;
    }

    .template-box {
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        background: var(--glass);
        transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        cursor: crosshair;
    }
    .template-box:hover {
        background: rgba(255,255,255,0.07);
        border-color: var(--gold);
        transform: translateY(-10px);
    }
    .template-label {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
    }

    .carousel-section {
        padding: 120px 8%;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%);
    }

    .carousel-title {
        text-align: center;
        font-size: 48px;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        margin-bottom: 60px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -2px;
    }

    .carousel-container {
        display: flex;
        gap: 20px;
        overflow-x: auto;
        overflow-y: hidden;
        padding: 20px 0;
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--gold) transparent;
        height: auto;
    }

    .carousel-container::-webkit-scrollbar { height: 8px; }
    .carousel-container::-webkit-scrollbar-track { background: transparent; }
    .carousel-container::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 4px; }

    .carousel-item-link { display: none; }
    .carousel-item-link:hover {
        border-color: var(--gold);
        transform: translateY(-15px);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    .carousel-item-image-only {
        flex: 0 0 800px;
        min-width: 800px;
        height: 360px;
        border-radius: 8px;
        overflow-y: auto;
        overflow-x: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
        background: rgba(255, 255, 255, 0.02);
    }

    .carousel-item-image-only:hover {
        border-color: var(--gold);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    .carousel-item-image-only::-webkit-scrollbar { width: 6px; }
    .carousel-item-image-only::-webkit-scrollbar-track { background: transparent; }
    .carousel-item-image-only::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 3px; }

    .carousel-item-image-only img {
        width: auto;
        height: auto;
        object-fit: cover;
        display: block;
        border-radius: 8px;
    }

    .carousel-item-link img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        border-radius: 8px;
    }

    .client-section {
        padding: 100px 8%;
        background: #0a0a0a;
        display: flex;
        align-items: center;
        gap: 50px;
    }

    .target-card {
        padding: 50px;
        background: white;
        color: black;
        border: 5px solid var(--accent);
        box-shadow: 15px 15px 0px var(--accent);
        height: 100%;
    }

    .step-row {
        display: flex;
        gap: 30px;
        margin-bottom: 60px;
        align-items: flex-start;
    }
    .step-num {
        font-size: 100px;
        font-weight: 900;
        color: transparent;
        -webkit-text-stroke: 1px rgba(255,255,255,0.3);
        line-height: 0.7;
    }

    .pricing-glass {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px 40px;
        border-radius: 2px;
        text-align: center;
    }
    .pricing-glass:hover { border-color: var(--accent); }

    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd);
        color: white;
        border: none;
        padding: 25px 60px;
        font-weight: 900;
        font-size: 22px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 0;
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.5);
    }

    .faq-highlighted {
        background: linear-gradient(135deg, rgba(123, 44, 191, 0.2) 0%, rgba(212, 175, 55, 0.1) 100%);
        border: 2px solid var(--gold);
        border-radius: 8px;
        padding: 40px;
        margin-bottom: 40px;
        box-shadow: 0 10px 50px rgba(212, 175, 55, 0.2);
    }

    .faq-highlighted-title {
        color: var(--gold);
        font-size: 24px;
        font-weight: 900;
        font-family: 'Inter', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }

    .faq-highlighted-content {
        color: #ffffff;
        font-size: 14px;
        line-height: 1.8;
        font-family: 'Inter', sans-serif;
    }

    .faq-highlight-icon {
        font-size: 28px;
        margin-right: 10px;
        color: var(--gold);
    }

    .template-scroll-container {
        width: 100%;
        max-width: 1000px;
        height: 800px;
        margin: 0 auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        overflow-y: scroll;
        overflow-x: hidden;
        background: rgba(255, 255, 255, 0.02);
        padding: 0;
        scroll-behavior: smooth;
    }

    .template-scroll-container::-webkit-scrollbar { width: 12px; }
    .template-scroll-container::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.05); border-radius: 10px; }
    .template-scroll-container::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 10px; border: 2px solid rgba(5, 5, 5, 0.5); }
    .template-scroll-container::-webkit-scrollbar-thumb:hover { background: #e8c547; }

    .template-scroll-image {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 0;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ELITE ---
st.markdown("""
<div class="navbar-elite">
    <div class="logo-elite">STTACK SITE</div>
    <div class="nav-links-container">
        <a href="#clientes" class="nav-link-elite">Clientes</a>
        <a href="#quem-atendemos" class="nav-link-elite">Quem Atendemos</a>
        <a href="#como-funciona" class="nav-link-elite">Como Funciona</a>
        <a href="#templates" class="nav-link-elite">Templates</a>
        <a href="#precos" class="nav-link-elite">Preços</a>
        <a href="#faq" class="nav-link-elite">FAQ</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 1 & 2. HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates prontos.</span></h1>
    <p class="hero-sub">A solução ideal para quem precisa de um site rápido, profissional e editável sem depender de agências ou programadores.</p>
    <div style="margin-top: 50px; width: 300px;">
""", unsafe_allow_html=True)
st.markdown("""
<a href="#templates" style="display: inline-block; background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white; border: none; padding: 25px 60px; font-weight: 900; font-size: 22px; text-transform: uppercase; letter-spacing: 2px; border-radius: 0; clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%); text-decoration: none; transition: 0.4s; cursor: pointer;">CONHEÇA NOSSOS TEMPLATES ↓</a>
""", unsafe_allow_html=True)

# --- 5. PROVA SOCIAL (AVATARES FLOATING) ---
st.markdown("""
<div id="clientes" class="client-section">
    <h2 style="font-size: 30px; letter-spacing: 0px;">CONFIE EM QUEM<br>JÁ DOMINA.</h2>
    <div style="display: flex;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/7.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/8.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/6.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/17.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/410.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/413.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/414.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/415.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/422.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <div style="width:80px; height:80px; border-radius:50%; background: var(--accent); margin-left: -20px; display:flex; align-items:center; justify-content:center; font-weight:900;">+500</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown('<div id="quem-atendemos" style="padding: 120px 8%;">', unsafe_allow_html=True)
col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.markdown("""
    <div class="target-card">
        <h3>Proprietários de negócios</h3>
        <p>Que busca colocar sua empresa na internet com o menor custo do mercado, garantindo sua presença digital em minutos.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u2:
    st.markdown("""
    <div class="target-card" style="background: var(--accent); color: white; box-shadow: 15px 15px 0px white;">
        <h3>Infoprodutores/ prestadores de serviço</h3>
        <p>Temos estruturas otimizadas para converter visitantes em compradores reais. Destaque seus serviços com um design que transmite autoridade e confiança.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u3:
    st.markdown("""
    <div class="target-card">
        <h3>Freelancer</h3>
        <p>Venda nossos sites para seus clientes sem precisar programar do zero e fature com isso, aumentando sua margem de lucro entregando em tempo recorde.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PASSO A PASSO (INDUSTRIAL) ---
st.markdown('<div id="como-funciona" style="padding: 100px 8%; background: #050505;">', unsafe_allow_html=True)
st.markdown('<h2>PROCESSO <span class="serif-heavy">sem falhas.</span></h2><br><br>', unsafe_allow_html=True)

steps = [
    ("SELECIONE O MODELO IDEAL", "Escolha entre mais de 30 modelos validados o que mais combina com a identidade do seu negócio."),
    ("CUSTOMIZAÇÃO RÁPIDA", "Utilize nosso ambiente exclusivo de edição para personalizar tudo o que precisar sem complicações."),
    ("SETUP TÉCNICO GRATUITO", "Hospedamos seu site em minutos, com as melhores técnicas de SEO e com domínio Streamlit sem custo adicional, de forma rápida."),
    ("LANÇAMENTO IMEDIATO", "Site no ar, otimizado e pronto para escalar seu negócio com uma estrutura de alta performance.")
]

for i, (title, desc) in enumerate(steps):
    st.markdown(f"""
    <div class="step-row">
        <div class="step-num">0{i+1}</div>
        <div>
            <h3 style="color: var(--gold);">{title}</h3>
            <p style="max-width: 400px; opacity: 0.6;">{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- 3 & 4. SHOWCASE DE TEMPLATES (GRID 2D COM SCROLL) ---
st.markdown('<div id="templates" style="padding: 120px 8%;">', unsafe_allow_html=True)
st.markdown('<h2>Clique e explore por completo os templates ideais para <span class="serif-heavy"> seu negócio:</span></h2><br><br>', unsafe_allow_html=True)
st.markdown("""
<div class="carousel-section" style="padding: 0; background: transparent;">
    <div class="carousel-container">
        <a href="https://sttacktemplates.streamlit.app/?cliente=template13" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/13.png" alt="Template 13"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template27" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/27.png" alt="Template 27"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template26" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/26.png" alt="Template 26"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template17" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/17.png" alt="Template 17"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template5" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/5.png" alt="Template 5"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template1" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/1.png" alt="Template 1"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template22" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/22.png" alt="Template 22"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template14" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/14.png" alt="Template 14"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template20" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/20.png" alt="Template 20"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template21" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/21.png" alt="Template 21"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template33" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/33.png" alt="Template 33"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template35" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/35.png" alt="Template 35"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template24" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/24.png" alt="Template 24"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template11" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/11.png" alt="Template 11"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template18" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/18.png" alt="Template 18"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template16" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/16.png" alt="Template 16"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template15" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/15.png" alt="Template 15"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template8" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/8.png" alt="Template 8"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template3" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/3.png" alt="Template 3"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template19" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/19.png" alt="Template 19"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template2" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/2.png" alt="Template 2"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template23" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/23.png" alt="Template 23"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template25" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/25.png" alt="Template 25"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template6" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/6.png" alt="Template 6"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template12" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/12.png" alt="Template 12"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template7" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/7.png" alt="Template 7"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template9" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/9.png" alt="Template 9"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template4" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/4.png" alt="Template 4"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template29" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/29.png" alt="Template 29"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template30" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/30.png" alt="Template 30"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template31" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/31.png" alt="Template 31"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template10" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/10.png" alt="Template 10"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template32" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/32.png" alt="Template 32"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template34" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/34.png" alt="Template 34"></div></a>
        <a href="https://sttacktemplates.streamlit.app/?cliente=template28" target="_blank" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/templates/main/imagens/28.png" alt="Template 28"></div></a>
    </div>
</div>
""", unsafe_allow_html=True)


# --- 8. PREÇOS (ELITE) ---
st.markdown('<div id="precos" style="padding: 120px 8%; text-align:center;">', unsafe_allow_html=True)
st.markdown('<h2>INVISTA NA SUA <span class="serif-heavy">Presença.</span></h2><br><br>', unsafe_allow_html=True)

p2, p3 = st.columns(2)

with p2: # Featured
    st.markdown("""
    <div class="pricing-glass" style="border-top: 5px solid var(--accent);">
        <p style="color: var(--gold); letter-spacing: 3px; font-weight: 900;">PROFESSIONAL</p>
        <h1 style="font-size: 80px; margin: 30px 0;">R$ 49</h1>
        <p>✓ Estrutura profissional pensada para gerar clientes</p>
        <p>✓ Integração com WhatsApp via botão direto no site</p>
        <p>✓ Site publicado rapidamente após a personalização</p>
        <p>✓ Edite seu site quando quiser e o que quiser com um painel simples</p>
        <p>✓ Site rápido e otimizado para performance</p>
        <p>✓ Domínio e hospedagem Streamlit inclusos</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Acesso vitalício aos templates</p>
        <p>✓ Atualizações de novos templates inclusas</p>
        <p>✓ Suporte técnico ágil</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("CRIAR MEU SITE AGORA", key="main_p")
    import streamlit.components.v1 as components
    components.html("""
    <script>
    function attachClick() {
        const buttons = window.parent.document.querySelectorAll('button');
        let found = false;
        buttons.forEach(btn => {
            if (btn.innerText.trim() === 'CRIAR MEU SITE AGORA') {
                btn.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    window.open('https://pay.kiwify.com.br/qE6dljc', '_blank');
                };
                found = true;
            }
        });
        if (!found) setTimeout(attachClick, 300);
    }
    attachClick();
    </script>
    """, height=0)

with p3:
    st.markdown("""
    <div class="pricing-glass">
        <p>BUSINESS</p>
        <h1 style="font-size: 60px; margin: 30px 0;">R$ 197</h1>
        <p>✓ Licença comercial para vender nossos templates</p>
        <p>✓ Estruturas prontas para entrega rápida ao cliente</p>
        <p>✓ Painel de edição simplificado para seus clientes</p>
        <p>✓ Atualizações contínuas de novos templates</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Modelo validado para gerar renda com sites</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Suporte específico para parceiros</p>
        <p>✓ Selo de parceiro desenvolvedor</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("LIBERAR ACESSO DE REVENDA", key="p3")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div id="faq" style="padding: 100px 20%; background: #080808;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center; font-size: 40px;">FAQ / <span class="serif-heavy">Respostas.</span></h2><br>', unsafe_allow_html=True)

faq = {
    "Como é a estrutura do site?": "Nossos sites são do tipo single-page (página única). Tudo está em um único lugar, você rola para baixo e encontra todas as seções: hero, sobre, serviços, preços, FAQ, etc. Isso torna a navegação mais fluida e intuitiva.",
    "Preciso saber programação ou design para criar meu site?": "Não. Você não precisa saber programação nem design. Criamos um editor visual simples e intuitivo onde você pode alterar textos, informações e imagens em poucos cliques, sem nenhuma parte técnica. O template já vem com estrutura profissional pronta, basta personalizar e publicar.",
    "Posso editar o site depois de publicado?": "Sim. Você pode editar seu site sempre que quiser, mesmo depois de publicado. Todas as alterações são feitas pelo painel de edição, de forma rápida e simples — sem precisar tirar o site do ar. Basta atualizar textos, imagens ou informações e as mudanças já ficam disponíveis automaticamente.",
    "Posso usar meu próprio domínio?": "Seu site é publicado com um domínio profissional utilizando a infraestrutura da Streamlit, no formato: https://nomedoseusite.streamlit.app. Esse modelo permite colocar seu site no ar de forma rápida, segura e sem custos adicionais de hospedagem. Caso queira, você também pode futuramente conectar um domínio próprio (ex.: seusite.com), mas isso é opcional, o site já funciona normalmente com o domínio incluído.",
    "A hospedagem é mesmo gratuita?": "Sim. Nosso método utiliza infraestruturas globais de alta performance que permitem manter sites profissionais online sem mensalidades de hospedagem.",
    "Posso vender os sites para clientes?": "Com o plano Business, você tem licença comercial completa para lucrar com nossos designs.",
    "O site funciona no celular?": "Sim. Todos os templates são 100% responsivos, ou seja, funcionam perfeitamente em celulares, tablets e computadores. O layout se adapta automaticamente ao tamanho da tela, garantindo que seu site fique organizado, rápido e profissional em qualquer dispositivo.",
    "É seguro realizar a compra?": "Sim! Toda a compra é processada pela Kiwify, uma das plataformas de pagamentos e educação mais seguras e reconhecidas do Brasil. Nenhum dado sensível passa por nós, tudo ocorre diretamente no ambiente da Kiwify, com criptografia, certificados de segurança e antifraude.",
    "Como recebo acesso após a compra?": "O acesso é 100% digital e imediato. Após a confirmação do pagamento, você receberá um e-mail da Kiwify com seus dados de acesso à área de membros. Lá, você encontrará os arquivos de todos os templates, além dos guias de customização e explicações organizados por módulos.",
    "Existe algum tipo de suporte?": "Sim. Oferecemos suporte técnico ágil via e-mail para ajudar você em todas as etapas, desde a personalização até a publicação do site. Sempre que precisar, nossa equipe estará disponível para orientar de forma rápida e prática.",
    "Política de reembolso": "Você tem 7 dias para testar o produto com total segurança. Caso não fique satisfeito por qualquer motivo, basta solicitar o reembolso dentro desse prazo e devolveremos 100% do valor pago, sem burocracia. Acreditamos na qualidade dos nossos templates e queremos que você tenha tempo suficiente para explorar o material, testar o painel de edição e verificar se faz sentido para o seu projeto."
}

for i, (q, a) in enumerate(faq.items()):
    if i == 0:
        with st.expander(q):
            st.markdown(f"<p style='color: var(--gold); font-size: 15px; font-weight: 600;'>{a}</p>", unsafe_allow_html=True)
    else:
        with st.expander(q):
            st.markdown(f"<p style='color: #ccc;'>{a}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 60px 8%; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 10px; opacity: 0.4; letter-spacing: 5px;">
    STTACK SITE ® - DOMINANDO A WEB DESDE 2019. Todos os direitos reservados
</div>
""", unsafe_allow_html=True)
