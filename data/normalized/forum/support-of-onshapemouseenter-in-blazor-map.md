# Support of onShapeMouseEnter in Blazor Map?

## Question

**Hir** asked on 11 Jun 2024

I see kendo Map UI demo like following and looking into source code, in there it's supporting events like "shapeMouseEnter", "shapeMouseLeave", etc. [https://demos.telerik.com/kendo-ui/html5-dashboard-sample-app](https://demos.telerik.com/kendo-ui/html5-dashboard-sample-app) On shape mouse enter or leave, it's setting hover color on region. Also, on click on shape, it's also setting background color of shape as well as doing some data filter logic. I am using Telerik Blazor, and my requirements are the same. I wanted to use shapeMouseEnter and shapeMouseLeave to highlight country. Also wanted to change its color when shape is clicked. Can you guide me on how to achieve same behavior with Telerik Blazor component?

### Response

**Rune** commented on 23 Sep 2024

Hi! We have the same functionality requirement. Should be possible to react on hover for shapes. This is very useful to provide additional information to the user.

## Answer

**Tsvetomir** answered on 26 Sep 2024

Hello Hiren and Rune, Thank you for the provided information about your requirements. Currently, the Map Shape layer doesn't expose such a hover event for the Shape layer. However, it sounds like a good idea for a feature request. Thus, I submitted it on your behalf on our Public Feedback Portal: Expose a hover event for the Map Shape Layer. I voted on your behalf to raise the priority of the item. Also, you can subscribe to the item to get notified via email for further status updates. Regards, Tsvetomir Progress Telerik
