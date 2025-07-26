# Blazor - Change Tab Text Color

## Question

**Dus** asked on 20 Nov 2023

Hey there! I'm not the greatest when it comes to editing the CSS in your components. Can you help me figure out how to change the text color on the Tab Stip? My default color is Red, but I would like to change that to grey so it looks less like a warning or an alert. I pasted an example from your demo site. I'd like to change what is currently blue. Thanks in advance for any assistance!!

## Answer

**Hristian Stefanov** answered on 20 Nov 2023

Hi Dustin, The easiest way to customize the Tabstrip text is to apply a custom " color " CSS style to the Tabstrip item HTML elements. I have prepared an example for you below. Additionally, the " Class " parameter helps in specifying the desired component instance. <style>.my-tabstrip.k-tabstrip-items-wrapper.k-item,.my-tabstrip.k-tabstrip-items-wrapper.k-item:hover { color: grey;
} </style> <TelerikTabStrip Class="my-tabstrip"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second" Disabled="true"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> Regards, Hristian Stefanov Progress Telerik

### Response

**Dustin** commented on 20 Nov 2023

Thank you! This helped me figure out what I was looking for.

### Response

**Hristian Stefanov** commented on 21 Nov 2023

I'm glad to hear that, Dustin!
