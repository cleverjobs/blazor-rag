# Grid ? for Multiple report results

## Question

**Dea** asked on 08 Nov 2022

I would like 1 page with 1 grid that depending on user choosing a DDL choice would have different column results. example: Rpt 1 choice: Columns=a1, a1, a3, ... Rpt 2 choice: Columns a1, b2, x4, .... Can this be done? Or do I have to have a grid for each different report set? And then just hide other grids not using atm. Thanks

## Answer

**Nadezhda Tacheva** answered on 11 Nov 2022

Hi Deasun, Generally speaking, the scenario is achievable with both of the approaches. If you prefer to use one Grid instance, you can declare all possible columns in it and toggle their visibility during runtime based on the user selection in the DropDownList. Here is a basic example that demonstrates this approach: [https://blazorrepl.telerik.com/cwPFFlkW39CwPJK103.](https://blazorrepl.telerik.com/cwPFFlkW39CwPJK103.) Some additional tips that may be useful: Depending on the exact scenario you may also consider another UI for such column configuration settings - for example, CheckBoxes, RadioButtons. This may be useful if you have only a couple of possible column configurations as such UI will take less space. Also, to reduce the popup size if you have a short DropDownList collection you may configure the Popup settings of the component. You may place the column configuration UI in the Toolbar of the Grid. The Grid exposes a built-in UI option to toggle the column visibility. It is currently controlled through a Column Menu and we will additionally expose a dedicated Column Chooser. This functionality allows the user to select the columns they want to see in the Grid. Based on the details you shared, I understand that you want to determine the column visibility for the user. However, I just wanted to mention that option in case it is a good fit. I hope the above information and sample will help you move forward with your application. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva Progress Telerik
