# Restricting the Editor

## Question

**Doo** asked on 01 Aug 2021

I'm trying to make the Editor a bit restricted for my users on specific pages. I have the following requirements: Only a specific font be applied from the get-go. No font selection Prevent pasting of other fonts Have only one font in the font combo Allow a default style of Ariel, 8 for normal text Allow two types of headings Allow Bold, Italic and underline style Is it possible to lock it down?

## Answer

**Dimo** answered on 04 Aug 2021

Hello Hassan, Here are the currently available options for the described use case: To apply default font styles to the regular (normal) text content, you will need a DIV edit mode, so that the editable content is part of the page and you can control its appearance with CSS. An alternative approach for the IFRAME mode would be to apply font styles programmatically on initial load. You can explicitly list only the tools that you want to appear in the toolbar. Example Documentation To limit the available font names or headings, you can customize the items in the toolbar dropdowns (font size, font name, format). The tricky part is to prevent pasting of other fonts, because these fonts can be applied in different ways. The Editor supports cleaning up of pasted content and this works with attributes and tags. If the undesired font style is applied with an inline style, you can filter it out if you strip the style attribute, which may remove other styles too. Regards, Dimo Progress Telerik
