import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image


st.set_page_config(page_title='Web Title',page_icon='💻',layout='wide')


# ---- ASSETS ----
lottie_coding = 'https://lottie.host/db140f34-106c-48c1-a45f-cd9f7aaab009/FOFIW7oaZi.json'
lottie_duvida = 'https://lottie.host/3fb172d7-1242-437a-a4a9-b8a5480595da/zeugrmJD3j.json'
lottie_duvida1 = 'https://lottie.host/37f9a371-73d5-4083-a756-73730abed6bd/ayy80UX1PH.json'
lottie_contact = 'https://lottie.host/795d2878-cfbf-4191-b111-b8e99dfd55e5/q967GDG1qO.json'



def buscarUrl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def localCSS(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

localCSS('style/style.css')

with st.container():
    st.title('Olá essa é minha Landing Page')
    st.subheader('Me chamo Miguel e sou programador! 🌐')
    st.write('Trabalho com automação e criação de landingPage e abaixo terá os meus projetos!')

with st.container():
    st.write('---')
    col_esquerda,col_direita = st.columns(2)
    with col_esquerda:
        st.write('##')
        st.subheader('Projetos:')
        st.write('''
        - Disparo automático de mensagens (Whatsapp)
        - Exportação de contatos automáticos (Whatsapp)
        - Criação de Landing Page em Python
        - Criação de WebSite em Python
        - Dashboards de dados em Python
        - Coleta de Leads (Lista de clientes)''')

    with col_direita:
        st_lottie(lottie_coding,height=250,key='coding')

with st.container():
    st.write('---')
    col_animacao, col_texto = st.columns((1,2))
    with col_animacao:
        st_lottie(lottie_duvida,height=250,key=True)

    with col_texto:
        st.header('Como funciona o Disparo automático?')
        st.write('''
        O programa irá pegar uma lista de contatos em CSV. \n
        E vai mandar mensagem no WhatsApp para cada contato dessa lista! \n
        E claro a mensagem é totalmente personalizada!!
        ''')

with st.container():
    st.write('---')
    col_esquerda,col_direita = st.columns(2)
    with col_esquerda:
        st.header('Como funciona a exportação de contatos?')
        st.write('''
        O programa irá entrar no grupo de whatsapp através de um link

        E irá fazer essa coleta de todos os contatos (não salvos) do grupo

        Após a coletagem irá salvar o arquivo em CSV''')

    with col_direita:
        st_lottie(lottie_duvida1,height=250)

with st.container():
    st.write('---')
    html_code = """
        <div style="display: flex; justify-content: center; align-items: center; height: 20vh;">
          <h2 style="color='white';">Tem dúvidas ou quer pedir o seu projeto? Entre em contato abaixo!</h2>
        </div>
        """

    st.markdown(html_code,unsafe_allow_html=True)

    col_esquerda,col_direita = st.columns(2)
    with col_esquerda:
        contato_form = """
             <form action="https://formsubmit.co/sitepythonstream@gmail.com" method="POST">
                 <input type="hidden" name="_captcha" value="false">
                 <input type="text" name="name" placeholder="Seu nome" required>
                 <input type="email" name="email" placeholder="Seu email" required>
                 <textarea name="mensagem" placeholder="Sua mensagem aqui" required></textarea>
                 <button type="submit">Enviar</button>
            </form>
            """
        with col_esquerda:
            st.markdown(contato_form,
                        unsafe_allow_html=True)  # O Markdown do Streamlit é um componente que permite exibir texto formatado de acordo com a sintaxe Markdown
        with col_direita:
            st_lottie(lottie_contact, height=300, key='contact')
            st.empty()