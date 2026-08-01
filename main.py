import streamlit as st

# 1. Configuração da página e SEO básico
st.set_page_config(
    page_title="Processamento de Dados e Automação para PMEs",
    page_icon="📊",
    layout="centered",  # 'centered' garante excelente leitura e responsividade mobile
    initial_sidebar_state="collapsed"
)

# Estilização CSS minimalista para ajustar espaçamentos e fontes
st.markdown("""
    <style>
    /* Remove margens excessivas no topo */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    /* Estilo de títulos */
    h1, h2, h3 {
        font-weight: 600;
        color: #1E293B;
    }
    /* Botão de contato em destaque */
    .stButton>button {
        width: 100%;
        background-color: #0F172A;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Cabeçalho / Hero Section
st.title("Transforme Dados Brutos em Decisões Inteligentes")
st.write("""
Ajudamos pequenas e médias empresas a automatizarem processos manuais 
e organizarem seus dados para economizar tempo e aumentar a lucratividade.
""")

st.divider()

# 3. Seção de Serviços
st.header("Nossos Serviços")

# Serviço 1
col1, col2 = st.columns([1, 1], vertical_alignment="center")

with col1:
    # Substitua 'imagem_servico_1.jpg' pelo caminho ou URL da sua imagem
    # use_container_width garante responsividade automática em telas menores
    st.image("i2.png", 
             caption="Automação de Fluxos de Trabalho", 
             use_container_width=True)

with col2:
    st.subheader("1. Automação de Processos")
    st.write("""
    Elimine tarefas repetitivas. Criamos rotinas automatizadas para integração 
    de sistemas, leitura de planilhas, geração de relatórios e envio de dados.
    """)

st.write("")  # Espaçamento vertical

# Serviço 2
col3, col4 = st.columns([1, 1], vertical_alignment="center")

with col3:
    st.subheader("2. Trativa e Estruturação de Dados")
    st.write("""
    Limpamos, organizamos e consolidamos dados de diferentes fontes 
    (Excel, sistemas internos, APIs) em painéis claros e prontos para uso.
    """)

with col4:
    # Substitua 'imagem_servico_2.jpg' pelo caminho ou URL da sua imagem
    st.image("i2.png", 
             caption="Tratamento e Integração", 
             use_container_width=True)

st.divider()

# 4. Diferenciais / Por que nos escolher
st.header("Por que automatizar com a gente?")
st.markdown("""
* **Eficiência:** Redução de erros manuais e ganho de tempo operacional.
* **Sob Medida:** Soluções enxutas e focadas no gargalo da sua empresa.
* **Segurança:** Trato rigoroso e confidencial com as suas informações.
""")

st.divider()

# 5. Seção de Contato
st.header("Entre em Contato")
st.write("Pronto para simplificar a gestão de dados da sua empresa? Fale conosco:")

# Formulário ou links diretos de contato
with st.container():
    st.write("📍 **Localização:** Atendimento Nacional / Remoto")
    st.write("📧 **E-mail:** contato@suaempresa.com.br")
    st.write("📱 **WhatsApp:** (00) 99999-9999")
    
    # Botão de ação (exemplo direcionando para o WhatsApp)
    whatsapp_link = "https://wa.me/5500999999999?text=Olá,%20gostaria%20de%20saber%20mais%20sobre%20os%20serviços%20de%20processamento%20de%20dados."
    st.link_button("Falar pelo WhatsApp", whatsapp_link, type="primary")

# Rodapé minimalista
st.markdown("---")
st.caption("© 2026 Sua Empresa de Processamento de Dados. Todos os direitos reservados.")