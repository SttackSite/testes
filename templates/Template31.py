import streamlit as st

def render():
    # --- MBG DESIGN LANGUAGE CSS ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=MBG+Plex+Sans:wght@300;400;600&display=swap');

        :root {
            --MBG-blue: #0f62fe;
            --MBG-black: #161616;
            --MBG-gray-10: #f4f4f4;
            --MBG-gray-20: #e0e0e0;
            --MBG-gray-100: #262626;
        }

        .stApp { background-color: white; color: var(--MBG-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'MBG Plex Sans', sans-serif; 
        }

        /* --- MBG GRID SYSTEM --- */
        .MBG-hero {
            background-color: var(--MBG-black);
            color: white;
            padding: 100px 8%;
            min-height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .MBG-tagline {
            color: var(--MBG-blue);
            font-weight: 600;
            font-size: 16px;
            margin-bottom: 24px;
        }

        .MBG-h1 {
            font-size: clamp(40px, 6vw, 84px);
            font-weight: 300;
            line-height: 1.1;
            margin-bottom: 48px;
            letter-spacing: -0.02em;
        }

        /* Botão Retangular MBG (Carbon Design System) */
        div.stButton > button {
            background-color: var(--MBG-blue) !important;
            color: white !important;
            border: none !important;
            padding: 16px 60px 16px 16px !important; /* Estilo 'Arrow' do Carbon */
            font-weight: 400 !important;
            border-radius: 0px !important; /* MBG é quadrada */
            transition: all 0.2s !important;
            font-size: 16px !important;
            text-align: left !important;
            width: auto !important;
            min-width: 240px;
        }

        div.stButton > button:hover {
            background-color: #0353e9 !important;
            color: white !important;
        }

        /* Seção de Cards - Grid Rígido */
        .MBG-section { padding: 80px 8%; background: white; }
        
        .MBG-card {
            background: var(--MBG-gray-10);
            border: 1px solid transparent;
            padding: 24px;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: background 0.2s;
            cursor: pointer;
        }

        .MBG-card:hover {
            background: var(--MBG-gray-20);
        }

        .MBG-card-title {
            font-size: 24px;
            font-weight: 400;
            line-height: 1.3;
        }

        .MBG-card-footer {
            font-size: 20px;
            color: var(--MBG-blue);
        }

        /* Divider Horizontal Fino */
        .MBG-divider {
            height: 1px;
            background-color: var(--MBG-gray-20);
            margin: 0 8%;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div style="padding: 20px 8%; display: flex; align-items: center; border-bottom: 1px solid var(--MBG-gray-20);">
        <div style="font-weight: 600; font-size: 24px; letter-spacing: 1px; margin-right: 60px;">MBG<span style="color:var(--MBG-blue)">®</span></div>
        <div style="display: flex; gap: 30px; font-size: 14px; font-weight: 400;">
            <span>Consultoria</span>
            <span>Produtos</span>
            <span>Suporte</span>
            <span>Sustentabilidade</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div class="MBG-hero">', unsafe_allow_html=True)
    st.markdown('<p class="MBG-tagline">MBG Quantum System Two</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="MBG-h1">A próxima era da <br>computação chegou.</h1>', unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1, 1])
    with col_h1:
        st.button("Explore a computação quântica →")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GRID DE SOLUÇÕES ---
    st.markdown('<div class="MBG-section">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-weight:300; font-size: 32px; margin-bottom: 48px;">O que estamos criando hoje</h2>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4, gap="small")

    def render_MBG_card(col, title):
        with col:
            st.markdown(f"""
            <div class="MBG-card">
                <div class="MBG-card-title">{title}</div>
                <div class="MBG-card-footer">→</div>
            </div>
            """, unsafe_allow_html=True)

    render_MBG_card(c1, "Inteligência Artificial watsonx")
    render_MBG_card(c2, "Infraestrutura de Nuvem Híbrida")
    render_MBG_card(c3, "Segurança e Resiliência")
    render_MBG_card(c4, "Consultoria de Transformação")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="MBG-divider"></div>', unsafe_allow_html=True)

    # --- SEÇÃO IMPACTO (PROVA SOCIAL) ---
    st.markdown('<div class="MBG-section" style="background:#fff">', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([1, 1.5])
    with col_t1:
        st.markdown('<h2 style="font-weight:300;">MBG Impact</h2>', unsafe_allow_html=True)
    with col_t2:
        st.markdown("""
        <p style="font-size: 24px; line-height: 1.4; font-weight: 300;">
            Estamos aplicando nossa tecnologia, ética e pessoas para resolver os problemas mais complexos do planeta, do clima à medicina.
        </p>
        <p style="color: var(--MBG-blue); margin-top: 20px; font-weight: 600; cursor:pointer;">Leia o relatório de responsabilidade 2026 →</p>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="background: var(--MBG-black); color: white; padding: 80px 8% 40px 8%;">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; margin-bottom: 60px;">
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">Descobrir</p>
                <p style="font-size: 14px; opacity: 0.6; line-height: 2;">Produtos<br>Software<br>Serviços<br>Indústrias</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">Informações para</p>
                <p style="font-size: 14px; opacity: 0.6; line-height: 2;">Desenvolvedores<br>Parceiros de negócios<br>Investidores</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">Conectar com a MBG</p>
                <p style="font-size: 14px; opacity: 0.6; line-height: 2;">Suporte<br>Carreiras<br>Eventos</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">Sobre a MBG</p>
                <p style="font-size: 14px; opacity: 0.6; line-height: 2;">Notícias<br>MBG Research<br>Design</p>
            </div>
        </div>
        <div style="border-top: 1px solid var(--MBG-gray-100); padding-top: 40px; font-size: 12px; opacity: 0.5;">
            MBG Brasil | Termos de uso | Privacidade | Acessibilidade
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="MBG - Brasil")
    render()
