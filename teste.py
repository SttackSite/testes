import streamlit as st
import requests
import re
from io import StringIO
import sys

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="STTACK - Galeria de Templates",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS GLOBAL ---
st.markdown("""
<style>
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* Navbar da galeria */
    .gallery-navbar {
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
    
    .gallery-logo {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        font-family: 'Inter', sans-serif;
        color: #d4af37;
        text-transform: uppercase;
    }
    
    .gallery-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 12px;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR DA GALERIA ---
st.markdown("""
<div class="gallery-navbar">
    <div>
        <div class="gallery-logo">STTACK SITE</div>
        <div class="gallery-subtitle">Galeria de Templates</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- LISTA DE TEMPLATES ---
templates_list = [
    ("Template 1", "https://raw.githubusercontent.com/SttackSite/template1/main/Template1.py"),
    ("Template 2", "https://raw.githubusercontent.com/SttackSite/template2/main/Template2.py"),
    ("Template 3", "https://raw.githubusercontent.com/SttackSite/template3/main/Template3.py"),
    ("Template 4", "https://raw.githubusercontent.com/SttackSite/template4/main/Template4.py"),
    ("Template 5", "https://raw.githubusercontent.com/SttackSite/template5/main/Template5.py"),
    ("Template 6", "https://raw.githubusercontent.com/SttackSite/template6/main/Template6.py"),
    ("Template 7", "https://raw.githubusercontent.com/SttackSite/template7/main/Template7.py"),
    ("Template 8", "https://raw.githubusercontent.com/SttackSite/template8/main/Template8.py"),
    ("Template 9", "https://raw.githubusercontent.com/SttackSite/template9/main/Template9.py"),
    ("Template 10", "https://raw.githubusercontent.com/SttackSite/template10/main/Template10.py"),
    ("Template 11", "https://raw.githubusercontent.com/SttackSite/template11/main/Template11.py"),
    ("Template 12", "https://raw.githubusercontent.com/SttackSite/template12/main/Template12.py"),
    ("Template 13", "https://raw.githubusercontent.com/SttackSite/template13/main/Template13.py"),
    ("Template 14", "https://raw.githubusercontent.com/SttackSite/template14/main/Template14.py"),
    ("Template 15", "https://raw.githubusercontent.com/SttackSite/template15/main/Template15.py"),
    ("Template 16", "https://raw.githubusercontent.com/SttackSite/template16/main/Template16.py"),
    ("Template 17", "https://raw.githubusercontent.com/SttackSite/template17/main/Template17.py"),
    ("Template 18", "https://raw.githubusercontent.com/SttackSite/template18/main/Template18.py"),
    ("Template 19", "https://raw.githubusercontent.com/SttackSite/template19/main/Template19.py"),
    ("Template 20", "https://raw.githubusercontent.com/SttackSite/template20/main/Template20.py"),
    ("Template 21", "https://raw.githubusercontent.com/SttackSite/template21/main/Template21.py"),
    ("Template 22", "https://raw.githubusercontent.com/SttackSite/template22/main/Template22.py"),
    ("Template 23", "https://raw.githubusercontent.com/SttackSite/template23/main/Template23.py"),
    ("Template 24", "https://raw.githubusercontent.com/SttackSite/template24/main/Template24.py"),
    ("Template 25", "https://raw.githubusercontent.com/SttackSite/template25/main/Template25.py"),
    ("Template 26", "https://raw.githubusercontent.com/SttackSite/template26/main/Template26.py"),
    ("Template 27", "https://raw.githubusercontent.com/SttackSite/template27/main/Template27.py"),
    ("Template 28", "https://raw.githubusercontent.com/SttackSite/template28/main/Template28.py"),
]

# --- FUNÇÃO PARA CARREGAR E RENDERIZAR TEMPLATE ---
@st.cache_data(ttl=3600)
def load_template_code(url):
    """Carrega o código do template do GitHub"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Erro ao carregar template: {str(e)}"

def render_template(template_code):
    """Renderiza o template removendo st.set_page_config()"""
    try:
        # Remove st.set_page_config() para evitar conflitos
        cleaned_code = re.sub(
            r'st\.set_page_config\([^)]*\)',
            '',
            template_code,
            flags=re.DOTALL
        )
        
        # Remove import streamlit duplicado (mantém o primeiro)
        lines = cleaned_code.split('\n')
        import_removed = False
        filtered_lines = []
        
        for line in lines:
            if line.strip().startswith('import streamlit') or line.strip().startswith('from streamlit'):
                if not import_removed:
                    filtered_lines.append(line)
                    import_removed = True
            else:
                filtered_lines.append(line)
        
        cleaned_code = '\n'.join(filtered_lines)
        
        # Executa o código
        exec(cleaned_code, {'st': st, '__name__': '__main__'})
        
    except Exception as e:
        st.error(f"❌ Erro ao renderizar template: {str(e)}")

# --- CRIAR ABAS ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h2 style="color: #d4af37; font-size: 32px; margin: 0;">Escolha seu Template</h2>
    <p style="color: rgba(255,255,255,0.6); margin-top: 10px;">Visualize cada um dos 28 templates disponíveis</p>
</div>
""", unsafe_allow_html=True)

# Criar abas
tabs = st.tabs([name for name, _ in templates_list])

# Preencher cada aba com seu template
for tab, (template_name, template_url) in zip(tabs, templates_list):
    with tab:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Mostrar indicador de carregamento
        with st.spinner(f"Carregando {template_name}..."):
            template_code = load_template_code(template_url)
            
            if "Erro ao carregar" in template_code:
                st.error(template_code)
            else:
                # Renderizar o template
                render_template(template_code)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="padding: 40px 8%; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 10px; opacity: 0.4; letter-spacing: 5px;">
    STTACK SITE // GALERIA DE TEMPLATES 2026
</div>
""", unsafe_allow_html=True)
