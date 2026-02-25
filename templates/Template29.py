import streamlit as st

def render():
    # --- CSS IPDV ONLINE STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;800&family=Inter:wght@400;500&display=swap');

        :root {
            --ipdv-blue-dark: #0a192f;
            --ipdv-blue-main: #00d2ff;
            --ipdv-cyan: #00f2ff;
            --ipdv-text-gray: #64748b;
            --ipdv-bg-soft: #f8fafc;
        }

        .stApp {
            background-color: white;
            color: var(--ipdv-blue-dark);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia Sora (Moderna e Tech) */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Sora', sans-serif;
            font-weight: 800;
            color: var(--ipdv-blue-dark);
        }

        /* Hero Section - Inteligência no PDV */
        .hero-ipdv {
            padding: 100px 10%;
            background: linear-gradient(135deg, var(--ipdv-blue-dark) 0%, #112240 100%);
            color: white;
            position: relative;
            overflow: hidden;
            border-bottom: 5px solid var(--ipdv-blue-main);
        }

        .hero-ipdv h1 { color: white; font-size: clamp(32px, 5vw, 52px); line-height: 1.2; }
        .ipdv-highlight { color: var(--ipdv-blue-main); }

        /* Cards de Funcionalidades */
        .ipdv-card {
            background: white;
            padding: 35px;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            transition: all 0.4s ease;
            height: 100%;
            position: relative;
        }

        .ipdv-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 210, 255, 0.1);
            border-color: var(--ipdv-blue-main);
        }

        .ipdv-icon {
            font-size: 32px;
            margin-bottom: 20px;
            display: inline-block;
        }

        /* Botão iPDV (Estilo Dashboard) */
        div.stButton > button {
            background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%) !important;
            color: white !important;
            border: none !important;
            padding: 14px 35px !important;
            font-family: 'Sora', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            transition: 0.3s !important;
            box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3) !important;
        }

        div.stButton > button:hover {
            transform: scale(1.03) !important;
            box-shadow: 0 8px 25px rgba(0, 210, 255, 0.5) !important;
        }

        /* Faixa de Clientes */
        .client-strip {
            padding: 40px 10%;
            background: var(--ipdv-bg-soft);
            display: flex;
            justify-content: space-around;
            align-items: center;
            opacity: 0.6;
            filter: grayscale(100%);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; background: white; border-bottom: 1px solid #eee;">
        <div style="font-weight: 800; font-size: 24px; color: var(--ipdv-blue-dark);">iPDV<span style="color:var(--ipdv-blue-main)">_</span>ONLINE</div>
        <div style="display: flex; gap: 30px; font-weight: 600; font-size: 13px; color: var(--ipdv-text-gray);">
            <span>PLATAFORMA</span>
            <span>SOLUÇÕES</span>
            <span>CASES</span>
            <span style="color: var(--ipdv-blue-main)">SOLICITAR DEMO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO ---
    st.markdown("""
    <div class="hero-ipdv">
        <div style="max-width: 800px;">
            <p style="text-transform: uppercase; letter-spacing: 2px; font-weight: 600; font-size: 14px; margin-bottom: 20px; color: var(--ipdv-cyan);">Trade Marketing Inteligente</p>
            <h1>Sua operação de campo guiada por <span class="ipdv-highlight">dados em tempo real.</span></h1>
            <p style="font-size: 18px; opacity: 0.8; margin: 30px 0 40px 0; line-height: 1.6;">
                A plataforma completa para gestão de promotores, auditoria de estoque e execução perfeita no ponto de venda.
            </p>
    """, unsafe_allow_html=True)
    st.button("QUERO MODERNIZAR MEU PDV")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # --- 3 & 4. CARDS DE FUNCIONALIDADES (GRID) ---
    st.markdown('<div style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 60px;">Controle total da sua execução</h2>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3, gap="large")

    def render_ipdv_card(col, title, desc, icon):
        with col:
            st.markdown(f"""
            <div class="ipdv-card">
                <div class="ipdv-icon">{icon}</div>
                <h3 style="font-size: 20px; margin-bottom: 15px;">{title}</h3>
                <p style="color: var(--ipdv-text-gray); font-size: 14px; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    render_ipdv_card(c1, "Check-in Geolocalizado", "Garanta que sua equipe esteja no lugar certo com validação via GPS e cercas digitais.", "📍")
    render_ipdv_card(c2, "Auditoria de Ruptura", "Identifique falta de produtos na gôndola e acione o repasse imediatamente para não perder vendas.", "🛒")
    render_ipdv_card(c3, "Pesquisas Customizadas", "Crie formulários inteligentes para coletar preços da concorrência e participação de mercado.", "📊")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. DASHBOARD PREVIEW ---
    st.markdown("""
    <div style="background: var(--ipdv-bg-soft); padding: 100px 10%;">
        <div style="display: flex; align-items: center; gap: 60px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <h2 style="font-size: 32px;"> dashboards que <span class="ipdv-highlight">falam.</span></h2>
                <p style="color: var(--ipdv-text-gray); font-size: 16px; margin-top: 20px; line-height: 1.8;">
                    Transforme fotos e formulários em indicadores de performance (KPIs). Acompanhe o ROI das suas ações de trade marketing em um painel intuitivo e potente.
                </p>
                <ul style="margin-top: 20px; color: var(--ipdv-blue-dark); font-weight: 500;">
                    <li>✓ Análise de Share de Gôndola</li>
                    <li>✓ Gestão de Alertas de Validade</li>
                    <li>✓ Ranking de Performance de Equipe</li>
                </ul>
            </div>
            <div style="flex: 1.2; min-width: 300px; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 30px 60px rgba(0,0,0,0.05);">
                <img src="https://images.unsplash.com/photo-1551288049-bbda4865cda1?w=800" style="width: 100%; border-radius: 10px;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. CTA FINAL ---
    st.markdown("""
    <div style="padding: 100px 10%; text-align: center; background: var(--ipdv-blue-dark); color: white;">
        <h2 style="color: white; font-size: 40px; margin-bottom: 25px;">Pronto para transformar sua execução?</h2>
        <p style="opacity: 0.7; margin-bottom: 40px; font-size: 18px;">Agende uma demonstração gratuita com nossos especialistas em varejo.</p>
    """, unsafe_allow_html=True)
    st.button("SOLICITAR DEMONSTRAÇÃO", key="ipdv_cta")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 40px 10%; background: white; border-top: 1px solid #eee; display: flex; justify-content: space-between; font-size: 12px; color: var(--ipdv-text-gray);">
        <div>© 2026 iPDV Online - Tecnologia para o Varejo.</div>
        <div>Siga-nos: LinkedIn / Instagram</div>
    </div>
    """, unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="iPDV | Inteligência de Campo")
    render()
