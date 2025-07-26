# User-defined Columns

## Question

**Kel** asked on 24 Apr 2020

I would like to allow the user to add columns at runtime and inline edit the column header text. Is this possible?

## Answer

**Svetoslav Dimitrov** answered on 28 Apr 2020

Hello Kelly, Thank you for participating in our Blazor community! Showing/hiding columns at runtime is currently available as showcased in this demo: [https://demos.telerik.com/blazor-ui/grid/columns.](https://demos.telerik.com/blazor-ui/grid/columns.) Also there is an open Feature Request on our Feedback Portal regarding a Column Menu and also in the thread there is a solution on how to implement one: [https://feedback.telerik.com/blazor/1450105-column-chooser.](https://feedback.telerik.com/blazor/1450105-column-chooser.) A live demo of the Column Menu can be seen in our product suite for MVC, link here: [https://demos.telerik.com/aspnet-mvc/grid/column-menu.](https://demos.telerik.com/aspnet-mvc/grid/column-menu.) You can Follow this Feature Request for email notifications on status updates and I believe you have already added your Vote to it. If you want to let the user control some aspects of those columns, you should let them edit the grid in the example (or the desired portions of it) so they can generate the grid column descriptor data. On the second topic, we have an available Header Template (more information here: [https://docs.telerik.com/blazor-ui/components/grid/templates#header-template](https://docs.telerik.com/blazor-ui/components/grid/templates#header-template) ) where you can define your own rules for changing the Title, but leaves icons for Filtering and Sorting available. Another option would be to add a simple button that toggles a bool variable and if the value is true show a Telerik TextBox and use it to set the new value for the Title, otherwise hide the Textbox. Regards, Svetoslav Dimitrov
