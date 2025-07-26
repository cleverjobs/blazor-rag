# TelerikEditor allowing style tags

## Question

**Joh** asked on 07 Dec 2021

One of the most basic features, and a reason why many would want to use an HTML editor, is to use style tags to style the content of the HTML editor. However, it appears if you use the iframe, you cannot do this. The whole point of an iframe is to stop scope creep both ways, which means style tags should work without issue. Although they seem to be ignored in the editor, and HTML is placed inside an <textarea> outside of the iframe, making the style tag affect the entire web app. And if you use a div instead of an iframe, you get the scope creep. Seriously.... why is this not implemented???? Is there a way to make the iframe honor the style tags?

## Answer

**Apostolos** answered on 08 Dec 2021

Hi John, I understand that custom content styling may be important for your use case. I apologize if the lack of support is a major showstopper for you. There is a related feature request. My suggestion is to vote for it and follow it for status updates. We plan some Editor enhancements for our next major release (R1, due in early 2022) and I asked our dev team to consider this feature as well. Adding a <style> tag to the iframe <body> (as part of the Editor value) will allow the user to delete it by mistake. That is why we intend to enable developers to inject CSS files to the iframe <head> instead. In the meantime, if the feature is critical for you, consider a JavaScript approach. Here is how to inject a <style> tag to the Editor iframe <head>. Regards, Apostolos
