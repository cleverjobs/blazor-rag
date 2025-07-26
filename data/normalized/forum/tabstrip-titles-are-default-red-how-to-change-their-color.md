# Tabstrip titles are default red how to change their color

## Question

**Ayu** asked on 11 Nov 2022

Tabstrip titles are default red how to change their color

## Answer

**Hristian Stefanov** answered on 15 Nov 2022

Hi Ayush, The easiest way to customize the Tabstrip titles is to apply a custom " color " CSS style to the title HTML elements. I have prepared an example for you below. Additionally, the " Class " parameter helps in specifying the desired component instance. <style>.my-tabstrip.k-tabstrip-items-wrapper.k-item,.my-tabstrip.k-tabstrip-items-wrapper.k-item:hover { color: lawngreen;
} </style> <TelerikTabStrip Class="my-tabstrip"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second" Disabled="true"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> Let me know if we can help with more information. Regards, Hristian Stefanov Progress Telerik
