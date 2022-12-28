import streamlit as st
import spacy_streamlit

models = ["de_core_news_sm", "de_core_news_md"]

default_text = """Mit seiner Tagesaufenthalts- und Übernachtungsstätte verfolgt das Harburger Rote Kreuz das Ziel, Not und Hilfebedürftigkeit von obdachlosen Menschen in Harburg sowohl kurzfristig zu lindern als auch langfristig zu beheben.

Das Harburg-Huus bietet tagsüber eine Aufenthaltsmöglichkeit mit bedarfsgerechten Angeboten an sozialen Hilfeleistungen in Form von Obdach, Verpflegung, Hygieneleistungen, medizinischer Grundversorgung, Freizeitangeboten, sozialen Kontakten und einer niedrigschwelligen Sozialberatung.

In den Abend- und Nachtstunden finden obdachlose Menschen hier einen Schutzraum und Schlafmöglichkeiten – bei Bedarf auch zusammen mit ihren Hunden. Es stehen 15 Betten in Ein- bis Vierbettzimmern zur Verfügung. Frauen können in einem gesonderten Schlafraum übernachten.."""

st.caption("https://www.drk-harburg.hamburg/obdachlosenhilfe.html")

spacy_streamlit.visualize(models, default_text)
