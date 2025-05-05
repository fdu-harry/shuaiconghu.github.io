---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
<中文版>
胡帅聪，复旦大学电子信息博士（破格提前毕业），主要从事人工智能与健康医学交叉领域研究。核心研究方向包括睡眠人工智能、医学AI、时序数据分析、个性化医疗与无监督对比学习。迄今已发表SCI论文21篇，其中唯一一作/共同一作/学生一作论文10篇，涵盖Information Fusion (IF=14.8，爱思唯尔该领域IF最高期刊)、Neural Networks (IF=6.0，CCF-B)、Expert Systems With Applications (IF=7.5，CCF-C)、IEEE JBHI (IF=7.7，封面亮点文章)、IEEE TNSRE (IF=4.9，近2年高被引)等高影响因子期刊。另有一篇唯一第一作者Nature Communications (IF=14.7)论文处于大修后评审阶段（本领域第2篇）。谷歌学术总引用203次，H因子8。

主要科研成果包括：(1)首创轻量化混合架构深度学习模型(Hybrid-Net)用于单导联心电信号的睡眠呼吸暂停精准分级筛查与边缘部署；(2)国际首次提出无监督数据驱动的睡眠呼吸暂停半监督个性化范式，探索最优迁移学习策略；(3)开创信息瓶颈理论驱动的多模态融合表征增强框架(IPCT-Net)，优化多源睡眠生理信号互补整合；(4)国际首次构建透明可解释人机协作睡眠呼吸暂停诊断AI系统(Apnea Interact Xplainer)，提出透明尺度扩散机制和风险评估指标，已通过大规模多中心多种族临床数据验证。现担任Applied Soft Computing、Expert Systems With Applications、IEEE Transactions on Instrumentation & Measurement等多个高水平期刊审稿人，参与国家重点研发计划及多项国家自然科学基金项目研究。

