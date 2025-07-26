# How to Programatically set focus to a panel bar?

## Question

**Mik** asked on 14 Nov 2023

I'd like to be able to programmatically set the focus to a panel bar component. How can I go about doing this? Alt-W is not what I'm looking for. Ideally, I'd like to be able to do this from an anchor link.

## Answer

**Nadezhda Tacheva** answered on 17 Nov 2023

Hi Mike, You can do that with some JS interop and invoking the focus() method. Call that in the OnAfterRenderAsync with a bit of a delay to ensure the component and its elements will be rendered. To target the element of the first PanelBar item you can use the id attribute value that we are adding by design (e.g. "tree-item-0"). Here is a runnable sample that showcases the approach: [https://blazorrepl.telerik.com/GdvPlBbI07ZL26Ab48.](https://blazorrepl.telerik.com/GdvPlBbI07ZL26Ab48.) Regards, Nadezhda Tacheva Progress Telerik
