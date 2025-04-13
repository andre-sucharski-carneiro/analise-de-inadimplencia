import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

# Configuração da página
# Garantindo que o título da página seja codificado corretamente em UTF-8
st.set_page_config(
    page_title="Análise de Inadimplência",
    page_icon="📉",  # Emoji compatível com Streamlit
    layout="wide",
)

# Título principal
st.markdown("# 📊 Análise Exploratória da Previsão de Renda")
st.markdown("Este painel apresenta visualizações exploratórias com base nas variáveis que influenciam a renda dos clientes de uma instituição financeira. A análise busca identificar padrões relevantes para futuras etapas de modelagem preditiva.")

# Leitura dos dados
url = "https://raw.githubusercontent.com/andre-sucharski-carneiro/analise-de-inadimplencia/main/projeto%202/input/previsao_de_renda.csv"
try:
    renda = pd.read_csv(url)
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

# Gráficos ao longo do tempo
st.markdown("---")
st.markdown("## 🕒 Gráficos Temporais")
st.markdown("As visualizações abaixo mostram como a renda se comporta ao longo do tempo em relação a variáveis categóricas.")

fig, ax = plt.subplots(8, 1, figsize=(12, 70))

# Correção: Evitar uso inadequado da função plot diretamente em DataFrames com ax
sns.histplot(data=renda, x='renda', hue='posse_de_imovel', kde=True, ax=ax[0])
ax[0].set_title("Distribuição da renda por posse de imóvel")
ax[0].legend(title="Posse de Imóvel")

sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
ax[1].set_title("Renda ao longo do tempo por posse de imóvel")

sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
ax[2].set_title("Renda ao longo do tempo por posse de veículo")

sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
ax[3].set_title("Renda ao longo do tempo por quantidade de filhos")

sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
ax[4].set_title("Renda ao longo do tempo por tipo de renda")

sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
ax[5].set_title("Renda ao longo do tempo por nível de educação")

sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
ax[6].set_title("Renda ao longo do tempo por estado civil")

sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
ax[7].set_title("Renda ao longo do tempo por tipo de residência")

sns.despine()
st.pyplot(fig)

# Gráficos bivariados
st.markdown("---")
st.markdown("## 📈 Gráficos Bivariados")
st.markdown("As barras representam a média da renda em função das variáveis categóricas. Esses gráficos ajudam a entender o impacto direto de cada categoria na variável alvo.")

fig2, ax = plt.subplots(7, 1, figsize=(12, 50))
sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax[0])
ax[0].set_title("Renda média por posse de imóvel")

sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1])
ax[1].set_title("Renda média por posse de veículo")

sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2])
ax[2].set_title("Renda média por quantidade de filhos")

sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3])
ax[3].set_title("Renda média por tipo de renda")

sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4])
ax[4].set_title("Renda média por nível de educação")

sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5])
ax[5].set_title("Renda média por estado civil")

sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6])
ax[6].set_title("Renda média por tipo de residência")

sns.despine()
st.pyplot(fig2)