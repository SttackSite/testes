import streamlit as st

def render():
    # --- CSS SUSTENTÁVEL STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;800&family=Lora:italic,wght@0,400;1,500&display=swap');

        :root {
            --eco-green: #2d5a27;
            --eco-light: #f0f4ef;
            --eco-accent: #8eb486;
            --eco-dark: #1a2e19;
            --text-gray: #4a4a4a;
        }

        .stApp {
            background-color: var(--eco-light);
            color: var(--eco-dark);
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            color: var(--eco-dark);
            letter-spacing: -0.03em;
        }

        /* Hero */
        .hero-eco {
            padding: 120px 10%;
            background: linear-gradient(180deg, #e4ede3 0%, var(--eco-light) 100%);
            text-align: center;
            border-bottom: 1px solid rgba(45, 90, 39, 0.1);
        }

        .hero-h1 {
            font-size: clamp(34px, 6vw, 68px);
            line-height: 1;
            margin-bottom: 25px;
        }

        .eco-italic {
            font-family: 'Lora', serif;
            font-style: italic;
            font-weight: 500;
            color: var(--eco-green);
        }

        /* Cards Orgânicos */
        .eco-card {
            background: white;
            padding: 40px;
            border-radius: 40px 10px 40px 10px;
            border: 1px solid rgba(142, 180, 134, 0.2);
            transition: 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
            height: 100%;
        }

        .eco-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(45, 90, 39, 0.05);
            border-color: var(--eco-green);
        }

        /* Badge Carbono */
        .carbon-badge {
            display: inline-block;
            background: white;
            padding: 10px 20px;
            border-radius: 100px;
            border: 1px solid var(--eco-green);
            color: var(--eco-green);
            font-size: 12px;
            font-weight: 800;
            margin-bottom: 20px;
            text-transform: uppercase;
        }

        /* Botão Eco (link estilizado) */
        .eco-btn {
            display: inline-block;
            background-color: var(--eco-green);
            color: white !important;
            border: none;
            padding: 18px 45px;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 16px;
            border-radius: 100px;
            text-decoration: none !important;
            transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
            margin-top: 14px;
        }
        .eco-btn:hover {
            background-color: var(--eco-dark);
            color: white !important;
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(45, 90, 39, 0.2);
        }

        /* Links da navbar */
        .nav-link-eco {
            color: var(--text-gray) !important;
            text-decoration: none !important;
            font-weight: 500;
            font-size: 14px;
            transition: color 0.2s;
        }
        .nav-link-eco:hover {
            color: var(--eco-green) !important;
        }
        .nav-link-eco.active {
            color: var(--eco-green) !important;
            font-weight: 800;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 25px 10%; display: flex; justify-content: space-between; align-items: center; background: transparent;">
        <div style="font-weight: 800; font-size: 22px; color: var(--eco-green); display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 30px;">🌿</span> Website Sustentável
        </div>
        <div style="display: flex; gap: 35px; align-items: center;">
            <a href="#diferenciais" class="nav-link-eco">Manifesto</a>
            <a href="#impacto" class="nav-link-eco">Certificação</a>
            <a href="#diferenciais" class="nav-link-eco">Tecnologia</a>
            <a href="#footer" class="nav-link-eco active">CONTATO</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO ---
    st.markdown("""
    <div class="hero-eco" id="hero">
        <div class="carbon-badge">Otimizado para baixo consumo</div>
        <h1 class="hero-h1">Seu site pode ser mais <span class="eco-italic">rápido</span> e menos <span class="eco-italic">poluente.</span></h1>
        <p style="font-size: 19px; color: var(--text-gray); max-width: 750px; margin: 0 auto 40px auto; line-height: 1.6;">
            Desenvolvemos tecnologias web focadas em performance extrema e responsabilidade ambiental.
            O futuro da internet é <b>sustentável</b>.
        </p>
        <a href="#diferenciais" class="eco-btn">CERTIFIQUE SEU WEBSITE</a>
    </div>
    """, unsafe_allow_html=True)

    # --- 3 & 4. DIFERENCIAIS (GRID) ---
    st.markdown('<div id="diferenciais" style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 60px;">Por que ser sustentável?</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    def render_eco_card(col, title, desc, icon):
        with col:
            st.markdown(f"""
            <div class="eco-card">
                <div style="font-size: 40px; margin-bottom: 25px;">{icon}</div>
                <h3 style="font-size: 22px; margin-bottom: 15px;">{title}</h3>
                <p style="color: var(--text-gray); font-size: 15px; line-height: 1.7;">{desc}</p>
                <a href="https://www.google.com/" target="_blank" class="eco-btn" style="margin-top:25px; padding:12px 30px; font-size:13px;">SAIBA MAIS</a>
            </div>
            """, unsafe_allow_html=True)

    render_eco_card(col1, "Baixa Emissão",  "Reduzimos o tamanho dos arquivos e a requisição de servidores, diminuindo a pegada de carbono de cada acesso.", "🍃")
    render_eco_card(col2, "SEO Consciente", "Sites mais leves carregam instantaneamente, o que o Google ama. Sustentabilidade é a melhor estratégia de ranking.", "🔍")
    render_eco_card(col3, "Green Hosting",  "Hospedagem em servidores alimentados por fontes de energia 100% renováveis e limpas.", "🔋")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. SEÇÃO DE IMPACTO ---
    st.markdown("""
    <div id="impacto" style="background: var(--eco-green); color: white; padding: 100px 10%; border-radius: 0 100px 0 100px; margin: 0 5%;">
        <div style="display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap; gap: 50px;">
            <div>
                <h1 style="color: var(--eco-accent); font-size: 60px;">-40%</h1>
                <p style="font-weight: 300; letter-spacing: 1px;">NA EMISSÃO DE CO2</p>
            </div>
            <div>
                <h1 style="color: var(--eco-accent); font-size: 60px;">2.5x</h1>
                <p style="font-weight: 300; letter-spacing: 1px;">MAIS VELOCIDADE</p>
            </div>
            <div>
                <h1 style="color: var(--eco-accent); font-size: 60px;">100%</h1>
                <p style="font-weight: 300; letter-spacing: 1px;">ENERGIA LIMPA</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. CTA FINAL ---
    st.markdown("""
    <div id="cta" style="padding: 120px 10%; text-align: center;">
        <h2 style="font-size: 40px; margin-bottom: 25px;">Pronto para o próximo passo?</h2>
        <p style="color: var(--text-gray); margin-bottom: 45px; font-size: 18px;">Seja parte da mudança positiva no ecossistema digital.</p>
        <a href="https://www.google.com/" target="_blank" class="eco-btn">SOLICITAR ORÇAMENTO VERDE</a>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div id="footer" style="padding: 50px 10%; background: var(--eco-dark); color: white; display: flex; justify-content: space-between; font-size: 13px; opacity: 0.8;">
        <div>© 2026 Website Sustentável. Tecnologia com Propósito.</div>
        <div style="display: flex; gap: 30px;">
            <a href="https://www.google.com/" target="_blank" style="color:white; text-decoration:none;">Política de Privacidade</a>
            <a href="https://www.google.com/" target="_blank" style="color:white; text-decoration:none;">Eco-Design Guide</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Website Sustentável | Eco-Design")
    render()
