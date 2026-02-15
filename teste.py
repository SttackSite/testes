import streamlit as st
import requests
import textwrap

# 1. Configuração de página (obrigatório ser o primeiro comando Streamlit)
st.set_page_config(page_title="Sttack Site", page_icon="💎", layout="wide")

# --- LÓGICA DE ROTEAMENTO ---
query_params = st.query_params
template_id = query_params.get("view")

if template_id:
    # Botão de voltar fixo
    st.markdown("""
        <a href="/" target="_self" style="position:fixed; top:20px; left:20px; z-index:9999; 
        background:#7b2cbf; color:white; text-decoration:none; padding:12px 24px; 
        border-radius:50px; font-weight:900; border: 2px solid white;">← VOLTAR</a>
    """, unsafe_allow_html=True)

    try:
        # URL do seu repositório
        url = f"https://raw.githubusercontent.com/SttackSite/template{template_id}/main/Template{template_id}.py"
        response = requests.get(url)
        
        if response.status_code == 200:
            # O SEGREDO: Usar textwrap.dedent e remover linhas em branco iniciais
            raw_code = response.text
            
            # Remove o set_page_config do template para não conflitar
            raw_code = raw_code.replace("st.set_page_config", "# st.set_page_config")
            
            # Limpeza cirúrgica: Remove espaços de indentação global que causam o erro de linha 5
            # mas preserva a indentação interna de funções/ifs
            clean_code = textwrap.dedent(raw_code).strip()
            
            # Executa com um dicionário global próprio para isolar o escopo
            exec(clean_code, globals())
        else:
            st.error(f"Template {template_id} não encontrado.")
    except Exception as e:
        st.error(f"Erro ao processar template: {e}")
    
    st.stop()

# --- LANDING PAGE (SÓ CARREGA SE NÃO HOUVER TEMPLATE_ID) ---

# CSS DO CARROSSEL (Unificado para não quebrar o efeito visual)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    .stApp { background-color: #050505; color: white; }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; }

    /* Estilo do Carrossel */
    .carousel-wrapper {
        display: flex;
        gap: 20px;
        overflow-x: auto;
        padding: 40px 8%;
        scroll-behavior: smooth;
    }
    .carousel-wrapper::-webkit-scrollbar { height: 5px; }
    .carousel-wrapper::-webkit-scrollbar-thumb { background: #7b2cbf; }

    .card {
        flex: 0 0 450px;
        height: 280px;
        border-radius: 12px;
        border: 1px solid #333;
        overflow: hidden;
        transition: 0.3s;
    }
    .card:hover { transform: translateY(-10px); border-color: #d4af37; }
    .card img { width: 100%; height: 100%; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

# Navbar Simples
st.markdown("<div style='padding: 20px 8%; font-weight: 900; color: #d4af37;'>STTACK SITE</div>", unsafe_allow_html=True)

# Título
st.markdown("<h2 style='padding: 0 8%;'>NOSSOS TEMPLATES</h2>", unsafe_allow_html=True)

# Renderização do Carrossel
# Montamos todo o HTML antes e damos um único st.markdown para não quebrar as DIVs
carousel_html = '<div class="carousel-wrapper">'
for i in range(1, 29):
    img_url = f"https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/{i}.png"
    carousel_html += f'<a href="/?view={i}" target="_self" class="card"><img src="{img_url}"></a>'
carousel_html += '</div>'

st.markdown(carousel_html, unsafe_allow_html=True)

# Cole aqui o restante da sua Landing Page original (Preços, FAQ, etc)
