
import streamlit as st
import pandas as pd

st.title("Radar de Vagas DS")
st.write("**Escopo**: Ao consolidar e analisar as competências requisitadas por cada empresa, o projeto apoia a inserção de profissionais no mercado de trabalho, contribuindo para a geração de empregos e o desenvolvimento de uma força de trabalho com qualificação alinhada ao mercado. Isso não só ajuda os profissionais a encontrar melhores oportunidades de trabalho, mas também fortalece a economia ao atender à demanda das empresas por talentos qualificados. Este visa atender à ODS 8 (Trabalho Decente e Crescimento Econômico).")
st.write("""
**Objetivos**: Desenvolver uma aplicação web que consolide anúncios de vagas de cientista de dados no LinkedIn, analisando as competências e funções mais solicitadas por nível de vaga.
* Coletar dados de anúncios de vagas de cientista de dados no LinkedIn.
* Utilizar modelo LLM para analisar descrições de vagas e identificar competências e funções especificadas.
* Desenvolver visualizações em Streamlit para apresentar os resultados.
* Oferecer insights para candidatos, recrutadores e instituições de ensino sobre tendências de mercado.
""")
