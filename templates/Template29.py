import streamlit as st

def render():
    # --- CSS SPEEDTASK STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        :root {
            --speed-blue-dark: #0f172a;
            --speed-blue-main: #2563eb;
            --speed-blue-light: #eff6ff;
            --speed-text: #475569;
        }

        .stApp {
            background-color: white;
            color: var(--speed-blue-dark);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia Jakarta */
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        h1, h2, h3 {
            color: var(--speed-blue-dark);
            font-weight: 800;
            letter-spacing: -0.02em;
        }

        /* Hero Section SaaS */
        .hero-speed {
            padding: 120px 10% 80px 10%;
            background: linear-gradient(180deg, var(--speed-blue-light) 0%, #ffffff 100%);
            text-align: center;
        }

        .hero-h1 { 
            font-size: clamp(32px, 5vw, 64px); 
            line-height: 1.1;
            margin-bottom: 24px;
        }

        .highlight-blue { color: var(--speed-blue-main); }

        /* Funcionalidades - Grid Moderno */
        .feature-box {
            background: white;
            padding: 32px;
            border-radius: 24px;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
            height: 100%;
        }

        .feature-box:hover {
            border-color: var(--speed-blue-main);
            box-shadow: 0 20px 40px rgba(37, 99, 235, 0.05);
            transform: translateY(-5px);
        }

        .icon-wrapper {
            width: 48px;
            height: 48px;
            background: var(--speed-blue-light);
            color: var(--speed-blue-main);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 20px;
        }

        /* Botão SpeedTask (Corrigido) */
        div.stButton > button {
            background-color: var(--speed-blue-main) !important;
            color: white !important;
            border: none !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            transition: 0.3s !important;
            width: auto !important;
        }

        div.stButton > button:hover {
            background-color: var(--speed-blue-dark) !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
        }

        /* Dashboard Mockup */
        .mockup-container {
            margin: 60px auto 0 auto;
            max-width: 1000px;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 50px 100px rgba(15, 23, 42, 0.1);
            border: 8px solid white;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; background: white; border-bottom: 1px solid #f1f5f9;">
        <div style="font-weight: 800; font-size: 22px; color: var(--speed-blue-dark); display: flex; align-items: center; gap: 8px;">
            <div style="width: 32px; height: 32px; background: var(--speed-blue-main); border-radius: 8px;"></div>
            SpeedTask
        </div>
        <div style="display: flex; gap: 32px; font-weight: 600; font-size: 14px; color: var(--speed-text);">
            <span>Recursos</span>
            <span>Preços</span>
            <span>Empresas</span>
            <span style="color: var(--speed-blue-main)">Entrar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO ---
    st.markdown("""
    <div class="hero-speed">
        <h1 class="hero-h1">Gerencie tarefas em <br><span class="highlight-blue">velocidade recorde.</span></h1>
        <p style="font-size: 18px; color: var(--speed-text); max-width: 650px; margin: 0 auto 40px auto; line-height: 1.6;">
            A plataforma completa para equipes que não têm tempo a perder. Organize processos, acompanhe prazos e escale sua produtividade.
        </p>
    """, unsafe_allow_html=True)
    
    col_h1, col_h2, col_h3 = st.columns([1, 1, 1])
    with col_h2:
        st.button("TESTAR GRÁTIS AGORA")
    
    st.markdown("""
        <div class="mockup-container">
            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200" style="width: 100%;">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3 & 4. FEATURES GRID ---
    st.markdown('<div style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 60px;">Tudo o que você precisa para <span class="highlight-blue">entregar mais</span></h2>', unsafe_allow_html=True)
    
    f1, f2, f3 = st.columns(3, gap="large")

    def render_feature(col, title, icon, desc):
        with col:
            st.markdown(f"""
            <div class="feature-box">
                <div class="icon-wrapper">{icon}</div>
                <h3 style="font-size: 20px; margin-bottom: 12px;">{title}</h3>
                <p style="color: var(--speed-text); font-size: 14px; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    render_feature(f1, "Fluxos Ágeis", "⚡", "Crie quadros Kanban e listas de tarefas personalizadas para o ritmo do seu time.")
    render_feature(f2, "Relatórios Inteligentes", "📊", "Visualize gargalos e produtividade em tempo real com dashboards automáticos.")
    render_feature(f3, "Automação de Rotina", "🤖", "Elimine tarefas repetitivas integrando suas ferramentas favoritas em poucos cliques.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. SEÇÃO DE PROVA SOCIAL ---
    st.markdown("""
    <div style="background: var(--speed-blue-dark); color: white; padding: 80px 10%; text-align: center;">
        <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 12px; opacity: 0.6; margin-bottom: 40px;">Empresas que confiam na nossa velocidade</p>
        <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 40px; opacity: 0.8; filter: grayscale(100%) invert(100%);">
            <h2 style="color:white">LOGO 1</h2>
            <h2 style="color:white">LOGO 2</h2>
            <h2 style="color:white">LOGO 3</h2>
            <h2 style="color:white">LOGO 4</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. CTA FINAL ---
    st.markdown("""
    <div style="padding: 120px 10%; text-align: center; background: white;">
        <h2 style="font-size: 42px; margin-bottom: 24px;">Pronto para acelerar?</h2>
        <p style="color: var(--speed-text); margin-bottom: 40px;">Comece hoje mesmo seu teste de 14 dias. Sem cartão de crédito.</p>
    """, unsafe_allow_html=True)
    st.button("CRIAR MINHA CONTA", key="final_speed_cta")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 60px 10%; border-top: 1px solid #f1f5f9; display: flex; justify-content: space-between; font-size: 14px; color: var(--speed-text);">
        <div>© 2026 SpeedTask Software.</div>
        <div style="display: flex; gap: 24px;">
            <span>Segurança</span>
            <span>Privacidade</span>
            <span>Suporte</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="SpeedTask | Gestão de Tarefas Ágil")
    render()
