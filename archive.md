---
layout: page
title: Archive
permalink: /archive/
---

<div class="archive-list">
  <ol class="posts-list">
    {% for post in site.posts %}
    <li class="post-item">
      <span class="post-rank">{{ forloop.index }}</span>
      <div class="post-content">
        <div class="post-header">
          <a href="{{ post.url | relative_url }}" class="post-title">{{ post.title }}</a>
        </div>
        <div class="post-meta">
          <span class="post-points">{{ post.points | default: 0 }} points</span>
          <span class="post-author">by {{ post.author | default: site.author.name }}</span>
          <span class="post-time">{{ post.date | date: "%Y-%m-%d" }}</span>
        </div>
      </div>
    </li>
    {% endfor %}
  </ol>
</div>
