import streamlit as st

def render():
    # --- SISTEMA DE DESIGN SCENCO MUSEUM ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

        :root {
            --un-bg: #F5F5F0;
            --un-black: #1A1A1A;
            --un-blue: #0070FF;
            --un-accent: #B58D3D;
        }

        .stApp { background-color: var(--un-bg); color: var(--un-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- TYPOGRAPHY --- */
        .un-serif { font-family: 'Playfair Display', serif; }
        
        .un-h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(50px, 12vw, 160px);
            font-weight: 400;
            line-height: 0.85;
            letter-spacing: -0.04em;
            text-align: center;
            margin-bottom: 40px;
        }

        .un-label {
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--un-accent);
            text-align: center;
            display: block;
            margin-bottom: 20px;
        }

        /* --- NAVEGAÇÃO IMERSIVA --- */
        .un-nav {
            padding: 40px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: absolute;
            width: 100%;
            z-index: 100;
        }

        /* --- SEÇÕES NARRATIVAS --- */
        .un-section {
            padding: 120px 8%;
            position: relative;
        }

        .un-image-container {
            width: 100%;
            height: 80vh;
            background-size: cover;
            background-position: center;
            filter: sepia(0.2) contrast(1.1);
            margin: 60px 0;
            border-radius: 2px;
        }

        .un-quote {
            font-family: 'Playfair Display', serif;
            font-size: clamp(24px, 4vw, 48px);
            font-style: italic;
            line-height: 1.2;
            max-width: 800px;
            margin: 100px auto;
            text-align: center;
        }

        /* --- BOTÃO MUSEU --- */
        div.stButton > button {
            background-color: transparent !important;
            color: var(--un-black) !important;
            border: 1px solid var(--un-black) !important;
            padding: 15px 40px !important;
            border-radius: 0px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            letter-spacing: 0.1em;
            transition: 0.4s !important;
            text-transform: uppercase;
        }

        div.stButton > button:hover {
            background-color: var(--un-black) !important;
            color: white !important;
        }

        /* --- FOOTER CLASSIC --- */
        .un-footer {
            background: var(--un-black);
            color: white;
            padding: 100px 8% 50px 8%;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="un-nav">
        <div style="font-weight: 700; font-size: 20px; letter-spacing: 2px;">SCENCO</div>
        <div style="display: flex; gap: 40px; font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;">
            <span>Exposições</span>
            <span>Coleções</span>
            <span>História</span>
            <span style="color: var(--un-accent)">Explorar →</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO (IMERSIVO) ---
    st.markdown('<div class="un-section" style="padding-top: 200px;">', unsafe_allow_html=True)
    st.markdown('<span class="un-label">Museu Digital do Patrimônio Mundial</span>', unsafe_allow_html=True)
    st.markdown('<h1 class="un-h1">UMA JORNADA<br>PELO <span class="un-serif" style="font-style:italic">Tempo.</span></h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="un-image-container" style="background-image: url('https://images.unsplash.com/photo-1548013146-72479768bbaa?w=1600');"></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="un-quote">"O patrimônio é o nosso legado do passado, o que vivemos hoje e o que transmitimos às gerações futuras."</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE COLEÇÃO (GRID ASSIMÉTRICO) ---
    st.markdown('<div class="un-section" style="background: white;">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
            <div style="padding-top: 100px;">
                <span class="un-label" style="text-align:left;">Arquitetura & Ruínas</span>
                <h2 class="un-serif" style="font-size: 60px; margin-bottom: 30px;">Templos de<br>Angkor Wat</h2>
                <p style="font-size: 18px; color: #555; line-height: 1.6; margin-bottom: 40px;">
                    Explore a complexidade do maior monumento religioso do mundo, uma obra-prima da civilização Khmer que resistiu aos séculos.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.button("VER COLEÇÃO COMPLETA", key="angkor")
        st.markdown('<div style="height: 400px; background-image: url(\'https://images.unsplash.com/photo-1569350080881-22442426302e?w=800\'); background-size: cover; margin-top: 80px;"></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div style="height: 600px; background-image: url(\'https://images.unsplash.com/photo-1503917988258-f197e2f4192d?w=800\'); background-size: cover; margin-bottom: 60px;"></div>', unsafe_allow_html=True)
        st.markdown("""
            <h2 class="un-serif" style="font-size: 60px; margin-bottom: 30px;">A Magia de<br>Mont-Saint-Michel</h2>
            <p style="font-size: 18px; color: #555; line-height: 1.6; margin-bottom: 40px;">
                Uma abadia gótica situada em uma ilha rochosa no coração de uma baía imensa, desafiando as marés e o horizonte.
            </p>
        """, unsafe_allow_html=True)
        st.button("EXPLORAR LOCAL", key="mont")

    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE MAPA / EXPLORAÇÃO ---
    st.markdown("""
    <div class="un-section" style="text-align: center; border-top: 1px solid #ddd;">
        <span class="un-label">Mapa Global</span>
        <h2 class="un-serif" style="font-size: 80px; margin-bottom: 40px;">Onde a História Vive</h2>
        <div style="background: #e5e5e0; height: 500px; width: 100%; border-radius: 4px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
            <img src="https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=1600" style="width: 100%; opacity: 0.3; filter: grayscale(1);">
            <div style="position: absolute; font-size: 14px; font-weight: 600; letter-spacing: 2px;">CARREGANDO MAPA INTERATIVO...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER DENSO ---
    st.markdown("""
    <div class="un-footer">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 80px; margin-bottom: 100px;">
            <div>
                <div style="font-weight: 700; font-size: 28px; margin-bottom: 30px;">SCENCO</div>
                <p style="opacity: 0.6; line-height: 1.6;">O Museu do Patrimônio Mundial da SCENCO é uma iniciativa para preservar a memória cultural através da inovação digital.</p>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 25px;">EXPLORAR</p>
                <ul style="list-style: none; padding: 0; opacity: 0.6; line-height: 2.5; font-size: 14px;">
                    <li>África</li>
                    <li>Américas</li>
                    <li>Ásia & Pacífico</li>
                    <li>Europa</li>
                </ul>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 25px;">CRÉDITOS</p>
                <ul style="list-style: none; padding: 0; opacity: 0.6; line-height: 2.5; font-size: 14px;">
                    <li>Curadoria Digital</li>
                    <li>Parceiros Tecnológicos</li>
                    <li>Open Data</li>
                </ul>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 25px;">SIGA-NOS</p>
                <ul style="list-style: none; padding: 0; opacity: 0.6; line-height: 2.5; font-size: 14px;">
                    <li>Instagram</li>
                    <li>Twitter</li>
                    <li>Youtube</li>
                </ul>
            </div>
        </div>
        <div style="border-top: 1px solid #333; padding-top: 40px; display: flex; justify-content: space-between; font-size: 11px; opacity: 0.4; letter-spacing: 1px;">
            <span>SCENCO WORLD HERITAGE CENTRE © 2026.</span>
            <span>POLÍTICAS DE PRESERVAÇÃO DIGITAL | TERMOS DE USO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="SCENCO | Museu Digital")
    render()
