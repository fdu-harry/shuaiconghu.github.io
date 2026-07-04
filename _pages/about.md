---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div id="top"></div>
<div id="about-me" class="page-anchor"></div>

<!-- Mobile-only section jump bar. The desktop top navigation remains unchanged. -->
<nav class="mobile-jump-nav" aria-label="Mobile section navigation">
  <a href="#about-me">About</a>
  <a href="#research-impact">Focus</a>
  <a href="#news">News</a>
  <a href="#representative-publications">Papers</a>
  <a href="#publications">Publications</a>
  <a href="#honors-and-awards">Awards</a>
  <a href="#educations">Education</a>
  <a href="#research-experience">Experience</a>
  <a href="#academic-service">Service</a>
  <a href="#technical-skills">Skills</a>
</nav>

<div class="mobile-intro-spacer" aria-hidden="true"></div>

<div class="intro-block" markdown="1">

Shuaicong Hu is a Postdoctoral Fellow in the Department of Electrical and Computer Engineering at The University of Hong Kong. He received his Ph.D. in Electronic Information from Fudan University (复旦大学, exceptional early graduation). His research focuses on **medical foundation models**, **heterogeneous multi-agent systems**, **multimodal physiological intelligence**, **interpretable clinical AI**, and **deployable healthcare systems** across sleep medicine, ECG, EEG, PPG, polysomnography, and clinical risk modeling.

His work bridges large-scale physiological signal modeling, specialist-model orchestration, interpretable AI, uncertainty-aware clinical prediction, and real-world healthcare validation. To date, he has published **31 SCI papers**, including **12 sole first-author, co-first-author, or student first-author papers**, with selected work in **Nature Communications**, **ICML**, **Information Fusion**, **Neural Networks**, **Expert Systems With Applications**, **IEEE Journal of Biomedical and Health Informatics**, **IEEE Transactions on Neural Systems and Rehabilitation Engineering**, and **IEEE Transactions on Instrumentation and Measurement**.

</div>

<div class="scholar-panel">
  <a href='https://scholar.google.com/citations?user=worq2P0AAAAJ&hl=zh-CN'>
    Google Scholar Profile:
    <strong><span id="scholar_total_cit">Loading</span></strong>
    citations
  </a>

  <div class="scholar-badges">
    <span class="scholar-badge scholar-citations">
      Citations: <span id="scholar_badge_citations">Loading</span>
    </span>
    <span class="scholar-badge scholar-hindex">
      h-index: <span id="scholar_badge_hindex">Loading</span>
    </span>
    <span class="scholar-badge scholar-i10">
      i10-index: <span id="scholar_badge_i10index">Loading</span>
    </span>
  </div>
</div>

<style>
html {
  scroll-padding-top: 76px;
}

/* =========================================================
   Global stability fixes
   ========================================================= */
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  max-width: 100%;
  overflow-x: hidden;
}

/* Reserve space for the fixed top navigation bar on desktop */
#main,
.initial-content,
.page,
.page__content {
  padding-top: 50px;
}

/* Mobile-only jump bar is hidden on desktop */
.mobile-jump-nav {
  display: none;
}

/* Invisible anchors for navigation */
.page-anchor {
  display: block;
  position: relative;
  top: -90px;
  visibility: hidden;
  height: 0;
}

/* Prevent section titles from being hidden behind the fixed navigation bar */
h1[id] {
  scroll-margin-top: 90px;
}

/* Make content images responsive without touching author avatar proportions */
.page__content img,
.paper-box img {
  max-width: 100%;
  height: auto;
}

/* Keep the theme author avatar square before circular cropping, avoiding distortion */
.author__avatar img {
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border-radius: 50%;
}

.scholar-panel {
  max-width: 100%;
}

.scholar-badges {
  margin-top: 6px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.scholar-badge {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 13px;
  font-weight: 600;
  color: white;
  line-height: 1.4;
}

.scholar-citations {
  background-color: #2ea44f;
}

.scholar-hindex {
  background-color: #f57c00;
}

.scholar-i10 {
  background-color: #1976d2;
}

/* Full Publication List alignment */
.pub-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
  margin: 0;
  border-bottom: 1px solid #ddd;
}

.pub-table td {
  vertical-align: top !important;
  padding-top: 8px;
  padding-bottom: 8px;
}

.pub-journal {
  width: 1%;
  white-space: nowrap;
  padding-right: 22px;
  text-align: left;
  vertical-align: top !important;
}

.pub-title {
  width: auto;
  vertical-align: top !important;
  line-height: 1.45;
  padding-left: 0;
}

.pub-journal .badge {
  display: inline-block;
  margin-top: 0;
  line-height: 1.2;
  vertical-align: top;
  white-space: nowrap;
  position: relative;
  top: 1px;
}

/* =========================================================
   Mobile responsive redesign
   Desktop layout remains unchanged.
   ========================================================= */
