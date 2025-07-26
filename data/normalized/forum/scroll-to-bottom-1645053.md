# Scroll to Bottom

## Question

**Eri** asked on 15 Mar 2024

Is there a way to programmatically force the grid to scroll to the bottom. I am using the grid to display history, so when they add a new item, i was to force the grid to the last row so show the last item they added.

## Answer

**Hristian Stefanov** answered on 18 Mar 2024

Hi Eric, The scrolling is a browser function, and the browser takes care of it. Therefore, to control that function, you need to use the Javascript method - scrollIntoVew. I have prepared an example for you in this REPL link. Please run and test it to see the result. In short, the example shows, every time a new item is added, how to target the latest item in the Grid content and scroll to it. Regards, Hristian Stefanov Progress Telerik
