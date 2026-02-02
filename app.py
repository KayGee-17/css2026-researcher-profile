# -*- coding: utf-8 -*-
"""

@author: Kgothatso Khosa
"""

import streamlit as st

import streamlit as st

# Page config
st.set_page_config(
    page_title="Researcher Profile | Kgothatso Khosa",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Kgothatso Gift Khosa")
st.subheader("BSc Mathematical Sciences | Mathematics & Computer Science")

st.markdown("""
Welcome to my researcher profile page.  
This page showcases my academic background, research interests, skills, and projects.
""")

st.divider()

# About Me
st.header("👤 About Me")
st.markdown("""
I am a Bachelor of Science student in **Mathematical Sciences**, majoring in
**Mathematics and Computer Science** at **Sefako Makgatho Health Sciences University (SMU)**.

My interests are:
- Applied Mathematics  
- Probability & Statistics  
- Data Analysis  
- Programming and Software Development 
- Gaming(Esport) 
- Soccer


I enjoy using mathematical theory and computational tools to solve real-world problems.
""")

# Research Interests
st.header("🔬 Research Interests")
st.markdown("""
- Probability Distributions and Statistical Modelling  
- Data Science and Exploratory Data Analysis  
- Algorithm Design and Analysis  
- Mathematical Modelling  
- Software Development for Data Applications  
""")

# Projects
st.header("💻 Projects & Academic Work")
st.markdown("""
- **Statistical Analysis Projects**  
  Analysis of real and simulated datasets using probability distributions.

- **Python Programming**  
  File handling, data processing scripts, and automation tasks.

- **Streamlit Applications**  
  Interactive web apps for data analysis and visualization.

- **Coursework Assignments**  
  Mathematical proofs, computational problem solving, and software-based solutions.
""")

# Skills
st.header("🛠 Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Technical Skills**
    - Python  
    - Streamlit  
    - Git & GitHub  
    - Data Analysis  
    - SQL (Advance) 
    - Programming
    - Mathlab
    - Microsoft
    """)

with col2:
    st.markdown("""
    **Mathematical Skills**
    - Probability & Statistics  
    - Linear Algebra  
    - Calculus  
    - Discrete Mathematics 
    - Mathematical Analysis
    - Abstract Algebra
    """)

# Contact
st.header("📬 Contact")
st.markdown("""
- **Email:** kgothatsogiftkhosa17@gmail.com 
- **GitHub:** https://github.com/KayGee-17 
- **LinkedIn:** https://www.linkedin.com/in/kgothatso-khosa-490213244?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

  
""")

st.divider()
st.caption("© 2026 | Researcher Profile App built with Streamlit")