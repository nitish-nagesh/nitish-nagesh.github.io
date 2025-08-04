---
layout: page
permalink: /about/
subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Moto. Etc.
more_info: >
  <p>I'm a Ph.D. student in Computer Science at the Donald Bren School of Information and Computer Sciences, UC Irvine, advised by Prof. Amir M. Rahmani.</p>
  <p>My research focuses on <strong>causal inference</strong>, <strong>generative AI</strong>, and <strong>large language models</strong> for real-world healthcare. I build tools that aim to make AI fair, explainable, and clinically useful.</p>
  <p>I've published in venues like <em>IEEE Medicine & Biology</em> and <em>Elsevier Smart Health</em>, and my current work includes building causally fair synthetic data pipelines and LLM-powered diet coaching agents.</p>
  <p>I'm fluent in Python, R, SQL, PyTorch, TensorFlow, and LangChain. I enjoy developing end-to-end AI applications — from data engineering to model deployment.</p>
---

{%- if site.enable_contact == true -%}
<p class="desc">{{ page.description }}</p>
<div class="row">
  <div class="col">
    {%- include about/skills.html title="Skills" source=site.data.skills -%}
  </div>
  <div class="col">
    {% include about/soft-skills.html title="Soft Skills" source=site.data.soft-skills %}
  </div>
</div>
<div class="row">
  <div class="col">
    {%- include about/education.html -%}
  </div>
  <div class="col">
    {%- include about/career.html -%}
  </div>
</div>
{%- endif -%}
