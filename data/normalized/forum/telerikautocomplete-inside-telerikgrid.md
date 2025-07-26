# TelerikAutoComplete inside TelerikGrid

## Question

**Lou** asked on 19 Feb 2023

Hello, Blazor WebApp here. I try TelerikAutoComplete inside a TelerikGird without success. Do you provide a complete example so I can use it? How I can get the current field value as searchTerm to send it to the API? <GridColumn OnCellRender="@((GridCellRenderEventArgs args)=> OnCellInfosEmplacementDestinationRenderHandler(args, " emplacementDescriptionCompleteFr "))" Field=@nameof(treltlkpEmplacementViewModel.emplacementDescriptionCompleteFr) Title="Description FRANÇAISE" TextAlign="@ColumnTextAlign.Left"> <Template> <TelerikAutoComplete TItem="@String" Id="TitreFr" ScrollMode="@DropDownScrollMode.Scrollable" ItemHeight="30" PageSize="10" OnRead="@OnReadAutoCompleteEmplacementDescriptionCompleteFr" @bind-Value="@((context as treltlkpEmplacementViewModel).emplacementDescriptionCompleteFr)" FillMode="@Telerik.Blazor.ThemeConstants.AutoComplete.FillMode.Solid"> <AutoCompleteSettings> <AutoCompletePopupSettings Height="100px" /> </AutoCompleteSettings> </TelerikAutoComplete> </Template> </GridColumn> async Task OnReadAutoCompleteEmplacementDescriptionCompleteFr(AutoCompleteReadEventArgs args)
{
treltlkpEmplacementViewModel item=(treltlkpEmplacementViewModel)args.Data;

if (!string.IsNullOrWhiteSpace(?????????))
{
await ObtenirEmplacementDescriptionCompleteAutoCompleteAsync(args, SafetyStudioSolution.Shared.Constants.cultureNameFr, ?????????);
}
} Thank you for your fast answer.

## Answer

**Svetoslav Dimitrov** answered on 22 Feb 2023

Hello Louis, The Template controls the content of a Grid cell when the component is in view/read mode. Based on your description I am suggesting that you would like to type something in the Grid and get the user input in the code so that you can send it to the back end. I would like to suggest some documentation resources that might be useful: Knowledge-based article - Edit Grid CheckBoxes with Single Click - this KB article showcases how to get editing of the Grid in Read mode. It showcases a checkbox editing, however the same approach is applicable to all other inputs (incl. AutoComplete). Editor Template - in general, the Grid is supposed to render editors when the user wants to edit some data. You can use that template to control what editor is rendered in edit mode. Use a AutoComplete to Filter the Grid - you can add the AutoComplete component in the GridToolBarTemplate and use the State to programmatically filter the component. Regards, Svetoslav Dimitrov

### Response

**Louis** answered on 25 Feb 2023

Hello Svetoslav, Thank you for all your information. But I try another way. I get all the data from my API and use the filter option. <GridColumn OnCellRender="@((GridCellRenderEventArgs args)=> OnCellInfosEmplacementDestinationRenderHandler(args, " emplacementDescriptionCompleteFr "))" Field=@nameof(treltlkpEmplacementViewModel.emplacementDescriptionCompleteFr) Title="Description FRANÇAISE" TextAlign="@ColumnTextAlign.Left"> <EditorTemplate> <TelerikAutoComplete TItem="@String" Id="TitreFr" ScrollMode="@DropDownScrollMode.Scrollable" ItemHeight="30" PageSize="10" OnRead="@OnReadAutoCompleteEmplacementDescriptionCompleteFr" @bind-Value="@((context as treltlkpEmplacementViewModel).emplacementDescriptionCompleteFr)" FillMode="@Telerik.Blazor.ThemeConstants.AutoComplete.FillMode.Solid" Filterable="true" FilterOperator="@StringFilterOperator.Contains"> <AutoCompleteSettings> <AutoCompletePopupSettings Height="100px" /> </AutoCompleteSettings> </TelerikAutoComplete> </EditorTemplate> </GridColumn> And razor.cs file : async Task OnReadAutoCompleteEmplacementDescriptionCompleteFr(AutoCompleteReadEventArgs args)
{
List <string> result=await AdditionalInformationDataService.ObtenirEmplacementDescriptionCompleteAutoCompleteAsync(SafetyStudioSolution.Shared.Constants.cultureNameFr);
var filtered=await result.ToDataSourceResultAsync(args.Request);
args.Data=filtered.Data;
args.Total=filtered.Total;
} The only downside I see is that all data is loaded to then apply the filter

### Response

**Svetoslav Dimitrov** answered on 01 Mar 2023

Hello Louis, You can implement filtering like in the OnRead documentation sample. That way, you can get only the records that will be shown after the filtering. Regards, Svetoslav Dimitrov
