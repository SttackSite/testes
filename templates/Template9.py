import streamlit as st

def render():
    """Renderiza o template Dockyard Social - Edição Sofisticada"""
    
    # ❌ NÃO ALTERE: CSS de Alta Fidelidade
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&family=Oswald:wght@500;700&display=swap');

        :root {
            --dock-yellow: #ffcc00;
            --dock-black: #0e0e0e;
            --dock-white: #ffffff;
            --dock-gray: #f8f8f8;
        }

        /* Reset e Base */
        .stApp { background-color: var(--dock-white); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia Brutalista */
        h1, h2, h3 {
            font-family: 'Oswald', sans-serif;
            text-transform: uppercase;
            letter-spacing: -2px;
            line-height: 0.85;
            color: var(--dock-black);
        }

        /* Navegação VIP */
        .nav-dock {
            background-color: rgba(14, 14, 14, 0.98);
            backdrop-filter: blur(10px);
            color: var(--dock-yellow);
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 204, 0, 0.2);
        }

        .nav-link {
            color: white !important;
            text-decoration: none !important;
            font-family: 'Oswald';
            font-size: 14px;
            letter-spacing: 2px;
            transition: 0.4s;
            text-transform: uppercase;
        }

        .nav-link:hover { color: var(--dock-yellow) !important; }

        /* Hero Section Impacto */
        .hero-dock {
            background-color: var(--dock-yellow);
            padding: 120px 8%;
            clip-path: polygon(0 0, 100% 0, 100% 90%, 0% 100%);
            margin-bottom: -50px;
        }

        .hero-h1 { font-size: clamp(50px, 10vw, 130px); }

        /* Cards Estilo Galeria */
        .dock-card {
            background: var(--dock-white);
            border: 1px solid #ddd;
            overflow: hidden;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            margin-bottom: 20px;
        }
        
        .dock-card:hover {
            transform: translateY(-10px) rotate(1deg);
            box-shadow: 20px 20px 0px var(--dock-black);
            border-color: var(--dock-black);
        }

        .card-img-container {
            height: 300px;
            overflow: hidden;
            background: var(--dock-black);
        }

        .card-img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: 0.8s;
            opacity: 0.9;
        }

        .dock-card:hover img {
            transform: scale(1.1);
            opacity: 1;
        }

        /* Botões Sofisticados */
        .custom-btn {
            display: inline-block;
            background-color: var(--dock-black);
            color: var(--dock-yellow) !important;
            padding: 18px 45px;
            font-family: 'Oswald', sans-serif;
            font-size: 18px;
            text-decoration: none !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: 0.3s;
            border: 2px solid var(--dock-black);
            cursor: pointer;
            text-align: center;
        }

        .custom-btn:hover {
            background-color: transparent;
            color: var(--dock-black) !important;
            box-shadow: 8px 8px 0px var(--dock-yellow);
        }

        .announcement {
            background: var(--dock-black);
            color: var(--dock-yellow);
            padding: 12px;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 3px;
            text-align: center;
            font-family: 'Inter';
        }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: NAVEGAÇÃO ==========
    st.markdown('<div class="announcement">OPENING HOURS: FRI 5PM-11PM • SAT 12PM-11PM • SUN 12PM-8PM</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nav-dock">
        <div style="font-size: 28px; font-family: 'Oswald'; font-weight: 700; letter-spacing: -1px;">DOCKYARD<span style="color:white">.</span></div>
        <div style="display: flex; gap: 40px;">
            <a href="#" class="nav-link">O QUE ROLA</a>
            <a href="#" class="nav-link">FOOD</a>
            <a href="#" class="nav-link">DRINKS</a>
            <a href="#" class="nav-link" style="color:var(--dock-yellow) !important;">BOOK NOW</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 2: HERO ==========
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">STREET FOOD.<br>CRAFT BEER.<br><span style="color:white">REAL VIBES.</span></h1>
        <p style="font-family:'Inter'; font-size: 18px; max-width: 600px; margin-top: 30px; font-weight: 400; color: #111; line-height: 1.6;">
            The best street food vendors in Scotland, world-class cocktails, and an atmosphere that defines Glasgow's weekends.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 3: GRID DE CONTEÚDO ==========
    st.write("")
    st.write("")
    st.markdown('<div style="padding: 100px 8% 50px 8%;">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    def render_dock_card(col, title, tag, img_url):
        with col:
            st.markdown(f"""
            <div class="dock-card">
                <div class="card-img-container">
                    <img src="{img_url}">
                </div>
                <div style="padding: 30px;">
                    <p style="font-size: 12px; font-weight: 900; color: var(--dock-yellow); background: black; display: inline-block; padding: 2px 10px; margin-bottom: 15px;">{tag}</p>
                    <h2 style="font-size: 35px; margin: 0;">{title}</h2>
                </div>
            </div>
            """, unsafe_allow_html=True)

    render_dock_card(col1, "KITCHEN TAKEOVER", "10+ VENDORS", "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800")
    render_dock_card(col2, "CRAFT & COCKTAILS", "PREMIUM BAR", "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=800")
    render_dock_card(col3, "THE WAREHOUSE", "LIVE MUSIC", "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=800")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 4: CTA RESERVA ==========
    st.markdown("""
    <div style="background-color: var(--dock-gray); padding: 120px 8%; text-align: center; border-top: 1px solid #eee;">
        <h2 style="font-size: 70px; margin-bottom: 20px;">GET IN THE DOCK.</h2>
        <p style="font-family:'Inter'; font-size: 20px; color: #666; margin-bottom: 50px;">Entry is only £5. Support local, eat well, stay social.</p>
        <a href="#" class="custom-btn">SECURE YOUR TICKETS</a>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: FOOTER ==========
    st.markdown("""
    <div style="padding: 80px 8%; background: var(--dock-black); color: white;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 40px;">
            <div style="flex: 1; min-width: 300px;">
                <h2 style="color: var(--dock-yellow); font-size: 50px;">DOCKYARD<br>SOCIAL.</h2>
                <p style="opacity: 0.6; margin-top: 20px;">952 South St, Glasgow G14 0BX</p>
            </div>
            <div style="flex: 1; min-width: 200px; font-family: 'Oswald';">
                <p style="color: var(--dock-yellow); letter-spacing: 2px;">SOCIALS</p>
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 15px;">
                    <a href="#" class="nav-link" style="font-size: 24px;">INSTAGRAM</a>
                    <a href="#" class="nav-link" style="font-size: 24px;">TIKTOK</a>
                    <a href="#" class="nav-link" style="font-size: 24px;">FACEBOOK</a>
                </div>
            </div>
        </div>
        <div style="margin-top: 80px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; display: flex; justify-content: space-between; font-size: 11px; opacity: 0.5;">
            <span>© 2026 DOCKYARD SOCIAL GLASGOW</span>
            <span>POWERED BY STREAMLIT PRO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ❌ NÃO COLOQUE st.set_page_config() aqui se for usar em um multipage app.
# Se for rodar este arquivo sozinho, descomente a linha abaixo:
# if __name__ == "__main__": st.set_page_config(layout="wide"); render()
