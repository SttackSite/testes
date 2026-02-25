import streamlit as st
import sys
import os
import importlib

# ✅ Adicionar pasta templates ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'templates'))

# ✅ CONFIGURAÇÃO INICIAL
st.set_page_config(
    page_title="Multi-Cliente",
    page_icon="🌐",
    layout="wide"
)

# ✅ DICIONÁRIO DE TEMPLATES (Mapeamento de nomes para módulos)
TEMPLATES = {
    "template1": "Template1",
    "template2": "Template2",
    "template3": "Template3",
    "template4": "Template4",
    "template5": "Template5",
    "template6": "Template6",
    "template7": "Template7",
    "template8": "Template8",
    "template9": "Template9",
    "template10": "Template10",
    "template11": "Template11",
    "template12": "Template12",
    "template13": "Template13",
    "template14": "Template14",
    "template15": "Template15",
    "template16": "Template16",
    "template17": "Template17",
    "template18": "Template18",
    "template19": "Template19",
    "template20": "Template20",
    "template21": "Template21",
    "template22": "Template22",
    "template23": "Template23",
    "template24": "Template24",
    "template25": "Template25",
    "template26": "Template26",
    "template27": "Template27",
    "template28": "Template28",
    "template29": "Template29",
    "template30": "Template30",
    "template31": "Template31",
    "template32": "Template32",
    "template33": "Template33",
    "template34": "Template34",
    "template35": "Template35",
    "template36": "Template36",
    "template37": "Template37",
    "template38": "Template38",
}

# ✅ OBTER CLIENTE DA URL
cliente = st.query_params.get("cliente", "template1").lower()

# ✅ CARREGAR TEMPLATE CORRETO
if cliente in TEMPLATES:
    try:
        # Importar dinamicamente o módulo
        modulo = importlib.import_module(TEMPLATES[cliente])
        
        # Chamar a função render()
        if hasattr(modulo, 'render'):
            modulo.render()
        else:
            st.error(f"❌ Erro: O arquivo {TEMPLATES[cliente]}.py não tem uma função `render()`")
    except ImportError as e:
        st.error(f"❌ Erro ao carregar template: {e}")
else:
    st.error(f"❌ Cliente '{cliente}' não encontrado!")
    st.info("📌 Use: `?cliente=template1` até `?cliente=template28`")
    
    # Mostrar lista de templates disponíveis
    st.markdown("### 📋 Templates Disponíveis:")
    cols = st.columns(4)
    for idx, (key, value) in enumerate(TEMPLATES.items()):
        with cols[idx % 4]:
            st.markdown(f"- `?cliente={key}`")
