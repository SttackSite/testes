import streamlit as st
import json
import os
from datetime import datetime

# ✅ CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Sttack Site - Editor",
    page_icon="💎",
    layout="wide"
)

# ✅ Carregar configurações do config.json
CONFIG_FILE = "config.json"

def load_config():
    """✅ Carrega as configurações do arquivo config.json"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_config_to_file(config):
    """✅ Salva as configurações em config.json"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

# ✅ Inicializar session_state com config
if "config" not in st.session_state:
    st.session_state.config = load_config()

config = st.session_state.config

# ✅ CSS RADICAL (PLUNDER + DOCKYARD + QUDRIX)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');

    :root {{
        --accent: {config.get('colors', {}).get('accent', '#7b2cbf')};
        --gold: {config.get('colors', {}).get('gold', '#d4af37')};
        --dark: {config.get('colors', {}).get('dark', '#050505')};
        --glass: {config.get('colors', {}).get('glass', 'rgba(255, 255, 255, 0.03)')};
    }}

    .stApp {{
        background-color: var(--dark);
        color: #ffffff;
    }}
    
    [data-testid="stHeader"] {{ display: none; }}
    .block-container {{ padding: 0 !important; max-width: 100% !important; }}

    /* Tipografia de Impacto Brutalista */
    h1, h2 {{
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -3px;
        line-height: 0.85;
    }}

    .serif-heavy {{
        font-family: 'Playfair Display', serif;
        font-style: italic;
        text-transform: none;
        letter-spacing: -1px;
    }}

    /* ❌ NÃO ALTERE: NAVBAR ESTILO YOLU ADAPTADO PARA SITE STTACK */
    .navbar-elite {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25px 8%;
        background: rgba(5, 5, 5, 0.5);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        width: 100%;
        box-sizing: border-box;
    }}
    
    /* ❌ NÃO ALTERE: Logo da navbar */
    .logo-elite {{
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        font-family: 'Inter', sans-serif;
        color: var(--gold);
        text-transform: uppercase;
    }}

    /* ❌ NÃO ALTERE: Container de links de navegação */
    .nav-links-container {{
        display: flex;
        gap: 45px;
        align-items: center;
    }}

    /* ❌ NÃO ALTERE: Links de navegação */
    .nav-link-elite {{
        color: #ffffff !important;
        text-decoration: none !important;
        font-size: 12px;
        letter-spacing: 1px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        cursor: pointer;
        text-transform: uppercase;
    }}

    /* ❌ NÃO ALTERE: Efeito hover nos links */
    .nav-link-elite:hover {{
        color: var(--gold) !important;
        text-decoration: none !important;
    }}

    .nav-link-elite:visited {{
        color: #ffffff !important;
        text-decoration: none !important;
    }}

    /* 1 & 2. HERO RADICAL */
    .hero-section {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 8%;
        background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .hero-h1 {{ font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }}
    .hero-sub {{ 
        font-size: 24px; 
        max-width: 600px; 
        line-height: 1.4; 
        color: rgba(255,255,255,0.7);
        border-left: 4px solid var(--accent);
        padding-left: 20px;
    }}

    /* 3 & 4. TEMPLATES SHOWCASE (ASSIMÉTRICO) */
    .template-box {{
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        background: var(--glass);
        transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        cursor: crosshair;
    }}
    .template-box:hover {{
        background: rgba(255,255,255,0.07);
        border-color: var(--gold);
        transform: translateY(-10px);
    }}
    .template-label {{
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
    }}

    /* GRID 2D COM SCROLL HORIZONTAL E VERTICAL */
    .carousel-section {{
        padding: 120px 8%;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%);
    }}

    .carousel-title {{
        text-align: center;
        font-size: 48px;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        margin-bottom: 60px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -2px;
    }}

    /* ❌ NÃO ALTERE: Container principal com scroll 2D */
    .carousel-container {{
        display: flex;
        gap: 20px;
        overflow-x: auto;
        overflow-y: hidden;
        padding: 20px 0;
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--gold) transparent;
        height: 900px;
    }}

    .carousel-container::-webkit-scrollbar {{
        height: 8px;
    }}

    .carousel-container::-webkit-scrollbar-track {{
        background: transparent;
    }}

    .carousel-container::-webkit-scrollbar-thumb {{
        background: var(--gold);
        border-radius: 4px;
    }}

    /* ❌ NÃO ALTERE: Container de cada template com scroll vertical */
    .carousel-item-image-only {{
        flex: 0 0 800px;
        min-width: 800px;
        height: 900px;
        border-radius: 8px;
        overflow-y: auto;
        overflow-x: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
        background: rgba(255, 255, 255, 0.02);
    }}

    .carousel-item-image-only:hover {{
        border-color: var(--gold);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }}

    .carousel-item-image-only::-webkit-scrollbar {{
        width: 6px;
    }}

    .carousel-item-image-only::-webkit-scrollbar-track {{
        background: transparent;
    }}

    .carousel-item-image-only::-webkit-scrollbar-thumb {{
        background: var(--gold);
        border-radius: 3px;
    }}

    .carousel-item-image-only img {{
        width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
        border-radius: 8px;
    }}

    /* 5. CLIENTS (FLOATING AVATARS) */
    .client-section {{
        padding: 100px 8%;
        background: #0a0a0a;
        display: flex;
        align-items: center;
        gap: 50px;
    }}

    /* 6. É PARA VOCÊ QUE (CARDS NEO-BRUTALISTAS) */
    .target-card {{
        padding: 50px;
        background: white;
        color: black;
        border: 5px solid var(--accent);
        box-shadow: 15px 15px 0px var(--accent);
        height: 100%;
    }}

    /* 7. PASSO A PASSO (VERTICAL & BOLD) */
    .step-row {{
        display: flex;
        gap: 30px;
        margin-bottom: 60px;
        align-items: flex-start;
    }}
    .step-num {{
        font-size: 100px;
        font-weight: 900;
        color: transparent;
        -webkit-text-stroke: 1px rgba(255,255,255,0.3);
        line-height: 0.7;
    }}

    /* 8. PREÇOS (GLASSMORPHISM) */
    .pricing-glass {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px 40px;
        border-radius: 2px;
        text-align: center;
    }}
    .pricing-glass:hover {{
        border-color: var(--accent);
    }}

    /* Botão de Alta Conversão */
    div.stButton > button {{
        background: linear-gradient(90deg, var(--accent), #9d4edd);
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
    }}
    div.stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.5);
    }}

    /* ❌ NÃO ALTERE: FAQ Destacado - Política de Reembolso */
    .faq-highlighted {{
        background: linear-gradient(135deg, rgba(123, 44, 191, 0.2) 0%, rgba(212, 175, 55, 0.1) 100%);
        border: 2px solid var(--gold);
        border-radius: 8px;
        padding: 40px;
        margin-bottom: 40px;
        box-shadow: 0 10px 50px rgba(212, 175, 55, 0.2);
    }}

    /* ❌ NÃO ALTERE: Título do FAQ Destacado */
    .faq-highlighted-title {{
        color: var(--gold);
        font-size: 24px;
        font-weight: 900;
        font-family: 'Inter', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}

    /* ❌ NÃO ALTERE: Conteúdo do FAQ Destacado */
    .faq-highlighted-content {{
        color: #ffffff;
        font-size: 14px;
        line-height: 1.8;
        font-family: 'Inter', sans-serif;
    }}

    /* ❌ NÃO ALTERE: Ícone de atenção */
    .faq-highlight-icon {{
        font-size: 28px;
        margin-right: 10px;
        color: var(--gold);
    }}

    /* PAINEL DE EDIÇÃO */
    .editor-panel {{
        position: fixed;
        right: 0;
        top: 0;
        width: 400px;
        height: 100vh;
        background: rgba(10, 10, 10, 0.95);
        border-left: 2px solid var(--gold);
        overflow-y: auto;
        padding: 20px;
        z-index: 1000;
    }}

    .editor-panel h3 {{
        color: var(--gold);
        margin-bottom: 15px;
        font-size: 18px;
    }}

    .editor-input {{
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid var(--gold);
        color: white;
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
    }}

    .editor-input::placeholder {{
        color: rgba(255, 255, 255, 0.5);
    }}

    .editor-button {{
        width: 100%;
        padding: 12px;
        background: var(--accent);
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: 900;
        cursor: pointer;
        margin-top: 10px;
        transition: 0.3s;
    }}

    .editor-button:hover {{
        background: var(--gold);
        color: black;
    }}

    .main-content {{
        margin-right: 420px;
    }}
</style>
""", unsafe_allow_html=True)

# ✅ NAVBAR
st.markdown(f"""
<div class="navbar-elite">
    <div class="logo-elite">{config.get('navbar', {}).get('logo', 'STTACK')}</div>
    <div class="nav-links-container">
        <a href="#quem-atendemos" class="nav-link-elite">Quem Atendemos</a>
        <a href="#como-funciona" class="nav-link-elite">Como Funciona</a>
        <a href="#templates" class="nav-link-elite">Templates</a>
        <a href="#precos" class="nav-link-elite">Preços</a>
        <a href="#faq" class="nav-link-elite">FAQ</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ✅ PAINEL DE EDIÇÃO (SIDEBAR)
st.sidebar.markdown("## ✏️ EDITOR DE SITE")
st.sidebar.markdown("---")

# ✅ Seção: Cores
st.sidebar.markdown("### 🎨 Cores")
new_accent = st.sidebar.color_picker("Cor Accent (Roxo)", config.get('colors', {}).get('accent', '#7b2cbf'))
new_gold = st.sidebar.color_picker("Cor Gold", config.get('colors', {}).get('gold', '#d4af37'))

# ✅ Seção: Hero
st.sidebar.markdown("### 🚀 Hero Section")
hero_title = st.sidebar.text_input("Título Principal", config.get('hero', {}).get('title', ''))
hero_subtitle = st.sidebar.text_area("Subtítulo", config.get('hero', {}).get('subtitle', ''), height=80)

# ✅ Seção: Navbar
st.sidebar.markdown("### 📍 Navbar")
navbar_logo = st.sidebar.text_input("Logo", config.get('navbar', {}).get('logo', 'STTACK'))

# ✅ Seção: Links de Navegação
st.sidebar.markdown("### 🔗 Links de Navegação")
for i, link in enumerate(config.get('navbar', {}).get('links', [])):
    col1, col2 = st.sidebar.columns(2)
    with col1:
        link['name'] = st.text_input(f"Nome Link {i+1}", link.get('name', ''), key=f"link_name_{i}")
    with col2:
        link['url'] = st.text_input(f"URL Link {i+1}", link.get('url', ''), key=f"link_url_{i}")

# ✅ Seção: Títulos das Seções
st.sidebar.markdown("### 📝 Títulos das Seções")
carousel_title = st.sidebar.text_input("Título Carousel", config.get('sections', {}).get('carousel_title', 'TEMPLATES DISPONÍVEIS'))
target_title = st.sidebar.text_input("Título Alvo", config.get('sections', {}).get('target_title', 'É PARA VOCÊ QUE'))
steps_title = st.sidebar.text_input("Título Passos", config.get('sections', {}).get('steps_title', 'COMO FUNCIONA'))
pricing_title = st.sidebar.text_input("Título Preços", config.get('sections', {}).get('pricing_title', 'PLANOS'))
faq_title = st.sidebar.text_input("Título FAQ", config.get('sections', {}).get('faq_title', 'PERGUNTAS FREQUENTES'))

# ✅ Seção: Botões CTA
st.sidebar.markdown("### 🔘 Botões Principais")
cta_main_text = st.sidebar.text_input("Texto CTA Principal", config.get('buttons', {}).get('cta_main', {}).get('text', 'COMECE AGORA'))
cta_main_url = st.sidebar.text_input("URL CTA Principal", config.get('buttons', {}).get('cta_main', {}).get('url', 'https://www.google.com/'))

# ✅ BOTÃO SALVAR
st.sidebar.markdown("---")
if st.sidebar.button("💾 SALVAR CONFIGURAÇÕES", use_container_width=True):
    # ✅ Atualizar config com valores editados
    config['colors']['accent'] = new_accent
    config['colors']['gold'] = new_gold
    config['hero']['title'] = hero_title
    config['hero']['subtitle'] = hero_subtitle
    config['navbar']['logo'] = navbar_logo
    config['sections']['carousel_title'] = carousel_title
    config['sections']['target_title'] = target_title
    config['sections']['steps_title'] = steps_title
    config['sections']['pricing_title'] = pricing_title
    config['sections']['faq_title'] = faq_title
    config['buttons']['cta_main']['text'] = cta_main_text
    config['buttons']['cta_main']['url'] = cta_main_url
    
    # ✅ Salvar em arquivo
    save_config_to_file(config)
    st.session_state.config = config
    
    st.sidebar.success("✅ Configurações salvas em config.json!")
    st.sidebar.info(f"Salvo em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# ✅ CONTEÚDO PRINCIPAL
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ✅ 1 & 2. HERO SECTION
st.markdown(f"""
<div class="hero-section">
    <h1 class="hero-h1">{hero_title}<br><span class="serif-heavy" style="color:{new_gold}">Apenas editando templates prontos.</span></h1>
    <p class="hero-sub">{hero_subtitle}</p>
    <div style="margin-top: 50px; width: 300px;">
""", unsafe_allow_html=True)
st.markdown(f"""
<a href="#templates" style="display: inline-block; background: linear-gradient(90deg, {new_accent}, #9d4edd); color: white; border: none; padding: 25px 60px; font-weight: 900; font-size: 22px; text-transform: uppercase; letter-spacing: 2px; border-radius: 0; clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%); text-decoration: none; transition: 0.4s; cursor: pointer;">{cta_main_text} ↓</a>
""", unsafe_allow_html=True)

# ✅ 5. PROVA SOCIAL (AVATARES FLOATING)
st.markdown("""
<div id="clientes" class="client-section">
    <h2 style="font-size: 30px; letter-spacing: 0px;">CONFIE EM QUEM<br>JÁ DOMINA.</h2>
    <div style="display: flex;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/7.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/8.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/6.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/17.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/site/main/410.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/site/main/413.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/site/main/414.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/site/main/415.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/SttackSite/site/main/422.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <div style="width:80px; height:80px; border-radius:50%; background: var(--accent); margin-left: -20px; display:flex; align-items:center; justify-content:center; font-weight:900;">+500</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ✅ 6. É PARA VOCÊ QUE
st.markdown('<div id="quem-atendemos" style="padding: 120px 8%;">', unsafe_allow_html=True)
st.markdown(f'<h2>{target_title}</h2>', unsafe_allow_html=True)
col_u1, col_u2, col_u3 = st.columns(3)

target_cards = config.get('sections', {}).get('target_cards', [])
with col_u1:
    st.markdown(f"""
    <div class="target-card">
        <h3>{target_cards[0].get('title', 'Proprietários de negócios')}</h3>
        <p>{target_cards[0].get('description', '')}</p>
    </div>
    """, unsafe_allow_html=True)

with col_u2:
    st.markdown(f"""
    <div class="target-card" style="background: var(--accent); color: white; box-shadow: 15px 15px 0px white;">
        <h3>{target_cards[1].get('title', 'Infoprodutores')}</h3>
        <p>{target_cards[1].get('description', '')}</p>
    </div>
    """, unsafe_allow_html=True)

with col_u3:
    st.markdown(f"""
    <div class="target-card">
        <h3>{target_cards[2].get('title', 'Freelancer')}</h3>
        <p>{target_cards[2].get('description', '')}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ 7. PASSO A PASSO
st.markdown(f'<div id="como-funciona" style="padding: 100px 8%; background: #050505;"><h2>{steps_title}</h2><br><br>', unsafe_allow_html=True)

steps = config.get('sections', {}).get('steps', [])
for i, step in enumerate(steps):
    st.markdown(f"""
    <div class="step-row">
        <div class="step-num">0{i+1}</div>
        <div>
            <h3 style="color: var(--gold);">{step.get('title', '')}</h3>
            <p style="max-width: 400px; opacity: 0.6;">{step.get('description', '')}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ 3 & 4. SHOWCASE DE TEMPLATES
st.markdown(f'<div id="templates" style="padding: 120px 8%;"><h2>{carousel_title}</h2><br><br>', unsafe_allow_html=True)
st.markdown("""
<div class="carousel-section" style="padding: 0; background: transparent;">
    <div class="carousel-container">
        <a href="#precos" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/20.png" alt="Template 1"></div></a>
        <a href="#precos" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/17.png" alt="Template 2"></div></a>
        <a href="#precos" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/24.png" alt="Template 3"></div></a>
        <a href="#precos" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/11.png" alt="Template 4"></div></a>
        <a href="#precos" style="text-decoration: none;"><div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/22.png" alt="Template 5"></div></a>
    </div>
</div>
""", unsafe_allow_html=True)

# ✅ 8. PREÇOS
st.markdown(f'<div id="precos" style="padding: 120px 8%; text-align:center;"><h2>{pricing_title}</h2><br><br>', unsafe_allow_html=True)

pricing_plans = config.get('sections', {}).get('pricing_plans', [])
p1, p2, p3 = st.columns(3)

with p2:
    st.markdown(f"""
    <div class="pricing-glass" style="border-top: 5px solid var(--accent);">
        <p style="color: var(--gold); letter-spacing: 3px; font-weight: 900;">{pricing_plans[1].get('name', 'PRO')}</p>
        <h1 style="font-size: 80px; margin: 30px 0;">{pricing_plans[1].get('price', 'R$ 197')}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.button(pricing_plans[1].get('button_text', 'QUERO AGORA'), key="main_p")

with p1:
    st.markdown(f"""
    <div class="pricing-glass">
        <p>{pricing_plans[0].get('name', 'STARTER')}</p>
        <h1 style="font-size: 60px; margin: 30px 0;">{pricing_plans[0].get('price', 'R$ 97')}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.button(pricing_plans[0].get('button_text', 'INICIAR'), key="p1")

with p3:
    st.markdown(f"""
    <div class="pricing-glass">
        <p>{pricing_plans[2].get('name', 'ENTERPRISE')}</p>
        <h1 style="font-size: 60px; margin: 30px 0;">{pricing_plans[2].get('price', 'Sob Consulta')}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.button(pricing_plans[2].get('button_text', 'FALAR COM VENDAS'), key="p3")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ 9. FAQ
st.markdown(f'<div id="faq" style="padding: 100px 20%; background: #080808;"><h2 style="text-align:center; font-size: 40px;">{faq_title}</h2><br>', unsafe_allow_html=True)

faq_items = config.get('sections', {}).get('faq_items', [])
for faq in faq_items:
    with st.expander(faq.get('question', '')):
        st.write(faq.get('answer', ''))

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
