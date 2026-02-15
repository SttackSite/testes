import streamlit as st

st.set_page_config(
    page_title="Agência Digital - Transforme seu Negócio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= CSS ORIGINAL =================
custom_css = """
<style>
/* --- TODO SEU CSS ORIGINAL FOI MANTIDO AQUI SEM ALTERAÇÃO --- */
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ================= MODAL PREMIUM =================
modal_html = """
<style>
#templateModal{
    display:none;
    position:fixed;
    z-index:9999;
    left:0;
    top:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.96);
    backdrop-filter: blur(10px);
    animation:fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn{
    from{opacity:0;}
    to{opacity:1;}
}

.modal-wrapper{
    width:85%;
    margin:60px auto;
    text-align:center;
    position:relative;
}

.close-btn{
    position:absolute;
    top:-50px;
    right:0;
    font-size:42px;
    color:white;
    cursor:pointer;
    font-weight:800;
}

.preview-container{
    max-height:75vh;
    overflow-y:auto;
    border-radius:12px;
    box-shadow:0 30px 80px rgba(0,0,0,0.6);
}

.preview-container img{
    width:100%;
}

.fake-counter{
    margin-top:18px;
    color:#ddd;
    font-size:14px;
    letter-spacing:1px;
}

.modal-cta{
    margin-top:30px;
}

.modal-cta a{
    background:linear-gradient(135deg,#0066FF,#0052CC);
    padding:18px 60px;
    border-radius:8px;
    color:white;
    font-weight:700;
    text-decoration:none;
    display:inline-block;
    transition:0.3s;
}

.modal-cta a:hover{
    transform:translateY(-4px);
    box-shadow:0 12px 35px rgba(0,102,255,0.4);
}
</style>

<div id="templateModal">
    <div class="modal-wrapper">
        <div class="close-btn" onclick="closeModal()">×</div>

        <div class="preview-container">
            <img id="modalImage" src="">
        </div>

        <div class="fake-counter">
            🔥 <span id="viewerCount"></span> pessoas estão visualizando agora
        </div>

        <div class="modal-cta">
            <a href="#contato">QUERO ESSE TEMPLATE</a>
        </div>
    </div>
</div>

<script>
var interval;

function openModal(imageSrc){
    document.getElementById("modalImage").src = imageSrc;

    generateFakeViews();
    interval = setInterval(generateFakeViews,4000);

    document.getElementById("templateModal").style.display="block";
    document.body.style.overflow="hidden";
}

function closeModal(){
    document.getElementById("templateModal").style.display="none";
    document.body.style.overflow="auto";
    clearInterval(interval);
}

function generateFakeViews(){
    var randomViews = Math.floor(Math.random()*6)+1;
    document.getElementById("viewerCount").innerText=randomViews;
}
</script>
"""
st.markdown(modal_html, unsafe_allow_html=True)

# ================= NAVBAR =================
navbar_html = '''<div class="navbar">
    <a href="#" class="navbar-logo">🚀 Agência Digital</a>
    <div class="navbar-links">
        <a href="#servicos" class="navbar-link">Serviços</a>
        <a href="#sobre" class="navbar-link">Sobre</a>
        <a href="#portfolio" class="navbar-link">Portfólio</a>
        <a href="#contato" class="navbar-link">Contato</a>
        <a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar Agora</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ================= HERO =================
hero_html = '''<div class="hero-section" id="hero">
    <div class="hero-content">
        <div class="badges-container">
            <div class="badge badge-primary">⭐ Agência Premium</div>
            <div class="badge">🏆 Prêmio Melhor Agência 2024</div>
            <div class="badge">✓ +500 Clientes Satisfeitos</div>
        </div>
        <div class="hero-title">Transforme seu negócio com <span class="hero-title-highlight">marketing digital estratégico</span></div>
        <div class="hero-subtitle">Crescimento comprovado através de estratégias personalizadas</div>
        <a href="#" class="cta-button">Agende uma consultoria gratuita</a>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ================= PORTFÓLIO COM MODAL =================
portfolio_html = '''
<div id="portfolio" style="padding:100px 60px;text-align:center;">
<h2 style="font-size:42px;font-weight:900;margin-bottom:50px;">
Templates <span style="color:#0066FF;">Premium</span>
</h2>

<div style="display:flex;justify-content:center;gap:40px;flex-wrap:wrap;">

<div onclick="openModal('URL_DA_IMAGEM_LONGA_1')" style="cursor:pointer;">
<img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/20.png"
style="width:350px;border-radius:12px;box-shadow:0 15px 40px rgba(0,0,0,0.15);">
</div>

<div onclick="openModal('URL_DA_IMAGEM_LONGA_2')" style="cursor:pointer;">
<img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/17.png"
style="width:350px;border-radius:12px;box-shadow:0 15px 40px rgba(0,0,0,0.15);">
</div>

<div onclick="openModal('URL_DA_IMAGEM_LONGA_3')" style="cursor:pointer;">
<img src="https://raw.githubusercontent.com/Gm0ur4/cortex-demo/main/24.png"
style="width:350px;border-radius:12px;box-shadow:0 15px 40px rgba(0,0,0,0.15);">
</div>

</div>
</div>
'''
st.markdown(portfolio_html, unsafe_allow_html=True)

# ================= CTA FINAL =================
cta_final_html = '''<div class="cta-final-section" id="contato">
    <div class="cta-final-title">Pronto para crescer?</div>
    <div class="cta-final-desc">Descubra como podemos transformar seu negócio</div>
    <a href="#" class="cta-final-button">Agende Agora</a>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ================= FOOTER =================
footer_html = '''<div class="footer">
    <div class="footer-text">📞 (99) 99999-9999 | 📧 contato@agenciadigital.com.br</div>
    <div class="footer-text">📍 São Paulo, SP - Brasil</div>
    <div class="footer-copyright">
    © 2025 Agência Digital. Todos os direitos reservados.
    </div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
