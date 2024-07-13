import random

temas_acoes = [
        "Se maquia",
        "Enche balão",
        "Anda de Skate",
        "Corta Carne",
        "Monta Uma Montanha Russa",
        "Faz ASMR",
        "Fala sobre tecnologia",
        "Programa",
        "Fala sobre Aviação",
        "Faz Panela de Barro",
        "Faz Lettering",
        "Fala sobre Ciência",
        "Faz churrasco",
        "Toca forró",
        "Fala Sobre Tipos de Regrigerante",
        "Fala Sobre Trens",
        "Toca pagode",
        "Fofoca sobre famosos",
        "Cozinha",
        "Pilota Jet-Ski",
        "Se mantêm acordada",
        "Luta com urso panda",
        "Dança Tiktok",
        "Faz pegadinha do presente misterioso",
        "Fabrica frutas de plástico",
        "Monta móveis de qualidade duvidosa",
        "Ensina a fazer estrelinha",
        "Lê em Silêncio",
        "Toca saxofone vestido de Pé Grande",
        "Faz React",
        "Exibe vídeo satisfatório",
        "Apresenta Podcast",
        ]

primeira_acao = random.choice(temas_acoes)
segunda_acao = random.choice([acao for acao in temas_acoes if acao != primeira_acao])

print("{} enquanto {}".format(primeira_acao, segunda_acao))
