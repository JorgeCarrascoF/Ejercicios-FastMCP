# Consultas de prueba para el servidor MCP

## Consultas para tools
- "Usa la tool greet con mi nombre 'Juan' y dime la respuesta."
- "Suma 12 y 34 con la tool add, y luego resta 5 usando subtract."
- "Multiplica 7 por 8 con multiply y divide el resultado entre 4 usando divide."
- "Pide system_info para ver estado, usuarios y carga."
- "Calcula word_stats del texto: 'Hola mundo hola prueba'."
- "Genera los primeros 10 numeros de la serie con la tool fibonacci."
- "Convierte 25 grados c a f y k con temperature_convert."
- "Lanza 3 dados de 20 caras con roll_dice y muetra los resultados."
- "Dame un iso_timestamp actual."
- "Solicita un random_quote y un generate_uuid."
- "Baraja la lista ['rojo','verde','azul'] con shuffle_items."
- "Prueba un caso borde: divide 10 entre 0 y mira el mensaje de error." 

## Consultas para resources
- "Recupera el resource://greeting."
- "Lee data://config y data://system_config y muestralos."
- "Devuelve el texto largo de resource://lorem."
- "Carga el catalogo de productos desde data://product_catalog."
- "Consulta la base de conocimiento en data://knowledge_base (faqs y ejemplos)."
- "Obtén el manual en data://handbook."
- "Revisa metricas en data://benchmarks."
- "Pide logs de ejemplo de data://sample_logs."
- "Muestra el changelog en resource://changelog."

## Consultas para prompts
- "Usa ask_about_topic para que explique 'SSE' a un 'principiante'."
- "Resume este texto con summarize_text enfocado en 'riesgos': El servidor procesa peticiones SSE y expone tools, resources y prompts; debemos validar entradas y limitar retardos para evitar sobrecarga." 
- "Traduce el texto 'Hola mundo' al ingles con translate_text."
- "Haz brainstorming de 5 ideas sobre 'mejoras de observabilidad' con el prompt brainstorming."
- "Pasa este snippet a code_review_snippet indicando lenguaje python: def dividir(a, b):\n    return a / b" 
