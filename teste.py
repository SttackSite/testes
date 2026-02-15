import streamlit as st
import requests
import re

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- CSS RADICAL (PLUNDER + DOCKYARD + QUDRIX) + MODAL ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');

    :root {
        --accent: #7b2cbf; /* Roxo Profundo */
        --gold: #d4af37;
        --dark: #050505;
        --glass: rgba(255, 255, 255, 0.03);
    }

    .stApp {
        background-color: var(--dark);
        color: #ffffff;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia de Impacto Brutalista */
    h1, h2 {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -3px;
        line-height: 0.85;
    }

    .serif-heavy {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        text-transform: none;
        letter-spacing: -1px;
    }

    /* ❌ NÃO ALTERE: NAVBAR ESTILO YOLU ADAPTADO PARA SITE STTACK */
    .navbar-elite {
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
    
    /* ❌ NÃO ALTERE: Logo da navbar */
    .logo-elite {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        font-family: 'Inter', sans-serif;
        color: var(--gold);
        text-transform: uppercase;
    }

    /* ❌ NÃO ALTERE: Container de links de navegação */
    .nav-links-container {
        display: flex;
        gap: 45px;
        align-items: center;
    }

    /* ❌ NÃO ALTERE: Links de navegação */
    .nav-link-elite {
        color: #ffffff !important;
        text-decoration: none !important;
        font-size: 12px;
        letter-spacing: 1px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        cursor: pointer;
        text-transform: uppercase;
    }

    /* ❌ NÃO ALTERE: Efeito hover nos links */
    .nav-link-elite:hover {
        color: var(--gold) !important;
        text-decoration: none !important;
    }

    .nav-link-elite:visited {
        color: #ffffff !important;
        text-decoration: none !important;
    }

    /* 1 & 2. HERO RADICAL */
    .hero-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 8%;
        background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .hero-h1 { font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }
    .hero-sub { 
        font-size: 24px; 
        max-width: 600px; 
        line-height: 1.4; 
        color: rgba(255,255,255,0.7);
        border-left: 4px solid var(--accent);
        padding-left: 20px;
    }

    /* 3 & 4. TEMPLATES SHOWCASE (ASSIMÉTRICO) */
    .template-box {
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        background: var(--glass);
        transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        cursor: crosshair;
    }
    .template-box:hover {
        background: rgba(255,255,255,0.07);
        border-color: var(--gold);
        transform: translateY(-10px);
    }
    .template-label {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
    }

    /* CARROSSEL HORIZONTAL - APENAS IMAGENS GRANDES */
    .carousel-section {
        padding: 120px 8%;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%);
    }

    .carousel-title {
        text-align: center;
        font-size: 48px;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        margin-bottom: 60px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -2px;
    }

    .carousel-container {
        display: flex;
        gap: 40px;
        overflow-x: auto;
        padding: 20px 0;
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--gold) transparent;
    }

    .carousel-container::-webkit-scrollbar {
        height: 8px;
    }

    .carousel-container::-webkit-scrollbar-track {
        background: transparent;
    }

    .carousel-container::-webkit-scrollbar-thumb {
        background: var(--gold);
        border-radius: 4px;
    }

    /* ❌ NÃO ALTERE: Link do item do carrossel */
    .carousel-item-link {
        display: block;
        flex: 0 0 calc(33.333% - 27px);
        min-width: 705px;
        height: 315px;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
        text-decoration: none;
    }

    /* ❌ NÃO ALTERE: Efeito hover no link do carrossel */
    .carousel-item-link:hover {
        border-color: var(--gold);
        transform: translateY(-15px);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    .carousel-item-image-only {
        flex: 0 0 calc(33.333% - 27px);
        min-width: 705px;
        height: 315px;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
    }

    .carousel-item-image-only:hover {
        border-color: var(--gold);
        transform: translateY(-15px);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    .carousel-item-image-only img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        border-radius: 8px;
    }

    /* ❌ NÃO ALTERE: Imagem dentro do link */
    .carousel-item-link img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        border-radius: 8px;
    }

    /* 5. CLIENTS (FLOATING AVATARS) */
    .client-section {
        padding: 100px 8%;
        background: #0a0a0a;
        display: flex;
        align-items: center;
        gap: 50px;
    }

    /* 6. É PARA VOCÊ QUE (CARDS NEO-BRUTALISTAS) */
    .target-card {
        padding: 50px;
        background: white;
        color: black;
        border: 5px solid var(--accent);
        box-shadow: 15px 15px 0px var(--accent);
        height: 100%;
    }

    /* 7. PASSO A PASSO (VERTICAL & BOLD) */
    .step-row {
        display: flex;
        gap: 30px;
        margin-bottom: 60px;
        align-items: flex-start;
    }
    .step-num {
        font-size: 100px;
        font-weight: 900;
        color: transparent;
        -webkit-text-stroke: 1px rgba(255,255,255,0.3);
        line-height: 0.7;
    }

    /* 8. PREÇOS (GLASSMORPHISM) */
    .pricing-glass {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px 40px;
        border-radius: 2px;
        text-align: center;
    }
    .pricing-glass:hover {
        border-color: var(--accent);
    }

    /* Botão de Alta Conversão */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd);
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
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.5);
    }

    /* ❌ NÃO ALTERE: FAQ Destacado - Política de Reembolso */
    .faq-highlighted {
        background: linear-gradient(135deg, rgba(123, 44, 191, 0.2) 0%, rgba(212, 175, 55, 0.1) 100%);
        border: 2px solid var(--gold);
        border-radius: 8px;
        padding: 40px;
        margin-bottom: 40px;
        box-shadow: 0 10px 50px rgba(212, 175, 55, 0.2);
    }

    /* ❌ NÃO ALTERE: Título do FAQ Destacado */
    .faq-highlighted-title {
        color: var(--gold);
        font-size: 24px;
        font-weight: 900;
        font-family: 'Inter', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }

    /* ❌ NÃO ALTERE: Conteúdo do FAQ Destacado */
    .faq-highlighted-content {
        color: #ffffff;
        font-size: 14px;
        line-height: 1.8;
        font-family: 'Inter', sans-serif;
    }

    /* ❌ NÃO ALTERE: Ícone de atenção */
    .faq-highlight-icon {
        font-size: 28px;
        margin-right: 10px;
        color: var(--gold);
    }

    /* ✅ MODAL PARA VISUALIZAR TEMPLATES */
    .modal-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(5px);
        z-index: 9999;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }

    .modal-overlay.active {
        display: flex;
    }

    .modal-content {
        background: var(--dark);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        width: 90%;
        height: 90vh;
        max-width: 1200px;
        display: flex;
        flex-direction: column;
        position: relative;
        box-shadow: 0 50px 200px rgba(0, 0, 0, 0.9);
    }

    .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(5, 5, 5, 0.8);
    }

    .modal-close {
        background: none;
        border: none;
        color: var(--gold);
        font-size: 28px;
        cursor: pointer;
        transition: all 0.3s ease;
        padding: 0;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .modal-close:hover {
        transform: scale(1.2);
        color: #ffffff;
    }

    .modal-body {
        flex: 1;
        overflow-y: auto;
        padding: 0;
    }

    .modal-footer {
        display: flex;
        gap: 15px;
        padding: 25px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(5, 5, 5, 0.8);
        justify-content: center;
    }

    .modal-btn {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd);
        color: white;
        border: none;
        padding: 15px 40px;
        font-weight: 900;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 0;
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .modal-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.5);
    }

    .modal-btn-secondary {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid var(--gold);
        color: var(--gold);
    }

    .modal-btn-secondary:hover {
        background: rgba(212, 175, 55, 0.1);
    }

    /* Template iframe dentro do modal */
    .template-iframe {
        width: 100%;
        height: 100%;
        border: none;
        background: white;
    }
