# Tabstrip Drag to Reorder

## Question

**Sco** asked on 12 Jul 2024

Hello, Does the Blazor Tabstrip support drag to reorder? I see the Telerik UI for ASP.NET AJAX supports it. This is what I need. Thanks, Scott

## Answer

**Tsvetomir** answered on 15 Jul 2024

Hello Scott, We have an open feature request in your feedback portal for the desired functionality - Expose Reorderable parameter and OnDragReorder event. I voted on your behalf the bump the priority. Currently, the status of the item is Unplanned. Additionally, you can subscribe to the item to get further status updates via email. In the meantime, if any workaround appears we will share it in the linked item. Regards, Tsvetomir Progress Telerik

### Response

**Scott Michetti** commented on 16 Jul 2024

Thank you for your response. Is there another Telerik Blazor control or multiple controls I can use to have a similar layout? I would have the tabs on the left, and the HTML on the right. Something like below. The buttons on the left are dynamically created, and when clicked display HTML on the right. I would also like to be able drag and reorder the buttons on the left. Thanks, Scott

### Response

**Scott Michetti** commented on 18 Jul 2024

Hello Tsvetomir, Do you have any recommendations for the question above? Any Telerik Blazor control that I can drag and drop might work, as long as I can make it look like the panel above. Thanks, Scott

### Response

**Tsvetomir** commented on 18 Jul 2024

Hello Scott, Currently, the drag reordering functionality is supported by the Grid and TreeList components. With additional CSS customizations, it seems possible to achieve a similar layout, though it may not be entirely perfect. However, until the reordering functionality in the TabStrip component is available, I recommend using the Drawer component. The Drawer has the same layout as the one shown in the screenshot but is missing the reordering functionality. I hope the provided information helps you to move forward.
