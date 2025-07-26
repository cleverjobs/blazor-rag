# Specific TelerikGrid Header alignment: how to?

## Question

**Cla** asked on 08 Oct 2021

I have a TelerikGrid component with some columns. I need to center the header text for one of these. I read some solutions adding css, but it apply to all columns, or it select the column by position. I need to apply the align style only for specific columns and not reference it by position. It is possible? I also tried HeaderTemplate but to center align a column i need to access the parent element with .k-link and the header template is nested inside it. How to solve? Thanks

## Answer

**Svetoslav Dimitrov** answered on 13 Oct 2021

Hello Claudio, We have an open feature request regarding the ability to set a CSS class to the header cell of a Grid column. I have added your vote for it and you can follow it to receive email notifications on status updates. In the meantime, you can use an approach like shown in the "Wrap and center the Grid Column Header text" knowledge base article. You can further extend the CSS rules to target a single column in the Grid. The downside would be that if there are some interactions like hiding/reordering the column the CSS rules would not be bound to it, but to the targeted location in the component. Regards, Svetoslav Dimitrov

### Response

**David** commented on 28 Jun 2022

This is what I used to format my header: <style>.k-grid th.k-header { background-color: red; color: white; text-align:center;
} </style> This is placed in my Razor page.

### Response

**Diego Camilo** commented on 24 Jan 2023

I feel very sorry for my company when they bought a framework that offers so little at such a high cost, something as simple as centering a header with telerik is something complex, Telerik's documentation is poor and that's why the ui in our developments it is simple and inflexible. I add to the previous answer so that the centering is applied to headers with filter: <style>.k-link { justify-content: center; white-space: normal; vertical-align: middle;
}
</style>
