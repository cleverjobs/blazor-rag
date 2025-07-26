# Prevent sorting action on custom column's header's item

## Question

**Iva** asked on 11 Dec 2020

Hello! Please help: i have custom column's grid header that contains CheckBox and column's title The column is sortable. A checkbox calls a specific method, but clicking on it also triggers a sort. How to prevent sorting when clicking a specific component in a column header? <GridColumn Filed="nameof(CrmViewElements)"> <HeaderTemplate> <div class="row"> <div class="col d-flex align-items-center"> <div style="padding-right: 1rem; cursor: pointer" data-toggle="tooltip" data-placement="bottom" title="Show all elements"> <TelerikCheckBox @bind-Value="@showAllComponents" /> </div> <span>Elements</span> </div> </div> </HeaderTemplate> </GridColumn>

## Answer

**Nadezhda Tacheva** answered on 16 Dec 2020

Hi Ivan, The reason behind this behavior is called Event Bubbling, also known as one of the event Propagation phases. Clicking the checkbox event fires up to its parent element (in this case the column header) and also triggers the event called in the parent (the sorting). A common approach to reduce that bubbling is to use the stopPropagation feature in the child element. That will result in triggering only the desired event from child. To better illustrate this solution I have created this knowledge base article that also has a simple example with a checkbox in the header template. I hope you will find the above information useful. Regards, Nadezhda

### Response

**Ivan** answered on 19 Dec 2020

Thank you for reply!!
