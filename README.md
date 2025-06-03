# organizador_financeiro# | Organizador Financeiro Pessoal

Sistema simples de controle financeiro pessoal desenvolvido em **Python** com banco de dados **SQLite**. O objetivo é permitir o gerenciamento de **receitas e despesas**, com funcionalidades de **registro, edição, exclusão e visualização** de transações por data, categoria e tipo.

---

##  Funcionalidades

- [x] Adicionar despesas e receitas
- [x] Editar despesas e receitas por ID
- [x] Excluir despesas e receitas por ID
- [x] Visualizar registros por data, categoria ou tipo
- [x] Interface de texto simples e intuitiva

---

##  Tecnologias utilizadas

- Python 3
- SQLite (via `sqlite3`)
- Terminal/CLI

---

##  Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/otaviorm/organizador-financeiro.git
   cd organizador-financeiro
2. (Opcional) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate #Se estiver no Linux/macOS
    venv\Scripts\activate    #Se estiver no Windows
3. Execute o arquivo principal:
    ```bash
    python app.py