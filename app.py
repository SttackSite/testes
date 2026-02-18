import streamlit as st
import json
import os
from datetime import datetime
import subprocess
import base64

# ✅ CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="SttackSite - Multi Cliente", page_icon="🚀", layout="wide")

# ✅ VARIÁVEIS DE CONFIGURAÇÃO
GITHUB_TOKEN = "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"
GITHUB_REPO = "seu-usuario/seu-repositorio"  # ✅ ALTERE: seu repositório
GITHUB_BRANCH = "main"
CONFIGS_DIR = "configs"

# ✅ Criar diretório de configs se não existir
os.makedirs(CONFIGS_DIR, exist_ok=True)

# ✅ FUNÇÃO: Fazer commit no GitHub
def commit_to_github(arquivo, mensagem):
    """Faz commit automático no GitHub"""
    try:
        # Ler o arquivo
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Codificar em base64
        conteudo_b64 = base64.b64encode(conteudo.encode()).decode()
        
        # Fazer requisição para GitHub API
        import requests
        
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{arquivo}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Content-Type": "application/json"
        }
        
        # Primeiro, obter o SHA do arquivo atual
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            sha = response.json()["sha"]
        else:
            sha = None
        
        # Dados para o commit
        data = {
            "message": mensagem,
            "content": conteudo_b64,
            "branch": GITHUB_BRANCH
        }
        
        if sha:
            data["sha"] = sha
        
        # Fazer o commit
        response = requests.put(url, json=data, headers=headers)
        
        if response.status_code in [200, 201]:
            return True, "✅ Commitado com sucesso no GitHub!"
        else:
            return False, f"❌ Erro ao commitar: {response.json()}"
    
    except Exception as e:
        return False, f"❌ Erro: {str(e)}"

# ✅ FUNÇÃO: Carregar config do cliente
def load_client_config(cliente):
    """Carrega a configuração do cliente"""
    config_path = f"{CONFIGS_DIR}/{cliente}.json"
    
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return None

# ✅ FUNÇÃO: Salvar config do cliente
def save_client_config(cliente, config):
    """Salva a configuração do cliente"""
    config_path = f"{CONFIGS_DIR}/{cliente}.json"
    
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

# ✅ OBTER CLIENTE DA URL
cliente = st.query_params.get("cliente", "paix").lower()
template = st.query_params.get("template", "design").lower()

# ✅ CARREGAR CONFIG
config = load_client_config(cliente)

if config is None:
    st.error(f"❌ Cliente '{cliente}' não encontrado!")
    st.stop()

# ✅ BOTÃO DE EDIÇÃO (Canto superior direito)
col1, col2, col3 = st.columns([1, 1, 0.1])
with col3:
    if st.button("✏️", key="edit_btn", help="Editar site"):
        st.session_state.editing = True

