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

📈 Roadmap futuro
	•	Simulación basada en redes de oferta y demanda
	•	Agentes con aprendizaje adaptativo (Q-learning, PPO)
	•	Interfaz web o multiplataforma
	•	Modo multijugador asincrónico (torneos o partidas cronometradas)
	•	Exportación de partidas como datasets para investigación económica/IA

⸻

🤝 Contribuciones

Este proyecto está en desarrollo activo y abierto a colaboración, desde diseño y gameplay hasta modelado económico o interfaces. ¿Tienes ideas? ¿Quieres escribir un país-agente distópico? ¡Súmate!