@media screen and (max-width: 900px) {

  html,
  body {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
    -webkit-text-size-adjust: 100% !important;
    text-size-adjust: 100% !important;
  }

  html {
    scroll-padding-top: 72px !important;
  }

  body {
    font-size: 16px !important;
  }

  /* Keep the original theme header/navigation visible on mobile. */
  .masthead,
  .masthead__inner-wrap,
  .masthead__menu,
  .greedy-nav,
  .visible-links {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .masthead {
    position: relative !important;
    transform: none !important;
    z-index: 20 !important;
  }

  .masthead__inner-wrap {
    padding-left: 10px !important;
    padding-right: 10px !important;
  }

  .masthead__menu {
    overflow: visible !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
  }

  .greedy-nav {
    display: flex !important;
    align-items: center !important;
    position: relative !important;
    overflow: visible !important;
    white-space: nowrap !important;
    z-index: 9998 !important;
  }

  .visible-links {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    white-space: nowrap !important;
    scrollbar-width: none !important;
  }

  .visible-links::-webkit-scrollbar {
    display: none !important;
  }

  .visible-links li {
    display: inline-block !important;
    flex: 0 0 auto !important;
  }

  /* Keep the right hamburger dropdown usable and compact on phones. */
  .greedy-nav button,
  .greedy-nav .greedy-nav__toggle,
  .greedy-nav .search__toggle {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 0 0 auto !important;
    z-index: 10000 !important;
  }

  .greedy-nav .hidden-links {
    position: absolute !important;
    top: calc(100% + 6px) !important;
    right: 0 !important;
    left: auto !important;
    width: min(250px, calc(100vw - 24px)) !important;
    max-height: 56vh !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    margin: 0 !important;
    padding: 6px 0 !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 12px !important;
    background: #ffffff !important;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.14) !important;
    z-index: 9999 !important;
    white-space: normal !important;
  }

  .greedy-nav .hidden-links.hidden {
    display: none !important;
  }

  .greedy-nav .hidden-links li {
    display: block !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    border-bottom: 1px solid #f1f3f5 !important;
    text-align: left !important;
  }

  .greedy-nav .hidden-links li:last-child {
    border-bottom: 0 !important;
  }

  .greedy-nav .hidden-links a {
    display: block !important;
    width: 100% !important;
    padding: 9px 13px !important;
    color: #333 !important;
    font-size: 0.82rem !important;
    line-height: 1.25 !important;
    text-decoration: none !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
  }

  .greedy-nav .hidden-links a:hover,
  .greedy-nav .hidden-links a:active {
    background: #f6f8fa !important;
    color: #1f5f9f !important;
    text-decoration: none !important;
  }

  /* Fully release the desktop left-column layout on mobile. */
  #main,
  .initial-content,
  .page,
  .page__content,
  .page__inner-wrap,
  .archive,
  .wrapper,
  .container,
  .layout--single .page,
  .layout--single .archive {
    float: none !important;
    clear: both !important;
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 10px !important;
    padding-right: 10px !important;
    overflow-x: hidden !important;
  }

  #main,
  .initial-content,
  .page,
  .page__content {
    padding-top: 8px !important;
  }

  .page__inner-wrap {
    padding-top: 0 !important;
  }

  .page__content {
    font-size: 0.92rem !important;
    line-height: 1.55 !important;
  }

  .page__content p {
    margin-top: 0 !important;
    margin-bottom: 0.72rem !important;
  }

  /* ---------------------------------------------------------
     Compact original author profile on mobile.
     Do NOT hide it: transform the Minimal Mistakes sidebar into
     a normal compact card above the text.
     --------------------------------------------------------- */
  .sidebar,
  .sidebar.sticky {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: static !important;
    float: none !important;
    clear: both !important;
    width: calc(100% - 20px) !important;
    max-width: 430px !important;
    min-width: 0 !important;
    height: auto !important;
    margin: 8px auto 8px auto !important;
    padding: 10px 11px !important;
    overflow: visible !important;
    border: 1px solid #e8e8e8 !important;
    border-radius: 14px !important;
    background: #fff !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.035) !important;
    text-align: left !important;
    transform: none !important;
  }

  .sidebar > div,
  .sidebar .author__profile {
    display: grid !important;
    grid-template-columns: 82px minmax(0, 1fr) !important;
    column-gap: 11px !important;
    row-gap: 0 !important;
    align-items: center !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .author__avatar {
    grid-column: 1 !important;
    grid-row: 1 / 3 !important;
    display: block !important;
    float: none !important;
    clear: none !important;
    width: 82px !important;
    max-width: 82px !important;
    min-width: 82px !important;
    height: 82px !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .author__avatar img {
    display: block !important;
    width: 82px !important;
    height: 82px !important;
    max-width: 82px !important;
    max-height: 82px !important;
    margin: 0 !important;
    border-radius: 50% !important;
    aspect-ratio: 1 / 1 !important;
    object-fit: cover !important;
  }

  .author__content {
    grid-column: 2 !important;
    grid-row: 1 !important;
    display: block !important;
    float: none !important;
    clear: none !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    text-align: left !important;
  }

  .author__name {
    display: block !important;
    margin: 0 0 2px 0 !important;
    padding: 0 !important;
    max-width: 100% !important;
    font-size: 1.06rem !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    text-align: left !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  .author__bio,
  .author__content p {
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
    max-width: 100% !important;
    font-size: 0.74rem !important;
    line-height: 1.35 !important;
    text-align: left !important;
    color: #555 !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  /* Convert the default mobile dropdown into compact chips. */
  .author__urls-wrapper {
    grid-column: 1 / -1 !important;
    grid-row: 3 !important;
    display: block !important;
    position: static !important;
    float: none !important;
    clear: both !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin: 8px 0 0 0 !important;
    padding: 7px 0 0 0 !important;
    border-top: 1px solid #eeeeee !important;
    box-shadow: none !important;
    background: transparent !important;
    text-align: left !important;
    transform: none !important;
  }

  .author__urls-wrapper button,
  .author__urls-wrapper .btn {
    display: none !important;
  }

  .author__urls {
    display: grid !important;
    grid-template-columns: repeat(3, max-content) !important;
    grid-auto-rows: auto !important;
    align-items: center !important;
    justify-content: flex-start !important;
    column-gap: 7px !important;
    row-gap: 5px !important;
    position: static !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    height: auto !important;
    margin: 0 !important;
    padding: 0 !important;
    list-style: none !important;
    border: 0 !important;
    box-shadow: none !important;
    background: transparent !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
  }

  .author__urls::before,
  .author__urls::after {
    display: none !important;
  }

  .author__urls li {
    display: inline-flex !important;
    width: auto !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    text-align: left !important;
    white-space: normal !important;
  }

  /* First two items are location/affiliation rows. Keep them on separate lines.
     This forces Email to start from the next row after The University of Hong Kong. */
  .author__urls li:nth-child(1),
  .author__urls li:nth-child(2) {
    grid-column: 1 / -1 !important;
    display: flex !important;
    width: 100% !important;
  }

  /* Email / ResearchGate / Google Scholar are aligned in one horizontal row. */
  .author__urls li:nth-child(3),
  .author__urls li:nth-child(4),
  .author__urls li:nth-child(5) {
    grid-column: auto !important;
    grid-row: 3 !important;
  }

  /* Prevent duplicated icon-only rows sometimes generated by mobile browsers/theme SVG fallback. */
  .author__urls li:nth-child(n+6) {
    display: none !important;
  }

  .author__urls a,
  .author__urls span,
  .author__urls li span {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    max-width: 100% !important;
    min-width: 0 !important;
    padding: 3px 7px !important;
    border-radius: 999px !important;
    background: #f6f8fa !important;
    color: #444 !important;
    font-size: 0.70rem !important;
    line-height: 1.25 !important;
    text-decoration: none !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  /* Location/affiliation rows should read as normal text, not chips. */
  .author__urls li:nth-child(1) a,
  .author__urls li:nth-child(1) span,
  .author__urls li:nth-child(2) a,
  .author__urls li:nth-child(2) span {
    justify-content: flex-start !important;
    padding: 0 !important;
    border-radius: 0 !important;
    background: transparent !important;
    font-size: 0.74rem !important;
    line-height: 1.28 !important;
  }

  .author__urls i,
  .author__urls svg {
    flex: 0 0 auto !important;
    width: 0.92em !important;
    height: 0.92em !important;
    max-width: 0.92em !important;
    max-height: 0.92em !important;
    font-size: 0.92em !important;
    margin-right: 4px !important;
  }

  .author__urls li > i:only-child,
  .author__urls li > svg:only-child {
    display: none !important;
  }

  /* Mobile section jump bar: this restores a reliable jump/navigation bar
     even in mobile browsers where the theme's greedy-nav collapses. */
  .mobile-jump-nav {
    display: flex !important;
    flex-wrap: nowrap !important;
    gap: 6px !important;
    width: 100% !important;
    max-width: 430px !important;
    margin: 0 auto 10px auto !important;
    padding: 6px 2px 7px 2px !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    scrollbar-width: none !important;
  }

  .mobile-jump-nav::-webkit-scrollbar {
    display: none !important;
  }

  .mobile-jump-nav a {
    display: inline-flex !important;
    flex: 0 0 auto !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 4px 9px !important;
    border-radius: 999px !important;
    border: 1px solid #e2e6ea !important;
    background: #ffffff !important;
    color: #1f5f9f !important;
    font-size: 0.74rem !important;
    line-height: 1.2 !important;
    text-decoration: none !important;
  }

  .mobile-jump-nav a:active,
  .mobile-jump-nav a:hover {
    background: #f4f7fb !important;
    text-decoration: none !important;
  }

  /* Prevent long words, DOI links, titles and names from breaking the page width. */
  p,
  li,
  td,
  a,
  strong,
  .pub-title,
  .paper-box-text,
  .page__content,
  .impact-list {
    max-width: 100% !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  /* Keep list indentation compact on small screens. */
  .page__content ul,
  .page__content ol {
    padding-left: 1.05rem !important;
    margin-top: 0.25rem !important;
    margin-bottom: 0.75rem !important;
  }

  .page__content li {
    margin-bottom: 0.38rem !important;
  }

  /* Scholar panel and badges wrap neatly. */
  .scholar-panel,
  .scholar-panel a {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    overflow-wrap: anywhere !important;
  }

  .scholar-panel {
    margin: 8px 0 14px 0 !important;
  }

  .scholar-badges {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 5px !important;
    margin-top: 6px !important;
  }

  .scholar-badge {
    font-size: 11.5px !important;
    padding: 3px 7px !important;
    max-width: 100% !important;
  }

  /* Representative publication cards: image on top, text below. */
  .paper-box {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin: 0 0 16px 0 !important;
    padding: 0 !important;
    overflow: visible !important;
    content-visibility: auto;
    contain-intrinsic-size: 360px 520px;
  }

  .paper-box-image,
  .paper-box-text {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    float: none !important;
    clear: both !important;
    padding: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .paper-box-image {
    margin-bottom: 8px !important;
  }

  .paper-box-image > div {
    width: 100% !important;
    max-width: 100% !important;
  }

  .paper-box-image img,
  .paper-box img,
  .page__content .paper-box img {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    object-fit: contain !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  /* Full publication list: journal badge above title on mobile. */
  .pub-table,
  .pub-table tbody,
  .pub-table tr,
  .pub-table td {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
  }

  .pub-table {
    margin-bottom: 8px !important;
    border-bottom: 1px solid #ddd !important;
  }

  .pub-table td {
    padding-top: 4px !important;
    padding-bottom: 4px !important;
  }

  .pub-journal {
    padding-right: 0 !important;
    padding-bottom: 2px !important;
    white-space: normal !important;
  }

  .pub-title {
    padding-left: 0 !important;
    line-height: 1.42 !important;
  }

  .pub-journal .badge,
  .badge {
    display: inline-block !important;
    max-width: 100% !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    line-height: 1.25 !important;
    margin-bottom: 3px !important;
    top: 0 !important;
  }

  /* Section titles smaller and tighter on mobile. */
  h1 {
    font-size: 1.20em !important;
    line-height: 1.28 !important;
    margin-top: 1.0em !important;
    margin-bottom: 0.45em !important;
  }

  h2,
  h3 {
    line-height: 1.32 !important;
  }
}

/* Extra-small phones */
@media screen and (max-width: 420px) {
  #main,
  .initial-content,
  .page,
  .page__content,
  .page__inner-wrap,
  .archive,
  .wrapper,
  .container,
  .layout--single .page,
  .layout--single .archive {
    padding-left: 9px !important;
    padding-right: 9px !important;
  }

  .page__content {
    font-size: 0.90rem !important;
    line-height: 1.52 !important;
  }

  .sidebar,
  .sidebar.sticky {
    width: calc(100% - 18px) !important;
    margin-top: 6px !important;
    margin-bottom: 8px !important;
    padding: 9px !important;
    border-radius: 13px !important;
  }

  .sidebar > div,
  .sidebar .author__profile {
    grid-template-columns: 72px minmax(0, 1fr) !important;
    column-gap: 9px !important;
  }

  .author__avatar,
  .author__avatar img {
    width: 72px !important;
    height: 72px !important;
    max-width: 72px !important;
    max-height: 72px !important;
    min-width: 72px !important;
  }

  .author__name {
    font-size: 0.99rem !important;
  }

  .author__bio,
  .author__content p {
    font-size: 0.68rem !important;
    line-height: 1.32 !important;
  }

  .author__urls a,
  .author__urls span,
  .author__urls li span,
  .mobile-jump-nav a {
    font-size: 0.66rem !important;
    padding: 3px 6px !important;
  }

  .author__urls li:nth-child(1) a,
  .author__urls li:nth-child(1) span,
  .author__urls li:nth-child(2) a,
  .author__urls li:nth-child(2) span {
    font-size: 0.68rem !important;
    padding: 0 !important;
  }

  .author__urls {
    column-gap: 5px !important;
  }

  .scholar-badge {
    font-size: 11px !important;
  }
}

/* =========================================================
   Final mobile author-card and hamburger-menu overrides
   ========================================================= */
@media screen and (max-width: 900px) {

  /* Use the theme hamburger menu as the single jump menu.
     The extra chip jump bar is intentionally hidden to avoid duplicate navigation. */
  .mobile-jump-nav {
    display: none !important;
  }

  /* Make the author card height fully participate in normal page flow. */
  .sidebar,
  .sidebar.sticky {
    overflow: visible !important;
    height: auto !important;
  }

  .sidebar > div,
  .sidebar .author__profile {
    grid-template-rows: auto auto !important;
    align-items: start !important;
    overflow: visible !important;
    height: auto !important;
  }

  .author__avatar {
    grid-column: 1 !important;
    grid-row: 1 !important;
    align-self: start !important;
  }

  .author__content {
    grid-column: 2 !important;
    grid-row: 1 !important;
    display: block !important;
    min-width: 0 !important;
    overflow: visible !important;
  }

  .author__name {
    overflow: visible !important;
    text-overflow: clip !important;
  }

  /* Keep the short author bio under the name readable and wrapped. */
  .author__bio,
  .author__content p {
    display: block !important;
    max-width: 100% !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }

  .author__bio p {
    margin: 0 !important;
    max-width: 100% !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }

  .author__urls-wrapper {
    grid-column: 1 / -1 !important;
    grid-row: 2 !important;
    margin-top: 9px !important;
    padding-top: 8px !important;
    border-top: 1px solid #eeeeee !important;
    overflow: visible !important;
  }

  /* Hide the theme-generated list only on mobile, and replace it with
     a controlled layout that preserves icons + text. */
  .author__urls {
    display: none !important;
  }

  .mobile-author-meta {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    overflow: visible !important;
  }

  .mobile-meta-row {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 0 4px 0 !important;
    padding: 0 !important;
    color: #444 !important;
    font-size: 0.76rem !important;
    line-height: 1.28 !important;
    white-space: normal !important;
    overflow-wrap: break-word !important;
    word-break: normal !important;
  }

  .mobile-meta-icon {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 0 0 1.15em !important;
    width: 1.15em !important;
    min-width: 1.15em !important;
    margin-right: 6px !important;
    color: #111 !important;
    font-size: 0.95em !important;
    line-height: 1 !important;
  }

  .mobile-contact-row {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 6px !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 6px 0 0 0 !important;
    padding: 0 !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
  }

  .mobile-contact-row::-webkit-scrollbar {
    display: none !important;
  }

  .mobile-contact-chip {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 0 0 auto !important;
    gap: 4px !important;
    padding: 3px 7px !important;
    border-radius: 999px !important;
    background: #f6f8fa !important;
    color: #444 !important;
    font-size: 0.70rem !important;
    line-height: 1.25 !important;
    text-decoration: none !important;
    white-space: nowrap !important;
  }

  .mobile-contact-chip:hover,
  .mobile-contact-chip:active {
    background: #eef2f6 !important;
    color: #1f5f9f !important;
    text-decoration: none !important;
  }

  .mobile-contact-chip i,
  .mobile-contact-chip svg {
    flex: 0 0 auto !important;
    width: 0.95em !important;
    height: 0.95em !important;
    font-size: 0.95em !important;
    margin: 0 !important;
  }

  /* Make sure the first body paragraph starts after the author card rather than underneath it. */
  .page,
  .page__inner-wrap,
  .page__content {
    clear: both !important;
  }

  .page__content > p:first-of-type {
    clear: both !important;
  }

  /* Compact, non-duplicated hamburger dropdown. */
  .greedy-nav .hidden-links {
    width: min(240px, calc(100vw - 24px)) !important;
    max-height: 52vh !important;
    overflow-y: auto !important;
  }

  .greedy-nav .hidden-links li {
    display: block !important;
  }

  .greedy-nav .hidden-links a {
    padding: 9px 13px !important;
    font-size: 0.82rem !important;
  }
}

@media screen and (max-width: 420px) {
  .mobile-meta-row {
    font-size: 0.68rem !important;
    line-height: 1.24 !important;
  }

  .mobile-contact-row {
    gap: 5px !important;
  }

  .mobile-contact-chip {
    font-size: 0.66rem !important;
    padding: 3px 6px !important;
  }

  .mobile-meta-icon {
    margin-right: 5px !important;
  }
}


/* =========================================================
   Hard mobile flow fix
   =========================================================
   On Minimal Mistakes, author_profile is rendered as a sidebar before
   the page body. Some mobile browsers can still let the first paragraph
   wrap under/around that sidebar even after float:none overrides. The
   following rules make #main a vertical flex container only on mobile,
   forcing the author card and the page body into two real rows.
   ========================================================= */
@media screen and (max-width: 900px) {
  #main {
    display: flex !important;
    flex-direction: column !important;
    align-items: stretch !important;
    flex-wrap: nowrap !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    overflow-x: hidden !important;
  }

  #main > .sidebar,
  #main > .sidebar.sticky {
    order: 1 !important;
    flex: 0 0 auto !important;
    display: block !important;
    float: none !important;
    clear: both !important;
    position: static !important;
    transform: none !important;
    z-index: 2 !important;
  }

  #main > .page,
  #main > .archive,
  #main > article.page {
    order: 2 !important;
    flex: 0 0 auto !important;
    display: block !important;
    float: none !important;
    clear: both !important;
    position: relative !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    transform: none !important;
    z-index: 1 !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin-top: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-top: 0 !important;
    overflow: visible !important;
  }

  .page__inner-wrap,
  .page__content {
    display: block !important;
    float: none !important;
    clear: both !important;
    position: relative !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    transform: none !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    overflow: visible !important;
  }

  .intro-block {
    display: block !important;
    float: none !important;
    clear: both !important;
    position: relative !important;
    z-index: 3 !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin-top: 0.6rem !important;
    margin-bottom: 0.8rem !important;
    padding-top: 0 !important;
    overflow: visible !important;
  }

  .intro-block::before,
  .page__content::before,
  .page__inner-wrap::before {
    content: "" !important;
    display: table !important;
    clear: both !important;
  }

  .intro-block p:first-child {
    margin-top: 0 !important;
  }
}


/* =========================================================
   Real mobile spacer before intro text
   =========================================================
   This is a real block inserted before the first intro paragraph.
   It controls the visible blank space directly, so changing
    will always change the mobile gap.

   How to tune:
   - If the first paragraph is still covered, increase 260px.
   - If the blank space is too large, decrease 260px.
   - Do not adjust #main > .page margin-top for this issue.
   ========================================================= */
.mobile-intro-spacer {
  display: none;
}

@media screen and (max-width: 900px) {
  :root {
    --mobile-intro-spacer-height: 150px;
  }

  .mobile-intro-spacer {
    display: block !important;
    width: 100% !important;
    height: var(--mobile-intro-spacer-height) !important;
    min-height: var(--mobile-intro-spacer-height) !important;
    max-height: var(--mobile-intro-spacer-height) !important;
    flex: 0 0 auto !important;
    clear: both !important;
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    overflow: hidden !important;
  }

  .intro-block {
    display: block !important;
    clear: both !important;
    margin-top: 0 !important;
    padding-top: 0 !important;
  }

  .intro-block p:first-child,
  .page__content > .intro-block:first-child p:first-child,
  .page__content > p:first-of-type {
    margin-top: 0 !important;
    padding-top: 0 !important;
  }
}


</style>

<script>
(function() {
  const statsUrl = "{{ '/google-scholar-stats/gs_data.json' | relative_url }}?v=" + new Date().getTime();

  fetch(statsUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to load gs_data.json: " + response.status);
      }
      return response.json();
    })
    .then(data => {
      const citedby = data.citedby ?? "N/A";
      const hindex = data.hindex ?? "N/A";
      const i10index = data.i10index ?? "N/A";

      document.getElementById("scholar_total_cit").textContent = citedby;
      document.getElementById("scholar_badge_citations").textContent = citedby;
      document.getElementById("scholar_badge_hindex").textContent = hindex;
      document.getElementById("scholar_badge_i10index").textContent = i10index;
    })
    .catch(error => {
      console.error("Failed to load Google Scholar stats:", error);

      document.getElementById("scholar_total_cit").textContent = "N/A";
      document.getElementById("scholar_badge_citations").textContent = "N/A";
      document.getElementById("scholar_badge_hindex").textContent = "N/A";
      document.getElementById("scholar_badge_i10index").textContent = "N/A";
    });
})();
</script>


<script>
(function() {
  const mobileMenuItems = [
    ["#research-impact", "Research Focus"],
    ["#news", "News"],
    ["#representative-publications", "Representative Publications"],
    ["#publications", "Full Publication List"],
    ["#patents", "Patents"],
    ["#honors-and-awards", "Honors and Awards"],
    ["#educations", "Education"],
    ["#research-experience", "Research Experience"],
    ["#academic-service", "Academic Service"],
    ["#technical-skills", "Technical Skills"]
  ];

  function isMobile() {
    return window.matchMedia && window.matchMedia("(max-width: 900px)").matches;
  }

  function rebuildMobileGreedyMenu() {
    if (!isMobile()) {
      return;
    }

    const nav = document.querySelector(".greedy-nav");
    if (!nav) {
      return;
    }

    let hiddenLinks = nav.querySelector(".hidden-links");
    if (!hiddenLinks) {
      hiddenLinks = document.createElement("ul");
      hiddenLinks.className = "hidden-links hidden";
      nav.appendChild(hiddenLinks);
    }

    /* Remove the theme-overflow items and our older injected items on mobile.
       This prevents duplicate entries such as About / Research Focus / News appearing twice. */
    hiddenLinks.innerHTML = "";

    mobileMenuItems.forEach(([href, label]) => {
      const li = document.createElement("li");
      li.setAttribute("data-mobile-section-link", "true");

      const a = document.createElement("a");
      a.href = href;
      a.textContent = label;
      a.addEventListener("click", function() {
        hiddenLinks.classList.add("hidden");
      });

      li.appendChild(a);
      hiddenLinks.appendChild(li);
    });
  }

  function findLink(items, fallbackIndex, matcher) {
    const links = items
      .map(item => item.querySelector("a"))
      .filter(Boolean);

    const matched = links.find(link => {
      const href = (link.getAttribute("href") || "").toLowerCase();
      const text = (link.textContent || "").toLowerCase();
      const html = (link.innerHTML || "").toLowerCase();
      return matcher(href, text, html);
    });

    if (matched) return matched;

    const fallbackItem = items[fallbackIndex];
    return fallbackItem ? fallbackItem.querySelector("a") : null;
  }

  function normalizeMobileAuthorCard() {
    if (!isMobile()) {
      return;
    }

    const sidebar = document.querySelector(".sidebar");
    if (!sidebar) {
      return;
    }

    const urlsWrapper = sidebar.querySelector(".author__urls-wrapper");
    const originalList = sidebar.querySelector(".author__urls");
    if (!urlsWrapper || !originalList) {
      return;
    }

    const items = Array.from(originalList.querySelectorAll("li"));

    const emailLink = findLink(items, 2, function(href, text, html) {
      return href.startsWith("mailto:") || text.includes("email") || html.includes("fa-envelope");
    });

    const researchGateLink = findLink(items, 3, function(href, text, html) {
      return href.includes("researchgate") || text.includes("researchgate") || html.includes("researchgate");
    });

    const scholarLink = findLink(items, 4, function(href, text, html) {
      return href.includes("scholar.google") || text.includes("google scholar") || html.includes("graduation-cap");
    });

    const oldMeta = urlsWrapper.querySelector(".mobile-author-meta");
    if (oldMeta) {
      oldMeta.remove();
    }

    const meta = document.createElement("div");
    meta.className = "mobile-author-meta";

    meta.innerHTML = `
      <div class="mobile-meta-row mobile-meta-location">
        <span class="mobile-meta-icon" aria-hidden="true"><i class="fas fa-map-marker-alt"></i></span>
        <span>Hong Kong, China</span>
      </div>
      <div class="mobile-meta-row mobile-meta-affiliation">
        <span class="mobile-meta-icon" aria-hidden="true"><i class="fas fa-map-marker-alt"></i></span>
        <span>The University of Hong Kong</span>
      </div>
      <div class="mobile-contact-row" aria-label="Contact and academic profiles">
        <a class="mobile-contact-chip mobile-email-chip" href="${emailLink ? emailLink.href : '#'}">
          <i class="fas fa-envelope" aria-hidden="true"></i><span>Email</span>
        </a>
        <a class="mobile-contact-chip mobile-rg-chip" href="${researchGateLink ? researchGateLink.href : '#'}">
          <i class="fab fa-researchgate" aria-hidden="true"></i><span>ResearchGate</span>
        </a>
        <a class="mobile-contact-chip mobile-scholar-chip" href="${scholarLink ? scholarLink.href : 'https://scholar.google.com/citations?user=worq2P0AAAAJ&hl=zh-CN'}">
          <i class="fas fa-graduation-cap" aria-hidden="true"></i><span>Google Scholar</span>
        </a>
      </div>
    `;

    urlsWrapper.appendChild(meta);
  }

  function runMobileFixes() {
    rebuildMobileGreedyMenu();
    normalizeMobileAuthorCard();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", runMobileFixes);
  } else {
    runMobileFixes();
  }

  window.addEventListener("resize", runMobileFixes);
})();
</script>



<h1 id="research-impact">🌟 Research Focus and Impact</h1>

<div class="impact-list" markdown="1">

- **Medical foundation models and multi-agent intelligence.** Developed a heterogeneous multi-agent paradigm for medical AI, accepted by **ICML 2026**, showing how specialist models can complement general-purpose foundation models in high-stakes clinical reasoning and risk prediction.

- **Clinically validated interpretable medical AI.** Built a transparent and interactive sleep apnea assessment system, published as a **sole first-author Nature Communications** paper and validated across large-scale, multi-center, multi-ethnic overnight recordings involving **over 15,000 subjects**.

- **Multimodal physiological representation learning.** Designed information-bottleneck-based and Transformer-based frameworks for ECG, EEG, PPG, and polysomnography analysis, with selected first-author publications in **Information Fusion**, **Neural Networks**, **IEEE JBHI**, and **IEEE TIM**.

- **Deployable healthcare intelligence.** Developed lightweight, interpretable, and edge-compatible models for sleep apnea detection, physiological signal quality assessment, ECG-based disease screening, and personalized health monitoring.

- **Translation-oriented AI research.** Experienced in converting AI algorithms into clinical-style systems, including interpretable user interfaces, uncertainty-aware risk indicators, multi-center validation, edge deployment, and human-AI collaborative diagnosis.

</div>

<h1 id="news">🔥 News</h1>

- *2026.06*: &nbsp;🎉 Our paper **"Why specialist models still matter: a heterogeneous multi-agent paradigm for medical artificial intelligence"** has been accepted by **ICML 2026**. This work explores specialist-model orchestration and heterogeneous multi-agent collaboration for high-stakes medical AI, bridging foundation models, clinical reasoning, and deployable healthcare intelligence.
- *2025.07*: &nbsp;🚀 Our paper **"Transparent artificial intelligence--enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios"** has been accepted by **Nature Communications**.
- *2025.04*: &nbsp;🎉 Our paper **"XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis"** has been accepted by **Information Fusion**.
- *2025.03*: &nbsp;🎓 Awarded the qualification for **exceptional early graduation** at Fudan University.
- *2024.10*: &nbsp;🔍 Our work **"IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis"** was published in **Neural Networks**.
- *2023.10*: &nbsp;💡 Our personalized sleep apnea diagnosis study was selected as a **cover highlight article** in **IEEE Journal of Biomedical and Health Informatics**.

<h1 id="representative-publications">⭐ Representative Publications</h1>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications 2025</div><img src="{{ '/images/NC_fig.png' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[Transparent artificial intelligence–enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios](https://www.nature.com/articles/s41467-025-62864-x)

**Shuaicong Hu**, Jian Liu, Yanan Wang, Cong Fu, Jiehu Zhu, Huan Yu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=worq2P0AAAAJ&sortby=pubdate&citation_for_view=worq2P0AAAAJ:WHdLCjDvYFkC)
- Built a transparent and interpretable human-AI collaborative sleep apnea assessment system
- Validated on multi-center, multi-ethnic overnight recordings involving **over 15,000 subjects**
- Received signed transparent peer-review praise from Prof. Thomas Penzel, President of the World Sleep Society, highlighting its future high-impact potential
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src="{{ '/images/ICML_500x276.jpg' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[Why specialist models still matter: a heterogeneous multi-agent paradigm for medical artificial intelligence](https://arxiv.org/pdf/2605.29744)

Yanan Wang†, **Shuaicong Hu†**, Jian Liu, et al.

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=worq2P0AAAAJ&sortby=pubdate&citation_for_view=worq2P0AAAAJ:7Hz3ACDFbsoC)
- Proposed a heterogeneous multi-agent paradigm for medical artificial intelligence
- Demonstrated why specialist models remain essential in high-stakes clinical scenarios and can complement general-purpose foundation models
- Explored specialist-model orchestration for clinically grounded reasoning, risk assessment, and deployable medical AI systems
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Fusion 2025</div><img src="{{ '/images/INFFUS_500x300.jpg' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis](https://www.sciencedirect.com/science/article/abs/pii/S1566253525003483)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&sortby=pubdate&citation_for_view=worq2P0AAAAJ:e5wmG9Sq2KIC)
- Developed a dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis
- Applied information bottleneck theory to multimodal physiological signal fusion
- Improved diagnostic accuracy and interpretability across heterogeneous sleep monitoring scenarios
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESWA 2025</div><img src="{{ '/images/ESWA_500x300.png' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[LEAF-Net: A real-time fine-grained quality assessment system for physiological signals using lightweight evolutionary attention fusion](https://www.sciencedirect.com/science/article/pii/S0957417425006177)

Jian Liu†, **Shuaicong Hu†**, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Xujian Feng, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:0EnyYjriUFMC)
- Developed a lightweight evolutionary attention fusion network for real-time fine-grained quality assessment of physiological signals
- Designed multi-scale feature extraction and attention fusion mechanisms for robust signal quality estimation
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neural Networks 2025</div><img src="{{ '/images/NN_500x300.png' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S0893608024000844)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Zhaoqiang Cui, Cuiwei Yang, Zhifeng Yao, Junbo Ge

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:dhFuZR0502QC)
- Developed an information-bottleneck-driven multimodal fusion framework for obstructive sleep apnea diagnosis
- Optimized complementary integration of multi-source sleep physiological signals through parallel information compression
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE JBHI 2023</div><img src="{{ '/images/JBHI_500x300.png' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[Semi-supervised learning for low-cost personalized obstructive sleep apnea detection using unsupervised deep learning and single-lead electrocardiogram](https://ieeexplore.ieee.org/document/10204654)

