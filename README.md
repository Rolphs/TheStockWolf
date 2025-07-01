# 🐺 The Stock Wolf

**Una simulación financiera basada en agentes, donde países, empresas y jugadores interactúan en un ecosistema económico global dinámico y competitivo.**

---

## 📘 Descripción

**The Stock Wolf** es un simulador de mercados bursátiles globales estructurado como un **sistema agentic**, donde:

- Cada país es un **agente autónomo** con políticas económicas propias.
- Las empresas cotizan en bolsas nacionales e internacionales.
- Los jugadores —ya sean humanos o bots— compiten por maximizar riqueza, influencia o estabilidad estratégica.
- El sistema evoluciona dinámicamente ante eventos globales, decisiones locales y estrategias de mercado.

---

## 🧠 Arquitectura del sistema

### Agentes principales:

| Tipo de agente | Rol | Decisiones clave |
|----------------|-----|------------------|
| `CountryAgent` | País soberano | Política fiscal, regulación de mercado, relaciones exteriores |
| `Company`      | Empresa cotizada | Expansión, emisión de acciones, dividendos, innovación |
| `Player`       | Fondo, entidad o individuo | Inversiones, manipulación, lobbying, especulación |
| `Market`       | Plataforma emergente | Precios, liquidez, crisis, ciclos |

Cada agente posee **estado interno**, **estrategias autónomas**, y puede reaccionar o anticipar el comportamiento de otros agentes.

---

## 🧬 Tecnologías

- **Python 3.12+**
- Sistema modular basado en `classes` y `event loops`
- Simulación secuencial por "ticks" de tiempo
- Opcional: integración futura con ML (reinforcement learning, modelado predictivo)
- Visualización con `Tkinter` o `PyQt` (en desarrollo)

---

## 🚀 Primer MVP

- [ ] Implementar al menos 3 países con perfiles económicos distintos.
- [ ] Un ciclo de simulación base (`ticks`) donde los agentes reaccionen a shocks.
- [ ] Agente `Player` humano que pueda comprar/vender acciones.
- [ ] Lógica inicial de mercados con precios volátiles y dependientes de eventos.
- [ ] Visualización básica de portafolios y estado global.

---

## 📦 Instalación

```bash
git clone https://github.com/Rolphs/TheStockWolf.git
cd TheStockWolf
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m stockwolf.main
```

## ▶️ Running the game

After installing the requirements you can launch either the classic text game or the StockWolf simulation:

```bash
pip install -r requirements.txt
agentics        # launches the text game
stockwolf       # runs the simulation demo
```

- `agentics` opens a retro, turn–based trading game.
- `stockwolf` executes a small simulation showcasing the project’s economic agents.

You can also supply a custom YAML file and the number of ticks to simulate:

```bash
stockwolf --yaml my_world.yaml --ticks 20
```

Without arguments the command uses `stockwolf/data/official.yaml` and runs for five ticks.

---

🎮 ¿Qué hace el jugador?
### Invierte en empresas multinacionales.
### Observa y manipula mercados en diferentes países.
### Compite contra otros jugadores controlados por IA.
### Adquiere información parcial, predice movimientos, reacciona a eventos.
### Puede especializarse como fondo indexado, fondo buitre, banco global, etc.

⸻

🌐 Mundo dinámico

El mundo de The Stock Wolf evoluciona constantemente:
	•	Eventos globales: crisis, guerras, pandemias, revoluciones tecnológicas.
	•	Relaciones internacionales: tratados, sanciones, zonas económicas.
	•	Estilos de juego: agresivo, conservador, político, desestabilizador.

⸻

📁 Estructura del repositorio

TheStockWolf/
├── agents/           # country.py, company.py, player.py, market.py
├── engine/           # simulation.py, event_system.py
├── interface/        # gui.py, dashboard.py
├── data/             # Configuración de países y empresas
├── stockwolf/
│   └── main.py       # Entry point del juego
├── requirements.txt
└── README.md

⸻

## 🌍 Bolsas Nacionales Ficticias en *The Stock Wolf*

