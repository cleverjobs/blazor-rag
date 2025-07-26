# Selected row highlight

## Question

**Dia** asked on 25 Feb 2021

I am unclear how or what makes the selected Blazor Grid row highlighted when selected. I can select the row, but it doesn't get highlighted. I've looked at the demos, and for the life of me, I cannot tell how the selected row is highlighted. I assume class attribute requires something added. What am I missing here? Thx

## Answer

**Eric R | Senior Technical Support Engineer** answered on 26 Feb 2021

Hi Diana, For styling when using the Built-In themes, the selection applies the k-state-selected class to indicate it is selected which works with the Kendo Themes. See the following screenshot for a visual reference. Can you confirm if you are using a Built-In theme with your Blazor Application? If not, you may be able to add the class k-state-selected upon selection. If none of the above options apply to your implementation, can you provide a sample of you grid component and styling? Please let me know if you need any additional information. Thank you for using the Blazor forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Diana** answered on 26 Feb 2021

Hi Eric, Thanks for the reply. I am using the built-in theme, in particular the Bootstrap theme. One of the pages I am working on, is as simple as this demo, [https://demos.telerik.com/blazor-ui/grid/editing-popup](https://demos.telerik.com/blazor-ui/grid/editing-popup) example. So it appears the selected highlight is not automatic by the control.

### Response

**Diana** answered on 26 Feb 2021

Hi Eric, I found out why a row did not show selected when clicked. It seems if you don't include the attribute to the grid SelectionMode="@GridSelectionMode.Single" for example, the row will not show as selected in the case of a single row mode. It seems without the attribute it doesn't default to single or multiple. A selected row just doesn't highlight when selected. Looks like if you don't include the attribute it defaults to "None", "Single" would have been a better default given by the number of times I have seen notes in various forums about the same thing. Thx Diana

### Response

**Eric R | Senior Technical Support Engineer** answered on 01 Mar 2021

Hi Diana, Thank you for the additional information. You are correct. To enable row selection in the Grid, the SelectionMode should be set to either Single or Multiple and the default is None. I see that you found the answer to this in our documentation as well. As for changing the default value, there are many features in the Grid and the pattern we like to follow is to keep features off until it is explicitly turned on. For this, we also put emphasis on the documentation and demos. Please let me know if you need any additional information. Thank you for choosing UI for Blazor. Regards, Eric R | Senior Technical Support Engineer
