# FilterCellTemplate with operator

## Question

**Cla** asked on 19 Jul 2022

I made a custom filter using FilterCellTemplate, now i would like to add filter operator and filter clear button. For filter clear button it's simple just adding <TelerikButton OnClick="ClearLogic"><span class="k-icon k-i-filter-clear k-button-icon"></TelerikButton> but how to add filter operator selection? default filter operator selection is a TelerikDropdownList without span.k-input-inner element, and with k-filter-icon in the button, how can i reply this component? there is one out of the box? Thanks

## Answer

**Claudio** answered on 19 Jul 2022

I solved with this code: <FilterCellTemplate> <!-- Filter combo --> <TelerikDropDownList Data="InvoiceTypes" Filterable="true" @bind-Value="InvoiceType" OnChange="Grid.Rebind" /> <!-- Filter operator | reset button --> <div class="k-filtercell-operator"> <!-- Filter operator --> <TelerikDropDownList Data="CustomFilterOperators" TItem="Utils.ComboBoxItem<Utils.Entity.NumberOperator>" TValue="Utils.Entity.NumberOperator" Class="k-dropdown-operator" @bind-Value="InvoiceTypeOperator" OnChange="Grid.Rebind"> <DropDownListSettings> <DropDownListPopupSettings Width="Auto" /> </DropDownListSettings> </TelerikDropDownList> <!-- Reset button --> <TelerikButton Class="k-icon-button" Enabled="InvoiceType !=null" OnClick="()=> { InvoiceType=null; Grid.Rebind(); }"> <span class="k-icon k-i-filter-clear k-button-icon"> </span> </TelerikButton> </div> </FilterCellTemplate> and replacing the default dropdownlist icon with the filter icon in css: .k-dropdownlist.k-dropdown-operator> button> span.k-icon.k-i-arrow-60-down:before {
content: "\e129"
} but, there is a better way?

### Response

**Svetoslav Dimitrov** answered on 22 Jul 2022

Hello Claudio, I am happy to see that you have taken the correct approach to add filter operation to the filter row. Regards, Svetoslav Dimitrov
