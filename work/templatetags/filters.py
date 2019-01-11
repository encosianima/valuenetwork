from django import template

register = template.Library()

@register.filter
def related_agent(jn_reqs, agent):
    if jn_reqs and agent:
        reqs = []
        for req in jn_reqs:
            if req.project.agent == agent:
                reqs.append(req)
        return reqs
    else:
        return jn_reqs
