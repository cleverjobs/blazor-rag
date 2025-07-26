# GridCommandButton not showing Tool Tip when its Enabled false

## Question

**Vis** asked on 05 Oct 2021

Hi Team, In GridCommandButton when we Enabled=false, TheTool Tip is not showing. <GridCommandButton Command="Edit" Enabled="false" OnClick="@DeleteSelectedItemClicked" Title="This is Delete.">Delete</GridCommandButton> Thanks, Vishnu Vardhanan

### Response

**Vishnu** commented on 05 Oct 2021

Please help on this ASAP

### Response

**Vishnu** commented on 06 Oct 2021

Please help on this

## Answer

**Dimo** answered on 08 Oct 2021

Hi Vishnu, Disabled HTML elements do not fire mouse events, so the Tooltip can't find out when the user hovers a disabled button. So the observed behavior is expected. Theoretically, you can wrap the disabled button in some other element and use the Tooltip for this other element. However, there must be some space between the wrapper boundaries and the button, otherwise the tooltip will not show again. Regards, Dimo
