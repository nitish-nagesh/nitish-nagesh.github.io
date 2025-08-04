---
layout: page
permalink: /
permalink_name: home
title: home
---

<div class="post">

  <header class="post-header">
    <h1 class="post-title">
     {% if site.title == "blank" %}<span class="font-weight-bold">{{ site.first_name }}</span> {{ site.middle_name }} {{ site.last_name }}{% else %}{{ site.title }}{% endif %}
    </h1>
     <p class="desc">{{ page.description }}</p>
  </header>

  <article>
    {% if page.profile %}
    <div class="profile float-{% if page.profile.align == 'left' %}left{% else %}right{% endif %}">
      {% if page.profile.image %}
        <img class="img-fluid z-depth-1 rounded" src="{{ page.profile.image | prepend: '/assets/img/' | relative_url }}">
      {% endif %}
      {% if page.profile.address %}
        <div class="address">
          {{ page.profile.address }}
        </div>
      {% endif %}
    </div>
    {% endif %}

    <div class="clearfix">
      <h2>Welcome to my academic website!</h2>
      <p>This is the new al-folio theme in action. If you can see this message, the theme is working correctly.</p>
      
      <h3>About Me</h3>
      <p>I'm a Ph.D. student in Computer Science at UC Irvine, focusing on causal inference, generative AI, and large language models for healthcare.</p>
      
      <h3>Research Areas</h3>
      <ul>
        <li>Causal Inference</li>
        <li>Generative AI</li>
        <li>Large Language Models</li>
        <li>Healthcare AI</li>
        <li>Fairness in AI</li>
      </ul>
    </div>

    {% if page.news %}
      {% include news.html %}
    {% endif %}

    {% if page.selected_papers %}
      {% include selected_papers.html %}
    {% endif %}

    {% if page.social %}
    <div class="social">
      <div class="contact-icons">
        {% include social.html %}
      </div>
      <div class="contact-note">
        {{ site.contact_note }}
      </div>
    </div>
    {% endif %}
  </article>

</div>

<!-- TEST: AL-FOLIO THEME IS WORKING! -->
<div style="background: red; color: white; padding: 20px; margin: 20px; text-align: center; font-size: 24px;">
  🎉 AL-FOLIO THEME IS NOW ACTIVE! 🎉
</div>