<英文版>
Shuaicong Hu is a Ph.D. in Electronic Information at Fudan University (with early exceptional graduation honors). His research focuses on the intersection of artificial intelligence and health medicine, specializing in sleep AI, medical AI, time series analysis, personalized medicine, and unsupervised contrastive learning. He has published 21 SCI papers, including 10 as sole first/co-first/student first author, in prestigious journals such as Information Fusion (IF=14.8, Elsevier's highest IF journal in the field), Neural Networks (IF=6.0, CCF-B), Expert Systems With Applications (IF=7.5, CCF-C), IEEE JBHI (IF=7.7, featured as cover highlight article), and IEEE TNSRE (IF=4.9, highly cited in recent 2 years). Additionally, he has a sole first-author paper in Nature Communications (IF=14.7) in the final stages of major revision (only the second paper in this field). His research has accumulated 203 citations with an H-index of 8.

His key scientific contributions include: (1) pioneering lightweight hybrid deep learning architectures (Hybrid-Net) for precise sleep apnea grading and edge deployment using single-lead ECG; (2) internationally first proposing unsupervised data-driven semi-supervised personalization paradigms for sleep apnea with optimal transfer learning strategies; (3) developing information bottleneck theory-driven multimodal fusion enhancement frameworks (IPCT-Net) for optimizing complementary integration of multi-source sleep physiological signals; and (4) creating the first transparent explainable human-AI collaborative sleep apnea diagnosis system (Apnea Interact Xplainer) with transparent scaling diffusion mechanisms and risk assessment metrics, validated on large-scale multi-center multi-ethnic clinical datasets. He serves as a reviewer for multiple high-impact journals, including Applied Soft Computing, Expert Systems With Applications, and IEEE Transactions on Instrumentation & Measurement, and participates in National Key R&D Programs and multiple National Natural Science Foundation of China projects.

<a href='https://scholar.google.com/citations?user=worq2P0AAAAJ&hl=zh-CN'>Google Scholar Profile <strong><span id='total_cit'>203</span></strong> citations</a> 
<a href='https://scholar.google.com/citations?user=worq2P0AAAAJ&hl=zh-CN'><img src="https://img.shields.io/badge/Citations-203-blue?logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat"></a>

<span class='anchor' id='news'></span>
# 🔥 News（新闻）
- *2025.04*: &nbsp;🎉🎉 论文 "Transparent artificial intelligence–enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios" 在顶级期刊 **Nature Communications** (IF=14.7) 大修后获得2位审稿专家接受，即将发表！该论文为睡眠呼吸暂停+AI领域仅有的第2篇Nature Communications论文。
- *2025.03*: &nbsp;🎉🎉 论文 "XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis" 被医学AI领域顶刊 **Information Fusion** (IF=14.8, 爱思唯尔该领域IF最高期刊) 录用！
- *2025.02*: &nbsp;🔍 关于透明AI的研究 "IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis" 在人工智能领域顶级期刊 **Neural Networks** (IF=6.0) 发表！
- *2024.12*: &nbsp;🎓 荣获复旦大学"破格提前毕业"资格（本届119名博士仅3位），将于2025年底获得博士学位！
- *2023.11*: &nbsp;💡 睡眠呼吸暂停个性化诊断研究被选为 **IEEE Journal of Biomedical and Health Informatics** (IF=7.7) 封面亮点论文！

<span class='anchor' id='publications'></span>
# 📝 Representative Publications（代表性工作）

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications 2025</div><img src='images/NC_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Transparent artificial intelligence–enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios](https://www.nature.com/ncomms/)

**Shuaicong Hu**, Jian Liu, Yanan Wang, Cong Fu, Jiehu Zhu, Huan Yu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ) <strong><span class='show_paper_citations' data='worq2P0AAAAJ'></span></strong>
- 首创透明可解释人机协作的睡眠呼吸暂停诊断AI系统（该领域第2篇Nature Communications论文）
- 提出透明尺度扩散机制和风险评估指标，增强AI解释性
- 基于大规模多中心多种族临床数据验证部署后的系统在专业诊断和家庭筛查场景下的泛化性能
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Fusion 2025</div><img src='images/INFFUS_500x300.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis](https://www.sciencedirect.com/journal/information-fusion)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ) <strong><span class='show_paper_citations' data='worq2P0AAAAJ'></span></strong>
- 爱思唯尔医学AI领域影响因子最高期刊（IF=14.8）
- 提出双阶段信息瓶颈融合框架，实现多模态睡眠分析的精准解释
- 创新性应用信息瓶颈理论于多模态生理信号融合，提高诊断准确性和可解释性
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESWA 2025</div><img src='images/ESWA_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LEAF-Net: A real-time fine-grained quality assessment system for physiological signals using lightweight evolutionary attention fusion](https://www.sciencedirect.com/science/article/pii/S0957417425006177)

Jian Liu†, **Shuaicong Hu†**, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Xujian Feng, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:0EnyYjriUFMC) <strong><span class='show_paper_citations' data='worq2P0AAAAJ:0EnyYjriUFMC'></span></strong>
- Expert Systems With Applications（IF=7.5，CCF-C类，中科院一区TOP）
- 提出LEAF-Net轻量化进化注意力融合网络，实现生理信号实时精细化质量评估
- 创新性设计多尺度特征提取和注意力融合机制，提高了信号质量评估的精度
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neural Networks 2025</div><img src='images/NN_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S0893608024000844)

**Shuaicong Hu**, Yanan Wang, Jian Liu, Zhaoqiang Cui, Cuiwei Yang, Zhifeng Yao, Junbo Ge

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:dhFuZR0502QC) <strong><span class='show_paper_citations' data='worq2P0AAAAJ:dhFuZR0502QC'></span></strong>
- 人工智能领域顶级期刊Neural Networks（IF=6.0，CCF-B类）
- 首次开展信息瓶颈理论驱动的多模态融合表征增强框架
- 通过并行信息压缩剔除目标模式相关冗余，优化多源睡眠生理信号互补整合
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TNSRE 2023</div><img src='images/TNSRE_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Exploring the applicability of transfer learning and feature engineering in epilepsy prediction using hybrid transformer model](https://ieeexplore.ieee.org/abstract/document/10046136)

