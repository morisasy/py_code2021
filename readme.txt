-- python3 -m venv venv
-- activate
---- source venv/bin/activate 

----  pip3 install -r requirements.txt



"
page = a random starting page
article_chain = []
while title of page isn't 'Philosophy' and we have not discovered a cycle:
    append page to article_chain
    download the page content
    find the first link in the content
    page = that link
    pause for a second

"
