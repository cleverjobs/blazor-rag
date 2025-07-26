# Component in GridColumn Template

## Question

**Ati** asked on 24 Feb 2020

I have added Component in <TelerikGrid>/<GridColumn>/<Template>. Grid is loading based on data in a text field. All columns are getting update except column having component. <GridColumns> <GridColumn Field="@(nameof(Fee.FEE_ID))" Title="STD"> <Template> @{ Fee Fee=context as Fee; <RTP_SMS.Pages.Components.CompStdNN id="@Fee.FEE_ID"></RTP_SMS.Pages.Components.CompStdNN> } </Template> </GridColumn> </GridColumns>

## Answer

**Marin Bratanov** answered on 24 Feb 2020

Hello Atif, Can you confirm that the CompStdNN uses the OnParametersSet/OnParametersSetAsync event to update? Once instantiated the first time in the grid, if the grid data changes, the child component will only receive new parameters, it will not initialize from scratch, so logic running in the OnInitialized event will not fire. Regards, Marin Bratanov

### Response

**Atif** answered on 24 Feb 2020

I did not added OnParametersSet or OnParametersSetAsync, but after adding it resolved issue. Thanks for quick response.
