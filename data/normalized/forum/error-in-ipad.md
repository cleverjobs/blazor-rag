# Error in ipad

## Question

**Ila** asked on 10 Apr 2022

I'm getting the error: Exception: Microsoft.JSInterop.JSException: this.mediaQueryList.addEventListener is not a function. (In 'this.mediaQueryList.addEventListener("change",this.onMediaChange)', 'this.mediaQueryList.addEventListener' is undefined) value On ipad. Is there a fix for it?

### Response

**Marin Bratanov** commented on 11 Apr 2022

Does this happen on other browsers? Does clearing the cache (and the other steps from this article ) help?

### Response

**Patrick** commented on 28 Apr 2022

Hi Martin, I have the same problem, happening at a customer using Mobile Safari 12.1. Already removed the 'defer' attribute and change the order. <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"></script> <script src="_framework/blazor.server.js" autostart="false"></script> I've attached the call stack, maybe it helps.

## Answer

**Svetoslav Dimitrov** answered on 03 May 2022

Hello Ilan, We have an open bug report - The MediaQuery throws an error on iPad Safari. I can see that you have voted for it, and I would encourage you to click the Follow button to subscribe for email notifications on status updates. This is the best way to be notified when the bug fix will be planned and the release it will be live. Regards, Svetoslav Dimitrov