</style>
""", unsafe_allow_html=True)

# --- MODAL HTML ---
st.markdown("""
<div id="templateModal" class="modal-overlay">
    <div class="modal-content">
        <div class="modal-header">
            <div style="flex: 1;"></div>
            <button class="modal-close" onclick="closeTemplateModal()">✕</button>
        </div>
        <div class="modal-body" id="modalBody">
            <div style="display: flex; justify-content: center; align-items: center; height: 100%; color: #ccc;">
                Carregando template...
            </div>
        </div>
        <div class="modal-footer">
            <button class="modal-btn" onclick="goToPricing()">IR PARA PREÇOS</button>
            <button class="modal-btn modal-btn-secondary" onclick="closeTemplateModal()">FECHAR</button>
        </div>
    </div>
</div>

<script>
function openTemplateModal(templateNumber) {
    const modal = document.getElementById('templateModal');
    const modalBody = document.getElementById('modalBody');
    
    // Mostrar carregando
    modalBody.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; height: 100%; color: #ccc; font-size: 16px;">⏳ Carregando template ' + templateNumber + '...</div>';
    modal.classList.add('active');
    
    // Chamar Streamlit para carregar o template
    window.parent.postMessage({
        type: 'streamlit:setComponentValue',
        key: 'template_viewer',
        value: templateNumber
    }, '*');
}

