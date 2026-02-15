import streamlit as st
import requests

# --- CONFIGURAÇÃO INICIAL (DEVE SER A PRIMEIRA COISA) ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- LÓGICA DE ROTEAMENTO (TEMPLATES) ---
query_params = st.query_params
view_mode = query_params.get("view")

if view_mode:
    # Botão flutuante para voltar à loja
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:rgba(123, 44, 191, 0.8); color:white; text-decoration:none; padding:10px 20px; 
        border-radius:50px; font-weight:bold; font-family:sans-serif; border: 1px solid white;">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        # Constrói a URL Raw do GitHub baseada no parâmetro (ex: view=1)
        # Formato: https://raw.githubusercontent.com/SttackSite/template1/main/Template1.py
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        
        response = requests.get(raw_url)
        if response.status_code == 200:
            code = response.text
            # Remove set_page_config do código importado para não dar erro
            code = code.replace("st.set_page_config", "# st.set_page_config")
            exec(code) # Executa o código do template em tempo real
        else:
            st.error(f"Template {view_mode} não encontrado. Verifique se o repositório é público.")
    except Exception as e:
        st.error(f"Erro ao carregar template: {e}")
    
    st.stop() # Interrompe a execução aqui para não carregar a landing page abaixo

# --- SE NÃO HOUVER VIEW_MODE, CARREGA A LANDING PAGE ABAIXO ---

# --- CSS RADICAL ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');
    :root { --accent: #7b2cbf; --gold: #d4af37; --dark: #050505; --glass: rgba(255, 255, 255, 0.03); }
    .stApp { background-color: var(--dark); color: #ffffff; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    h1, h2 { font-family: 'Inter', sans-serif; font-weight: 900; text-transform: uppercase; letter-spacing: -3px; line-height: 0.85; }
    .serif-heavy { font-family: 'Playfair Display', serif; font-style: italic; text-transform: none; letter-spacing: -1px; }
    
    /* NAVBAR */
    .navbar-elite { display: flex; justify-content: space-between; align-items: center; padding: 25px 8%; background: rgba(5, 5, 5, 0.5); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); width: 100%; box-sizing: border-box; }
    .logo-elite { font-size: 22px; font-weight: 900; letter-spacing: 2px; font-family: 'Inter', sans-serif; color: var(--gold); text-transform: uppercase; }
    .nav-links-container { display: flex; gap: 45px; align-items: center; }
    .nav-link-elite { color: #ffffff !important; text-decoration: none !important; font-size: 12px; letter-spacing: 1px; font-weight: 600; font-family: 'Inter', sans-serif; transition: all 0.3s ease; text-transform: uppercase; }
    .nav-link-elite:hover { color: var(--gold) !important; }

    /* HERO */
    .hero-section { height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 0 8%; background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%); border-bottom: 1px solid rgba(255,255,255,0.1); }
    .hero-h1 { font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }
    .hero-sub { font-size: 24px; max-width: 600px; line-height: 1.4; color: rgba(255,255,255,0.7); border-left: 4px solid var(--accent); padding-left: 20px; }

    /* CARROSSEL */
    .carousel-section { padding: 120px 8%; background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%); }
    .carousel-container { display: flex; gap: 40px; overflow-x: auto; padding: 20px 0; scroll-behavior: smooth; }
    .carousel-item-link { display: block; flex: 0 0 calc(33.333% - 27px); min-width: 705px; height: 315px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.4s ease; text-decoration: none; }
    .carousel-item-link:hover { border-color: var(--gold); transform: translateY(-15px); box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3); }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    /* FAQ E PREÇOS */
    .pricing-glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 60px 40px; text-align: center; }
    .target-card { padding: 50px; background: white; color: black; border: 5px solid var(--accent); box-shadow: 15px 15px 0px var(--accent); height: 100%; }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
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

# --- HERO ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates prontos.</span></h1>
    <p class="hero-sub">A solução ideal para quem precisa de um site rápido, profissional e editável sem depender de agências ou programadores.</p>
</div>
""", unsafe_allow_html=True)

# --- CARROSSEL DINÂMICO ---
st.markdown('<div id="templates" style="padding: 120px 8%;"><h2>Clique e explore o template:</h2><br>', unsafe_allow_html=True)

# Gerando os itens do carrossel programaticamente do 1 ao 28
carousel_html = '<div class="carousel-section"><div class="carousel-container">'
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    # O link agora aponta para a mesma página com o parâmetro ?view=X
    carousel_html += f"""
        <a href="/?view={i}" target="_self" class="carousel-item-link">
            <img src="{img_url}" alt="Template {i}">
        </a>
    """
carousel_html += '</div></div>'

st.markdown(carousel_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- DEMAIS SEÇÕES (CLIENTES, PREÇOS, FAQ) ---
# [Mantenha aqui o restante do seu código original de Clientes, Cards, Preços e FAQ]
# Por brevidade, incluí apenas a lógica principal de navegação. 
# Basta colar o restante do seu código original (Section 5 até o Footer) abaixo.

st.markdown('<div style="text-align:center; padding: 50px;">Use o carrossel acima para testar os templates!</div>', unsafe_allow_html=True)
