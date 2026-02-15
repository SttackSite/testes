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
    # Botão flutuante de voltar
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; font-family:sans-serif; border: 2px solid white;">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        response = requests.get(raw_url)
        
        if response.status_code == 200:
            linhas = response.text.splitlines()
            codigo_limpo = []
            
            for linha in linhas:
                # Remove st.set_page_config para evitar erro de execução dupla
                if "st.set_page_config" in linha:
                    codigo_limpo.append("# " + linha.lstrip())
                else:
                    # O segredo: .lstrip() remove espaços à esquerda de cada linha individualmente
                    codigo_limpo.append(linha.lstrip())
            
            final_code = "\n".join(codigo_limpo)
            exec(final_code)
        else:
            st.error(f"Não foi possível carregar o template {view_mode}")
    except Exception as e:
        st.error(f"Erro crítico: {e}")
    
    st.stop()

# --- LANDING PAGE ORIGINAL ---

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&display=swap');
    :root { --accent: #7b2cbf; --gold: #d4af37; --dark: #050505; }
    .stApp { background-color: var(--dark); color: #ffffff; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* NAVBAR */
    .navbar-elite { display: flex; justify-content: space-between; align-items: center; padding: 25px 8%; background: rgba(5,5,5,0.8); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.1); width: 100%; box-sizing: border-box; position: sticky; top: 0; z-index: 999; }
    .logo-elite { font-size: 22px; font-weight: 900; color: var(--gold); font-family: 'Inter'; }

    /* CARROSSEL - CORREÇÃO DO EFEITO */
    .carousel-section { padding: 80px 8%; background: #050505; }
    .carousel-container { 
        display: flex; 
        gap: 30px; 
        overflow-x: auto; 
        padding: 40px 0; 
        scroll-behavior: smooth;
        -webkit-overflow-scrolling: touch;
    }
    .carousel-container::-webkit-scrollbar { height: 6px; }
    .carousel-container::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 10px; }

    .carousel-item-link { 
        flex: 0 0 450px; /* Largura fixa para manter o scroll horizontal */
        height: 280px; 
        border-radius: 12px; 
        overflow: hidden; 
        border: 1px solid rgba(255,255,255,0.1); 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: block;
    }
    .carousel-item-link:hover { 
        transform: scale(1.05) translateY(-10px); 
        border-color: var(--gold); 
        box-shadow: 0 20px 50px rgba(123, 44, 191, 0.3);
    }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    h2 { font-family: 'Inter'; font-weight: 900; text-transform: uppercase; padding-left: 8%; }
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar-elite"><div class="logo-elite">STTACK SITE</div></div>', unsafe_allow_html=True)

# Seção de Templates
st.markdown('<div style="padding-top: 100px;"><h2>Explore os Templates</h2></div>', unsafe_allow_html=True)

# CONSTRUINDO O CARROSSEL EM UMA ÚNICA STRING PARA NÃO QUEBRAR O CSS
carousel_html = '<div class="carousel-section"><div class="carousel-container">'
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    carousel_html += f'<a href="/?view={i}" target="_self" class="carousel-item-link"><img src="{img_url}"></a>'
carousel_html += '</div></div>'

st.markdown(carousel_html, unsafe_allow_html=True)

# Restante do site...
st.markdown("<div style='text-align:center; color:gray; padding: 50px;'>Role para o lado para ver mais templates →</div>", unsafe_allow_html=True)
