import streamlit as st
from libraries.ideas import domain_ideas
from libraries.domain import check_availability


st.title("Domain ideas*")

st.write("Add group of keywords (e.g. '**website ideas**'), one group per line, to get some available domain ideas (e.g. '*websiteideas.it*', '*website-ideas.it*', etc.):")

form = st.form("main-form", clear_on_submit=False)

keywords = form.text_area("keywords")

tlds = dict()
for tld in ['it', 'org', 'net', 'info']:
    tlds[tld] = form.checkbox(tld, value=(tld == 'it'), key=None, label_visibility="visible")

submit = form.form_submit_button("Invia")

if submit:
    ideas = domain_ideas(keywords, [tld for tld, value in tlds.items() if value])
    available = [domain for domain in check_availability(ideas)]
    st.table(available)
