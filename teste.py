import streamlit as st
import requests
import textwrap

# --- CONFIGURAÇÃO DA PÁGINA (DEVE SER A PRIMEIRA COISA) ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- LÓGICA DE ROTEAMENTO (TEMPLATES) ---
query_params = st.query_params
view_mode = query_params.get("view")

if view_mode:
    # Botão de voltar customizado
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; font-family:sans-serif; border: 2px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        # URL Raw do GitHub
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        
        response = requests.get(raw_url)
        if response.status_code == 200:
            raw_code = response.text
            
            # 1. Comenta configurações de página para evitar conflitos
            clean_code = raw_code.replace("st.set_page_config", "# st.set_page_config")
            
            # 2. LIMPEZA DE INDENTAÇÃO (Resolve o erro do seu print)
            # Remove espaços fantasmas no início do arquivo
            final_code = textwrap.dedent(clean_code)
            
            # Executa o código limpo
            exec(final_code)
        else:
            st.error(f"Template {view_mode} não encontrado no repositório.")
    except Exception as e:
        st.error(f"Erro ao carregar template: {e}")
    
    st.stop()

# --- ABAIXO SEGUE SUA LANDING PAGE ORIGINAL COMPLETA ---

# CSS RADICAL [cite: 103, 104, 105, 124, 147]
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');
    :root { --accent: #7b2cbf; --gold: #d4af37; --dark: #050505; --glass: rgba(255, 255, 255, 0.03); }
    .stApp { background-color: var(--dark); color: #ffffff; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    h1, h2 { font-family: 'Inter', sans-serif; font-weight: 900; text-transform: uppercase; letter-spacing: -3px; line-height: 0.85; }
    .serif-heavy { font-family: 'Playfair Display', serif; font-style: italic; text-transform: none; letter-spacing: -1px; }
    
    /* NAVBAR [cite: 106, 107, 109, 111, 112] */
    .navbar-elite { display: flex; justify-content: space-between; align-items: center; padding: 25px 8%; background: rgba(5, 5, 5, 0.5); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); width: 100%; box-sizing: border-box; }
    .logo-elite { font-size: 22px; font-weight: 900; color: var(--gold); text-transform: uppercase; }
    .nav-links-container { display: flex; gap: 45px; align-items: center; }
    .nav-link-elite { color: #ffffff !important; text-decoration: none !important; font-size: 12px; font-weight: 600; text-transform: uppercase; }

    /* CARROSSEL [cite: 127, 132, 133, 135, 141] */
    .carousel-container { display: flex; gap: 40px; overflow-x: auto; padding: 20px 0; scroll-behavior: smooth; }
    .carousel-item-link { display: block; flex: 0 0 calc(33.333% - 27px); min-width: 705px; height: 315px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.4s ease; text-decoration: none; }
    .carousel-item-link:hover { border-color: var(--gold); transform: translateY(-15px); box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3); }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    /* PREÇOS [cite: 147, 150, 151] */
    .pricing-glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 60px 40px; text-align: center; }
    div.stButton > button { background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white; border: none; padding: 25px 60px; font-weight: 900; clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%); }
</style>
""", unsafe_allow_html=True)

# NAVBAR [cite: 106]
st.markdown('<div class="navbar-elite"><div class="logo-elite">STTACK SITE</div><div class="nav-links-container"><a href="#clientes" class="nav-link-elite">Clientes</a><a href="#templates" class="nav-link-elite">Templates</a><a href="#precos" class="nav-link-elite">Preços</a><a href="#faq" class="nav-link-elite">FAQ</a></div></div>', unsafe_allow_html=True)

# HERO [cite: 116, 160]
st.markdown('<div style="height:100vh; display:flex; flex-direction:column; justify-content:center; padding:0 8%; background:radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%);"><h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates.</span></h1></div>', unsafe_allow_html=True)

# CARROSSEL DINÂMICO (DO 1 AO 28) [cite: 171, 180]
st.markdown('<div id="templates" style="padding: 120px 8%;"><h2>Clique para testar:</h2>', unsafe_allow_html=True)
carousel_html = '<div class="carousel-container">'
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    # O target="_self" garante que abra na mesma aba para o roteamento funcionar
    carousel_html += f'<a href="/?view={i}" target="_self" class="carousel-item-link"><img src="{img_url}"></a>'
carousel_html += '</div>'
st.markdown(carousel_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FAQ E PREÇOS (Resumidos conforme seu arquivo original) [cite: 181, 186, 202] ---
# ... (Cole aqui o restante das suas colunas de preço e o loop do FAQ do seu arquivo original)
