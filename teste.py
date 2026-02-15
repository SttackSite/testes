import streamlit as st
import requests
import textwrap

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- LÓGICA DE ROTEAMENTO (TEMPLATES) ---
query_params = st.query_params
view_mode = query_params.get("view")

if view_mode:
    # Botão flutuante de voltar (Estilo Sttack)
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; font-family:sans-serif; border: 2px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        # Busca o código Raw do GitHub
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        response = requests.get(raw_url)
        
        if response.status_code == 200:
            raw_code = response.text
            
            # 1. Comenta configurações de página para evitar conflitos de execução
            clean_code = raw_code.replace("st.set_page_config", "# st.set_page_config")
            
            # 2. LIMPEZA TOTAL DE ESPAÇOS (Resolve o erro 'unexpected indent')
            # O .strip() remove espaços/quebras de linha no início e fim do arquivo
            # O dedent remove indentações acidentais em bloco
            final_code = textwrap.dedent(clean_code).strip()
            
            # Executa o código purificado
            exec(final_code)
        else:
            st.error(f"Erro {response.status_code}: Não consegui acessar o Template {view_mode}.")
    except Exception as e:
        st.error(f"Erro crítico ao carregar: {e}")
    
    st.stop() # Mata a execução para não carregar a landing page por baixo

# --- INÍCIO DA LANDING PAGE ORIGINAL ---

# Estilos CSS (Copiados fielmente do seu arquivo) [cite: 1, 2, 3, 4, 15, 16, 17, 18, 23, 31, 33, 46, 49, 53]
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');
    :root { --accent: #7b2cbf; --gold: #d4af37; --dark: #050505; --glass: rgba(255, 255, 255, 0.03); }
    .stApp { background-color: var(--dark); color: #ffffff; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    h1, h2 { font-family: 'Inter', sans-serif; font-weight: 900; text-transform: uppercase; letter-spacing: -3px; line-height: 0.85; }
    .serif-heavy { font-family: 'Playfair Display', serif; font-style: italic; text-transform: none; letter-spacing: -1px; }
    
    .navbar-elite { display: flex; justify-content: space-between; align-items: center; padding: 25px 8%; background: rgba(5, 5, 5, 0.5); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); width: 100%; box-sizing: border-box; }
    .logo-elite { font-size: 22px; font-weight: 900; color: var(--gold); }
    .nav-links-container { display: flex; gap: 45px; }
    .nav-link-elite { color: #ffffff !important; text-decoration: none !important; font-size: 12px; font-weight: 600; text-transform: uppercase; }

    .hero-section { height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 0 8%; background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%); border-bottom: 1px solid rgba(255,255,255,0.1); }
    .hero-h1 { font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }
    .hero-sub { font-size: 24px; max-width: 600px; border-left: 4px solid var(--accent); padding-left: 20px; color: rgba(255,255,255,0.7); }

    .carousel-section { padding: 120px 8%; background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%); }
    .carousel-container { display: flex; gap: 40px; overflow-x: auto; padding: 20px 0; scroll-behavior: smooth; }
    .carousel-item-link { display: block; flex: 0 0 calc(33.333% - 27px); min-width: 705px; height: 315px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.4s ease; }
    .carousel-item-link:hover { border-color: var(--gold); transform: translateY(-15px); box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3); }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    .target-card { padding: 50px; background: white; color: black; border: 5px solid var(--accent); box-shadow: 15px 15px 0px var(--accent); height: 100%; }
    .pricing-glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 60px 40px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Renderização da Landing Page (Navbar, Hero, etc.) [cite: 5, 8, 59]
st.markdown('<div class="navbar-elite"><div class="logo-elite">STTACK SITE</div><div class="nav-links-container"><a href="#templates" class="nav-link-elite">Templates</a><a href="#precos" class="nav-link-elite">Preços</a><a href="#faq" class="nav-link-elite">FAQ</a></div></div>', unsafe_allow_html=True)

st.markdown('<div class="hero-section"><h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates prontos.</span></h1><p class="hero-sub">A solução ideal para sites rápidos e profissionais.</p></div>', unsafe_allow_html=True)

# --- SEÇÃO DE TEMPLATES COM LOOP DINÂMICO --- [cite: 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
st.markdown('<div id="templates" style="padding: 120px 8%;"><h2>Clique para visualizar o template completo:</h2><div class="carousel-container">', unsafe_allow_html=True)

for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    # IMPORTANTE: target="_self" para recarregar na mesma aba com o parâmetro de URL
    st.markdown(f'<a href="/?view={i}" target="_self" class="carousel-item-link"><img src="{img_url}"></a>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# --- IMPORTANTE: ADICIONE O RESTANTE DO SEU CÓDIGO (PREÇOS E FAQ) ABAIXO ---
# Use o que você já tinha no 'landing completa.txt' para as seções finais.
