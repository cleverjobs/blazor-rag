# In a horizontal tab strip I would like align a single tab to the right of the tab strip.

## Question

**Jst** asked on 07 Jul 2022

In a horizontal tab strip I would like align a single tab to the right of the tab strip. Is this possible?

## Answer

**Dimo** answered on 12 Jul 2022

Hi John, Yes. Assign a custom CSS Class to the desired tab and apply absolute position to it with higher specificity. <TelerikTabStrip Width="800px"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third" Class="right-tab"> Third tab content. </TabStripTab> </TelerikTabStrip> <style>.k-tabstrip-items.k-item.right-tab { position: absolute; right: 0;
} </style> Regards, Dimo
