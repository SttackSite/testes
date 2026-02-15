import streamlit as st
import requests
import types

# --- CONFIGURAÇÃO DA PÁGINA (SÓ PODE EXISTIR AQUI) ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- LÓGICA DE ROTEAMENTO ---
query_params = st.query_params
view_mode = query_params.get("view")

if view_mode:
    # Botão flutuante de voltar
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:999999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; font-family:sans-serif; border: 2px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        ← VOLTAR PARA STTACK
        </a>
    """, unsafe_allow_html=True)
    
    try:
        # Busca o código do GitHub
        raw_url = f"https://raw.githubusercontent.com/SttackSite/template{view_mode}/main/Template{view_mode}.py"
        response = requests.get(raw_url)
        
        if response.status_code == 200:
            source_code = response.text
            
            # Remove o set_page_config do template para não dar erro de duplicata
            source_code = source_code.replace("st.set_page_config", "# st.set_page_config")
            
            # CRIAÇÃO DE MÓDULO VIRTUAL (Isso ignora erros de indentação global)
            module_name = f"template_{view_mode}"
            virtual_module = types.ModuleType(module_name)
            virtual_module.st = st # Passa o streamlit para dentro do módulo
            
            # Executa o código dentro do contexto do módulo virtual
            exec(source_code, virtual_module.__dict__)
        else:
            st.error(f"Template {view_mode} não encontrado no repositório.")
    except Exception as e:
        st.error(f"Erro ao carregar template {view_mode}: {e}")
    
    st.stop()

# --- LANDING PAGE ORIGINAL (RESTAURADA) ---

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

    /* CARROSSEL - VOLTANDO AO ORIGINAL */
    .carousel-section { padding: 80px 0; background: #050505; }
    .carousel-container { 
        display: flex; 
        gap: 30px; 
        overflow-x: auto; 
        padding: 40px 8%; 
        scroll-behavior: smooth;
    }
    .carousel-container::-webkit-scrollbar { height: 6px; }
    .carousel-container::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 10px; }

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
        transform: scale(1.05); 
        border-color: var(--gold); 
    }
    .carousel-item-link img { width: 100%; height: 100%; object-fit: cover; }
    
    h2 { font-family: 'Inter'; font-weight: 900; text-transform: uppercase; padding-left: 8%; margin-top: 40px;}
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar-elite"><div class="logo-elite">STTACK SITE</div></div>', unsafe_allow_html=True)

# Seção de Templates
st.markdown('<h2>Clique na imagem para ver o site completo:</h2>', unsafe_allow_html=True)

# Construção do Carrossel (HTML ÚNICO para não quebrar)
carousel_items = ""
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    carousel_items += f'<a href="/?view={i}" target="_self" class="carousel-item-link"><img src="{img_url}"></a>'

st.markdown(f"""
<div class="carousel-section">
    <div class="carousel-container">
        {carousel_items}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:gray;'>Role para o lado para ver mais templates →</p>", unsafe_allow_html=True)
