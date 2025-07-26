# Hide the expand icon on Blazor Panelbar items when there is nothing to expand.

## Question

**Dan** asked on 09 Feb 2024

How can I hide the expand button on the right side of the panelbar header if there is nothing to expand? I am willing to do this either through code somehow or even if I have to access the css and set the fill of the svg icon to white I will, but I have not been able to do so, thus far. At very least disabling the expand button would be an option as well. As you can see in my image, the top item I want an expand button but the one beneath it since it has zero hours should be removed. Any help would be appreciated.

## Answer

**Hristian Stefanov** answered on 14 Feb 2024

Hi Daniel, We render the expand icon under the following conditions: `HasChildren` is not equal to `false` `Items` is not equal to `null` , or: `ContentTemplate` is configured From the screenshot, it seems that you have `ContentTemplate` configured. Generally speaking, the ContentTemplate is rendered only for the items that have no children. It displays like a child item and allows you to add your desired content for these items (be that some additional information, HTML elements or even other components). Thus, when ContentTemplate is defined the component expects some additional content will be rendered for the items. It displays an expand arrow to allow the user actually open the item and explore its content. To override this behavior you can subscribe to the OnItemRender event of the PanelBar, to add a custom class to the items based on your desired condition. Then you can cascade through that item class to hide the expand/collapse arrow with some CSS. Thus, the arrow will not be visible but the actual ContentTemplate will still be rendered for the specific item. To handle this, you can use conditional statements inside the template and not add any content where you don't need to. I've prepared the following example to better illustrate the described approach: [https://blazorrepl.telerik.com/cyYGlebm37quqUKh35.](https://blazorrepl.telerik.com/cyYGlebm37quqUKh35.) Regards, Hristian Stefanov Progress Telerik

### Response

**Daniel** commented on 14 Feb 2024

Thank you for the reply, this worked for me. I did struggle with getting the css to apply properly, I ended up having to do something like this: ::deep .no-expand-icon svg { display: none !important; } but this applied the css correctly and fixes my issue. Thanks again for your help on this.

### Response

**Hristian Stefanov** commented on 14 Feb 2024

Hi Daniel, Thank you for your feedback. I'm glad I was able to help. Kind Regards, Hristian