| País            | Bolsa Ficticia                                        | Siglas  | Estilo Narrativo / Económico                   |
|-----------------|--------------------------------------------------------|---------|-----------------------------------------------|
| 🇲🇽 México        | Bolsa Revolucionaria Nacional                          | BRN     | Posrevolucionaria, nacionalista, clientelar    |
| 🇨🇺 Cuba          | Bolsa Nacional de Ron y Puros                          | BNRP    | Tropical, planificada, simbólica               |
| 🇺🇸 EE.UU.        | National Resource Authority                            | NRA     | Extractivista, imperial, lobbycrática          |
| 🇧🇷 Brasil        | Mercado Federal do Samba e Harmonia                   | MFSAH   | Tropicalista, rítmico, populista               |
| 🇮🇳 India         | Comisión Estática de Castas                           | CEC     | Estructuralista, rígido, cínico                |
| 🇷🇺 Rusia         | Ministerio de Transacciones Estratégicas              | MTE     | Oligárquico, beligerante, opaco                |
| 🇨🇳 China         | Comité para la Prosperidad Ordenada del Pueblo        | CPOP    | Tecnocracia regulada, socialista de mercado    |
| 🇦🇷 Argentina     | Bolsa de Nieve Maradoniana                            | BdNM    | Volátil, emocional, heroico-trágico            |
| 🇩🇪 Alemania      | Cámara Germánica de Estabilidad Capitalista           | CGEC    | Ordenada, racional, tecnocrática               |
| 🇯🇵 Japón         | Instituto Nipón de Precisión Económica                | INPE    | Zen, eficiente, disciplinado                   |
| 🇿🇦 Sudáfrica     | Foro de Intercambios Minerales de África Austral      | FIMAA   | Extractivo, postcolonial, regionalizado        |
| 🇸🇦 Arabia Saudita| Fundación de Rentas Sagradas del Desierto             | FRSD    | Teocrático, petrolero, opulento                |
| 🇸🇬 Singapur      | Autoridad Compacta de Flujo de Capital                 | ACFC    | Neoliberalismo eficiente, aséptico             |
| 🇨🇭 Suiza         | Centro Helvético de Custodia y Silencio               | CHCS    | Neutra, opaca, elegante                        |
| 🇰🇷 Corea del Sur | Red Integrada de Capital y Tecnología de Oriente      | RICTO   | Dinámico, digital, industrializado             |

⸻

## 📈 Empresas cotizantes por país

| País             | Empresa                                         | Ticker | Descripción                                           |
|------------------|-------------------------------------------------|--------|-------------------------------------------------------|
| 🇲🇽 México        | Petróleos Unidos del Pueblo                    | PUP    | Estatal simbólica, atrapada en deuda y discurso       |
| 🇲🇽 México        | Comercializadora Azteca de Paguitos            | CAP    | Minorista popular, sostenida por créditos imposibles  |
| 🇨🇺 Cuba          | Servicios Médicos Internacionales de la Patria | SMIP   | Exporta médicos, deuda y reputación                   |
| 🇨🇺 Cuba          | Cañaverales Unidos de la Revolución            | CUR    | Azúcar, machete y retórica                            |
| 🇺🇸 EE.UU.        | FreedomCloud Defense Systems                   | FCDS   | Defensa en la nube, subsidios infinitos               |
| 🇺🇸 EE.UU.        | McCapital Unlimited Inc.                       | MCUI   | Todo lo compra, incluso tu empresa                    |
| 🇧🇷 Brasil        | Samba Agroexportadora Integrada                | SAI    | Exporta feijoada, café y esperanza                    |
| 🇧🇷 Brasil        | Minerales & Carnaval Sociedad Anónima          | MiCaSA | Cotiza samba, litio y corrupción local                |
| 🇮🇳 India         | CastaTech Solutions Pvt. Ltd.                  | CTSP   | Software jerárquico para todos los rangos             |
| 🇮🇳 India         | Bharata Holdings of Ancestral Wealth           | BHAW   | Conglomerado con herencia en código                   |
| 🇷🇺 Rusia         | GazComPriv Export JSC                          | GCPE   | Petróleo, gas y sanciones                             |
| 🇷🇺 Rusia         | SberFuture Artificial Stability                | SFAS   | Banca predictiva con vodka neural                     |
| 🇨🇳 China         | Pueblo Digital Unificado S.A.                  | PDU    | Todo está conectado... con el Partido                 |
| 🇨🇳 China         | Dragón Celeste de Infraestructura Estatal      | DCIE   | Hormigón, acero, datos                                |
| 🇦🇷 Argentina     | Alfajores Bursátiles del Sur S.A.              | ABS    | Dulce de leche cotiza más que el peso                 |
| 🇦🇷 Argentina     | Litio Emocional Sociedad Anónima               | LESA   | El mineral del futuro con presente ansioso            |
| 🇩🇪 Alemania      | Ordnung Maschinenbau AG                        | OMA    | Precisión, eficiencia, exportación                    |
| 🇩🇪 Alemania      | Banco Federal de Precisión Financiera          | BFPF   | Donde el euro va a disciplinarse                      |
| 🇯🇵 Japón         | Nippon Kikai Zen Corporation                   | NKZC   | Robots que meditan y ensamblan                        |
| 🇯🇵 Japón         | Sakura Neuralware Co.                          | SNC    | IA con honor, eficiencia y sakura                     |
| 🇿🇦 Sudáfrica     | PanMinerals SA Holdings Ltd.                   | PMSA   | Extrae esperanza de minas profundas                   |
| 🇿🇦 Sudáfrica     | Ubuntu Energy Transition Inc.                  | UETI   | Transición verde con alma africana                    |
| 🇸🇦 Arabia Saudita| Desierto Profundo Petroleros Ltd.              | DPPL   | Petróleo, desierto y silencio                         |
| 🇸🇦 Arabia Saudita| Peregrinaje Global de Servicios Hajj           | PGSH   | Religión y logística de lujo                          |
| 🇸🇬 Singapur      | Capitales Compactos Asia Pte. Ltd.             | CCAP   | Fondos densos, fríos y eficientes                     |
| 🇸🇬 Singapur      | Red Financiera Transoceánica                   | RFT    | Flujo monetario que nunca se moja                     |
| 🇨🇭 Suiza         | Fondo Eterno de Patrimonio Silente             | FEPS   | Nadie sabe qué hace, pero siempre gana                |
| 🇨🇭 Suiza         | Custodia Alpina Unificada SA                   | CAUSA  | Guarda secretos en cajas fuertes blancas              |
| 🇰🇷 Corea del Sur | Tecnología Orientada al Consenso               | TOC    | Firma software donde todos acuerdan                   |
| 🇰🇷 Corea del Sur | SeoulQuantum Industrial Holdings               | SQIH   | Microchips con orgullo y café helado                  |
⸻

