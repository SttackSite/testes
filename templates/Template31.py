import streamlit as st

def render():
    # --- BALANCE DESIGN LANGUAGE CSS ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Bento+Sans:wght@300;500&display=swap');

        :root {
            --bl-bg: #050505;
            --bl-accent: #f0f0f0;
            --bl-muted: #888888;
            --bl-border: rgba(255, 255, 255, 0.1);
            --bl-glass: rgba(255, 255, 255, 0.03);
        }

        .stApp { background-color: var(--bl-bg); color: var(--bl-accent); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            -webkit-font-smoothing: antialiased;
        }

        /* --- BACKGROUND GLOWS --- */
        .glow-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at 50% -20%, #1a1a1a 0%, #050505 60%);
            z-index: -1;
        }

        /* --- TYPOGRAPHY --- */
        .bl-h1 {
            font-size: clamp(40px, 8vw, 100px);
            font-weight: 400;
            letter-spacing: -0.05em;
            line-height: 0.9;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.5) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* --- CARDS (GLASSMORPhISM) --- */
        .bl-card {
            background: var(--bl-glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--bl-border);
            border-radius: 24px;
            padding: 40px;
            height: 100%;
            transition: all 0.5s cubic-bezier(0.2, 1, 0.2, 1);
        }

        .bl-card:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-5px);
        }

        /* --- BALANCE BUTTON (THE PILL) --- */
        div.stButton > button {
            background-color: white !important;
            color: black !important;
            border: none !important;
            padding: 12px 32px !important;
            font-weight: 600 !important;
            border-radius: 100px !important;
            transition: 0.4s !important;
            font-size: 15px !important;
            box-shadow: 0 0 20px rgba(255,255,255,0.2) !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 0 40px rgba(255,255,255,0.4) !important;
        }

        /* --- NAV --- */
        .bl-nav {
            padding: 30px 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            position: sticky; top: 0; z-index: 100;
        }

        .bl-badge {
            border: 1px solid var(--bl-border);
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--bl-muted);
            margin-bottom: 20px;
            display: inline-block;
        }
    </style>
    <div class="glow-bg"></div>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="bl-nav">
        <div style="font-weight: 500; font-size: 20px; letter-spacing: -0.5px;">Balance<span style="opacity:0.4">.farm</span></div>
        <div style="display: flex; gap: 40px; font-size: 13px; color: var(--bl-muted);">
            <span>Markets</span>
            <span>Vaults</span>
            <span>Security</span>
            <span style="color: white;">Launch App</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div style="padding: 120px 10% 80px 10%; text-align: center;">', unsafe_allow_html=True)
    st.markdown('<div class="bl-badge">Now Live on Mainnet</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="bl-h1">Stable yield<br>for the digital era.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: var(--bl-muted); font-size: 20px; max-width: 600px; margin: 0 auto 48px auto; line-height: 1.5;">Modernizing high-frequency yield farming through elegant automation and risk management.</p>', unsafe_allow_html=True)
    
    col_h1, col_h2, col_h3 = st.columns([1, 0.6, 1])
    with col_h2:
        st.button("Connect Wallet")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DASHBOARD PREVIEW (THE FLOATING ELEMENT) ---
    st.markdown("""
    <div style="padding: 0 10%; margin-bottom: 120px;">
        <div style="background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, transparent 100%); 
                    border: 1px solid var(--bl-border); border-radius: 32px; padding: 10px;">
            <img src="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1600" 
                 style="width: 100%; border-radius: 24px; opacity: 0.8; filter: saturate(0) brightness(1.2);">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- INFO GRID ---
    st.markdown('<div style="padding: 0 10% 120px 10%;">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="large")

    def render_bl_card(col, num, title, desc):
        with col:
            st.markdown(f"""
            <div class="bl-card">
                <div style="color: var(--bl-muted); font-size: 13px; margin-bottom: 100px;">{num}</div>
                <h3 style="font-size: 28px; font-weight: 500; margin-bottom: 20px;">{title}</h3>
                <p style="color: var(--bl-muted); line-height: 1.6; font-size: 15px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    render_bl_card(c1, "01", "Automated Harvest", "Our smart contracts execute compounding strategies 24/7 to maximize your returns.")
    render_bl_card(c2, "02", "Risk Mitigation", "Dynamic rebalancing ensures your capital is always allocated to the safest pools.")
    render_bl_card(c3, "03", "Full Transparency", "Real-time auditing of all vaults and strategies directly on the blockchain.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER DARK ---
    st.markdown("""
    <div style="padding: 100px 10%; border-top: 1px solid var(--bl-border); display: flex; justify-content: space-between;">
        <div>
            <h2 style="font-size: 24px; margin-bottom: 20px;">Balance</h2>
            <p style="color: var(--bl-muted); font-size: 14px;">The future of DeFi, balanced.</p>
        </div>
        <div style="display: flex; gap: 60px; font-size: 14px; color: var(--bl-muted);">
            <div>Twitter<br>Discord<br>GitHub</div>
            <div>Docs<br>Audit<br>Careers</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Balance | DeFi Automation")
    render()
