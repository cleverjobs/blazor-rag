# How to dynamically populate DropDownButtonItems

## Question

**Pau** asked on 22 Mar 2024

I'm building a TelerikDropDownButton, and I'd like to base the DropDownButtonItems on data pulled from SQL. But I don't see anything in the documentation that allows for that to happen, and I've tried in-line C# in the items node, and it cases the build to break. Is there a way to attach a data object list to the DropDownButtonItems to generate the items dynamically?

## Answer

**Nadezhda Tacheva** answered on 25 Mar 2024

Hi Paul, The DropDownButton is not a data-bound component, it uses a declarative approach for its DropDownButtonItems. Thus, it cannot accept a list of items to automatically render a set of DropDownButtonItems. However, you can iterate through your collection and render a dedicated DropDownButtonItem for each entity. Here is an example: [https://blazorrepl.telerik.com/wSaRwJPy24nNOcP958.](https://blazorrepl.telerik.com/wSaRwJPy24nNOcP958.) Regards, Nadezhda Tacheva Progress Telerik