# ✅ PAINEL DE EDIÇÃO
if st.session_state.get("editing"):
    st.markdown("---")
    st.markdown("## ✏️ EDITOR DE SITE")
    
    with st.form("edit_form"):
        st.markdown("### 🎨 Configurações Gerais")
        config["page_title"] = st.text_input("Título da Página", config.get("page_title", ""))
        config["logo"] = st.text_input("Logo/Marca", config.get("logo", ""))
        
        st.markdown("### 🚀 Hero Section")
        config["hero"]["subtitle"] = st.text_input("Subtítulo", config.get("hero", {}).get("subtitle", ""))
        config["hero"]["title"] = st.text_area("Título Principal", config.get("hero", {}).get("title", ""), height=100)
        config["hero"]["description"] = st.text_area("Descrição", config.get("hero", {}).get("description", ""), height=100)
        
        st.markdown("### 📍 Navegação")
        for i, link in enumerate(config.get("nav_links", [])):
            col1, col2 = st.columns(2)
            with col1:
                link["name"] = st.text_input(f"Nome Link {i+1}", link.get("name", ""), key=f"nav_name_{i}")
            with col2:
                link["url"] = st.text_input(f"URL Link {i+1}", link.get("url", ""), key=f"nav_url_{i}")
        
        st.markdown("### 📝 Conteúdo Adicional")
        if "projects" in config:
            st.write("**Projetos:**")
            for i, project in enumerate(config.get("projects", [])):
                with st.expander(f"Projeto {i+1}"):
                    project["title"] = st.text_input(f"Título Projeto {i+1}", project.get("title", ""), key=f"proj_title_{i}")
                    project["location"] = st.text_input(f"Localização {i+1}", project.get("location", ""), key=f"proj_loc_{i}")
                    project["year"] = st.text_input(f"Ano {i+1}", project.get("year", ""), key=f"proj_year_{i}")
                    project["image"] = st.text_input(f"URL Imagem {i+1}", project.get("image", ""), key=f"proj_img_{i}")
        
        if "products" in config:
            st.write("**Produtos:**")
            for i, product in enumerate(config.get("products", [])):
                with st.expander(f"Produto {i+1}"):
                    product["title"] = st.text_input(f"Título Produto {i+1}", product.get("title", ""), key=f"prod_title_{i}")
                    product["category"] = st.text_input(f"Categoria {i+1}", product.get("category", ""), key=f"prod_cat_{i}")
                    product["description"] = st.text_area(f"Descrição {i+1}", product.get("description", ""), key=f"prod_desc_{i}")
                    product["image"] = st.text_input(f"URL Imagem {i+1}", product.get("image", ""), key=f"prod_img_{i}")
        
        st.markdown("### 📞 Rodapé")
        if "footer" in config:
            config["footer"]["company"] = st.text_input("Empresa", config.get("footer", {}).get("company", ""))
            config["footer"]["email"] = st.text_input("Email", config.get("footer", {}).get("email", ""))
        
        st.markdown("---")
        
        # ✅ BOTÃO SALVAR
        if st.form_submit_button("💾 SALVAR E COMMITAR", use_container_width=True):
            # Salvar localmente
            save_client_config(cliente, config)
            
            # Commitar no GitHub
            arquivo = f"{CONFIGS_DIR}/{cliente}.json"
            mensagem = f"Atualizar configurações de {cliente} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            
            sucesso, mensagem_commit = commit_to_github(arquivo, mensagem)
            
            if sucesso:
                st.success(mensagem_commit)
                st.session_state.editing = False
                st.rerun()
            else:
                st.error(mensagem_commit)
    
    st.markdown("---")

# ✅ ============================================
# ✅ RENDERIZAR TEMPLATE BASEADO NO CLIENTE
# ✅ ============================================

