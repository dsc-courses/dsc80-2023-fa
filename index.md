---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

<!-- [Jump to the current week](#week-9-code-sklearn-code-pipelines-generalization-and-cross-validation){: .btn } -->

<!-- [Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } -->

<!-- {: .warning }
**This site is under construction and everything is subject to change.** -->

{: .note }
Oct 10, 2023: Our lecture and discussion rooms have changed!
Our lectures are now in WLH 2005 and our discussions in CENTR 115 for the rest
of the quarter.

<!-- To view the lecture recordings, click on the 🎥 button for each lecture. -->

<!-- **Some office hours on Wednesday 3/8, Thursday 3/9, and Tuesday 3/21 are being held in the SDSC Auditorium instead of the 2nd floor – look closely at the [calendar](calendar) for details.** Treat these office hours as study sessions – come to them to work on projects or study for the final exam! -->

{% for module in site.modules %}
{{ module }}
{% endfor %}

<!-- <center>
<iframe src="10-80-enrollment.html" scrolling="no" style="border:none;" seamless="seamless" height="480" width="100%">
</center> -->
