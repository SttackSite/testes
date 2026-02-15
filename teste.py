import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sttack Site",
    page_icon="💎",
    layout="wide"
)

# --- CSS RADICAL (PLUNDER + DOCKYARD + QUDRIX) ---
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

    /* GRID 2D COM SCROLL HORIZONTAL E VERTICAL */
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

    /* ❌ NÃO ALTERE: Container principal com scroll 2D */
    .carousel-container {
        display: flex;
        gap: 20px;
        overflow-x: auto;
        overflow-y: hidden;
        padding: 20px 0;
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--gold) transparent;
        height: 900px;
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
        display: none;
    }

    /* ❌ NÃO ALTERE: Efeito hover no link do carrossel */
    .carousel-item-link:hover {
        border-color: var(--gold);
        transform: translateY(-15px);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    /* ❌ NÃO ALTERE: Container de cada template com scroll vertical */
    .carousel-item-image-only {
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
    }

    .carousel-item-image-only:hover {
        border-color: var(--gold);
        box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3);
    }

    /* ❌ NÃO ALTERE: Scrollbar vertical de cada template */
    .carousel-item-image-only::-webkit-scrollbar {
        width: 6px;
    }

    .carousel-item-image-only::-webkit-scrollbar-track {
        background: transparent;
    }

    .carousel-item-image-only::-webkit-scrollbar-thumb {
        background: var(--gold);
        border-radius: 3px;
    }

    .carousel-item-image-only img {
        width: 100%;
        height: auto;
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

    /* ✅ CONTAINER COM SCROLL VERTICAL PARA TEMPLATES */
    .template-scroll-container {
        width: 100%;
        max-width: 1000px;
        height: 800px;
        margin: 0 auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        overflow-y: scroll;
        overflow-x: hidden;
        background: rgba(255, 255, 255, 0.02);
        padding: 0;
        scroll-behavior: smooth;
    }

    /* ✅ SCROLLBAR ESTILIZADA */
    .template-scroll-container::-webkit-scrollbar {
        width: 12px;
    }

    .template-scroll-container::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }

    .template-scroll-container::-webkit-scrollbar-thumb {
        background: var(--gold);
        border-radius: 10px;
        border: 2px solid rgba(5, 5, 5, 0.5);
    }

    .template-scroll-container::-webkit-scrollbar-thumb:hover {
        background: #e8c547;
    }

    /* ✅ IMAGEM DENTRO DO CONTAINER */
    .template-scroll-image {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 0;
    }
</style>
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
    <h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates prontos.</span></h1>
    <p class="hero-sub">A solução ideal para quem precisa de um site rápido, profissional e editável sem depender de agências ou programadores.</p>
    <div style="margin-top: 50px; width: 300px;">
""", unsafe_allow_html=True)
st.markdown("""
<a href="#templates" style="display: inline-block; background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white; border: none; padding: 25px 60px; font-weight: 900; font-size: 22px; text-transform: uppercase; letter-spacing: 2px; border-radius: 0; clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%); text-decoration: none; transition: 0.4s; cursor: pointer;">CONHEÇA NOSSOS TEMPLATES ↓</a>
""", unsafe_allow_html=True)

# --- 5. PROVA SOCIAL (AVATARES FLOATING) ---
st.markdown("""
<div id="clientes" class="client-section">
    <h2 style="font-size: 30px; letter-spacing: 0px;">CONFIE EM QUEM<br>JÁ DOMINA.</h2>
    <div style="display: flex;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/7.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/8.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/6.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/17.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <div style="width:80px; height:80px; border-radius:50%; background: var(--accent); margin-left: -20px; display:flex; align-items:center; justify-content:center; font-weight:900;">+500</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown('<div id="quem-atendemos" style="padding: 120px 8%;">', unsafe_allow_html=True)
col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.markdown("""
    <div class="target-card">
        <h3>Proprietários de negócios</h3>
        <p>Que busca colocar sua empresa na internet com o menor custo do mercado, garantindo sua presença digital em minutos.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u2:
    st.markdown("""
    <div class="target-card" style="background: var(--accent); color: white; box-shadow: 15px 15px 0px white;">
        <h3>Infoprodutores/ prestadores de serviço</h3>
        <p>Temos estruturas otimizadas para converter visitantes em compradores reais. Destaque seus serviços com um design que transmite autoridade e confiança.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u3:
    st.markdown("""
    <div class="target-card">
        <h3>Freelancer</h3>
        <p>Venda nossos sites para seus clientes sem precisar programar do zero e fature com isso, aumentando sua margem de lucro entregando em tempo recorde.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PASSO A PASSO (INDUSTRIAL) ---
st.markdown('<div id="como-funciona" style="padding: 100px 8%; background: #050505;">', unsafe_allow_html=True)
st.markdown('<h2>PROCESSO <span class="serif-heavy">sem falhas.</span></h2><br><br>', unsafe_allow_html=True)

steps = [
    ("SELECIONE O MODELO IDEAL", "Escolha entre mais de 30 modelos validados o que mais combina com a identidade do seu negócio."),
    ("CUSTOMIZAÇÃO RÁPIDA", "Utilize nosso passo a passo detalhado para implementar o código e personalizar cada detalhe sem complicações."),
    ("SETUP TÉCNICO GRATUITO", "Te ensinamos onde hospedar seu site em segundos, como aplicar técnicas de SEO e configurar seu domínio personalizado sem custo adicional e de forma rápida."),
    ("LANÇAMENTO IMEDIATO", "Site no ar, otimizado e pronto para escalar seu negócio com uma estrutura de alta performance.")
]

for i, (title, desc) in enumerate(steps):
    st.markdown(f"""
    <div class="step-row">
        <div class="step-num">0{i+1}</div>
        <div>
            <h3 style="color: var(--gold);">{title}</h3>
            <p style="max-width: 400px; opacity: 0.6;">{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- 3 & 4. SHOWCASE DE TEMPLATES (GRID 2D COM SCROLL) ---
st.markdown('<div id="templates" style="padding: 120px 8%;">', unsafe_allow_html=True)
st.markdown('<h2>Clique e explore o template que mais combina com <span class="serif-heavy"> seu negócio:</span></h2><br><br>', unsafe_allow_html=True)
st.markdown("""
<div class="carousel-section" style="padding: 0; background: transparent;">
    <div class="carousel-container">
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/20.png" alt="Template 1"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/SttackSite/site/main/testeimagem1.png" alt="Template 2"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/24.png" alt="Template 3"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/11.png" alt="Template 4"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/22.png" alt="Template 5"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/13.png" alt="Template 6"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/1.png" alt="Template 7"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/21.png" alt="Template 8"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/26.png" alt="Template 9"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/18.png" alt="Template 10"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/14.png" alt="Template 11"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/16.png" alt="Template 12"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/10.png" alt="Template 13"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/8.png" alt="Template 14"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/15.png" alt="Template 15"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/3.png" alt="Template 16"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/27.png" alt="Template 17"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/2.png" alt="Template 18"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/19.png" alt="Template 19"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/28.png" alt="Template 20"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/23.png" alt="Template 21"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/25.png" alt="Template 22"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/6.png" alt="Template 23"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/12.png" alt="Template 24"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/9.png" alt="Template 25"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/5.png" alt="Template 26"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/7.png" alt="Template 27"></div>
        <div class="carousel-item-image-only"><img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/4.png" alt="Template 28"></div>
    </div>
</div>
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
