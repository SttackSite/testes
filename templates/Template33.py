import streamlit as st

def render():
    # --- SISTEMA DE DESIGN SAULO SIMON ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Inter:wght@400;700;900&display=swap');

        :root {
            --ss-bg: #ffae00; /* Laranja vibrante característico */
            --ss-black: #222222;
            --ss-white: #ffffff;
            --ss-card: #ffc445;
        }

        .stApp { 
            background-color: var(--ss-bg); 
            color: var(--ss-black);
            background-image: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.2) 0%, transparent 40%);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            cursor: url('https://cdn.custom-cursor.com/db/cursor/32/Game_Cursor_Hand.png'), auto;
        }

        /* --- TITULOS ESTILO JOGO --- */
        .ss-title {
            font-family: 'Bungee', cursive;
            font-size: clamp(40px, 10vw, 120px);
            line-height: 0.9;
            color: var(--ss-white);
            text-shadow: 8px 8px 0px var(--ss-black);
            margin-bottom: 20px;
            text-transform: uppercase;
        }

        .ss-subtitle {
            font-family: 'Bungee', cursive;
            font-size: 24px;
            color: var(--ss-black);
            margin-bottom: 40px;
        }

        /* --- BOTÕES TIPO GAMER --- */
        div.stButton > button {
            background-color: var(--ss-black) !important;
            color: var(--ss-white) !important;
            border: 4px solid var(--ss-black) !important;
            padding: 20px 40px !important;
            font-family: 'Bungee', cursive !important;
            font-size: 18px !important;
            border-radius: 0px !important;
            box-shadow: 8px 8px 0px rgba(0,0,0,0.2) !important;
            transition: all 0.1s ease !important;
            width: 100%;
        }

        div.stButton > button:hover {
            transform: translate(-4px, -4px);
            box-shadow: 12px 12px 0px var(--ss-black) !important;
            background-color: #333 !important;
        }

        div.stButton > button:active {
            transform: translate(4px, 4px);
            box-shadow: 0px 0px 0px var(--ss-black) !important;
        }

        /* --- CARDS DE PROJETOS (BENTO 3D) --- */
        .ss-project-card {
            background: var(--ss-card);
            border: 6px solid var(--ss-black);
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 12px 12px 0px var(--ss-black);
            transition: 0.3s;
        }

        .ss-project-card:hover {
            background: var(--ss-white);
            transform: rotate(-1deg);
        }

        .project-tag {
            background: var(--ss-black);
            color: var(--ss-white);
            padding: 4px 12px;
            font-size: 12px;
            font-weight: 800;
            display: inline-block;
            margin-bottom: 15px;
        }

        /* --- SEÇÕES --- */
        .ss-section {
            padding: 100px 8%;
        }

        .ss-footer {
            background: var(--ss-black);
            color: var(--ss-white);
            padding: 80px 8%;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 30px 8%; display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.05);">
        <div style="font-family: 'Bungee'; font-size: 28px; border: 4px solid #222; padding: 5px 15px;">ss</div>
        <div style="display: flex; gap: 30px; font-weight: 800; text-transform: uppercase; font-size: 14px;">
            <span>Projetos</span>
            <span>Experiências</span>
            <span>Sobre</span>
            <span style="color: white; text-shadow: 2px 2px 0 #000;">Dê o Play</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO (O MUNDO DO SAULO) ---
    st.markdown('<div class="ss-section" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('<h1 class="ss-title">SAULO<br>SIMON</h1>', unsafe_allow_html=True)
    st.markdown('<p class="ss-subtitle">DESENVOLVEDOR CREATIVO & MESTRE DO WEBGL</p>', unsafe_allow_html=True)
    
    col_h1, col_h2, col_h3 = st.columns([1, 1, 1])
    with col_h2:
        st.button("DIRIGIR PELO SITE")
    
    st.markdown("""
        <div style="margin-top: 60px; border: 8px solid #222; background: #eee; height: 400px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;">
            <div style="position: assolute; background: #222; color: #fff; padding: 10px 20px; font-family: 'Bungee';">SIMULAÇÃO INTERATIVA 3D</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PROJETOS (GRID COMPLETO) ---
    st.markdown('<div class="ss-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="ss-subtitle">TRABALHOS EM DESTAQUE</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="ss-project-card">
            <div class="project-tag">THREE.JS JOURNEY</div>
            <h3 style="font-family: 'Bungee'; font-size: 28px;">O curso definitivo de Three.js</h3>
            <p style="margin: 20px 0; font-weight: 600;">Aprenda a criar mundos 3D incríveis para a web partindo do zero assoluto.</p>
            <div style="height: 200px; background: #222; margin-top: 20px;"></div>
        </div>
        """, unsafe_allow_html=True)
        st.button("VER CURSO", key="p1")

    with col2:
        st.markdown("""
        <div class="ss-project-card">
            <div class="project-tag">WEBGL EXPERIENCE</div>
            <h3 style="font-family: 'Bungee'; font-size: 28px;">Oris: O Relógio Interativo</h3>
            <p style="margin: 20px 0; font-weight: 600;">Uma experiência imersiva para explorar cada detalhe da mecânica de luxo em tempo real.</p>
            <div style="height: 200px; background: #fff; border: 4px solid #222; margin-top: 20px;"></div>
        </div>
        """, unsafe_allow_html=True)
        st.button("VER PROJETO", key="p2")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO SOBRE (BIO COMPLETA) ---
    st.markdown('<div class="ss-section" style="background: rgba(255,255,255,0.3); border-top: 6px solid #222;">', unsafe_allow_html=True)
    c_b1, c_b2 = st.columns([1, 1.5], gap="large")
    with c_b1:
        st.markdown('<div style="width:100%; height:400px; background:#222; border: 8px solid white;"></div>', unsafe_allow_html=True)
    with c_b2:
        st.markdown('<h2 class="ss-subtitle" style="margin-bottom:20px;">QUEM É O SAULO?</h2>', unsafe_allow_html=True)
        st.markdown("""
            <p style="font-size: 20px; font-weight: 700; line-height: 1.4;">
                Sou um desenvolvedor freelancer francês apaixonado por criar experiências digitais que desafiam os limites do navegador. 
                Especialista em WebGL, Three.js e animações de alta performance.
            </p>
            <p style="font-size: 18px; margin-top: 20px;">
                Trabalho com agências e marcas globais para transformar conceitos asstratos em mundos interativos onde o usuário é o protagonista.
            </p>
        """, unsafe_allow_html=True)
        st.button("MEU SETUP DE TRABALHO")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div class="ss-footer">
        <h2 style="font-family: 'Bungee'; font-size: 50px; margin-bottom: 40px;">VAMOS JOGAR?</h2>
        <div style="display: flex; justify-content: center; gap: 50px; font-family: 'Bungee'; font-size: 20px;">
            <span>TWITTER</span>
            <span>GITHUB</span>
            <span>LINKEDIN</span>
            <span>E-MAIL</span>
        </div>
        <div style="margin-top: 60px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 40px; font-size: 12px; font-weight: 700;">
            © 2026 SAULO SIMON — DESENVOLVIDO COM CÓDIGO E PAIXÃO.
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="SAULO Simon | Creative Developer")
    render()
