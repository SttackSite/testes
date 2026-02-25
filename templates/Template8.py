import streamlit as st

def render():
    # --- CSS DE ALTA COSTURA (ESTILO R. YAZBEK) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&family=Playfair+Display:ital,wght@0,400;1,400&display=swap');

        :root {
            --bg-color: #ffffff;
            --text-color: #1a1a1a;
            --light-gray: #f9f9f9;
            --border-color: #eeeeee;
        }

        .stApp {
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            font-weight: 200;
            letter-spacing: 0.5px;
        }

        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 100;
            text-transform: uppercase;
            letter-spacing: 4px;
            color: var(--text-color);
        }

        .serif-italic {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-weight: 400;
            text-transform: none;
            letter-spacing: 0px;
        }

        /* Hero Section Assimétrica */
        .hero-container {
            height: 90vh;
            display: flex;
            align-items: center;
            padding: 0 8%;
            background-color: var(--bg-color);
        }

        .hero-content {
            max-width: 600px;
            border-left: 1px solid var(--text-color);
            padding-left: 40px;
        }

        /* Seção de Projetos (Grid Estilo Galeria) */
        .project-card {
            margin-bottom: 100px;
            transition: 0.8s cubic-bezier(0.2, 1, 0.2, 1);
        }
        
        .project-image {
            width: 100%;
            height: 70vh;
            object-fit: cover;
            filter: grayscale(100%);
            transition: 0.8s;
        }

        .project-image:hover {
            filter: grayscale(0%);
        }

        .project-info {
            margin-top: 20px;
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
        }

        /* Botão Minimalista */
        div.stButton > button {
            background: transparent;
            color: var(--text-color);
            border: 1px solid var(--text-color);
            border-radius: 0;
            padding: 10px 40px;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: 0.4s;
        }
        div.stButton > button:hover {
            background: var(--text-color);
            color: white;
        }

        /* Navegação Lateral Fake */
        .side-nav {
            position: fixed;
            right: 40px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 20px;
            z-index: 100;
        }
        .side-nav-item {
            font-size: 10px;
            writing-mode: vertical-rl;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #999;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 40px 8%; display: flex; justify-content: space-between; align-items: center; position: absolute; width: 100%; z-index: 10;">
        <div style="font-weight: 400; font-size: 18px; letter-spacing: 4px;">R. YAZBEK</div>
        <div style="display: flex; gap: 40px; font-size: 11px; letter-spacing: 2px;">
            <span>PROJETOS</span>
            <span>ESCRITÓRIO</span>
            <span>CONTATO</span>
        </div>
    </div>
    <div class="side-nav">
        <div class="side-nav-item">INSTAGRAM</div>
        <div class="side-nav-item">LINKEDIN</div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1. HERO ---
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <h1 style="font-size: 40px; margin-bottom: 20px;">Arquitetura de <br><span class="serif-italic">Propósito</span>.</h1>
            <p style="font-size: 16px; color: #666; line-height: 1.8;">
                Desenvolvemos espaços que transcendem a estética, focando na experiência humana e na perenidade do design contemporâneo.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. PROJETOS (GRID ASSIMÉTRICO) ---
    st.markdown('<div style="padding: 0 8% 100px 8%;">', unsafe_allow_html=True)
    
    # Projeto 1 - Lado Esquerdo (Grande)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class="project-card">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200" class="project-image">
            <div class="project-info">
                <h3>RESIDÊNCIA ALTO DE PINHEIROS</h3>
                <span class="mono">2024</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Projeto 2 - Lado Direito (Deslocado)
    c3, c4 = st.columns([1, 2])
    with c4:
        st.markdown("""
        <div class="project-card">
            <img src="https://images.unsplash.com/photo-1600607687940-477a128f198e?w=1200" class="project-image" style="height: 60vh;">
            <div class="project-info">
                <h3>EDIFÍCIO CORPORATIVO JARDINS</h3>
                <span class="mono">2023</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Projeto 3 - Centralizado
    _, c5, _ = st.columns([0.5, 2, 0.5])
    with c5:
        st.markdown("""
        <div class="project-card">
            <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1200" class="project-image">
            <div class="project-info">
                <h3>CASA DO LAGO</h3>
                <span class="mono">2024</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # --- 3. SOBRE / MANIFESTO ---
    st.markdown("""
    <div style="background-color: var(--light-gray); padding: 150px 20%; text-align: center;">
        <p class="serif-italic" style="font-size: 32px; margin-bottom: 40px; color: #333;">
            "O design essencial não é o que nada tem, mas o que nada sobra."
        </p>
        <div style="width: 40px; height: 1px; background: #1a1a1a; margin: 0 auto 40px auto;"></div>
        <p style="font-size: 14px; text-transform: uppercase; letter-spacing: 3px; color: #999;">
            R. Yazbek Arquitetos Associados
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. CONTATO ---
    st.markdown('<div style="padding: 100px 8%; text-align: left;">', unsafe_allow_html=True)
    st.markdown('<h2>VAMOS CONVERSAR?</h2><br>', unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("""
        <div style="font-size: 14px; line-height: 2;">
            RUA AMAURI, 116<br>
            SÃO PAULO, BRASIL<br><br>
            +55 11 3078 0000<br>
            CONTATO@RYAZBEK.COM.BR
        </div>
        """, unsafe_allow_html=True)
    
    with col_f2:
        st.button("ENVIAR MENSAGEM")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 40px 8%; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; font-size: 10px; color: #bbb; letter-spacing: 2px;">
        <span>© 2024 R. YAZBEK</span>
        <span>DESIGN BY STREAMLIT</span>
    </div>
    """, unsafe_allow_html=True)

# Execução direta para teste
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="R. Yazbek | Arquitetura")
    render()
