import streamlit as st

def render():
    # --- CSS HGQ COACHING STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Open+Sans:wght@400;600&display=swap');

        :root {
            --HGQ-blue: #003366;
            --HGQ-accent: #ffcc00;
            --HGQ-text: #333333;
            --HGQ-bg-gray: #f2f2f2;
        }

        .stApp {
            background-color: white;
            color: var(--HGQ-text);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia de Alta Conversão */
        html, body, [class*="css"] {
            font-family: 'Open Sans', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            color: var(--HGQ-blue);
        }

        /* 1 & 2. HERO - PROMETIDA E AUTORIDADE */
        .hero-HGQ {
            background: linear-gradient(90deg, #003366 40%, rgba(0,51,102,0.8) 100%), 
                        url('https://images.unsplash.com/photo-1475721027785-f74dea327912?w=1600');
            background-size: cover;
            background-position: center;
            padding: 120px 10%;
            color: white;
            min-height: 80vh;
            display: flex;
            align-items: center;
        }

        .hero-h1 { font-size: clamp(35px, 5vw, 60px); line-height: 1.1; color: white; margin-bottom: 20px; }
        .hero-sub { font-size: 22px; color: var(--HGQ-accent); font-weight: 700; margin-bottom: 30px; }

        /* 3 & 4. CARDS DE PROGRAMAS */
        .program-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            padding: 40px;
            text-align: center;
            height: 100%;
            border-top: 5px solid var(--HGQ-blue);
            transition: 0.3s;
        }
        .program-card:hover {
            transform: translateY(-10px);
            border-top-color: var(--HGQ-accent);
        }

        /* 5. SEÇÃO DE NÚMEROS */
        .stat-HGQ {
            background: var(--HGQ-blue);
            color: white;
            padding: 60px 10%;
            display: flex;
            justify-content: space-around;
            text-align: center;
        }

        /* 8. BOTÃO ESTILO HGQ */
        div.stButton > button {
            background: var(--HGQ-accent);
            color: var(--HGQ-blue);
            border: none;
            padding: 20px 50px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            font-size: 18px;
            border-radius: 50px;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 204, 0, 0.4);
            width: 100%;
        }
        div.stButton > button:hover {
            background: white;
            color: var(--HGQ-blue);
            transform: scale(1.05);
        }

        /* 9. DEPOIMENTOS */
        .testimony-box {
            background: var(--HGQ-bg-gray);
            padding: 30px;
            border-radius: 15px;
            font-style: italic;
            border-left: 10px solid var(--HGQ-accent);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; background: white; position: sticky; top:0; z-index:999; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <div style="font-weight: 900; font-size: 30px; color: var(--HGQ-blue);">HGQ<span style="color:var(--HGQ-accent)">.</span></div>
        <div style="display: flex; gap: 30px; font-weight: 700; font-size: 13px; color: var(--HGQ-blue);">
            <span>TREINAMENTOS</span>
            <span>FORMAÇÕES</span>
            <span>SOBRE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO SECTION ---
    st.markdown("""
    <div class="hero-HGQ">
        <div style="max-width: 700px;">
            <p class="hero-sub">VOCÊ NASCEU PARA ALGO MAIOR</p>
            <h1 class="hero-h1">TRANSFORME A SUA PAIXÃO POR AJUDAR PESSOAS EM UMA PROFISSÃO LUCRATIVA.</h1>
            <p style="font-size: 18px; opacity: 0.9; margin-bottom: 40px;">Participe da maior comunidade de coaches e líderes que estão mudando o Brasil.</p>
    """, unsafe_allow_html=True)
    st.button("QUERO COMEÇAR AGORA")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # --- 3 & 4. PROGRAMAS (GRID) ---
    st.markdown('<div style="padding: 100px 10%;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 60px;">NOSSAS SOLUÇÕES</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    def render_HGQ_card(col, title, subtitle, desc):
        with col:
            st.markdown(f"""
            <div class="program-card">
                <h3 style="font-size: 22px;">{title}</h3>
                <p style="color: var(--HGQ-accent); font-weight: 700; margin-bottom: 20px;">{subtitle}</p>
                <p style="font-size: 15px; color: #666; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.button(f"VER DETALHES", key=title)

    render_HGQ_card(col1, "FORMAÇÃO EM COACHING", "O Começo de Tudo", "O treinamento número #1 para quem deseja dominar as ferramentas e começar a atender.")
    render_HGQ_card(col2, "MENTORIA IMPACTO", "Alta Performance", "Para profissionais que já faturam e querem escalar o seu negócio e impacto.")
    render_HGQ_card(col3, "LIDERANÇA PRO", "Gestão de Equipas", "Desenvolva a mentalidade de um líder que inspira e gera resultados fora da curva.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. NÚMEROS (IMPACTO) ---
    st.markdown("""
    <div class="stat-HGQ">
        <div><h1 style="color:var(--HGQ-accent); margin:0;">+100k</h1><p>Alunos Formados</p></div>
        <div><h1 style="color:var(--HGQ-accent); margin:0;">+15</h1><p>Anos de Experiência</p></div>
        <div><h1 style="color:var(--HGQ-accent); margin:0;">4.9/5</h1><p>Avaliação Média</p></div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. PROVA SOCIAL / DEPOIMENTOS ---
    st.markdown('<div style="padding: 100px 15%; background: white;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center;">O QUE DIZEM NOSSOS ALUNOS</h2><br><br>', unsafe_allow_html=True)
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown("""<div class="testimony-box">"Minha vida mudou completamente após o treinamento. Hoje tenho clareza de propósito e faturo 3x mais."<br><br><b>- Maria Oliveira</b></div>""", unsafe_allow_html=True)
    with t_col2:
        st.markdown("""<div class="testimony-box">"O melhor investimento que fiz na minha carreira. As ferramentas são práticas e os resultados imediatos."<br><br><b>- João Pedro</b></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 60px 10%; background: var(--HGQ-blue); color: white; text-align: center;">
        <h3 style="color: white; margin-bottom: 20px;">HGQ - INSTITUTO GERÔNIMO THEML</h3>
        <p style="font-size: 14px; opacity: 0.7;">Termos de Uso | Políticas de Privacidade</p>
        <p style="font-size: 12px; margin-top: 30px; opacity: 0.5;">© 2026 Todos os direitos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="HGQ | Coaching e Liderança")
    render()
