import streamlit as st

def render():
    # --- SISTEMA DE DESIGN STATEMENT (VERSÃO BR) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

        :root {
            --st-bg: #e7f2e8; /* Verde Pistache Suave */
            --st-black: #000000;
            --st-border: #000000;
        }

        .stApp { background-color: var(--st-bg); color: var(--st-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            -webkit-font-smoothing: antialiased;
        }

        /* --- GRID BRUTALISTA --- */
        .st-grid-container {
            border-top: 2px solid var(--st-black);
            display: grid;
            grid-template-columns: 1fr 1fr;
        }

        .st-grid-item {
            border-right: 2px solid var(--st-black);
            border-bottom: 2px solid var(--st-black);
            padding: 80px 8%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* --- TIPOGRAFIA IMPACTANTE --- */
        .st-h1 {
            font-size: clamp(45px, 12vw, 150px);
            font-weight: 900;
            line-height: 0.8;
            letter-spacing: -0.07em;
            margin-bottom: 40px;
            text-transform: uppercase;
        }

        .st-h2 {
            font-size: 48px;
            font-weight: 900;
            line-height: 0.9;
            letter-spacing: -0.05em;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        /* --- BOTÃO STATEMENT (QUADRADO) --- */
        div.stButton > button {
            background-color: var(--st-black) !important;
            color: var(--st-bg) !important;
            border: 2px solid var(--st-black) !important;
            padding: 24px 40px !important;
            font-weight: 900 !important;
            border-radius: 0px !important;
            transition: 0.2s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
            font-size: 14px !important;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            width: 100% !important;
        }

        div.stButton > button:hover {
            background-color: transparent !important;
            color: var(--st-black) !important;
            transform: translate(6px, -6px);
            box-shadow: -6px 6px 0px var(--st-black);
        }

        /* --- NAVEGAÇÃO --- */
        .st-nav {
            padding: 40px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid var(--st-black);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="st-nav">
        <div style="font-weight: 900; font-size: 28px; letter-spacing: -2px;">STATEMENT.</div>
        <div style="display: flex; gap: 40px; font-size: 13px; font-weight: 900; text-transform: uppercase; letter-spacing: 1px;">
            <span>Projetos</span>
            <span>Estúdio</span>
            <span>Blog</span>
            <span style="border-bottom: 3px solid var(--st-black);">Contato</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div style="padding: 120px 5% 100px 5%;">', unsafe_allow_html=True)
    st.markdown('<h1 class="st-h1">REDEFININDO<br>O PADRÃO.</h1>', unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1.4, 1])
    with col_h1:
        st.markdown("""
            <p style="font-size: 26px; font-weight: 400; line-height: 1.2; max-width: 650px; letter-spacing: -0.02em;">
                Somos um estúdio criativo focado em marcas que desejam cortar o ruído. Através de clareza radical e design intencional, criamos presenças digitais que não podem ser ignoradas.
            </p>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GRID DE CONTEÚDO (BENTO BOX) ---
    st.markdown('<div class="st-grid-container">', unsafe_allow_html=True)
    
    # Item 1 - Estratégia
    st.markdown('<div class="st-grid-item">', unsafe_allow_html=True)
    st.markdown('<div><p style="font-weight:900; font-size:12px; margin-bottom:40px;">[ 01 ]</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="st-h2">ESTRATÉGIA<br>DIGITAL.</h2>', unsafe_allow_html=True)
    st.markdown('<p style="margin-bottom:40px; font-size:18px; line-height:1.4;">Mais que estética. Construímos as bases sólidas para o crescimento do seu negócio.</p></div>', unsafe_allow_html=True)
    st.button("VER DETALHES", key="btn1")
    st.markdown('</div>', unsafe_allow_html=True)

    # Item 2 - Identidade
    st.markdown('<div class="st-grid-item" style="border-right:none">', unsafe_allow_html=True)
    st.markdown('<div><p style="font-weight:900; font-size:12px; margin-bottom:40px;">[ 02 ]</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="st-h2">IDENTIDADE<br>VISUAL.</h2>', unsafe_allow_html=True)
    st.markdown('<p style="margin-bottom:40px; font-size:18px; line-height:1.4;">Identidade não é apenas um logo. É a materialização de uma promessa e um sentimento.</p></div>', unsafe_allow_html=True)
    st.button("EXPLORAR PROJETOS", key="btn2")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE IMPACTO ---
    st.markdown("""
    <div style="padding: 120px 5%; border-bottom: 2px solid black;">
        <h2 style="font-size: clamp(30px, 5vw, 60px); font-weight: 900; line-height: 1; letter-spacing: -0.05em; text-transform: uppercase;">
            Trabalhamos com quem entende que o design é a maior vantagem competitiva do século 21.
        </h2>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER DARK ---
    st.markdown("""
    <div style="padding: 120px 5%; background: var(--st-black); color: var(--st-bg);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 60px;">
            <div>
                <h1 style="color: var(--st-bg); font-size: clamp(60px, 15vw, 200px); font-weight: 900; margin-bottom: 20px; letter-spacing: -10px;">OLÁ.</h1>
                <p style="font-size: 20px; font-weight: 400;">São Paulo / Global</p>
            </div>
            <div style="text-align: right; font-weight: 900; text-transform: uppercase; font-size: 16px; letter-spacing: 2px; line-height: 1.8;">
                INSTAGRAM<br>LINKEDIN<br>BEHANCE<br><br>
                © 2026 STATEMENT STUDIO
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Statement | Estúdio Criativo")
    render()