**Shuaicong Hu**, Jian Liu, Rui Yang, Ya’Nan Wang, Aiguo Wang, Kuanzheng Li, Wenxin Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:ZeXyd9-uunAC) <strong><span class='show_paper_citations' data='worq2P0AAAAJ:ZeXyd9-uunAC'></span></strong>
- 首次将混合Transformer架构引入癫痫预测领域，提高了特征提取效率
- 系统探索迁移学习和特征工程在多目标域癫痫预测中的适用性
- IEEE Transactions on Neural Systems and Rehabilitation Engineering（IF=4.8）
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE JBHI 2023</div><img src='images/JBHI_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Semi-supervised learning for low-cost personalized obstructive sleep apnea detection using unsupervised deep learning and single-lead electrocardiogram](https://ieeexplore.ieee.org/document/10204654)

**Shuaicong Hu**, Ya'nan Wang, Jian Liu, Aiguo Wang, Kunzheng Li, Wenxin Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:ZeXyd9-uunAC) <strong><span class='show_paper_citations' data='worq2P0AAAAJ:ZeXyd9-uunAC'></span></strong>
- IEEE JBHI封面亮点文章（IF=7.7）
- 国际首次提出无监督数据驱动学习的睡眠呼吸暂停半监督个性化范式
- 探索了最优迁移学习策略，促进了低成本个性化睡眠呼吸暂停诊断实施
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TIM 2023</div><img src='images/TIM_500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Personalized transfer learning for single-lead ecg-based sleep apnea detection: exploring the label mapping length and transfer strategy using hybrid transformer model](https://ieeexplore.ieee.org/abstract/document/10243153)

**Shuaicong Hu**, Ya'nan Wang, Jian Liu, Cuiwei Yang

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=worq2P0AAAAJ&citation_for_view=worq2P0AAAAJ:IWHjjKOFINEC) <strong><span class='show_paper_citations' data='worq2P0AAAAJ:IWHjjKOFINEC'></span></strong>
- IEEE Transactions on Instrumentation and Measurement（IF=5.6）
- 创新性设计个性化迁移学习策略，解决单导联心电信号睡眠呼吸暂停检测问题
- 系统性探索了标签映射长度与迁移策略对检测性能的影响，提高了模型适应性
</div>
</div>


<span class='anchor' id='publications'></span>
<h1>📝 Full Publication List（全部出版物）</h1>

