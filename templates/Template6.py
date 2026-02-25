import streamlit as st

def render():
    # --- CSS DE PRECISÃO (ESTILO BAUTZ) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&family=JetBrains+Mono:wght@400&display=swap');

        :root {
            --bautz-black: #1a1a1a;
            --bautz-gray: #f5f5f7;
            --bautz-border: #e0e0e0;
            --bautz-accent: #0047bb; /* Azul Técnico */
        }

        .stApp {
            background-color: white;
            color: var(--bautz-black);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia Industrial */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: -1px;
        }

        .mono {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            text-transform: uppercase;
            color: #888;
        }

        /* 1 & 2. HERO - A ESTRUTURA */
        .hero-bautz {
            padding: 150px 8% 100px 8%;
            border-bottom: 1px solid var(--bautz-border);
            background: var(--bautz-gray);
        }
        .hero-h1 { font-size: clamp(40px, 6vw, 80px); line-height: 0.9; margin-bottom: 40px; }
        .hero-sub { font-size: 20px; max-width: 700px; color: #666; font-weight: 300; line-height: 1.6; }

        /* 3 & 4. TEMPLATES - GRID DE ENGENHARIA */
        .template-grid-item {
            border: 1px solid var(--bautz-border);
            background: white;
            transition: 0.3s;
            height: 100%;
        }
        .template-grid-item:hover {
            border-color: var(--bautz-accent);
        }
        .specs-box {
            padding: 20px;
            border-top: 1px solid var(--bautz-border);
        }

        /* 6. É PARA VOCÊ QUE - MÓDULOS */
        .module-card {
            padding: 40px;
            border-left: 1px solid var(--bautz-accent);
            background: white;
            margin-bottom: 20px;
        }

        /* 7. PASSO A PASSO - FLUXO DE TRABALHO */
        .workflow-line {
            display: flex;
            align-items: flex-start;
            gap: 30px;
            padding: 40px 0;
            border-top: 1px solid var(--bautz-border);
        }

        /* 8. PREÇOS - UNIDADES DE NEGÓCIO */
        .price-industrial {
            border: 1px solid var(--bautz-border);
            padding: 40px;
        }
        .price-industrial.active {
            background: var(--bautz-black);
            color: white;
        }

        /* Botão Técnico */
        div.stButton > button {
            background: var(--bautz-black);
            color: white;
            border: none;
            padding: 15px 35px;
            border-radius: 0;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: var(--bautz-accent);
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO SECTION ---
    st.markdown("""
    <div class="hero-bautz">
        <p class="mono">Codeless Architecture v2.0</p>
        <h1 class="hero-h1">SITES DE ALTA<br>PRECISÃO.</h1>
        <p class="hero-sub">
            Desenvolva a sua presença digital com a eficiência de um processo industrial. 
            Templates otimizados para velocidade, conversão e autonomia total.
        </p>
    """, unsafe_allow_html=True)
    st.button("CONFIGURAR AGORA")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- 3 & 4. TEMPLATES (SHOWCASE TÉCNICO) ---
    st.markdown('<div style="padding: 100px 8%;">', unsafe_allow_html=True)
    st.markdown('<p class="mono">// CATÁLOGO DE COMPONENTES</p>', unsafe_allow_html=True)
    st.markdown('<h2 style="margin-bottom: 60px;">MODELOS DISPONÍVEIS</h2>', unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3, gap="medium")

    def render_bautz_item(col, name, ref, img):
        with col:
            st.markdown(f"""
            <div class="template-grid-item">
                <img src="{img}" style="width:100%; height:250px; object-fit:cover; filter: grayscale(1);">
                <div class="specs-box">
                    <p class="mono" style="font-size:10px;">REF: {ref}</p>
                    <h3 style="font-size:20px; margin: 10px 0;">{name}</h3>
                    <p style="font-size:13px; color:#888;">Estrutura modular com 100% de pontuação no Core Web Vitals.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"INSPECIONAR {ref}", key=ref)

    render_bautz_item(t1, "STRUCTURAL MINIMAL", "BTZ-01", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600")
    render_bautz_item(t2, "DYNAMIC FLOW", "BTZ-02", "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600")
    render_bautz_item(t3, "CORPORATE CORE", "BTZ-03", "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=600")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. PROVA SOCIAL (LOGOS EM GRID) ---
    st.markdown("""
    <div style="padding: 60px 8%; border-top: 1px solid var(--bautz-border); border-bottom: 1px solid var(--bautz-border); display: flex; justify-content: space-between; align-items: center; opacity: 0.5;">
        <span class="mono">TRUSTED BY INDUSTRY LEADERS:</span>
        <span style="font-weight:900; font-size:20px;">MATTEL</span>
        <span style="font-weight:900; font-size:20px;">SIEMENS</span>
        <span style="font-weight:900; font-size:20px;">BMW</span>
        <span style="font-weight:900; font-size:20px;">BASF</span>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. É PARA VOCÊ QUE ---
    st.markdown('<div style="padding: 100px 8%; background: var(--bautz-gray);">', unsafe_allow_html=True)
    st.markdown('<h2 style="margin-bottom: 50px;">APLICAÇÕES DO SISTEMA</h2>', unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)

    with col_v1:
        st.markdown('<div class="module-card"><p class="mono">01 / AUTONOMIA</p><h3>Crie e customize em minutos sem depender de terceiros ou agências lentas.</h3></div>', unsafe_allow_html=True)
        st.markdown('<div class="module-card"><p class="mono">02 / RENTABILIDADE</p><h3>Venda sites profissionais com margem de lucro industrial para o mercado B2B.</h3></div>', unsafe_allow_html=True)
    with col_v2:
        st.markdown('<div class="module-card"><p class="mono">03 / PERFORMANCE</p><h3>Aumente a conversão dos seus produtos com layouts validados por testes de stress.</h3></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 7. PASSO A PASSO (WORKFLOW) ---
    st.markdown('<div style="padding: 100px 8%;">', unsafe_allow_html=True)
    st.markdown('<h2>FLUXO DE IMPLEMENTAÇÃO</h2>', unsafe_allow_html=True)

    def render_flow(num, title, desc):
        st.markdown(f"""
        <div class="workflow-line">
            <h1 style="color: var(--bautz-accent); margin:0;">{num}</h1>
            <div>
                <h4 style="margin:0;">{title}</h4>
                <p style="color:#666; max-width: 500px;">{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    render_flow("01", "AQUISIÇÃO DO MÓDULO", "Acesso imediato ao repositório de códigos fonte após a validação.")
    render_flow("02", "ASSEMBLY (MONTAGEM)", "Substitua textos e imagens seguindo o nosso manual de diretrizes visuais.")
    render_flow("03", "DEPLOYMENT", "Conecte o seu domínio e publique o site em servidores de alta velocidade.")
    render_flow("04", "OPERAÇÃO", "Seu site está pronto para gerar resultados com manutenção zero.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 8. PREÇOS (TABELA INDUSTRIAL) ---
    st.markdown('<div style="padding: 100px 8%; background: white;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center; margin-bottom:60px;">PLANOS DE ACESSO</h2>', unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3, gap="small")

    with p1:
        st.markdown('<div class="price-industrial"><p class="mono">BASIC UNIT</p><h1>R$ 97</h1><hr><p>1 Template Modular</p><p>Manual de Montagem</p></div>', unsafe_allow_html=True)
        st.button("ADQUIRIR BASIC", key="b1")

    with p2:
        st.markdown('<div class="price-industrial active"><p class="mono" style="color:var(--bautz-accent)">FULL STACK</p><h1>R$ 197</h1><hr><p>Todos os Templates</p><p>Suporte Técnico Direto</p><p>Updates de Engenharia</p></div>', unsafe_allow_html=True)
        st.button("ADQUIRIR FULL", key="b2")

    with p3:
        st.markdown('<div class="price-industrial"><p class="mono">ENTERPRISE</p><h1>R$ 497</h1><hr><p>Licença Comercial</p><p>Whitelabel Ready</p><p>Consultoria de Deploy</p></div>', unsafe_allow_html=True)
        st.button("ADQUIRIR ENTERPRISE", key="b3")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 9. FAQ ---
    st.markdown('<div style="padding: 100px 20%; background: var(--bautz-gray);">', unsafe_allow_html=True)
    with st.expander("O CÓDIGO É OTIMIZADO PARA SEO?"):
        st.write("Sim, todos os modelos seguem a semântica correta de HTML5 para máxima indexação.")
    with st.expander("POSSO ALTERAR AS CORES E FONTES?"):
        st.write("Absolutamente. O sistema é modular e permite alterações rápidas no ficheiro de estilos.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 60px 8%; border-top: 1px solid var(--bautz-border); display: flex; justify-content: space-between; font-size: 11px; color: #999;">
        <span>SITE PRO / ENGINEERING DIVISION</span>
        <span>© 2026 ALL RIGHTS RESERVED</span>
        <span class="mono">BUILD_V.4.0.1</span>
    </div>
    """, unsafe_allow_html=True)

# Execução direta se o script for rodado sozinho
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    render()
