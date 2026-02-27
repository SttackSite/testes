import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Site Pro | Interstellar Templates",
    page_icon="🌌",
    layout="wide"
)

# --- CSS DE ULTRA FIDELIDADE (ESTILO STAR ATLAS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@300;500&family=Inter:wght@200;400;900&display=swap');

    :root {
        --cyan: #00f2ff;
        --magenta: #ff00ff;
        --deep-space: #02040a;
        --border-color: rgba(0, 242, 255, 0.2);
    }

    .stApp {
        background-color: var(--deep-space);
        color: #ffffff;
    }

    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Futurista */
    h1, h2, .tech-font {
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 4px;
    }

    .mono-font {
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: var(--cyan);
        text-transform: uppercase;
    }

    /* 1 & 2. HERO */
    .hero-space {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background-image: linear-gradient(rgba(2, 4, 10, 0.8), rgba(2, 4, 10, 0.8)),
                          url('https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=1600');
        background-size: cover;
        background-position: center;
        border-bottom: 1px solid var(--border-color);
    }

    .glitch-text {
        font-size: clamp(40px, 8vw, 100px);
        font-weight: 900;
        text-shadow: 0 0 20px var(--cyan);
        margin-bottom: 20px;
    }

    /* 3 & 4. TEMPLATES - GALERIA */
    .ship-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--border-color);
        padding: 0;
        position: relative;
        transition: 0.5s;
        clip-path: polygon(0 0, 90% 0, 100% 10%, 100% 100%, 10% 100%, 0 90%);
    }
    .ship-card:hover {
        border-color: var(--cyan);
        background: rgba(0, 242, 255, 0.05);
        transform: scale(1.02);
    }

    /* 5. CLIENTES - DATA NODES */
    .data-node {
        border-right: 1px solid var(--border-color);
        padding: 20px;
        text-align: center;
    }

    /* 6. MISSION OBJECTIVES */
    .mission-box {
        background: linear-gradient(90deg, rgba(0,242,255,0.1) 0%, transparent 100%);
        border-left: 4px solid var(--cyan);
        padding: 30px;
        margin-bottom: 20px;
    }

    /* 7. PASSO A PASSO */
    .step-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 40px;
    }
    .hex-num {
        width: 60px;
        height: 60px;
        background: var(--cyan);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--deep-space);
        font-weight: 900;
        font-family: 'Orbitron';
        flex-shrink: 0;
    }

    /* 8. PREÇOS */
    .price-tier {
        background: rgba(2, 4, 10, 0.9);
        border: 1px solid var(--border-color);
        padding: 40px;
        text-align: center;
        position: relative;
    }
    .price-tier::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    }

    /* Botão de Comando (link estilizado) */
    .cmd-btn {
        display: inline-block;
        background: transparent;
        color: var(--cyan) !important;
        border: 1px solid var(--cyan);
        padding: 15px 40px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-decoration: none !important;
        transition: 0.3s;
        box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
        cursor: pointer;
        margin-top: 16px;
    }
    .cmd-btn:hover {
        background: var(--cyan);
        color: var(--deep-space) !important;
        box-shadow: 0 0 30px var(--cyan);
    }
    .cmd-btn-full {
        display: block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1 & 2. HERO SECTION ---
st.markdown("""
<div class="hero-space" id="hero">
    <p class="mono-font">[ STATUS: READY FOR DEPLOYMENT ]</p>
    <h1 class="glitch-text">CONSTRUA SUA<br>ESTAÇÃO DIGITAL.</h1>
    <p style="max-width: 700px; font-size: 18px; color: rgba(255,255,255,0.6); margin-bottom: 40px; font-family: 'Inter';">
        Aprenda a criar seu novo site profissional em minutos, sem a dependência de um programador.
        Economize 80% do tempo e lance sua marca na velocidade da luz.
    </p>
    <a href="#templates" class="cmd-btn">INICIAR SEQUÊNCIA →</a>
</div>
""", unsafe_allow_html=True)

# --- 3 & 4. TEMPLATES CARROSSEL ---
st.markdown('<div id="templates" style="padding: 100px 8%;">', unsafe_allow_html=True)
st.markdown('<p class="mono-font">// EXPLORAR CATÁLOGO DE TEMPLATES</p>', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 32px; margin-bottom: 60px;">ESQUADRÃO DE ELITE</h2>', unsafe_allow_html=True)

t_col1, t_col2, t_col3 = st.columns(3)

def render_ship(col, name, tier, img):
    with col:
        st.markdown(f"""
        <div class="ship-card">
            <img src="{img}" style="width:100%; height:200px; object-fit:cover; filter: hue-rotate(180deg) brightness(0.7);">
            <div style="padding: 25px;">
                <p class="mono-font" style="font-size: 10px;">TIER: {tier}</p>
                <h3 style="font-family: 'Orbitron'; font-size: 18px; margin: 10px 0;">{name}</h3>
                <div style="width: 100%; height: 1px; background: var(--border-color); margin-bottom: 15px;"></div>
                <p style="font-size: 12px; opacity: 0.6;">Configurado para máxima conversão e SEO otimizado.</p>
                <a href="https://www.google.com/" target="_blank" class="cmd-btn cmd-btn-full">
                    VER DATA-SHEET {name.split()[0]}
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

render_ship(t_col1, "NEON PULSE",    "LEGENDARY", "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600")
render_ship(t_col2, "QUANTUM SUITE", "EPIC",       "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600")
render_ship(t_col3, "VOID MINIMAL",  "RARE",       "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=600")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PROVA SOCIAL (DATA NODES) ---
st.markdown("""
<div id="stats" style="background: rgba(0, 242, 255, 0.02); padding: 80px 8%; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr);">
        <div class="data-node">
            <h2 style="color: var(--cyan);">1.2K</h2>
            <p class="mono-font">SITES PUBLICADOS</p>
        </div>
        <div class="data-node">
            <h2 style="color: var(--cyan);">98%</h2>
            <p class="mono-font">SATISFAÇÃO</p>
        </div>
        <div class="data-node">
            <h2 style="color: var(--cyan);">24/7</h2>
            <p class="mono-font">UPLINK SUPORTE</p>
        </div>
        <div class="data-node" style="border:none;">
            <h2 style="color: var(--cyan);">80%</h2>
            <p class="mono-font">MAIS RÁPIDO</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown('<div id="missao" style="padding: 100px 8%;">', unsafe_allow_html=True)
st.markdown('<h2>OBJETIVOS DA MISSÃO</h2><br>', unsafe_allow_html=True)

def mission_item(text):
    st.markdown(f"""
    <div class="mission-box">
        <p style="font-family: 'JetBrains Mono'; font-size: 16px; margin: 0;">>> {text}</p>
    </div>
    """, unsafe_allow_html=True)

mission_item("Quer criar seu próprio site e customizá-lo em minutos pelo menor preço de mercado.")
mission_item("Deseja trabalhar vendendo sites de elite para terceiros com alta margem.")
mission_item("Precisa escalar a conversão de seus produtos físicos ou digitais.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PASSO A PASSO ---
st.markdown('<div id="protocolo" style="padding: 100px 8%; background: #000;">', unsafe_allow_html=True)
st.markdown('<h2>PROTOCOLO DE LANÇAMENTO</h2><br>', unsafe_allow_html=True)

def render_step(num, title, desc):
    st.markdown(f"""
    <div class="step-container">
        <div class="hex-num">{num}</div>
        <div>
            <h4 style="font-family: 'Orbitron'; color: var(--cyan);">{title}</h4>
            <p style="font-size: 14px; opacity: 0.6; max-width: 400px;">{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

render_step("01", "DOWNLOAD DOS ASSETS",    "Após a compra, todos os templates são disponibilizados no seu painel de comando.")
render_step("02", "CUSTOMIZAÇÃO DE DADOS",  "Siga nosso passo a passo visual para inserir suas informações e imagens.")
render_step("03", "DEPLOY EM SEGUNDOS",     "Configure sua URL personalizada e suba os arquivos para a rede global.")
render_step("04", "SISTEMA ONLINE",         "Seu site está no ar e pronto para operações em larga escala.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PREÇOS ---
st.markdown('<div id="precos" style="padding: 100px 8%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;">ACESSO À FROTA</h2><br>', unsafe_allow_html=True)

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("""
    <div class="price-tier">
        <p class="mono-font">PILOT ACCESS</p>
        <h1 style="font-size: 50px; margin: 20px 0;">R$ 97</h1>
        <p>1 Template de Elite</p>
        <p>Suporte Básico</p>
        <a href="https://www.google.com/" target="_blank" class="cmd-btn cmd-btn-full">SELECIONAR PILOT</a>
    </div>
    """, unsafe_allow_html=True)

with p_col2:
    st.markdown("""
    <div class="price-tier" style="border-color: var(--cyan); background: rgba(0,242,255,0.05);">
        <p class="mono-font" style="color: var(--cyan);">COMMANDER ACCESS</p>
        <h1 style="font-size: 60px; margin: 20px 0; color: var(--cyan);">R$ 197</h1>
        <p>Todos os Templates</p>
        <p>Acesso à Comunidade</p>
        <p>Suporte Prioritário</p>
        <a href="https://www.google.com/" target="_blank" class="cmd-btn cmd-btn-full">ADQUIRIR COMMANDER</a>
    </div>
    """, unsafe_allow_html=True)

with p_col3:
    st.markdown("""
    <div class="price-tier">
        <p class="mono-font">ADMIRAL PASS</p>
        <h1 style="font-size: 50px; margin: 20px 0;">R$ 497</h1>
        <p>Licença Comercial</p>
        <p>Mentoria 1:1</p>
        <p>Updates Vitalícios</p>
        <a href="https://www.google.com/" target="_blank" class="cmd-btn cmd-btn-full">TORNAR-SE ADMIRAL</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div id="faq" style="padding: 100px 20%; background: #010206;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;">DATABASE / FAQ</h2><br>', unsafe_allow_html=True)

with st.expander("COMO É FEITA A TRANSFERÊNCIA DOS ARQUIVOS?"):
    st.write("Os códigos são entregues em formato digital pronto para deploy direto via GitHub ou hospedagens estáticas.")

with st.expander("TEREI SUPORTE NA CONFIGURAÇÃO DO DOMÍNIO?"):
    st.write("Sim, fornecemos manuais detalhados e suporte técnico para garantir que sua URL personalizada funcione perfeitamente.")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 60px 8%; text-align: center; border-top: 1px solid var(--border-color); opacity: 0.5;">
    <p class="mono-font">© 2026 SITE PRO // INTERSTELLAR DESIGN // ALL RIGHTS RESERVED</p>
</div>
""", unsafe_allow_html=True)
