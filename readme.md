# 💳 Análise de Churn de Clientes de Cartão de Crédito

Projeto completo de análise de dados e visualização em Power BI, com base no comportamento de mais de **10.000 clientes** de um banco emissor de cartões de crédito.

---

## 🎯 Objetivo

O objetivo é identificar os **principais fatores que influenciam a perda de clientes (churn)** e propor **estratégias de retenção** baseadas em dados.

---

## 📂 Estrutura do Projeto

credit-card-customer-churn/
├── data/ # Dados originais e tratados
├── notebooks/ # Notebooks de análise e EDA
├── scripts/ # Scripts Python para limpeza e tratamento
├── dashboard/ # Dashboard Power BI
├── img/ # Imagens e prints para o README
└── README.md # Documentação


---

## 🧠 Contexto do Negócio

Empresas financeiras dependem da **fidelização de clientes**.  
Com a base de dados de cartões de crédito, é possível entender:
- Quem são os clientes que **cancelam o cartão**?
- Quais características estão associadas à **maior lealdade**?
- Quais **ações estratégicas** o banco pode tomar para reduzir o churn?

---

## 🧹 Etapas do Projeto

### 1️⃣ Coleta e Preparação
- Importação do dataset `BankChurners.csv` (Kaggle)
- Tradução e padronização dos nomes das colunas para **português**
- Criação de variáveis derivadas:
  - `faixa_etaria`
  - `anos_relacionamento`
  - `valor_medio_transacao`
  - `percentual_limite_usado`
  - `alvo_churn` (1 = Cliente Perdido, 0 = Cliente Ativo)
- Tratamento de outliers e dados inconsistentes

### 2️⃣ Análise Exploratória (EDA)
- Distribuição de idade, gênero e faixa de renda
- Comparação entre clientes ativos e perdidos
- Identificação de padrões de uso do cartão e relacionamento

### 3️⃣ Visualização e Storytelling
- Construção de **dashboard no Power BI** com:
  - Taxa de churn total
  - Perfil de clientes ativos vs. perdidos
  - Churn por faixa etária, escolaridade e categoria do cartão
  - Indicadores de limite de crédito e uso médio

---

## 📊 Principais Insights

| Insight | Descrição |
|----------|------------|
| 🔹 **Uso baixo → maior churn** | Clientes com poucas transações e baixo uso do limite tendem a encerrar o cartão. |
| 🔹 **Casados e com renda alta → mais fiéis** | Maior estabilidade financeira reflete em menor churn. |
| 🔹 **Categoria Blue → maior risco de perda** | Segmento básico de cartões concentra a maioria das saídas. |
| 🔹 **Tempo de relacionamento > 3 anos → retenção maior** | Clientes antigos possuem menor propensão ao churn. |

---

## 🧩 Tecnologias Utilizadas

| Etapa | Ferramenta |
|-------|-------------|
| Limpeza e análise | Python (pandas, numpy, seaborn, matplotlib) |
| Visualização | Power BI |
| IDE / Editor | VS Code |
| Documentação | Markdown (GitHub) |

---

## ⚙️ Requisitos

Arquivo `requirements.txt`:
pandas
numpy
matplotlib
seaborn



Instale via terminal:
```bash
pip install -r requirements.txt

🖼️ Dashboard Power BI

Principais métricas:

Taxa de churn geral

Idade média dos clientes

Limite de crédito médio

Distribuição por faixa de renda

Comparativo churn por categoria de cartão

📈 Próximos Passos

Construir modelo preditivo de churn (Machine Learning)

Integrar com Streamlit para criar dashboard web interativo

Publicar o dashboard Power BI no Power BI Service e vincular ao GitHub

👤 Autor

Anthony Freitas
Engenheiro e Professor
📸 Instagram: @anthony_tijuduke