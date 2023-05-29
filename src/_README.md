# Machine learning for ECG resources

A list of machine learning for ECG interpretation resources.

## Code

{% for item in code %}
### {{ item.category }}
{% for p in item.content %}
- {{ p.name }}
  - {{ p.url }}
  
{% endfor %}
{% endfor %}

## Dataset


{% for p in datasets %}
- {{ p.name }}
  - [ {{ p.url }} ]( {{ p.url }} ) 
  - **{{ p.avaibility }}**
  - *{{ p.description }}*
{% endfor %}

