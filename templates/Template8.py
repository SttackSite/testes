import streamlit as st

def render():
    # --- CSS PATRUS TECH STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Roboto:wght@300;400&display=swap');

        :root {
            --patrus-orange: #ff6b00;
            --patrus-dark: #1a1a1a;
            --patrus-gray: #f4f4f4;
            --text-main: #333333;
        }

        .stApp {
            background-color: white;
            color: var(--text-main);
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
        }

        /* 1 & 2. HERO */
        .hero-patrus {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url('https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1600');
            background-size: cover;
            background-position: center;
            height: 70vh;
            display: flex;
            align-items: center;
            padding: 0 10%;
            color: white;
            border-bottom: 8px solid var(--patrus-orange);
        }

        .hero-title { font-size: clamp(30px, 5vw, 60px); line-height: 1.1; }
        .highlight { color: var(--patrus-orange); }

        /* 3 & 4. FEATURES */
        .tech-card {
            background: white;
            padding: 30px;
            border-bottom: 4px solid #ddd;
            transition: 0.3s;
            height: 100%;
        }
        .tech-card:hover {
            border-color: var(--patrus-orange);
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* 6. DIFERENCIAIS */
        .diff-box {
            display: flex;
            align-items: flex-start;
            gap: 20px;
            margin-bottom: 40px;
        }
        .icon-circle {
            background: var(--patrus-orange);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-weight: bold;
        }

        /* 8. SERVIÇOS */
        .service-card {
            background: var(--patrus-dark);
            color: white;
            padding: 40px;
            text-align: center;
            border-radius: 4px;
        }

        /* Botão Patrus (link estilizado) */
        .patrus-btn {
            display: inline-block;
            background: var(--patrus-orange);
            color: white !important;
            border: none;
            padding: 15px 40px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-radius: 4px;
            text-decoration: none !important;
            transition: background 0.3s, transform 0.3s;
            cursor: pointer;
            margin-top: 14px;
        }
        .patrus-btn:hover {
            background: #e66000;
            color: white !important;
            transform: scale(1.02);
        }
        .patrus-btn-full {
            display: block;
            width: 100%;
            box-sizing: border-box;
            text-align: center;
            margin-top: 20px;
        }

        /* Links da navbar */
        .nav-link {
            color: var(--text-main) !important;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            transition: color 0.2s;
        }
        .nav-link:hover {
            color: var(--patrus-orange) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee;">
        <div style="font-weight: 900; font-size: 24px; color: var(--patrus-dark);">PATRUS <span style="color:var(--patrus-orange)">TECH</span></div>
        <div style="display: flex; gap: 30px;">
            <a href="#ecossistema" class="nav-link">SOLUÇÕES</a>
            <a href="#diferenciais" class="nav-link">TECNOLOGIA</a>
            <a href="#verticais" class="nav-link">TRACKING</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO ---
    st.markdown("""
    <div class="hero-patrus" id="hero">
        <div style="max-width: 800px;">
            <p style="text-transform: uppercase; letter-spacing: 2px; font-weight: 700; margin-bottom: 10px;">Inovação em Movimento</p>
            <h1 class="hero-title">TECNOLOGIA QUE IMPULSIONA A <span class="highlight">LOGÍSTICA DO FUTURO.</span></h1>
            <p style="font-size: 18px; margin: 20px 0 40px 0; opacity: 0.9;">Dados em tempo real, inteligência artificial e a maior frota conectada do país.</p>
            <a href="#ecossistema" class="patrus-btn">CONHEÇA NOSSAS SOLUÇÕES</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3 & 4. TECNOLOGIAS (GRID) ---
    st.markdown('<div id="ecossistema" style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2>ECOSSISTEMA <span class="highlight">DIGITAL</span></h2><br>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    def render_tech(col, title, desc, img):
        with col:
            st.markdown(f"""
            <div class="tech-card">
                <img src="{img}" style="width:100%; height:180px; object-fit:cover; margin-bottom:20px; border-radius:4px;">
                <h3 style="font-size:18px;">{title}</h3>
                <p style="font-size:14px; color:#666; line-height:1.6;">{desc}</p>
                <a href="https://www.google.com/" target="_blank" class="patrus-btn patrus-btn-full">SAIBA MAIS</a>
            </div>
            """, unsafe_allow_html=True)

    render_tech(c1, "Telemetria Avançada", "Monitoramento em tempo real de cada unidade da frota, garantindo segurança e pontualidade.", "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=600")
    render_tech(c2, "IA de Roteirização",  "Algoritmos complexos que otimizam rotas para redução de custos e emissão de CO2.",         "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600")
    render_tech(c3, "Gestão 360°",         "Painéis de BI exclusivos para clientes com transparência total sobre a operação.",          "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. ESTATÍSTICAS ---
    st.markdown("""
    <div id="stats" style="background: var(--patrus-gray); padding: 80px 10%;">
        <div style="display: flex; justify-content: space-around; text-align: center;">
            <div><h1 style="color:var(--patrus-orange); font-size:50px;">+85</h1><p>CIDADES ATENDIDAS</p></div>
            <div><h1 style="color:var(--patrus-orange); font-size:50px;">3.5k</h1><p>VEÍCULOS CONECTADOS</p></div>
            <div><h1 style="color:var(--patrus-orange); font-size:50px;">100%</h1><p>RASTREAMENTO</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. DIFERENCIAIS ---
    st.markdown('<div id="diferenciais" style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2>POR QUE A <span class="highlight">PATRUS TECH?</span></h2><br><br>', unsafe_allow_html=True)

    d_col1, d_col2 = st.columns(2)

    with d_col1:
        st.markdown("""
        <div class="diff-box">
            <div class="icon-circle">01</div>
            <div>
                <h4 style="margin:0;">SEGURANÇA DE DADOS</h4>
                <p style="font-size:14px; opacity:0.7;">Infraestrutura em nuvem com criptografia de ponta a ponta.</p>
            </div>
        </div>
        <div class="diff-box">
            <div class="icon-circle">02</div>
            <div>
                <h4 style="margin:0;">EFICIÊNCIA OPERACIONAL</h4>
                <p style="font-size:14px; opacity:0.7;">Redução comprovada de 20% no tempo de entrega via otimização digital.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with d_col2:
        st.markdown("""
        <div class="diff-box">
            <div class="icon-circle">03</div>
            <div>
                <h4 style="margin:0;">SUSTENTABILIDADE TECH</h4>
                <p style="font-size:14px; opacity:0.7;">Uso de tecnologia para monitoramento e compensação de carbono.</p>
            </div>
        </div>
        <div class="diff-box">
            <div class="icon-circle">04</div>
            <div>
                <h4 style="margin:0;">SUPORTE ESPECIALIZADO</h4>
                <p style="font-size:14px; opacity:0.7;">Equipe de engenharia de dados disponível para integrações via API.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 8. SERVIÇOS/PLANOS ---
    st.markdown('<div id="verticais" style="padding: 100px 10%; background: var(--patrus-dark); color:white;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:white; text-align:center;">NOSSAS VERTICAIS</h2><br><br>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown("""
        <div class="service-card">
            <h4>LOGÍSTICA 4.0</h4>
            <p style="font-size:13px; opacity:0.6;">Sistemas integrados de gestão de armazém e transporte.</p>
            <a href="https://www.google.com/" target="_blank" class="patrus-btn patrus-btn-full">VER SOLUÇÃO</a>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="service-card" style="border: 1px solid var(--patrus-orange);">
            <h4>API CONNECT</h4>
            <p style="font-size:13px; opacity:0.6;">Integração direta com o seu ERP para automação total.</p>
            <a href="https://www.google.com/" target="_blank" class="patrus-btn patrus-btn-full">VER SOLUÇÃO</a>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="service-card">
            <h4>BI ANALYTICS</h4>
            <p style="font-size:13px; opacity:0.6;">Decisões baseadas em dados históricos e preditivos.</p>
            <a href="https://www.google.com/" target="_blank" class="patrus-btn patrus-btn-full">VER SOLUÇÃO</a>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 60px 10%; text-align: center; border-top: 1px solid #eee;">
        <p style="font-weight: 900; font-size: 20px;">PATRUS <span style="color:var(--patrus-orange)">TECH</span></p>
        <p style="font-size: 12px; color: #999;">© 2026 Patrus Transportes. Inovação em cada quilômetro.</p>
    </div>
    """, unsafe_allow_html=True)


# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Patrus Tech | Inovação")
    render()
