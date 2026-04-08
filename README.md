<h1>Sprint 4 — Machine Learn API + Frontend</h1>
<h4>Python · Flask · Docker</h4>

<h2>🚧 Status do projeto</h2>
<p>Em progresso</p>

<h2>🖥️ Pré-requisitos</h2>
<p>Antes de começar, você vai precisar ter instalado em sua máquina:</p>
<ul>
    <li><a href="https://git-scm.com">Git</a></li>
    <li><a href="https://www.docker.com">Docker</a> (com Docker Compose)</li>
    <li><a href="https://www.python.org">Python</a> — apenas para rodar os testes localmente</li>
</ul>


<h2>🚀 Rodando a aplicação</h2>

<h3>1. Clone o repositório</h3>
<pre><code>git clone &lt;url-do-repositorio&gt;
cd pasta-do-projeto
</code></pre>

<h3>2. Configure o arquivo de variáveis de ambiente</h3>
<p>Crie o arquivo <code>api/.env</code> com as variáveis necessárias.

<h3>3. Suba a API com Docker</h3>
<pre><code>cd api
docker compose up --build</code></pre>

<p>A API estará disponível em <code>http://localhost:3001</code> (ou na porta do <code>.env</code>).</p>

<h3>4. Acesse o Frontend</h3>
<p>O frontend é redirecionado pela API. Abra no navegador:</p>
<ul>
    <li><code>http://localhost:3001/</code> — redireciona para o frontend (<code>front/index.html</code>)</li>
</ul>

<h3>5. Documentação OpenAPI</h3>
<ul>
    <li><code>http://localhost:3001/openapi</code> — Swagger UI com todos os endpoints documentados</li>
    <li><code>http://localhost:3001/docs</code> — redireciona para <code>/openapi</code></li>
</ul>

<h2>🧪 Testes</h2>

<h3>Instalação das dependências (uma vez)</h3>
<pre><code>cd api
python install -r requirements.txt</code></pre>

<h3>Executar os testes com pytest</h3>
<pre><code>cd api
pytest</code></pre>

<h2>🧑🏻 Autor</h2>
<p>Feito por João Paulo</p>
<a href="mailto:joaopauloneto3687@gmail.com">
    <img src="https://img.shields.io/badge/-joaopauloneto3687@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:joaopauloneto3687@gmail.com">
</a>