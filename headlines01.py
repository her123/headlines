import feedparser
from flask import Flask

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  first_article = feed['entries'][0]
  second_article = feed['entries'][1]
  return """<html>
    <body>
        <h1> BBC Headlines </h1>
        <b>{0}</b> <br/>
        <i>{1}</i> <br/>
	<p>{2}</p> 
        <a href="{3}">{3}</a><br/><br/>
        <b>{4}</b> <br/>
        <i>{5}</i> <br/>
        <p>{6}</p> <br/>
	<a href="{7}">{7}</a> <br/>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"),first_article.get("link"),second_article.get("title"), second_article.get("published"), second_article.get("summary"),second_article.get("link"))

if __name__ == "__main__":
  app.run(port=5000, debug=True)
