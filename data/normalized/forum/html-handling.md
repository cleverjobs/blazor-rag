# HTML handling

## Question

**Hed** asked on 15 Aug 2020

Hello, Two quick questions: 1) Is it possible to use the control just for rendering HTML? Assuming that I want to use the control to enter and edit HTML and later just render it on a web page. Or should I just use the Blazor MarkupString for that? 2) Does the control provide some support for sanitising the HTML entered? Or do I need to analyse it to look for malware? regards

## Answer

**Marin Bratanov** answered on 16 Aug 2020

Hello Hedinn, The editor is designed to provide WYSIWYG (what you see is what you get) experience for the end user to create HTML visually, without having to know how to write HTML. It is not a rendering helper for you to use that HTML and I'd advise that you use standard framework approaches to render raw HTML instead of the editor - the MarkupString being the chief one for Blazor. For sanitizing HTML - this is up to the app as denoted in the docs. There are various existing tools and utilities that can help with such tasks. Regards, Marin Bratanov

### Response

**Hedinn** answered on 17 Aug 2020

Thank you for the prompt reply, sorry, I missed the sanitation paragraph in docs :) Otherwise looking forward to put the editor through its paces. regards
