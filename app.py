import streamlit as st

# ✅ CONFIGURAÇÃO INICIAL
st.set_page_config(
    page_title="Multi-Cliente",
    page_icon="🌐",
    layout="wide"
)

# ✅ OBTER CLIENTE DA URL
cliente = st.query_params.get("cliente", "paix").lower()

# ✅ TEMPLATE PAIX (DESIGN)
if cliente == "paix":
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');

        .stApp {
            background-color: #f7f7f7;
            color: #1a1a1a;
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            font-weight: 200;
            letter-spacing: 0.05em;
        }

        h1, h2, .serif-light {
            font-family: 'Cormorant Garamond', serif;
            font-weight: 300;
            font-size: 48px;
            line-height: 1.1;
        }

        .nav-paix {
            display: flex;
            justify-content: space-between;
            padding: 50px 5%;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 3px;
        }

        .nav-link {
            color: #1a1a1a !important;
            text-decoration: none !important;
            transition: 0.3s;
            cursor: pointer;
        }

        .nav-link:hover {
            opacity: 0.6;
            text-decoration: none !important;
        }

        .nav-link:visited {
            color: #1a1a1a !important;
            text-decoration: none !important;
        }

        .hero-paix {
            padding: 100px 5% 150px 5%;
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            gap: 100px;
        }

        .project-section {
            padding: 0 5% 200px 5%;
        }

        .project-card {
            margin-bottom: 250px;
            transition: opacity 0.6s ease;
        }
        
        .project-img {
            width: 100%;
            filter: grayscale(10%) contrast(1.05);
            margin-bottom: 25px;
        }

        .project-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 32px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 15px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .project-year {
            font-size: 10px;
            font-family: 'Inter', sans-serif;
            letter-spacing: 2px;
            color: #888;
        }

        .action-button {
            display: inline-block !important;
            background: #1a1a1a !important;
            color: #f7f7f7 !important;
            border: none !important;
            padding: 12px 30px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 400 !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            text-decoration: none !important;
            font-size: 10px !important;
            transition: 0.3s !important;
            cursor: pointer !important;
        }

        .action-button:hover {
            background-color: #333 !important;
            color: #f7f7f7 !important;
            text-decoration: none !important;
        }

        .action-button:visited {
            color: #f7f7f7 !important;
            text-decoration: none !important;
        }

        .footer-paix {
            padding: 100px 5%;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            letter-spacing: 2px;
            color: #666;
        }
    </style>
    """, unsafe_allow_html=True)

    # NAVEGAÇÃO
    st.markdown("""
    <div class="nav-paix">
        <div style="font-weight: 400;">PAIX DESIGN</div>
        <div style="display: flex; gap: 50px;">
            <a href="#projetos" class="nav-link">Projetos</a>
            <a href="#escritorio" class="nav-link">Escritório</a>
            <a href="#contato" class="nav-link">Contato</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # HERO SECTION
    st.markdown("""
    <div class="hero-paix">
        <div>
            <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #888; margin-bottom: 30px;">
                Arquitetura & Design de Interiores
            </p>
            <h1 class="serif-light">
                A beleza reside na <br>
                intenção e na calma.
            </h1>
        </div>
        <div style="font-size: 16px; line-height: 1.8; padding-top: 10px; color: #555;">
            PAIX é um estúdio de design focado na criação de espaços que transcendem o tempo. 
            Nossa abordagem é guiada pela pureza dos materiais e pela harmonia entre a luz natural e a forma construída.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # PROJETOS
    def render_paix_project(title, location, year, img_url):
        st.markdown(f"""
        <div id="projetos" class="project-section">
            <div class="project-card">
                <img src="{img_url}" class="project-img">
                <div class="project-title">
                    <span>{title} — {location}</span>
                    <span class="project-year">{year}</span>
                </div>
                <p style="font-size: 12px; color: #999; text-transform: uppercase; letter-spacing: 1px;">
                    Residencial / Design de Mobiliário
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    render_paix_project("Casa Minimalista", "Sintra", "2024", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600")
    render_paix_project("Apartamento Galeria", "Porto", "2023", "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600")

    # SEÇÃO SOBRE
    st.markdown("""
    <div id="escritorio" style="padding: 150px 20% 250px 20%; text-align: center;">
        <h2 class="serif-light" style="font-size: 56px; margin-bottom: 40px;">Atmosferas Tangíveis</h2>
        <p style="color: #666; line-height: 2;">
            Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, 
            desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente.
        </p>
        <div style="margin-top: 60px;">
            <a href="https://www.google.com/" target="_blank" class="action-button">Conheça Nosso Trabalho</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
    <div id="contato" class="footer-paix">
        <div>
            PAIX DESIGN STUDIO<br>
            AVENIDA DA LIBERDADE, LISBOA
        </div>
        <div style="text-align: right;">
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">INSTAGRAM</a> / 
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">BEHANCE</a> / 
            <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">LINKEDIN</a><br>
            <a href="mailto:hello@paix-design.com" style="color: #666; text-decoration: none;">HELLO@PAIX-DESIGN.COM</a>
        </div>
    </div>
    <div style="padding: 30px 5%; font-size: 9px; color: #bbb; letter-spacing: 1px;">
        © 2026 PAIX DESIGN. TODOS OS DIREITOS RESERVADOS.
    </div>
    """, unsafe_allow_html=True)

# ✅ TEMPLATE YOLU (BEAUTY)
elif cliente == "yolu":
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300&family=Noto+Sans+JP:wght@100;300;400&display=swap');

        .stApp {
            background: linear-gradient(180deg, #050a14 0%, #0f1c3d 50%, #1e1b4b 100%);
            color: #ffffff;
        }

        html, body, [class*="css"] {
            font-family: 'Noto Sans JP', sans-serif;
            font-weight: 300;
        }

        h1, h2, .serif-yolu {
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-weight: 300;
            letter-spacing: 2px;
        }

        .nav-yolu {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 6%;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(5, 10, 20, 0.4);
            backdrop-filter: blur(8px);
        }
        
        .logo-yolu {
            font-size: 28px;
            letter-spacing: 5px;
            font-weight: 400;
        }

        .nav-link {
            color: #ffffff !important;
            text-decoration: none !important;
            font-size: 11px;
            letter-spacing: 1px;
            transition: 0.3s;
            cursor: pointer;
        }

        .nav-link:hover {
            opacity: 0.6;
            text-decoration: none !important;
        }

        .nav-link:visited {
            color: #ffffff !important;
            text-decoration: none !important;
        }

        .hero-yolu {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600');
            background-size: cover;
            background-position: center;
            position: relative;
        }
        
        .hero-title-main {
            font-size: clamp(40px, 8vw, 100px);
            line-height: 1;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }

        .product-section {
            padding: 100px 6%;
        }

        .product-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0px;
            padding: 40px;
            text-align: center;
            transition: 0.5s;
        }
        
        .product-card:hover {
            background: rgba(255, 255, 255, 0.07);
            border-color: rgba(212, 175, 55, 0.5);
        }

        .btn-yolu {
            display: inline-block !important;
            padding: 12px 40px !important;
            border: 1px solid #fff !important;
            color: #fff !important;
            text-decoration: none !important;
            font-size: 12px !important;
            letter-spacing: 2px !important;
            margin-top: 20px !important;
            transition: 0.3s !important;
        }
        
        .btn-yolu:hover {
            background: #fff !important;
            color: #050a14 !important;
            text-decoration: none !important;
        }

        .btn-yolu:visited {
            color: #fff !important;
            text-decoration: none !important;
        }

        .moon-bg {
            position: absolute;
            top: 10%;
            right: 10%;
            width: 150px;
            height: 150px;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%;
            filter: blur(30px);
        }

        [data-testid="stHeader"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # NAVEGAÇÃO
    st.markdown("""
    <div class="nav-yolu">
        <div class="logo-yolu">YOLU</div>
        <div style="display: flex; gap: 40px;">
            <a href="#conceito" class="nav-link">CONCEITO</a>
            <a href="#produtos" class="nav-link">PRODUTOS</a>
            <a href="#contato" class="nav-link">CONTATO</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # HERO
    st.markdown("""
    <div class="hero-yolu">
        <div class="moon-bg"></div>
        <p style="letter-spacing: 8px; font-size: 12px; margin-bottom: 30px;">BELEZA QUE NASCE À NOITE</p>
        <h1 class="hero-title-main serif-yolu">A Night Calm<br>Experience</h1>
        <p style="max-width: 600px; font-size: 14px; opacity: 0.8; line-height: 2;">
            Reparação profunda enquanto você dorme. <br>
            Sinta a tranquilidade da noite em cada fio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # CONCEITO
    st.markdown("""
    <div id="conceito" style="padding: 150px 15%; text-align: center;">
        <h2 class="serif-yolu" style="font-size: 42px; margin-bottom: 40px;">Por que Cuidados Noturnos?</h2>
        <p style="font-size: 16px; line-height: 2.2; opacity: 0.7;">
            Durante a noite, o seu cabelo está livre das agressões externas do dia. 
            É o momento perfeito para a penetração intensa de nutrientes. 
            Nossa fórmula inspirada no "sono reparador" protege as cutículas do atrito com o travesseiro, 
            garantindo um despertar radiante.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # PRODUTOS
    st.markdown('<div id="produtos" class="product-section">', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600" style="width:100%; margin-bottom:30px; opacity:0.9;">
            <h3 class="serif-yolu" style="font-size: 28px;">Calm Night Repair</h3>
            <p style="font-size: 12px; color: #aaa; margin: 20px 0;">SHAMPOO & TRATAMENTO</p>
            <p style="font-size: 14px; line-height: 1.8;">Para cabelos secos e indisciplinados. Foco em hidratação profunda.</p>
            <a href="https://www.google.com/" target="_blank" class="btn-yolu">SAIBA MAIS</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600" style="width:100%; margin-bottom:30px; opacity:0.9;">
            <h3 class="serif-yolu" style="font-size: 28px;">Relax Night Repair</h3>
            <p style="font-size: 12px; color: #aaa; margin: 20px 0;">CUIDADO INTENSIVO</p>
            <p style="font-size: 14px; line-height: 1.8;">Para cabelos danificados por processos químicos. Foco em reconstrução.</p>
            <a href="https://www.google.com/" target="_blank" class="btn-yolu">SAIBA MAIS</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
    <div id="contato" style="padding: 100px 6% 40px 6%; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 100px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <h2 class="logo-yolu" style="margin-bottom: 20px;">YOLU</h2>
                <p style="font-size: 11px; opacity: 0.5;">© 2026 YOLU | I-ne Co., Ltd. <br> Todos os direitos reservados.</p>
            </div>
            <div style="text-align: right; font-size: 11px; letter-spacing: 2px;">
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">INSTAGRAM</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">TWITTER</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">REVIEWS</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ CLIENTE NÃO ENCONTRADO
else:
    st.error(f"❌ Cliente '{cliente}' não encontrado!")
    st.info("📌 Use: `?cliente=paix` ou `?cliente=yolu`")
