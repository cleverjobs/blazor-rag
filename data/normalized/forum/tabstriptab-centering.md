# TabStripTab centering

## Question

**Mar** asked on 06 Oct 2022

Hello, from your Web UI TabStrip doc: RadTabStrip supports two layouts - Horizontal (default) and Vertical. In Horizontal layout, the Align property allows you to specify the way tabs position themselves: Left - tabs will be left aligned; Right - tabs will be right aligned; Center - tabs will be centered; Justify - tabs will be proportionally resized to full-up the width of the tabstrip. In Vertical layout, the values of the Align property are as follows: Left - tabs will be aligned to the top; Right - tabs will be aligned to the bottom; Center - tabs will be positioned in the middle; Justify - tabs will be proportionally resized to full-up the height of the tabstrip. I am not able to find the same properties for the Blazor version of the control. Thanks

## Answer

**Dimo** answered on 06 Oct 2022

Hi Marcos, You can achieve the same behavior with some custom CSS that uses flexbox. Our TabStrip already applies flexbox styles to the tabs, so you only need minor adjustments. <style>.tabs-expand>.k-tabstrip-items-wrapper.k-tabstrip-item { flex-grow: 1;
}.tabs-expand>.k-tabstrip-items-wrapper.k-link { justify-content: center;
}.tabs-end>.k-tabstrip-items-wrapper>.k-tabstrip-items { justify-content: end;
} </style> <p> Top position, expand tabs, center text </p> <TelerikTabStrip TabPosition="@TabPosition.Top" Class="tabs-expand"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> <p> Bottom position, move tabs to the right </p> <TelerikTabStrip TabPosition="@TabPosition.Bottom" Class="tabs-end"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> <p> Left position, move tabs to the bottom </p> <TelerikTabStrip TabPosition="@TabPosition.Left" Class="tabs-end"> <TabStripTab Title="First"> First tab content start. <br /> <br /> <br /> <br /> <br /> <br /> First tab content end. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> Regards, Dimo

### Response

**Marcos Mataloni** commented on 06 Oct 2022

Hi Dimo, Thank you for your answer. Meanwhile I was testing the ThemeBuilder, which can also achieve this kind of behavior. Marcos
