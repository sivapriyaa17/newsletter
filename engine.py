from jinja2 import Environment,FileSystemLoader
def render_newsletter(articles,file="output/output.html"):
    env=Environment(loader=FileSystemLoader("sample"))
    temp=env.get_template("output.html")
    html = temp.render(articles=articles)
    with open(file,"w",encoding="utf-8") as f:
        f.write(html)
        