**Shuaicong Hu**, Ya'nan Wang, Jian Liu, Aiguo Wang, Kunzheng Li, Wenxin Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:ZeXyd9-uunAC)
- IEEE JBHI cover highlight article
- Proposed an unsupervised data-driven semi-supervised personalized paradigm for sleep apnea
- Explored transfer learning strategies for low-cost personalized sleep apnea diagnosis
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TIM 2023</div><img src="{{ '/images/TIM_500x300.png' | relative_url }}" alt="sym" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

[Personalized transfer learning for single-lead ecg-based sleep apnea detection: exploring the label mapping length and transfer strategy using hybrid transformer model](https://ieeexplore.ieee.org/abstract/document/10243153)

**Shuaicong Hu**, Ya'nan Wang, Jian Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:IWHjjKOFINEC)
- Designed personalized transfer learning strategies for single-lead ECG-based sleep apnea detection
- Systematically studied label mapping length and transfer strategies to improve model adaptability
</div>
</div>

<h1 id="publications">📝 Full Publication List</h1>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ICML 2026</span></td>
    <td class="pub-title">
      <a href="https://arxiv.org/pdf/2605.29744">Why specialist models still matter: a heterogeneous multi-agent paradigm for medical artificial intelligence</a>, 
      Yanan Wang†, <strong>Shuaicong Hu</strong>†, Jian Liu, et al. († co-first author)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Nature 2026</span></td>
    <td class="pub-title">
      Conversational agent for risk trajectory prediction in heart failure, 
      Yanan Wang†, <strong>Shuaicong Hu</strong>†, Jian Liu, et al. (Under revision; † co-first author)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Nature Communications 2025</span></td>
    <td class="pub-title">
      <a href="https://www.nature.com/articles/s41467-025-62864-x">Transparent artificial intelligence-enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios</a>, 
      <strong>Shuaicong Hu</strong>, Jian Liu, Yanan Wang, Cong Fu, Jiehu Zhu, Huan Yu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Information Fusion 2025</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/abs/pii/S1566253525003483">XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Neural Networks 2025</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0893608024007603">IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Zhaoqiang Cui, Cuiwei Yang, Zhifeng Yao, Junbo Ge.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ESWA 2025</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0957417425006177">LEAF-Net: A real-time fine-grained quality assessment system for physiological signals using lightweight evolutionary attention fusion</a>, 
      Jian Liu†, <strong>Shuaicong Hu</strong>†, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Cuiwei Yang. († co-first author)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE JBHI 2023</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/document/10204654">Semi-supervised learning for low-cost personalized obstructive sleep apnea detection using unsupervised deep learning and single-lead electrocardiogram</a>, 
      <strong>Shuaicong Hu</strong>, Ya'nan Wang, Jian Liu, Aiguo Wang, Kunzheng Li, Wenxin Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE TIM 2023</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10243153">Personalized transfer learning for single-lead ECG-based sleep apnea detection: exploring the label mapping length and transfer strategy using hybrid transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Ya'nan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE TNSRE 2023</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10046136/">Exploring the applicability of transfer learning and feature engineering in epilepsy prediction using hybrid transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Jian Liu, Rui Yang, Yanan Wang, Aiguo Wang, Kuanzheng Li, Wenxin Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE TIM 2022</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/9837102">A hybrid transformer model for obstructive sleep apnea detection based on self-attention mechanism using single-lead ECG</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">BSPC 2022</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1746809422002129">An automatic residual-constrained and clustering-boosting architecture for differentiated heartbeat classification</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Physiol. Meas. 2021</span></td>
    <td class="pub-title">
      <a href="https://iopscience.iop.org/article/10.1088/1361-6579/ac3e88">Robust wave-feature adaptive heartbeat classification based on self-attention mechanism using a transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Jiajun Zhou, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Computing in Cardiology 2020</span></td>
    <td class="pub-title">
      <a href="https://doi.org/10.22489/CinC.2020.039">Automatic 12-lead ECG classification using deep neural networks</a>, 
      Wenjie Cai, <strong>Shuaicong Hu</strong>, Jingying Yang, Jianjian Cao.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Pattern Recognition 2025</span></td>
    <td class="pub-title">
      Morphology Entropy: An efficient and parameter-free measure for revealing the morphological dynamic complexity of time series, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang. (Under review)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Applied Soft Computing 2025</span></td>
    <td class="pub-title">
      Entropy-based amplitude-phase pattern fusion and its application in efficient unsupervised ECG analysis, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang. (Under review)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ESWA 2025</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S095741742500939X">PULSE: A personalized physiological signal analysis framework via unsupervised domain adaptation and self-adaptive learning</a>, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Aiguo Wang, Guohui Zhou, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Applied Soft Computing 2024</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1568494624011645">Personalized blood pressure estimation using multisource fusion information of wearable physiological signals and transfer learning</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Wei Xiang, Qihan Hu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE JBHI 2023</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10314751">A lightweight hybrid model using multiscale Markov transition field for real-time quality assessment of photoplethysmography signals</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Qihan Hu, Daomiao Wang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">BSPC 2023</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1746809423006171">A novel interpretable feature set optimization method in blood pressure estimation using photoplethysmography signals</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Zhijun Xiao, Qihan Hu, Daomiao Wang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE IoT Journal 2024</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10722856/">An IoMT-driven framework for precision cardiovascular assessment incorporating multiscale perspectives and microfiber Bragg grating</a>, 
      Jian Liu, Heiquan Zhu, Wei Xiang, <strong>Shuaicong Hu</strong>, Qihan Hu, Daomiao Wang, Huan Yang, Zhengyi Mao, Fei Xu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">CIBM 2024</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0010482524001562">A multi-module algorithm for heartbeat classification based on unsupervised learning and adaptive feature transfer</a>, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Gaoyan Zhong, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">CMPB 2024</span></td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0169260724004474">ECG classification based on guided attention mechanism</a>, 
      Yangcheng Huang, Wenjing Liu, Ziyi Yin, <strong>Shuaicong Hu</strong>, Mingjie Wang, Wenjie Cai.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE IoT Journal 2025</span></td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/document/11036521">A dual-focus cloud-edge collaborative framework in multi-task hemodynamic parameter cross-scale analysis: The equilibrium of clinical performance and efficiency</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Wei Xiang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">EMBC 2025</span></td>
    <td class="pub-title">
      VAM: A parallel cross-modal hybrid network for accurate and interpretable vascular age estimation from PPG, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Cuiwei Yang. (Oral)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Information Fusion 2025</span></td>
    <td class="pub-title">
      Bridging the gap between computer vision and bioelectrical signal analysis, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Aiguo Wang, Guohui Zhou, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">IEEE JBHI 2025</span></td>
    <td class="pub-title">
      ECG-AuxNet: A dual-branch spatial-temporal feature fusion framework with auxiliary learning for enhanced cardiac disease diagnosis, 
      Ruiqi Shen, Yanan Wang, Chunge Cao, <strong>Shuaicong Hu</strong>, Jian Liu, Hongyu Wang, Gaoyan Zhong, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">EAAI 2025</span></td>
    <td class="pub-title">
      Edge-BP: An ultra-efficient edge AI system for real-time and remote health tracking, 
      Wei Xiang, Jian Liu, <strong>Shuaicong Hu</strong>, Haihui Zhang, Chao Huang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ESWA 2025</span></td>
    <td class="pub-title">
      Edge-intelligent cross-platform architecture for knowledge-intensive arterial blood pressure inference in distributed healthcare IoT networks, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Wei Xiang, Cuiwei Yang. (Revision)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">CISP-BMEI 2023</span></td>
    <td class="pub-title">
      <a href="https://doi.org/10.1109/CISP-BMEI60920.2023.10373266">DeT-Net: A two-stage method for accurate automatic heart segmentation</a>, 
      Yuhang Deng, <strong>Shuaicong Hu</strong>, Yuexiao Feng, Wei Jian, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ICCPR 2023</span></td>
    <td class="pub-title">
      <a href="https://dl.acm.org/doi/abs/10.1145/3633637.3633692">CardiacSegFormer: Transformer for semantic segmentation of cardiac images</a>, 
      Yuexiao Feng, <strong>Shuaicong Hu</strong>, Yuhang Deng, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">Physiol. Meas. 2022</span></td>
    <td class="pub-title">
      <a href="https://iopscience.iop.org/article/10.1088/1361-6579/ac7939/meta">Classification of multi-lead ECG with deep residual convolutional neural networks</a>, 
      Wenjie Cai, Fanli Liu, Bolin Xu, Xuan Wang, <strong>Shuaicong Hu</strong>, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal"><span class="badge">ICSAI 2021</span></td>
    <td class="pub-title">
      <a href="https://doi.org/10.1109/ICSAI53574.2021.9664075">Analysis of ECG de-noising using non-local means with approximate coefficients and particle swarm optimization</a>, 
      Jianjian Cao, Wenjie Cai, <strong>Shuaicong Hu</strong>, Jingying Yang, Yufeng Ji, Jadera Acen.
    </td>
  </tr>
</table>

<h1 id="patents">🧩 Patents</h1>

- Cuiwei Yang, **Shuaicong Hu**, Jian Liu, Yanan Wang. Invention Patent: **"A Time Series Analysis Method, Computer Equipment and Storage Medium,"** China, 202411334528.2, 2024-09-24.

<h1 id="honors-and-awards">🎖 Honors and Awards</h1>

- *2025.10* National Scholarship for Doctoral Students, Fudan University; featured as a representative case by Fudan University official media
- *2025.04* Outstanding Graduate of Fudan University
- *2023.10* Huatai Securities Technology Named Scholarship for Doctoral Students at Fudan University
- *2022.04* Outstanding Master's Graduate of Shanghai
- *2022.04* Outstanding Master's Graduate of University of Shanghai for Science and Technology
- *2024.08* Third Prize in China Graduate Student Artificial Intelligence Innovation Competition
- *2024.07* Second Prize in National Biomedical Engineering Innovation Design Competition
- *2023.07* Second Prize in National Biomedical Engineering Innovation Design Competition
- *2021.12* 5th Place Globally / 1st Place in China in PhysioNet International Physiological Signal Challenge
- *2021.12* 1st Place Nationally in CPSC China Physiological Signal Challenge
- *2021.10* Third Prize in the 18th China Graduate Student Mathematical Contest in Modeling "Huawei Cup"
- *2021.05* Silver Award in the 7th China International "Internet+" Innovation and Entrepreneurship Competition

<h1 id="educations">📖 Education</h1>

- *2026.03 - Present*, **The University of Hong Kong**, Department of Electrical and Computer Engineering, Postdoctoral Fellow  
  Research focus: medical foundation models, LLM-based clinical agents, multimodal physiological intelligence, and deployable healthcare AI.

- *2022.09 - 2025.12*, **Fudan University**, Electronic Information, Ph.D. in Engineering, exceptional early graduation  
  Research focus: transparent AI-enabled sleep apnea monitoring, interpretable physiological AI, multimodal sleep analysis, and human-AI collaborative diagnosis. Published 15 SCI papers during doctoral studies, including two first-author papers with IF>15, multiple high-impact journal papers, and two IEEE Transactions papers.

- *2019.09 - 2022.06*, **University of Shanghai for Science and Technology**, Electronic Information, M.Eng.  
  Research focus: ECG AI, deep learning for physiological time-series analysis, heartbeat classification, and single-lead ECG-based sleep apnea detection.

<h1 id="research-experience">💬 Research and Project Experience</h1>

- *2026*, **Heterogeneous Multi-agent Medical AI System**, Co-first Author, ICML 2026  
  Developed a heterogeneous multi-agent paradigm for medical AI, designed specialist-model orchestration mechanisms, and explored clinical reasoning and risk assessment in high-stakes medical scenarios.

- *2025*, **Interpretable and Interactive Sleep Apnea Assessment System**, Sole First Author, Nature Communications  
  Built a transparent AI-enabled interpretable and interactive system for sleep apnea assessment across flexible monitoring scenarios. The system was validated on large-scale, multi-center, multi-ethnic overnight recordings involving over 15,000 subjects.

- *2025*, **Multimodal Physiological Representation Learning for Sleep and Cardiovascular Intelligence**, First Author / Core Contributor  
  Developed multimodal fusion and representation learning frameworks for ECG, EEG, PPG, and polysomnography signals, including information-bottleneck-driven fusion mechanisms.

- *2024.11 - Present*, **National Key R&D Program**, Core Technical Contributor  
  Contributed to the construction of a non-invasive body-surface electroanatomical mapping algorithm framework for arrhythmia localization, including abnormal heartbeat detection, pathological feature mining, ECG inverse-problem modeling, and multimodal time-frequency feature fusion.

- *2024.01 - Present*, **National Natural Science Foundation General Program**, Core Member  
  Developed non-invasive multimodal assessment methods for atrial fibrillation progression using ECG, PPG, time-frequency analysis, physiological signal quality assessment, and machine learning.

- *2022.02 - Present*, **Smart Electrophysiology Diagnosis and Treatment Joint Laboratory**, Principal Participant  
  Contributed to smart electrophysiology diagnosis and treatment technologies, ECG/PPG signal fusion, AI-based cardiovascular assessment, polysomnography applications, and clinical-style deployment of physiological AI systems.

<h1 id="academic-service">💻 Academic Service</h1>

- Reviewer for over 30 journals and conferences in AI, medical AI, biomedical engineering, and digital health, including *The Lancet*, *Information Fusion*, *npj Digital Medicine*, *Artificial Intelligence Review*, *IEEE Transactions on Neural Networks and Learning Systems*, *Information Processing and Management*, *Expert Systems With Applications*, *IEEE Journal of Biomedical and Health Informatics*, *Applied Soft Computing*, *Computers in Biology and Medicine*, *Machine Learning: Science and Technology*, *IEEE Transactions on Instrumentation and Measurement*, and *Biomedical Signal Processing and Control*.
- Society Membership: Chinese Society of Biomedical Engineering.

<h1 id="technical-skills">🛠 Technical Skills</h1>

- **Medical Foundation Models and LLM Agents:** medical multi-agent systems, specialist-model orchestration, LLM-based clinical reasoning, risk-trajectory prediction, prompt/evaluation pipelines, and high-stakes medical AI system design.
- **Multimodal Physiological AI:** ECG, EEG, PPG, PSG, and wearable physiological signal modeling; multimodal fusion; sleep analysis; cardiovascular assessment; signal quality evaluation; clinical-style risk modeling.
- **Machine Learning and Deep Learning:** PyTorch, TensorFlow, CNNs, Transformers, GNNs, semi-supervised learning, unsupervised domain adaptation, transfer learning, uncertainty modeling, interpretable AI, and information-bottleneck-based representation learning.
- **Engineering and Deployment:** Linux, GPU servers, research computing environments, model training pipelines, model compression, edge deployment, real-time physiological monitoring, and AI system prototyping.
- **Data and System Development:** end-to-end pipelines from raw physiological data preprocessing, feature extraction, model training, evaluation, visualization, and interactive system deployment.
- **Visualization and Interface Development:** PyQt5, Matplotlib, scientific visualization, medical AI interface prototyping, paper-quality figure generation, Overleaf, and Adobe tools.
- **Personal Interests:** Piano, especially classical piano; interested in music, technology, and human-centered AI systems.
