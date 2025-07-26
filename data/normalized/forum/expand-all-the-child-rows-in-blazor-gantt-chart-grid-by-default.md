# Expand all the child rows in Blazor Gantt Chart grid by default

## Question

**Abi** asked on 19 Jan 2024

Hello there, I am trying to load the Gantt Chart - Tree List in expanded state by default. Is there a way to achieve this? Kindly advise. I am using the Telerik Blazor version 5.0.1. TIA

## Answer

**Nadezhda Tacheva** answered on 24 Jan 2024

Hi Abirami, You can programmatically control the expanded state of the items through the Gantt state. If you want to initialize the component with all items expanded, you can handle the OnStateInit event. You may create a state object and add all parent items from your data source to the ExpandedItems field. Then, pass that state to the State field of the OnStateInit event argument. I hope this will help you move forward with the configuration on your end. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik
