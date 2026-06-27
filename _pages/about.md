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

Shuaicong Hu is a Postdoctoral Fellow in the Department of Electrical and Computer Engineering at The University of Hong Kong. He received his Ph.D. in Electronic Information from Fudan University (复旦大学, exceptional early graduation). His research focuses on **medical foundation models**, **heterogeneous multi-agent systems**, **multimodal physiological intelligence**, **interpretable clinical AI**, and **deployable healthcare systems** across sleep medicine, ECG, EEG, PPG, polysomnography, and clinical risk modeling.

His work bridges large-scale physiological signal modeling, specialist-model orchestration, interpretable AI, uncertainty-aware clinical prediction, and real-world healthcare validation. To date, he has published **31 SCI papers**, including **12 sole first-author, co-first-author, or student first-author papers**, with selected work in **Nature Communications**, **ICML**, **Information Fusion**, **Neural Networks**, **Expert Systems With Applications**, **IEEE Journal of Biomedical and Health Informatics**, **IEEE Transactions on Neural Systems and Rehabilitation Engineering**, and **IEEE Transactions on Instrumentation and Measurement**.

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
  scroll-padding-top: 70px;
}

/* Reserve space for the fixed top navigation bar */
#main,
.initial-content,
.page,
.page__content {
  padding-top: 50px;
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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications 2025</div><img src='images/NC_fig.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Transparent artificial intelligence–enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios](https://www.nature.com/articles/s41467-025-62864-x)

**Shuaicong Hu**, Jian Liu, Yanan Wang, Cong Fu, Jiehu Zhu, Huan Yu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ)
- Built a transparent and interpretable human-AI collaborative sleep apnea assessment system
- Validated on multi-center, multi-ethnic overnight recordings involving **over 15,000 subjects**
- Received signed transparent peer-review praise from Prof. Thomas Penzel, President of the World Sleep Society, highlighting its future high-impact potential
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/ICML_500x276.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Why specialist models still matter: a heterogeneous multi-agent paradigm for medical artificial intelligence](https://arxiv.org/pdf/2605.29744)

Yanan Wang†, **Shuaicong Hu†**, Jian Liu, et al.

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=worq2P0AAAAJ&sortby=pubdate&citation_for_view=worq2P0AAAAJ:7Hz3ACDFbsoC)
- Proposed a heterogeneous multi-agent paradigm for medical artificial intelligence
- Demonstrated why specialist models remain essential in high-stakes clinical scenarios and can complement general-purpose foundation models
- Explored specialist-model orchestration for clinically grounded reasoning, risk assessment, and deployable medical AI systems
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Fusion 2025</div><img src='images/INFFUS_500x300.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis](https://www.sciencedirect.com/science/article/abs/pii/S1566253525003483)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&sortby=pubdate&citation_for_view=worq2P0AAAAJ:e5wmG9Sq2KIC)
- Developed a dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis
- Applied information bottleneck theory to multimodal physiological signal fusion
- Improved diagnostic accuracy and interpretability across heterogeneous sleep monitoring scenarios
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESWA 2025</div><img src='images/ESWA_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LEAF-Net: A real-time fine-grained quality assessment system for physiological signals using lightweight evolutionary attention fusion](https://www.sciencedirect.com/science/article/pii/S0957417425006177)

Jian Liu†, **Shuaicong Hu†**, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Xujian Feng, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:0EnyYjriUFMC)
- Developed a lightweight evolutionary attention fusion network for real-time fine-grained quality assessment of physiological signals
- Designed multi-scale feature extraction and attention fusion mechanisms for robust signal quality estimation
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neural Networks 2025</div><img src='images/NN_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S0893608024000844)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Zhaoqiang Cui, Cuiwei Yang, Zhifeng Yao, Junbo Ge

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:dhFuZR0502QC)
- Developed an information-bottleneck-driven multimodal fusion framework for obstructive sleep apnea diagnosis
- Optimized complementary integration of multi-source sleep physiological signals through parallel information compression
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE JBHI 2023</div><img src='images/JBHI_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Semi-supervised learning for low-cost personalized obstructive sleep apnea detection using unsupervised deep learning and single-lead electrocardiogram](https://ieeexplore.ieee.org/document/10204654)

**Shuaicong Hu**, Ya'nan Wang, Jian Liu, Aiguo Wang, Kunzheng Li, Wenxin Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:ZeXyd9-uunAC)
- IEEE JBHI cover highlight article
- Proposed an unsupervised data-driven semi-supervised personalized paradigm for sleep apnea
- Explored transfer learning strategies for low-cost personalized sleep apnea diagnosis
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TIM 2023</div><img src='images/TIM_500x300.png' alt="sym" width="100%"></div></div>
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
