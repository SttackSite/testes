import streamlit as st

def render():
    # --- CSS WIS EDUCATION STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&family=Inter:wght@300;400;700&display=swap');

        :root {
            --wis-blue: #0055ff;
            --wis-orange: #ff6600;
            --wis-dark: #1e1e1e;
            --wis-bg-light: #f8faff;
        }

        .stApp {
            background-color: white;
            color: var(--wis-dark);
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 800;
            color: var(--wis-dark);
        }

        /* 1 & 2. HERO */
        .hero-wis {
            padding: 100px 10%;
            background-color: var(--wis-bg-light);
            border-bottom-right-radius: 100px;
            display: flex;
            align-items: center;
        }

        .hero-title { font-size: clamp(32px, 5vw, 56px); line-height: 1.1; margin-bottom: 25px; }
        .wis-dot { color: var(--wis-blue); }

        /* 3 & 4. SOLUTIONS CARDS */
        .solution-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #eee;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            height: 100%;
        }
        .solution-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 85, 255, 0.1);
            border-color: var(--wis-blue);
        }

        /* 5. NUMBERS SECTION */
        .stat-box {
            text-align: center;
            padding: 40px;
        }
        .stat-number {
            font-size: 48px;
            font-weight: 800;
            color: var(--wis-blue);
            margin-bottom: 5px;
        }

        /* 6. DIFERENCIAIS - PILARES */
        .pilar-badge {
            background: rgba(0, 85, 255, 0.1);
            color: var(--wis-blue);
            padding: 5px 15px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 15px;
            display: inline-block;
        }

        /* Botão WIS (link estilizado) */
        .wis-btn {
            display: inline-block;
            background: var(--wis-blue);
            color: white !important;
            border: none;
            padding: 12px 35px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 14px;
            border-radius: 12px;
            text-decoration: none !important;
            transition: background 0.3s, transform 0.3s;
            box-shadow: 0 10px 20px rgba(0, 85, 255, 0.2);
            cursor: pointer;
            margin-top: 14px;
        }
        .wis-btn:hover {
            background: var(--wis-dark);
            color: white !important;
            transform: translateY(-2px);
        }

        /* Links da navbar */
        .nav-link-wis {
            color: #666 !important;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 14px;
            transition: color 0.2s;
        }
        .nav-link-wis:hover {
            color: var(--wis-blue) !important;
        }
        .nav-link-wis.active {
            color: var(--wis-blue) !important;
        }

        /* "Saiba mais →" nos cards */
        .card-link {
            color: var(--wis-blue) !important;
            font-weight: 700;
            text-decoration: none !important;
            display: inline-block;
            margin-top: 20px;
            transition: opacity 0.2s;
        }
        .card-link:hover {
            opacity: 0.75;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 25px 10%; display: flex; justify-content: space-between; align-items: center; background: white;">
        <div style="font-weight: 800; font-size: 28px; letter-spacing: -1px; color:var(--wis-dark)">WIS<span class="wis-dot">.</span></div>
        <div style="display: flex; gap: 30px; align-items: center;">
            <a href="#solucoes" class="nav-link-wis">SOLUÇÕES</a>
            <a href="#manifesto" class="nav-link-wis">QUEM SOMOS</a>
            <a href="https://www.google.com/" target="_blank" class="nav-link-wis">BLOG</a>
            <a href="#footer" class="nav-link-wis active">CONTATO</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO SECTION ---
    st.markdown("""
    <div class="hero-wis" id="hero">
        <div style="max-width: 800px;">
            <div class="pilar-badge">Learntech & Consultoria</div>
            <h1 class="hero-title">Prepare sua empresa para o <span style="color: var(--wis-blue)">próximo nível</span> da aprendizagem.</h1>
            <p style="font-size: 20px; color: #555; margin-bottom: 40px; line-height: 1.6;">
                Desenvolvemos soluções de aprendizagem corporativa personalizadas com foco em <b>Cultura e Performance</b>.
            </p>
            <a href="#solucoes" class="wis-btn">FALE COM ESPECIALISTAS</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3 & 4. SOLUÇÕES (GRID) ---
    st.markdown('<div id="solucoes" style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color: var(--wis-blue); font-weight:700;">NOSSAS SOLUÇÕES</p>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center; margin-bottom:60px;">Como podemos ajudar seu negócio?</h2>', unsafe_allow_html=True)

    col_s1, col_s2, col_s3 = st.columns(3, gap="large")

    def render_wis_card(col, title, desc, icon):
        with col:
            st.markdown(f"""
            <div class="solution-card">
                <div style="font-size: 40px; margin-bottom: 20px;">{icon}</div>
                <h3>{title}</h3>
                <p style="color: #777; font-size: 15px; line-height: 1.6; margin-top: 15px;">{desc}</p>
                <a href="https://www.google.com/" target="_blank" class="card-link">Saiba mais →</a>
            </div>
            """, unsafe_allow_html=True)

    render_wis_card(col_s1, "Learning Campaigns",    "Campanhas de aprendizagem engajadoras para mudanças de cultura e novos processos.", "🚀")
    render_wis_card(col_s2, "Design de Comunidades", "Criamos ecossistemas internos onde o conhecimento flui de forma orgânica e contínua.", "🤝")
    render_wis_card(col_s3, "Upskilling & Reskilling","Programas intensivos de desenvolvimento de novas competências para o futuro.", "📈")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. NÚMEROS (PROVA SOCIAL) ---
    st.markdown('<div id="numeros" style="background: var(--wis-dark); color: white; padding: 60px 10%;">', unsafe_allow_html=True)
    n1, n2, n3, n4 = st.columns(4)
    with n1: st.markdown('<div class="stat-box"><div class="stat-number">+12</div><div style="opacity:0.7">Anos de Mercado</div></div>', unsafe_allow_html=True)
    with n2: st.markdown('<div class="stat-box"><div class="stat-number">+900</div><div style="opacity:0.7">Projetos Entregues</div></div>', unsafe_allow_html=True)
    with n3: st.markdown('<div class="stat-box"><div class="stat-number">+100k</div><div style="opacity:0.7">Pessoas Impactadas</div></div>', unsafe_allow_html=True)
    with n4: st.markdown('<div class="stat-box"><div class="stat-number">+50</div><div style="opacity:0.7">Grandes Empresas</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 6. MANIFESTO / DIFERENCIAL ---
    st.markdown('<div id="manifesto" style="padding: 120px 10%; background: white;">', unsafe_allow_html=True)
    c_m1, c_m2 = st.columns([1, 1.2], gap="large")
    with c_m1:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800", use_container_width=True)
    with c_m2:
        st.markdown("""
        <div class="pilar-badge">Nossa Metodologia</div>
        <h2>Aprendizagem aplicada que gera resultado real.</h2>
        <p style="color:#555; font-size:18px; line-height:1.8; margin-top:20px;">
            Não acreditamos em treinamentos passivos. Nossa abordagem foca na <b>prática</b>,
            utilizando tecnologia e inovação para resolver desafios reais de liderança, cultura e vendas.
        </p>
        <a href="https://www.google.com/" target="_blank" class="wis-btn">CONHEÇA NOSSA HISTÓRIA</a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div id="footer" style="padding: 80px 10%; border-top: 1px solid #eee; background: #fafafa;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 50px;">
            <div>
                <h3 style="margin-bottom: 20px;">WIS<span class="wis-dot">.</span></h3>
                <p style="color: #888; font-size: 14px;">São Paulo | Vitória | Florianópolis</p>
            </div>
            <div>
                <h4 style="font-size: 14px; margin-bottom: 15px;">CONTATO</h4>
                <p style="color: #888; font-size: 14px;">contato@wis.digital<br>(11) 5555-5555</p>
            </div>
            <div>
                <h4 style="font-size: 14px; margin-bottom: 15px;">SIGA A GENTE</h4>
                <p style="color: #888; font-size: 14px;">
                    <a href="https://www.google.com/" target="_blank" style="color:#888; text-decoration:none;">Linkedin</a> /
                    <a href="https://www.google.com/" target="_blank" style="color:#888; text-decoration:none;">Instagram</a> /
                    <a href="https://www.google.com/" target="_blank" style="color:#888; text-decoration:none;">Spotify</a>
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Execução direta se rodado sozinho
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="WIS | Learntech")
    render()
