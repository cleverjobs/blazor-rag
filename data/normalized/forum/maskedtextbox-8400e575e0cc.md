# MaskedTextbox?

## Question

**Edw** asked on 05 Feb 2020

Hello, are there are any plans for a MaskedTextbox component? I think this is another very popular component that is currently missing from Blazor library. I can't think of any workarounds for this either. For example, I have a need for a masked textbox to collect telephone numbers.

## Answer

**Marin Bratanov** answered on 05 Feb 2020

Hello Edward, For anyone else findings this thread, you can Vote for and Follow the implementation of such a component here: [https://feedback.telerik.com/blazor/1433593-masked-input-textbox.](https://feedback.telerik.com/blazor/1433593-masked-input-textbox.) I see that you have already voted for it and what I can suggest at this point is to use a regex data annotation attribute and validation. Here's one example of creating several attributes: [https://www.aspsnippets.com/Articles/Using-Multiple-Regular-Expression-Regex-Data-Annotation-attributes-in-ASPNet-MVC.aspx.](https://www.aspsnippets.com/Articles/Using-Multiple-Regular-Expression-Regex-Data-Annotation-attributes-in-ASPNet-MVC.aspx.) Our inputs validate on ValueChanged so the user will get immediate feedback when entering disallowed symbols. Regards, Marin Bratanov