function closeTemplateModal() {
    const modal = document.getElementById('templateModal');
    modal.classList.remove('active');
}

function goToPricing() {
    closeTemplateModal();
    document.getElementById('precos').scrollIntoView({ behavior: 'smooth' });
}

// Fechar modal ao clicar fora
document.addEventListener('click', function(event) {
    const modal = document.getElementById('templateModal');
    if (event.target === modal) {
        closeTemplateModal();
    }
});

// Fechar modal com ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeTemplateModal();
    }
});
</script>
""", unsafe_allow_html=True)

# --- NAVBAR ELITE ---
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

# --- 1 & 2. HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-h1">TEMPLATES PROFISSIONAIS PRONTOS PARA VENDER</h1>
    <p class="hero-sub">Acesso vitalício a 28 sites premium. Customize, publique e monetize em minutos. Sem conhecimento técnico necessário.</p>
</div>
""", unsafe_allow_html=True)

# --- CARROSSEL COM MODAL ---
st.markdown("""
<div class="carousel-section">
    <div class="carousel-title">CLIQUE E ESCOLHA O TEMPLATE</div>
    <div class="carousel-container">
        <a onclick="openTemplateModal(1)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/20.png" alt="Template 1">
        </a>
        <a onclick="openTemplateModal(2)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/17.png" alt="Template 2">
        </a>
        <a onclick="openTemplateModal(3)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/24.png" alt="Template 3">
        </a>
        <a onclick="openTemplateModal(4)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/11.png" alt="Template 4">
        </a>
        <a onclick="openTemplateModal(5)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/8.png" alt="Template 5">
        </a>
        <a onclick="openTemplateModal(6)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/14.png" alt="Template 6">
        </a>
        <a onclick="openTemplateModal(7)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/19.png" alt="Template 7">
        </a>
        <a onclick="openTemplateModal(8)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/3.png" alt="Template 8">
        </a>
        <a onclick="openTemplateModal(9)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/16.png" alt="Template 9">
        </a>
        <a onclick="openTemplateModal(10)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/2.png" alt="Template 10">
        </a>
        <a onclick="openTemplateModal(11)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/10.png" alt="Template 11">
        </a>
        <a onclick="openTemplateModal(12)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/13.png" alt="Template 12">
        </a>
        <a onclick="openTemplateModal(13)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/15.png" alt="Template 13">
        </a>
        <a onclick="openTemplateModal(14)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/1.png" alt="Template 14">
        </a>
        <a onclick="openTemplateModal(15)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/18.png" alt="Template 15">
        </a>
        <a onclick="openTemplateModal(16)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/21.png" alt="Template 16">
        </a>
        <a onclick="openTemplateModal(17)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/22.png" alt="Template 17">
        </a>
        <a onclick="openTemplateModal(18)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/26.png" alt="Template 18">
        </a>
        <a onclick="openTemplateModal(19)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/27.png" alt="Template 19">
        </a>
        <a onclick="openTemplateModal(20)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/28.png" alt="Template 20">
        </a>
        <a onclick="openTemplateModal(21)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/23.png" alt="Template 21">
        </a>
        <a onclick="openTemplateModal(22)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/25.png" alt="Template 22">
        </a>
        <a onclick="openTemplateModal(23)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/6.png" alt="Template 23">
        </a>
        <a onclick="openTemplateModal(24)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/12.png" alt="Template 24">
        </a>
        <a onclick="openTemplateModal(25)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/9.png" alt="Template 25">
        </a>
        <a onclick="openTemplateModal(26)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/5.png" alt="Template 26">
        </a>
        <a onclick="openTemplateModal(27)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/7.png" alt="Template 27">
        </a>
        <a onclick="openTemplateModal(28)" style="cursor: pointer;" class="carousel-item-link">
            <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/4.png" alt="Template 28">
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- LÓGICA PARA CARREGAR TEMPLATES ---
@st.cache_data(ttl=3600)
def load_template_code(template_number):
    """Carrega o código do template do GitHub"""
    try:
        url = f"https://raw.githubusercontent.com/SttackSite/template{template_number}/main/Template{template_number}.py"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Erro ao carregar template: {str(e)}"

# Coluna invisível para capturar cliques no modal
col_modal = st.columns([1])[0]

# Verificar se há um template selecionado
if 'selected_template' not in st.session_state:
    st.session_state.selected_template = None

# Sidebar invisível para capturar eventos
with st.sidebar:
    selected = st.number_input("Template Selecionado", value=0, key="template_selector", label_visibility="collapsed")
    if selected > 0 and selected != st.session_state.selected_template:
        st.session_state.selected_template = selected

# Se um template foi selecionado, mostrar no modal
if st.session_state.selected_template and st.session_state.selected_template > 0:
    template_code = load_template_code(st.session_state.selected_template)
    
    if "Erro" not in template_code:
        # Remover st.set_page_config() para evitar conflitos
        cleaned_code = re.sub(
            r'st\.set_page_config\([^)]*\)',
            '',
            template_code,
            flags=re.DOTALL
        )
        
        # Renderizar o template em um container
        st.markdown("""
        <script>
        document.getElementById('templateModal').classList.add('active');
        </script>
        """, unsafe_allow_html=True)

# --- 8. PREÇOS (ELITE) ---
st.markdown('<div id="precos" style="padding: 120px 8%; text-align:center;">', unsafe_allow_html=True)
st.markdown('<h2>INVISTA NA SUA <span class="serif-heavy">Presença.</span></h2><br><br>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p2: # Featured
    st.markdown("""
    <div class="pricing-glass" style="border-top: 5px solid var(--accent);">
        <p style="color: var(--gold); letter-spacing: 3px; font-weight: 900;">PROFESSIONAL</p>
        <h1 style="font-size: 80px; margin: 30px 0;">R$ 197</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ 02 consultorias mensais para customização</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Integração do seu site ao seu WhatsApp</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("QUERO O ELITE BUNDLE", key="main_p")

with p1:
    st.markdown("""
    <div class="pricing-glass">
        <p>STARTER</p>
        <h1 style="font-size: 60px; margin: 30px 0;">R$ 67</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ Pagamento único</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("INICIAR", key="p1")

with p3:
    st.markdown("""
    <div class="pricing-glass">
        <p>BUSINESS</p>
        <h1 style="font-size: 60px; margin: 30px 0;">R$ 297</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Licença comercial para revenda ilimitada</p>
        <p>✓ Selo de parceiro desenvolvedor</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("SER VITALÍCIO", key="p3")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div id="faq" style="padding: 100px 20%; background: #080808;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center; font-size: 40px;">FAQ / <span class="serif-heavy">Respostas.</span></h2><br>', unsafe_allow_html=True)

faq = {
    "Preciso saber programação para usar os templates?": "Não é preciso. O código é entregue pronto e você segue o nosso guia detalhado para personalizar os textos, cores, imagens e o que precisar.",
    "É seguro realizar a compra?": "Sim! Toda a compra é processada pela Eduzz, uma das plataformas de pagamentos e educação mais seguras e reconhecidas do Brasil. Nenhum dado sensível passa por nós, tudo ocorre diretamente no ambiente da Eduzz, com criptografia, certificados de segurança e antifraude.",
    "⚠️ POLÍTICA DE REEMBOLSO (LEIA COM ATENÇÃO)": """<strong style='color: var(--gold); font-size: 16px;'>Prazo Legal – 7 dias:</strong> Nos termos do Art. 49 do Código de Defesa do Consumidor, você pode solicitar reembolso em até 7 dias corridos após a compra realizada online. Respeitamos integralmente esse direito.<br><br>

<strong style='color: var(--gold); font-size: 16px;'>Proteção Legal do Produto:</strong> Nossos templates são produtos digitais protegidos pela Lei 9.610/98 (Lei de Direitos Autorais). O código-fonte possui rastreio ofuscado e constitui obra intelectual protegida por lei.<br><br>

<strong style='color: var(--gold); font-size: 16px;'>Condição para Reembolso:</strong> A solicitação de reembolso implica na interrupção imediata do uso do material adquirido, incluindo:<br>
- Remoção do código de qualquer repositório<br>
- Remoção do deploy em qualquer servidor na internet (site)<br>
- Interrupção total da utilização comercial ou pessoal<br><br>

<strong style='color: var(--gold); font-size: 16px;'>Uso Indevido Após Reembolso:</strong> A permanência do uso do código após o reembolso configura violação de direito autoral (Art. 184 do Código Penal), uso indevido de propriedade intelectual e possível enriquecimento ilícito.<br><br>

Reservamo-nos o direito de registrar evidências técnicas de utilização indevida.<br><br>

Clientes legítimos são sempre respeitados. Todos os casos de má-fé até aqui foram tratados conforme a legislação vigente.<br><br>""",
    "Existe algum tipo de suporte?": "Com certeza. Todos os planos incluem suporte humano ágil via e-mail e com o plano professional você tem direito a 2 consultorias mensais para customização.",
    "Por onde acesso os templates?": "O acesso é 100% digital e imediato. Após a confirmação do pagamento, você receberá um e-mail da Eduzz com seus dados de acesso à área de membros. Lá, você encontrará os arquivos de todos os templates, além dos guias de setup e explicações organizados por módulos.",
    "A hospedagem é mesmo gratuita?": "Sim. Nosso método utiliza infraestruturas globais de alta performance que permitem manter sites profissionais online sem mensalidades de hospedagem. No passo a passo, ensinamos como configurar essa estrutura gratuita de forma segura, garantindo que você tenha um site rápido e estável sem custos fixos recorrentes.",
    "Posso vender os sites para clientes?": "Com o plano Business, você tem licença comercial completa para lucrar com nossos designs."
}

for i, (q, a) in enumerate(faq.items()):
    if i == 0:  # Primeiro item (Política de Reembolso) com destaque
        with st.expander(q):
            st.markdown(f"<p style='color: var(--gold); font-size: 15px; font-weight: 600;'>{a}</p>", unsafe_allow_html=True)
    else:  # Demais itens normais
        with st.expander(q):
            st.markdown(f"<p style='color: #ccc;'>{a}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 60px 8%; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 10px; opacity: 0.4; letter-spacing: 5px;">
    STTACK SITE ® - DOMINANDO A WEB DESDE 2019. Todos os direitos reservados
</div>
""", unsafe_allow_html=True)
