# blazor telerik grid indicate sortable column

## Question

**bim** asked on 19 Feb 2025

Hi folks, I would like to show some icon next to a column that indicates that the column can be sorted or not. I have set the Sortable="true" at the grid level and for one of the grid column the sortable is set as false. Any suggestions on how to implement this feature? Thanks, Bimal

## Answer

**Anislav** answered on 19 Feb 2025

Hi Bimal, By default, the Grid does not automatically sort the provided data, which is why no sorting indication is shown. To address this, I typically handle the OnStateInit event, which allows setting an initial state for the Grid. In this event handler, I add a Sort Descriptor to sort the first column upon initialization. For more details, you can refer to the official documentation: [https://www.telerik.com/blazor-ui/documentation/components/grid/state#onstateinit](https://www.telerik.com/blazor-ui/documentation/components/grid/state#onstateinit) Regards, Anislav Atanasov
