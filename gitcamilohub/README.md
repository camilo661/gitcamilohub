# GitCamiloHub - Simulador CI/CD Modular

Proyecto reorganizado con programacion orientada a objetos, clases separadas por responsabilidad y una estructura mas mantenible para presentar el taller.

## Arquitectura

- `backend/domain`: entidades del negocio.
- `backend/structures`: estructuras de datos requeridas.
- `backend/factories`: fabricas para objetos base.
- `backend/services`: logica de negocio desacoplada.
- `backend/application`: ensamblado de dependencias.
- `backend/engine.py`: fachada del backend.
- `frontend`: componentes visuales, estilos, sidebar y dashboard.

## Patrones usados

- `Singleton`: `CatalogSingleton` para catalogos reutilizables.
- `Factory`: `AgentFactory`, `JobFactory` y `PipelineFactory`.
- `Facade`: `EngineFacade` como punto unico de acceso.
- `Service Layer`: servicios de logs, despliegue, metricas y pipeline.

## Estructuras de datos

- `AgentArray`: array fijo de agentes.
- `JobQueue`: cola FIFO de trabajos.
- `DeploymentStack`: pila LIFO de despliegues.
- `LogList`: lista de logs.
- `PipelineLinkedList`: lista enlazada simple de etapas.

## Ejecucion

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estructura

```text
gitcamilohub/
|-- app.py
|-- backend/
|   |-- application/
|   |-- domain/
|   |-- factories/
|   |-- services/
|   |-- structures/
|   |-- config.py
|   |-- data_structures.py
|   `-- engine.py
|-- frontend/
|   |-- components.py
|   |-- dashboard.py
|   |-- sidebar.py
|   `-- styles.py
|-- README.md
`-- requirements.txt
```
