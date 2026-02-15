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
    # Botão de voltar
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; font-family:sans-serif; border: 2px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        response = requests.get(raw_url)
        
        if response.status_code == 200:
            raw_code = response.text
            
            # 1. Comentamos o set_page_config original do template para evitar erro
            clean_code = raw_code.replace("st.set_page_config", "# st.set_page_config")
            
            # 2. A CORREÇÃO REAL: Usamos dedent no bloco inteiro e strip apenas nas extremidades
            # Isso mantém a estrutura interna (ifs, fors, defs) mas remove o erro de indentação global
            final_code = textwrap.dedent(clean_code).strip()
            
            exec(final_code)
        else:
            st.error(f"Template {view_mode} não encontrado.")
    except Exception as e:
        st.error(f"Erro ao carregar o código: {e}")
    
    st.stop()

# --- LANDING PAGE ORIGINAL (CSS RADICAL) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    :root { --accent: #7b2cbf; --gold: #d4af37; --dark: #050505; }
    .stApp { background-color: var(--dark); color: #ffffff; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* NAVBAR */
    .navbar-elite { display: flex; justify-content: space-between; align-items: center; padding: 25px 8%; background: rgba(5,5,5,0.8); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.1); width: 100%; box-sizing: border-box; }
    .logo-elite { font-size: 22px; font-weight: 900; color: var(--gold); font-family: 'Inter'; }

    /* CARROSSEL - DESIGN RESTAURADO */
    .carousel-section { padding: 60px 0; background: #050505; overflow: hidden; }
    .carousel-container { 
        display: flex; 
        gap: 30px; 
        overflow-x: scroll; 
        padding: 40px 8%; 
        scroll-behavior: smooth;
    }
    .carousel-container::-webkit-scrollbar { display: none; } /* Esconde scrollbar */

    .carousel-item-link { 
        flex: 0 0 500px; 
        height: 300px; 
        border-radius: 15px; 
        overflow: hidden; 
        border: 1px solid rgba(255,255,255,0.1); 
        transition: all 0.4s ease;
        display: block;
    }
    .carousel-item-link:hover { 
        transform: scale(1.02); 
        border-color: var(--accent);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.4);
    }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    h2 { font-family: 'Inter'; font-weight: 900; text-transform: uppercase; padding-left: 8%; margin-top: 50px; }
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar-elite"><div class="logo-elite">STTACK SITE</div></div>', unsafe_allow_html=True)

# Título da Seção
st.markdown('<h2>Nossos Templates</h2>', unsafe_allow_html=True)

# CARROSSEL UNIFICADO (Para não quebrar o CSS)
carousel_html = '<div class="carousel-section"><div class="carousel-container">'
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    carousel_html += f'<a href="/?view={i}" target="_self" class="carousel-item-link"><img src="{img_url}"></a>'
carousel_html += '</div></div>'

st.markdown(carousel_html, unsafe_allow_html=True)

# Rodapé simples
st.markdown("<p style='text-align:center; color:#555;'>Clique na imagem para ver o template em tela cheia.</p>", unsafe_allow_html=True)
