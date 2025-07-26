# Controlling the width of a vertical tab strip?

## Question

**Jst** asked on 21 Oct 2021

With the upgrade to 2.27 My vertical tab strip has become narrower and my labels are wrapping. How would control the width of the vertical tab strip and/or control the size of the font in the labels?

## Answer

**Marin Bratanov** answered on 23 Oct 2021

Hi, Here's a basic example I made for you that shows how you can tweak those with CSS. You can inspect the rendering and applied rules with the browser dev tools to devise more specific rules. For example, you may want to cascade them through a specific class so they don't affect all tab strips on the page, you may want to utilize the active and disabled classes for items, and so on. You can also use the header template to render custom content as well. I can also suggest inspecting the rendering and CSS rules before you start customizing to see where the rules that are an issue for you come from, as they might be similar custom rules from the project rather than a theme change. <style>.k-tabstrip-left.k-tabstrip-items.k-reset { width: 300px;
}.k-tabstrip-item.k-link { font-size: 48px; color: cyan;
} </style> <TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Left"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second" Disabled="true"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> Regards, Marin Bratanov
