# The ViewHtml dialog in the Editor strips the onclick attribute no matter what EditorPasteSettings I use

## Question

**Rol** asked on 08 Mar 2022

I am trying to add something like <a href="#" onclick="doSomething()"> do something </a>

## Answer

**Svetoslav Dimitrov** answered on 11 Mar 2022

Hello Roland, We intentionally strip the event onclick attributes when you paste HTML in the Editor for security reasons. If the users of your application are able to add click handlers (or other events) that could potentially cause security vulnerabilities that stem from our Editor component. That is why we would not want to allow such attributes. I hope that gives you a good understanding of why we chose to take that route and strip such attributes. Regards, Svetoslav Dimitrov

### Response

**Roland** commented on 11 Mar 2022

" That is why we would not want to allow such attributes" Nor do I, unless I trust the user. I wanted the admins of the app to have full control. The rest does not even get the ViewHtml control. So it would have been better if there was an opt in for "no filtering". But I found a workaround. I can construct a valid tag with all needed information that the Editor accepts and that I can morph into the correct <a> tag with onclick handler before the browser sees it.
