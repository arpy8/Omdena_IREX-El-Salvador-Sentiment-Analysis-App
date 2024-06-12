PAGE_BANNER = "assets/img/banner.png"
PAGE_FAVICON = "assets/img/favicon.png"
PAGE_BACKGROUND = "assets/img/background.jpg"

ANALYSIS_REPORT_TEMPLATE = """
### Analysis Report

Here's the analysis report for the given text:

---

##### Sentiment Category: {sentiment_category}
##### Sentiment Score: {sentiment_score}
"""

CONTRIBUTORS = [
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
    ["John Doe", "https://www.linkedin.com/"],
]

TEXT_COLOR =  {
    "positive": "green",
     "neutral": "gray",
      "negative": "red"
}


from sklearn.feature_extraction import text as sklearn_text

spanish_stop_words = sklearn_text.ENGLISH_STOP_WORDS.union(set([
    'a', 'acá', 'ahí', 'al', 'algo', 'algunas', 'algunos', 'allá', 'allí', 'ambos', 'ante', 'antes', 'aquel', 'aquellas', 
    'aquellos', 'aquí', 'arriba', 'así', 'atras', 'aun', 'aunque', 'bajo', 'bastante', 'bien', 'cada', 'casi', 'cerca', 
    'cierto', 'ciertos', 'como', 'con', 'conmigo', 'contigo', 'contra', 'cual', 'cuales', 'cuando', 'cuanta', 'cuantas', 
    'cuanto', 'cuantos', 'de', 'dejar', 'del', 'demás', 'dentro', 'desde', 'donde', 'dos', 'el', 'él', 'ella', 'ellas', 
    'ellos', 'en', 'encima', 'entonces', 'entre', 'era', 'erais', 'eran', 'eras', 'eres', 'es', 'esa', 'esas', 'ese', 
    'eso', 'esos', 'esta', 'estaba', 'estabais', 'estaban', 'estabas', 'estad', 'estada', 'estadas', 'estado', 'estados', 
    'estamos', 'estando', 'estar', 'estaremos', 'estará', 'estarán', 'estarás', 'estaré', 'estaréis', 'estaría', 'estaríais', 
    'estaríamos', 'estarían', 'estarías', 'estas', 'este', 'estemos', 'esto', 'estos', 'estoy', 'estuve', 'estuviera', 
    'estuvierais', 'estuvieran', 'estuvieras', 'estuvieron', 'estuviese', 'estuvieseis', 'estuviesen', 'estuvieses', 'estuvimos', 
    'estuviste', 'estuvisteis', 'estuviéramos', 'estuviésemos', 'estuvo', 'ex', 'excepto', 'fue', 'fuera', 'fuerais', 'fueran', 
    'fueras', 'fueron', 'fuese', 'fueseis', 'fuesen', 'fueses', 'fui', 'fuimos', 'fuiste', 'fuisteis', 'gran', 'grandes', 'ha', 
    'habéis', 'había', 'habíais', 'habíamos', 'habían', 'habías', 'habida', 'habidas', 'habido', 'habidos', 'habiendo', 'habrá', 
    'habrán', 'habrás', 'habré', 'habréis', 'habría', 'habríais', 'habríamos', 'habrían', 'habrías', 'hace', 'haceis', 'hacemos', 
    'hacen', 'hacer', 'hacerlo', 'hacerme', 'hacernos', 'haceros', 'hacerse', 'haces', 'hacia', 'hago', 'han', 'hasta', 'incluso', 
    'intenta', 'intentais', 'intentamos', 'intentan', 'intentar', 'intentas', 'intento', 'ir', 'jamás', 'junto', 'juntos', 'la', 
    'largo', 'las', 'le', 'les', 'lo', 'los', 'mas', 'me', 'menos', 'mi', 'mía', 'mías', 'mientras', 'mío', 'míos', 'mis', 'misma', 
    'mismas', 'mismo', 'mismos', 'modo', 'mucha', 'muchas', 'muchísima', 'muchísimas', 'muchísimo', 'muchísimos', 'mucho', 'muchos', 
    'muy', 'nada', 'ni', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nos', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 
    'nuestro', 'nuestros', 'nunca', 'os', 'otra', 'otras', 'otro', 'otros', 'para', 'parecer', 'pero', 'poca', 'pocas', 'poco', 
    'pocos', 'podéis', 'podemos', 'poder', 'podría', 'podríais', 'podríamos', 'podrían', 'podrías', 'poner', 'por', 'por qué', 'porque', 
    'primero', 'puede', 'pueden', 'puedo', 'pues', 'que', 'qué', 'querer', 'quien', 'quién', 'quienes', 'quiénes', 'quiere', 'se', 
    'según', 'ser', 'si', 'sí', 'siempre', 'siendo', 'sin', 'sino', 'sobre', 'sois', 'solamente', 'solo', 'somos', 'soy', 'su', 'sus', 
    'también', 'tampoco', 'tan', 'tanto', 'te', 'teneis', 'tenemos', 'tener', 'tengo', 'ti', 'tiempo', 'tiene', 'tienen', 'toda', 
    'todas', 'todavía', 'todo', 'todos', 'tu', 'tú', 'tus', 'un', 'una', 'unas', 'uno', 'unos', 'usa', 'usas', 'usáis', 'usamos', 
    'usan', 'usar', 'usas', 'uso', 'usted', 'ustedes', 'va', 'vais', 'valor', 'vamos', 'van', 'varias', 'varios', 'vaya', 'verdad', 
    'verdadera', 'vosotras', 'vosotros', 'voy', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'y', 'ya', 'yo'
]))