if template == "design":
    # ✅ TEMPLATE PAIX (Design Minimalista)
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');

        .stApp {{
            background-color: #f7f7f7;
            color: #1a1a1a;
        }}
        
        [data-testid="stHeader"] {{ display: none; }}
        .block-container {{ padding: 0 !important; max-width: 100% !important; }}

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            font-weight: 200;
            letter-spacing: 0.05em;
        }}

        h1, h2, .serif-light {{
            font-family: 'Cormorant Garamond', serif;
            font-weight: 300;
            font-size: 48px;
            line-height: 1.1;
        }}

        .nav-paix {{
            display: flex;
            justify-content: space-between;
            padding: 50px 5%;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 3px;
        }}

        .nav-link {{
            color: #1a1a1a !important;
            text-decoration: none !important;
            transition: 0.3s;
            cursor: pointer;
        }}

        .nav-link:hover {{
            opacity: 0.6;
            text-decoration: none !important;
        }}

        .hero-paix {{
            padding: 100px 5% 150px 5%;
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            gap: 100px;
        }}

        .project-section {{
            padding: 0 5% 200px 5%;
        }}

        .project-card {{
            margin-bottom: 250px;
            transition: opacity 0.6s ease;
        }}
        
        .project-img {{
            width: 100%;
            filter: grayscale(10%) contrast(1.05);
            margin-bottom: 25px;
        }}

        .project-title {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 32px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 15px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .project-year {{
            font-size: 10px;
            font-family: 'Inter', sans-serif;
            letter-spacing: 2px;
            color: #888;
        }}

        .action-button {{
            display: inline-block !important;
            background: #1a1a1a !important;
            color: #f7f7f7 !important;
            border: none !important;
            padding: 12px 30px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 400 !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            text-decoration: none !important;
            font-size: 10px !important;
            transition: 0.3s !important;
            cursor: pointer !important;
        }}

        .action-button:hover {{
            background-color: #333 !important;
            color: #f7f7f7 !important;
            text-decoration: none !important;
        }}

        .footer-paix {{
            padding: 100px 5%;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            letter-spacing: 2px;
            color: #666;
        }}
    </style>
    """, unsafe_allow_html=True)

    # ✅ NAVEGAÇÃO
    st.markdown(f"""
    <div class="nav-paix">
        <div style="font-weight: 400;">{config.get('logo', 'PAIX DESIGN')}</div>
        <div style="display: flex; gap: 50px;">
    """, unsafe_allow_html=True)
    
    for link in config.get("nav_links", []):
        st.markdown(f'<a href="{link.get("url", "#")}" class="nav-link">{link.get("name", "")}</a>', unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

    # ✅ HERO SECTION
    st.markdown(f"""
    <div class="hero-paix">
        <div>
            <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #888; margin-bottom: 30px;">
                {config.get('hero', {}).get('subtitle', '')}
            </p>
            <h1 class="serif-light">
                {config.get('hero', {}).get('title', '')}
            </h1>
        </div>
        <div style="font-size: 16px; line-height: 1.8; padding-top: 10px; color: #555;">
            {config.get('hero', {}).get('description', '')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ✅ PROJETOS
    st.markdown('<div id="projetos" class="project-section">', unsafe_allow_html=True)
    
    for project in config.get("projects", []):
        st.markdown(f"""
        <div class="project-card">
            <img src="{project.get('image', '')}" class="project-img">
            <div class="project-title">
                <span>{project.get('title', '')} — {project.get('location', '')}</span>
                <span class="project-year">{project.get('year', '')}</span>
            </div>
            <p style="font-size: 12px; color: #999; text-transform: uppercase; letter-spacing: 1px;">
                Residencial / Design de Mobiliário
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ SOBRE
    st.markdown(f"""
    <div id="escritorio" style="padding: 150px 20% 250px 20%; text-align: center;">
        <h2 class="serif-light" style="font-size: 56px; margin-bottom: 40px;">Atmosferas Tangíveis</h2>
        <p style="color: #666; line-height: 2;">
            Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, 
            desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente.
        </p>
        <div style="margin-top: 60px;">
            <a href="https://www.google.com/" target="_blank" class="action-button">Conheça Nosso Trabalho</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ✅ FOOTER
    st.markdown(f"""
    <div id="contato" class="footer-paix">
        <div>
            {config.get('footer', {}).get('company', 'PAIX DESIGN STUDIO')}<br>
            {config.get('footer', {}).get('address', 'AVENIDA DA LIBERDADE, LISBOA')}
        </div>
        <div style="text-align: right;">
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">INSTAGRAM</a> / 
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">BEHANCE</a> / 
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">LINKEDIN</a><br>
            <a href="mailto:{config.get('footer', {}).get('email', 'hello@paix-design.com')}" style="color: #666; text-decoration: none;">{config.get('footer', {}).get('email', 'hello@paix-design.com')}</a>
        </div>
    </div>
    <div style="padding: 30px 5%; font-size: 9px; color: #bbb; letter-spacing: 1px;">
        © 2026 {config.get('footer', {}).get('company', 'PAIX DESIGN')}. TODOS OS DIREITOS RESERVADOS.
    </div>
    """, unsafe_allow_html=True)

elif template == "beauty":
    # ✅ TEMPLATE YOLU (Noturno/Beauty)
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300&family=Noto+Sans+JP:wght@100;300;400&display=swap');

        .stApp {{
            background: linear-gradient(180deg, #050a14 0%, #0f1c3d 50%, #1e1b4b 100%);
            color: #ffffff;
        }}

        html, body, [class*="css"] {{
            font-family: 'Noto Sans JP', sans-serif;
            font-weight: 300;
        }}

        h1, h2, .serif-yolu {{
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-weight: 300;
            letter-spacing: 2px;
        }}

        .nav-yolu {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 6%;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(5, 10, 20, 0.4);
            backdrop-filter: blur(8px);
        }}
        
        .logo-yolu {{
            font-size: 28px;
            letter-spacing: 5px;
            font-weight: 400;
        }}

        .nav-link {{
            color: #ffffff !important;
            text-decoration: none !important;
            font-size: 11px;
            letter-spacing: 1px;
            transition: 0.3s;
            cursor: pointer;
        }}

        .nav-link:hover {{
            opacity: 0.6;
            text-decoration: none !important;
        }}

        .hero-yolu {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600');
            background-size: cover;
            background-position: center;
            position: relative;
        }}
        
        .hero-title-main {{
            font-size: clamp(40px, 8vw, 100px);
            line-height: 1;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }}

        .product-section {{
            padding: 100px 6%;
        }}

        .product-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0px;
            padding: 40px;
            text-align: center;
            transition: 0.5s;
        }}
        
        .product-card:hover {{
            background: rgba(255, 255, 255, 0.07);
            border-color: rgba(212, 175, 55, 0.5);
        }}

        .btn-yolu {{
            display: inline-block !important;
            padding: 12px 40px !important;
            border: 1px solid #fff !important;
            color: #fff !important;
            text-decoration: none !important;
            font-size: 12px !important;
            letter-spacing: 2px !important;
            margin-top: 20px !important;
            transition: 0.3s !important;
        }}
        
        .btn-yolu:hover {{
            background: #fff !important;
            color: #050a14 !important;
            text-decoration: none !important;
        }}

        [data-testid="stHeader"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

    # ✅ NAVEGAÇÃO
    st.markdown(f"""
    <div class="nav-yolu">
        <div class="logo-yolu">{config.get('logo', 'YOLU')}</div>
        <div style="display: flex; gap: 40px;">
    """, unsafe_allow_html=True)
    
    for link in config.get("nav_links", []):
        st.markdown(f'<a href="{link.get("url", "#")}" class="nav-link">{link.get("name", "")}</a>', unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

    # ✅ HERO
    st.markdown(f"""
    <div class="hero-yolu">
        <p style="letter-spacing: 8px; font-size: 12px; margin-bottom: 30px;">{config.get('hero', {}).get('subtitle', '')}</p>
        <h1 class="hero-title-main serif-yolu">{config.get('hero', {}).get('title', '')}</h1>
        <p style="max-width: 600px; font-size: 14px; opacity: 0.8; line-height: 2;">
            {config.get('hero', {}).get('description', '')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ CONCEITO
    st.markdown(f"""
    <div id="conceito" style="padding: 150px 15%; text-align: center;">
        <h2 class="serif-yolu" style="font-size: 42px; margin-bottom: 40px;">Por que Cuidados Noturnos?</h2>
        <p style="font-size: 16px; line-height: 2.2; opacity: 0.7;">
            Durante a noite, o seu cabelo está livre das agressões externas do dia. 
            É o momento perfeito para a penetração intensa de nutrientes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ PRODUTOS
    st.markdown('<div id="produtos" class="product-section">', unsafe_allow_html=True)
    
    cols = st.columns(len(config.get("products", [])))
    
    for idx, product in enumerate(config.get("products", [])):
        with cols[idx]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{product.get('image', '')}" style="width:100%; margin-bottom:30px; opacity:0.9;">
                <h3 class="serif-yolu" style="font-size: 28px;">{product.get('title', '')}</h3>
                <p style="font-size: 12px; color: #aaa; margin: 20px 0;">{product.get('category', '')}</p>
                <p style="font-size: 14px; line-height: 1.8;">{product.get('description', '')}</p>
                <a href="https://www.google.com/" target="_blank" class="btn-yolu">SAIBA MAIS</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ FOOTER
    st.markdown(f"""
    <div id="contato" style="padding: 100px 6% 40px 6%; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 100px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <h2 class="logo-yolu" style="margin-bottom: 20px;">{config.get('footer', {}).get('company', 'YOLU')}</h2>
                <p style="font-size: 11px; opacity: 0.5;">© 2026 {config.get('footer', {}).get('company', 'YOLU')} | Todos os direitos reservados.</p>
            </div>
            <div style="text-align: right; font-size: 11px; letter-spacing: 2px;">
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">INSTAGRAM</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">TWITTER</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">REVIEWS</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error(f"❌ Template '{template}' não encontrado!")
