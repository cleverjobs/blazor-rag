# TelerikDropDownList - Set number of rows to show

## Question

**Cra** asked on 15 Nov 2023

Hi Currently the TelerikDropDownList I have only shows 3 rows of returned data before a scroller appears. See attached image. Is there a way of setting the minimum number of rows to be seen before the scroller appears? I've tried all the usual stuff around MinHeight etc but none of that works <TelerikDropDownList Data="@Companies" @bind-Value="@SelectedCompanyId" TextField="@nameof(CompanyDetail.CompanyName)" ValueField="@nameof(CompanyDetail.CompanyId)" Filterable="true" FilterOperator="@FilterOperator" FilterDebounceDelay="@DebounceDelay" DefaultText="Search Client" Width="400px">
</TelerikDropDownList>

## Answer

**Georgi** answered on 20 Nov 2023

Hi, Craig, Yes, It is possible to set the minimum number of rows by controlling the height of the DropDownList's popup. By design, the component allows you to modify its popup through the <DropDownListPopupSettings> tag. You can control the number of rows to show through the Heigh property like this: <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue"> <DropDownListSettings> <DropDownListPopupSettings Height="160px" /> </DropDownListSettings> </TelerikDropDownList> Let me know if additional help is needed. Best Regards, Georgi Progress Telerik