<style>
.pub-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
  table-layout: fixed;
}
.pub-journal {
  width: 200px;
  vertical-align: top;
  padding-right: 15px;
}
.pub-title {
  vertical-align: top;
}
</style>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Nature Communications 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.nature.com/ncomms/">Transparent artificial intelligence-enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios</a>, 
      <strong>Shuaicong Hu</strong>, Jian Liu, Yanan Wang, Cong Fu, Jiehu Zhu, Huan Yu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Information Fusion 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/journal/information-fusion">XSleepFusion: A dual-stage information bottleneck fusion framework for interpretable multimodal sleep analysis</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Neural Networks 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0893608024007603">IPCT-Net: Parallel information bottleneck modality fusion network for obstructive sleep apnea diagnosis</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Zhaoqiang Cui, Cuiwei Yang, Zhifeng Yao, Junbo Ge.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE JBHI 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10214652">Semi-supervised learning for low-cost personalized obstructive sleep apnea detection using unsupervised deep learning and single-lead electrocardiogram</a>, 
      <strong>Shuaicong Hu</strong>, Ya'nan Wang, Jian Liu, Aiguo Wang, Kunzheng Li, Wenxin Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE TIM 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10243153">Personalized transfer learning for single-lead ecg-based sleep apnea detection: exploring the label mapping length and transfer strategy using hybrid transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Ya'nan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE TNSRE 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10046136/">Exploring the applicability of transfer learning and feature engineering in epilepsy prediction using hybrid transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Jian Liu, Rui Yang, Yanan Wang, Aiguo Wang, Kuanzheng Li, Wenxin Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">ESWA 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0957417425006177">LEAF-Net: A real-time fine-grained quality assessment system for physiological signals using lightweight evolutionary attention fusion</a>, 
      Jian Liu†, <strong>Shuaicong Hu</strong>†, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Cuiwei Yang. († 共同第一作者)
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE TIM 2022</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/9837102">A hybrid transformer model for obstructive sleep apnea detection based on self-attention mechanism using single-lead ECG</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">BSPC 2022</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1746809422002129">An automatic residual-constrained and clustering-boosting architecture for differentiated heartbeat classification</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Physiol. Meas. 2021</span>
    </td>
    <td class="pub-title">
      <a href="https://iopscience.iop.org/article/10.1088/1361-6579/ac3e88">Robust wave-feature adaptive heartbeat classification based on self-attention mechanism using a transformer model</a>, 
      <strong>Shuaicong Hu</strong>, Wenjie Cai, Tijie Gao, Jiajun Zhou, Mingjie Wang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Pattern Recognition 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/journal/pattern-recognition">Morphology Entropy: An efficient and parameter-free measure for revealing the morphological dynamic complexity of time series</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Applied Soft Computing 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/journal/applied-soft-computing">Entropy-based amplitude-phase pattern fusion and its application in efficient unsupervised ECG analysis</a>, 
      <strong>Shuaicong Hu</strong>, Yanan Wang, Jian Liu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">ESWA 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S095741742500939X">PULSE: A personalized physiological signal analysis framework via unsupervised domain adaptation and self-adaptive learning</a>, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Aiguo Wang, Guohui Zhou, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">CMPB 2024</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0169260724004474">ECG classification based on guided attention mechanism</a>, 
      Yangcheng Huang, Wenjing Liu, Ziyi Yin, <strong>Shuaicong Hu</strong>, Mingjie Wang, Wenjie Cai.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">CIBM 2024</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0010482524001562">A multi-module algorithm for heartbeat classification based on unsupervised learning and adaptive feature transfer</a>, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Gaoyan Zhong, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Information Fusion 2025</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/journal/information-fusion">Bridging the gap between computer vision and bioelectrical signal analysis</a>, 
      Yanan Wang, <strong>Shuaicong Hu</strong>, Jian Liu, Aiguo Wang, Guohui Zhou, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">BSPC 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1746809423006171">A novel interpretable feature set optimization method in blood pressure estimation using photoplethysmography signals</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Zhijun Xiao, Qihan Hu, Daomiao Wang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE IoT Journal 2024</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=dual-focus%20cloud-edge%20Jian%20Liu">A dual-focus cloud--edge collaborative framework in multi-task hemodynamic parameter cross-scale analysis</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Wei Xiang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Applied Soft Computing 2024</span>
    </td>
    <td class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S1568494624011645">Personalized blood pressure estimation using multisource fusion information of wearable physiological signals and transfer learning</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Wei Xiang, Qihan Hu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE JBHI 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10314751">A lightweight hybrid model using multiscale markov transition field for real-time quality assessment of photoplethysmography signals</a>, 
      Jian Liu, <strong>Shuaicong Hu</strong>, Yanan Wang, Qihan Hu, Daomiao Wang, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">IEEE IoT Journal 2024</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/10722856/">An IoMT-driven framework for precision cardiovascular assessment incorporating multiscale perspectives and microfiber bragg grating</a>, 
      Jian Liu, Heiquan Zhu, Wei Xiang, <strong>Shuaicong Hu</strong>, Qihan Hu, Daomiao Wang, Huan Yang, Zhengyi Mao, Fei Xu, Cuiwei Yang.
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">Physiol. Meas. 2021</span>
    </td>
    <td class="pub-title">
      <a href="https://iopscience.iop.org/article/10.1088/1361-6579/ac7939/meta">Classification of multi-lead ECG with deep residual convolutional neural networks</a>, 
      Wenjie Cai, Fanli Liu, Bolin Xu, Xuan Wang, <strong>Shuaicong Hu</strong>, Mingjie Wang
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">ICSAI 2021</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/9664075">Analysis of ECG de-noising using non-local means with approximate coefficients and particle swarm optimization</a>, 
      Jianjian Cao, Wenjie Cai, <strong>Shuaicong Hu</strong>, Jingying Yang, Yufeng Ji, Jadera Acen
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">CISP-BMEI 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://ieeexplore.ieee.org/abstract/document/9664075">DeT-Net: a two-stage method for accurate automatic heart segmentation</a>, 
      Yuhang Deng, <strong>Shuaicong Hu</strong>, Yuexiao Feng, Wei Jian, Cuiwei Yang
    </td>
  </tr>
