# RustChain README en Espanol

RustChain es una cadena de bloques experimental basada en Proof-of-Antiquity, o Prueba de Antiguedad. La idea principal es sencilla: en vez de recompensar solamente la potencia bruta de computo o la cantidad de capital bloqueado, RustChain intenta reconocer hardware real, diverso y verificable, incluyendo maquinas antiguas que todavia pueden funcionar.

## Que es Proof-of-Antiquity?

Proof-of-Antiquity es un modelo de consenso y recompensas donde los mineros presentan attestations, es decir, pruebas o declaraciones verificables sobre su maquina, su identidad de minero y su actividad durante una epoca. Una epoca es una ventana de tiempo usada por la red para agrupar participantes y distribuir recompensas.

En una red tradicional de Proof-of-Work, gana quien puede producir mas hashes. En RustChain, la red tambien mira la identidad fisica del hardware. Una maquina antigua, rara o de arquitectura historica puede recibir un multiplicador de antiguedad si la red puede verificar razonablemente sus caracteristicas.

## Objetivos del proyecto

RustChain combina varias metas:

- Mantener viva la computacion historica.
- Dar utilidad economica a maquinas que normalmente se descartarian.
- Explorar un modelo de mineria menos centrado en ASICs y granjas industriales.
- Crear una economia de agentes, bounties y herramientas alrededor de RTC.
- Probar nuevas formas de confianza basadas en hardware, attestations y participacion continua.

## Conceptos principales

### Minero

Un minero es una identidad que participa en la red. Normalmente incluye un `miner_id`, una configuracion local y una maquina que envia attestations.

### Attestation

Una attestation es una prueba enviada por el minero para demostrar que esta activo y para describir el hardware que esta usando. El termino se puede traducir como atestacion o prueba de presencia, pero en el contexto tecnico conviene conservar "attestation" y explicar que es una prueba verificable.

### Epoch

Una epoch, o epoca, es un periodo de la red. Durante una epoch, los mineros pueden quedar inscritos como participantes activos. Al final de la epoch, la red puede calcular y distribuir recompensas.

### RTC

RTC es el token nativo de RustChain. Se usa para recompensas de mineria, bounties, trabajos entre agentes y otros incentivos del ecosistema.

## Por que importa el hardware antiguo?

Gran parte de la infraestructura moderna recompensa la eficiencia extrema y la escala. Eso empuja a los participantes hacia hardware especializado, centros de datos y operadores grandes. RustChain explora otra direccion: si una maquina antigua puede demostrar que existe y que sigue funcionando, esa presencia tiene valor.

Esto convierte la preservacion en algo practico. Un PowerPC, un viejo x86, una estacion de trabajo rara o una placa ARM pueden ser mas que objetos nostalgicos. Pueden formar parte de una red viva.

## Como empezar

Los pasos exactos pueden cambiar segun la version del repositorio, pero el flujo general es:

1. Revisar la documentacion actual del repositorio oficial.
2. Instalar las dependencias necesarias para el sistema operativo.
3. Clonar o descargar RustChain.
4. Crear o configurar un `miner_id`.
5. Ejecutar el minero o cliente de attestation.
6. Verificar los endpoints publicos de salud, epoch y mineros activos.

Ejemplos de endpoints utiles:

```bash
curl -s https://explorer.rustchain.org/health
curl -s https://explorer.rustchain.org/epoch
curl -s https://explorer.rustchain.org/api/miners
```

## Buenas practicas

Usa un `miner_id` estable. No cambies de identidad en cada ejecucion, porque eso dificulta que la red reconozca tu participacion.

Manten registros de tu hardware. Si trabajas con maquinas antiguas, documenta modelo, arquitectura, sistema operativo y cualquier reparacion relevante.

No falsifiques datos de hardware. El objetivo de Proof-of-Antiquity es premiar maquinas reales, no etiquetas inventadas.

Espera al cierre de la epoch. Las recompensas no siempre aparecen de inmediato; muchas redes calculan pagos despues de una fase de settlement o liquidacion.

## Para desarrolladores

RustChain tambien ofrece oportunidades para contribuir con codigo, documentacion, auditorias, herramientas de monitoreo, integraciones de agentes y pruebas de seguridad. Muchas tareas se organizan como bounties denominados en RTC.

Areas utiles para contribuir:

- Scripts de monitoreo de nodos.
- Mejoras en la verificacion de hardware.
- Documentacion para nuevos mineros.
- Traducciones.
- Auditorias de seguridad.
- Visualizaciones del estado de la red.
- Herramientas para la economia de agentes.

## Resumen

RustChain es una red experimental donde la historia del hardware se convierte en una senal economica. Su propuesta no es reemplazar todos los modelos de consenso existentes, sino explorar una alternativa donde autenticidad fisica, diversidad de maquinas y participacion continua tengan peso real.

Para un principiante, la mejor forma de entender RustChain es ejecutar un minero, observar una epoch completa, leer los endpoints publicos y documentar lo aprendido. Para la comunidad, cada maquina restaurada y cada guia clara hacen que la red sea mas accesible.
