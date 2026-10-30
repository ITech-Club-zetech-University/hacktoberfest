---
title: Project README Template
nav_exclude: true
permalink: /templates/project-readme-template/
description: "Downloadable, stack-neutral Markdown README for an original AI project."
---

# Project README Template

[Download the plain Markdown README]({{ site.baseurl }}/templates/downloads/README.md) and save it as `README.md` in your project repository. The download has no event-site front matter or Liquid tags. Replace placeholders, test your instructions and remove inapplicable sections; no project type or technology stack is prescribed.

Use the [idea canvas]({{ site.baseurl }}/templates/problem-statement/) to plan, then follow the [submission guide]({{ site.baseurl }}/submission/). This README does not replace the official OrganizerHQ form.

{% capture project_readme %}{% include_relative downloads/README.md %}{% endcapture %}
{{ project_readme | remove_first: "# [Project Name]" }}
