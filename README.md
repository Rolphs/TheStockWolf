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
python main.py


⸻

🎮 ¿Qué hace el jugador?
	•	Invierte en empresas multinacionales.
	•	Observa y manipula mercados en diferentes países.
	•	Compite contra otros jugadores controlados por IA.
	•	Adquiere información parcial, predice movimientos, reacciona a eventos.
	•	Puede especializarse como fondo indexado, fondo buitre, banco global, etc.

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
├── main.py           # Entry point del juego
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

### 🇲🇽 México – Bolsa Revolucionaria Nacional (BRN)

| Empresa                                | Ticker | Descripción                                  |
|----------------------------------------|--------|----------------------------------------------|
| Petróleos Unidos del Pueblo            | PUP    | Estatal simbólica, atrapada en deuda y discurso |
| Comercializadora Azteca de Paguitos   | CAP    | Minorista popular, sostenida por créditos imposibles |

---

### 🇨🇺 Cuba – Bolsa Nacional de Ron y Puros (BNRP)

| Empresa                                              | Ticker | Descripción                            |
|------------------------------------------------------|--------|----------------------------------------|
| Servicios Médicos Internacionales de la Patria       | SMIP   | Exporta médicos, deuda y reputación     |
| Cañaverales Unidos de la Revolución                  | CUR    | Azúcar, machete y retórica              |

---

### 🇺🇸 EE.UU. – National Resource Authority (NRA)

| Empresa                         | Ticker | Descripción                                    |
|----------------------------------|--------|------------------------------------------------|
| FreedomCloud Defense Systems    | FCDS   | Defensa en la nube, subsidios infinitos        |
| McCapital Unlimited Inc.        | MCUI   | Todo lo compra, incluso tu empresa             |

---

### 🇧🇷 Brasil – Mercado Federal do Samba e Harmonia (MFSAH)

| Empresa                                   | Ticker | Descripción                                 |
|-------------------------------------------|--------|---------------------------------------------|
| Samba Agroexportadora Integrada           | SAI    | Exporta feijoada, café y esperanza           |
| Minerales & Carnaval Sociedad Anónima     | MiCaSA | Cotiza samba, litio y corrupción local       |

---

### 🇮🇳 India – Comisión Estática de Castas (CEC)

| Empresa                                           | Ticker | Descripción                            |
|---------------------------------------------------|--------|----------------------------------------|
| CastaTech Solutions Pvt. Ltd.                    | CTSP   | Software jerárquico para todos los rangos |
| Bharata Holdings of Ancestral Wealth             | BHAW   | Conglomerado con herencia en código     |

---

### 🇷🇺 Rusia – Ministerio de Transacciones Estratégicas (MTE)

| Empresa                        | Ticker | Descripción                               |
|--------------------------------|--------|-------------------------------------------|
| GazComPriv Export JSC          | GCPE   | Petróleo, gas y sanciones                  |
| SberFuture Artificial Stability| SFAS   | Banca predictiva con vodka neural         |

---

### 🇨🇳 China – Comité para la Prosperidad Ordenada del Pueblo (CPOP)

| Empresa                                              | Ticker | Descripción                               |
|------------------------------------------------------|--------|-------------------------------------------|
| Pueblo Digital Unificado S.A.                        | PDU    | Todo está conectado... con el Partido     |
| Dragón Celeste de Infraestructura Estatal            | DCIE   | Hormigón, acero, datos                     |

---

### 🇦🇷 Argentina – Bolsa de Nieve Maradoniana (BdNM)

| Empresa                                      | Ticker | Descripción                               |
|----------------------------------------------|--------|-------------------------------------------|
| Alfajores Bursátiles del Sur S.A.            | ABS    | Dulce de leche cotiza más que el peso     |
| Litio Emocional Sociedad Anónima             | LESA   | El mineral del futuro con presente ansioso |

---

### 🇩🇪 Alemania – Cámara Germánica de Estabilidad Capitalista (CGEC)

| Empresa                                      | Ticker | Descripción                         |
|----------------------------------------------|--------|-------------------------------------|
| Ordnung Maschinenbau AG                      | OMA    | Precisión, eficiencia, exportación  |
| Banco Federal de Precisión Financiera        | BFPF   | Donde el euro va a disciplinarse    |

---

### 🇯🇵 Japón – Instituto Nipón de Precisión Económica (INPE)

| Empresa                          | Ticker | Descripción                         |
|----------------------------------|--------|-------------------------------------|
| Nippon Kikai Zen Corporation     | NKZC   | Robots que meditan y ensamblan      |
| Sakura Neuralware Co.            | SNC    | IA con honor, eficiencia y sakura   |

---

### 🇿🇦 Sudáfrica – Foro de Intercambios Minerales de África Austral (FIMAA)

| Empresa                          | Ticker | Descripción                                |
|----------------------------------|--------|--------------------------------------------|
| PanMinerals SA Holdings Ltd.     | PMSA   | Extrae esperanza de minas profundas        |
| Ubuntu Energy Transition Inc.    | UETI   | Transición verde con alma africana         |

---

### 🇸🇦 Arabia Saudita – Fundación de Rentas Sagradas del Desierto (FRSD)

| Empresa                                  | Ticker | Descripción                           |
|------------------------------------------|--------|---------------------------------------|
| Desierto Profundo Petroleros Ltd.        | DPPL   | Petróleo, desierto y silencio          |
| Peregrinaje Global de Servicios Hajj     | PGSH   | Religión y logística de lujo           |

---

### 🇸🇬 Singapur – Autoridad Compacta de Flujo de Capital (ACFC)

| Empresa                                | Ticker | Descripción                             |
|----------------------------------------|--------|-----------------------------------------|
| Capitales Compactos Asia Pte. Ltd.     | CCAP   | Fondos densos, fríos y eficientes        |
| Red Financiera Transoceánica           | RFT    | Flujo monetario que nunca se moja        |

---

### 🇨🇭 Suiza – Centro Helvético de Custodia y Silencio (CHCS)

| Empresa                                | Ticker | Descripción                              |
|----------------------------------------|--------|------------------------------------------|
| Fondo Eterno de Patrimonio Silente     | FEPS   | Nadie sabe qué hace, pero siempre gana   |
| Custodia Alpina Unificada SA           | CAUSA  | Guarda secretos en cajas fuertes blancas |

---

### 🇰🇷 Corea del Sur – Red Integrada de Capital y Tecnología de Oriente (RICTO)

| Empresa                                 | Ticker | Descripción                              |
|-----------------------------------------|--------|------------------------------------------|
| Tecnología Orientada al Consenso        | TOC    | Firma software donde todos acuerdan      |
| SeoulQuantum Industrial Holdings        | SQIH   | Microchips con orgullo y café helado     |
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