## 🧠 Sistema de agentes en *The Stock Wolf*

El juego está diseñado como una simulación económica emergente basada en agentes autónomos que interactúan entre sí. Cada tipo de agente tiene objetivos, reglas y consecuencias diferentes.

### 🧬 Tipos de agentes y su función

| Tipo de Agente      | Ejemplos / Nombres                     | Cantidad | Rol principal |
|---------------------|----------------------------------------|----------|----------------|
| `CountryAgent`      | México, China, Argentina…              | 15       | Define política económica, regula su mercado local |
| `CompanyAgent`      | PUP, MCUI, CAP, etc.                   | 30       | Actúan en bolsa, crecen, colapsan, pagan dividendos |
| `RegulatorAgent`    | Entidades fiscales globales, auditores| 5        | Detectan manipulación, sancionan, estabilizan |
| `BankAgent`         | FMI, Banco Mundial, BancEx, EcoFund…  | 5        | Prestan, rescatan y condicionan países o jugadores |
| `PlayerAgent`       | Jugadores IA (competencia)            | 5        | Compiten contigo con estrategias y metas propias |

**Total: 60 agentes activos en el ecosistema.**

---

### 🏗️ Arquitectura de código modular

Los agentes están organizados en archivos independientes, permitiendo extender o modificar cada comportamiento de manera aislada:

TheStockWolf/
├── agents/
│   ├── country.py         # Lógica de países
│   ├── company.py         # Lógica empresarial
│   ├── regulator.py       # Agencias de control
│   ├── bank.py            # Bancos internacionales
│   ├── player.py          # Jugadores IA
├── engine/
│   ├── simulation.py      # Motor principal de ticks
│   ├── events.py          # Sistema de eventos globales
├── data/
│   ├── countries.json     # Configuración de países
│   ├── companies.json     # Empresas cotizantes
│   ├── banks.json         # Bancos e instituciones
│   ├── regulators.json    # Autoridades fiscales
│   ├── players.json       # Rivales IA
├── main.py                # Script para ejecutar simulación

---

Cada agente evoluciona a través de ciclos (ticks), toma decisiones basadas en su contexto y puede interactuar con otros agentes de forma directa o mediada por el mercado.


⸻

📈 Roadmap futuro
	•	Simulación basada en redes de oferta y demanda
	•	Agentes con aprendizaje adaptativo (Q-learning, PPO)
	•	Interfaz web o multiplataforma
	•	Modo multijugador asincrónico (torneos o partidas cronometradas)
	•	Exportación de partidas como datasets para investigación económica/IA

⸻

🤝 Contribuciones

Este proyecto está en desarrollo activo y abierto a colaboración, desde diseño y gameplay hasta modelado económico o interfaces. ¿Tienes ideas? ¿Quieres escribir un país-agente distópico? ¡Súmate!