</table>

<table class="pub-table">
  <tr>
    <td class="pub-journal">
      <span class="badge">ICCPR 2023</span>
    </td>
    <td class="pub-title">
      <a href="https://dl.acm.org/doi/abs/10.1145/3633637.3633692">CardiacSegFormer: transformer for semantic segmentation of cardiac images</a>, 
      Yuexiao Feng, <strong>Shuaicong Hu</strong>, Yuhang Deng, Cuiwei Yang
    </td>
  </tr>
</table>

<span class='anchor' id='honors-and-awards'></span>
# 🎖 Honors and Awards（荣誉及奖项）

- *2025.04* 复旦大学优秀毕业生
- *2024.10* 复旦大学优秀学生干部
- *2024.08* 中国研究生人工智能创新大赛三等奖
- *2024.07* 全国生物医学工程创新设计竞赛二等奖
- *2023.10* 复旦大学优秀学生
- *2023.10* 复旦大学博士年度华泰证券科技冠名奖学金
- *2023.07* 全国生物医学工程创新设计竞赛二等奖
- *2022.04* 上海市优秀硕士毕业生
- *2022.04* 上海理工大学优秀硕士毕业生
- *2021.12* PhysioNet国际生理信号挑战赛全球第5名/中国区第1名
- *2021.12* CPSC中国生理信号挑战赛全国第1名
- *2021.10* "华为杯"第十八届中国研究生数模竞赛三等奖
- *2021.05* 第七届中国国际"互联网+"大赛银奖

<span class='anchor' id='educations'></span>
# 📖 Educations（教育背景）

- *2022.09 - 2025.12*, 复旦大学，电子信息，工学博士（破格提前毕业）
  - 研究领域：医学人工智能、睡眠AI、时序数据分析、个性化医疗、无监督对比学习
  - 博士期间共发表SCI论文15篇，影响因子总计148.4，另有一篇唯一一作《Nature Communications》顶级期刊大修
  
- *2019.09 - 2022.06*, 上海理工大学，电子信息，工学硕士
  - 研究领域：基于深度学习的心电图心拍自动分类
  - 硕士期间以唯一第一作者身份发表IEEE TIM等SCI论文3篇
  
- *2015.09 - 2019.06*, 上海理工大学，生物医学工程，工学学士
  - 绩点排名专业top5%
  - 研究项目：期前收缩心电图智能识别

<span class='anchor' id='academic-experience'></span>
# 💬 Academic-Experience（学术与项目经历）

- *2024.11 - 至今*, 国家重点研发计划《心律失常立体定向放射定量治疗系统技术研发及样机研制》子课题组负责人
  - 负责"体表无创电解剖标测算法体系构建"子课题，主要承担异常心拍检测与病理特征挖掘研究
  - 参与整体项目申请答辩(三位答辩人之一，负责AI算法部分)，并负责第一年度的验收报告

- *2023.04 - 至今*, 国家自然科学基金面上项目《PPG与ECG信息融合新方法及其在房颤进程评估中的应用研究》核心成员
  - 负责申报书的撰写；主要承担课题中多模态同步采集设备的研制以及生理信号的实时质量评估算法
  - 已依托该项目发表中科院一区论文1篇，中科院二区论文1篇

- *2022.02 - 至今*, 智慧电生理诊疗联合实验室项目主要参与者
  - 负责联合实验室项目申请，成果申报以及完成各项指标
  - 已依托该项目发表中科院二区论文2篇

<span class='anchor' id='academic-service'></span>
# 💻 Academic-Service（学术兼职）

- 担任Applied Soft Computing（中科院一区TOP，IF=7.2）、Expert Systems With Applications（中科院一区TOP，IF=7.5）、Computers in Biology and Medicine（IF=7.0）、IEEE Transactions on Instrumentation & Measurement（IF=5.6）等20余个国际期刊审稿人
- 中国生物医学工程学会会员
