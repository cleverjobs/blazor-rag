# Input sanitization

## Question

**Doo** asked on 12 Feb 2021

Hi! I have successfully used the editor control in my application. Now its priming time. I need guidance on sanitization as in the docs section, I only see this tip section: The application must sanitize the content before passing it to the editor and, optionally, before saving it to its storage after obtaining it from the editor. It is up to the application to ensure there is no malicious content (such as input sanitization, XSS attack prevention and other security concerns). Is there a best-practice or at least a minimum common rules to check for? Is there something you guys are using behind your online demo? I need to know because my site will be public facing and any malicious activity can get me in trouble.

## Answer

**Marin Bratanov** answered on 13 Feb 2021

Hi Hassan, The sanitization of the input is entirely up to the application and its needs. You may want to strip just about everything potentially dangerous (such as DOM event handlers and CSS experssions), others may want to keep even <script> tags. While I am not in a position to advise on how to do that and what third party tools you can use, I can suggest you start off with a few generic searches and threads like these ones: [https://stackoverflow.com/questions/188870/how-to-use-c-sharp-to-sanitize-input-on-an-html-page](https://stackoverflow.com/questions/188870/how-to-use-c-sharp-to-sanitize-input-on-an-html-page) [https://weblog.west-wind.com/posts/2012/jul/19/net-html-sanitation-for-rich-html-input](https://weblog.west-wind.com/posts/2012/jul/19/net-html-sanitation-for-rich-html-input) [https://www.google.com/search?q=how%20to%20sanitize%20html%20string%20C#](https://www.google.com/search?q=how%20to%20sanitize%20html%20string%20C#) Regards, Marin Bratanov

### Response

**Andy** answered on 15 May 2021

I use HtmlSanitizer [https://github.com/mganss/HtmlSanitizer](https://github.com/mganss/HtmlSanitizer)
