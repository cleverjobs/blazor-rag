# TelerikAutoComplete Loader

## Question

**Jer** asked on 21 Aug 2023

Hi, I am trying to implement a loading spinner with the <TelerikAutoComplete> control. I have overriden the <NoDataTemplate> <p>@IsLoading</p>
<TelerikAutoComplete
@ref="@AutoCompleteControl" Data="ActiveDataSet" @bind-Value="SearchTerm" DebounceDelay="500" Placeholder="Search here..." FilterOperator="StringFilterOperator.Contains" ClearButton="true">
<NoDataTemplate>
@if (IsLoading)
{
<TelerikLoader Visible="true" Size="@ThemeConstants.Loader.Size.Large" ThemeColor="@ThemeConstants.Loader.ThemeColor.Tertiary" Type="@LoaderType.ConvergingSpinner" />
} else {
<p>No Data</p>
}
</NoDataTemplate>
</TelerikAutoComplete> From the setter of SearchTerm I call 'Search' where I'm getting the data and updating my 'IsLoading' private async Task Search ( string searchTerm ) { try { // Long running search that updates the data } finally {
IsLoading=false;
StateHasChanged(); // AutoCompleteControl.Rebind(); // Without this the loading spinner never goes away }

} If I don't include the AutoCompleteControl.Rebind(); the loading indicator never goes away, despite the Data being updated and IsLoading being set to false. Is there something I'm missing about how to update the binding inside the <NoDataTemplate>? Thanks!

## Answer

**Georgi** answered on 24 Aug 2023

Hi Jeremy, Thank you for the provided code snippet. The issue appears to be that even though StateHasChanged is used, AutoComplete does not re-render itself after IsLoading is set to false. This leads to the Loading indicator staying on the screen indefinitely. In this scenario, the Rebind method serves the purpose of refreshing the data and the component. If you refresh only the component and hide the Loader, the change in the data won't be displayed. You can verify this by using AutoCompleteControl.Refresh(), which only refreshes the component. Alternatively, if you would like to avoid using Rebind. You can refresh the data by creating a new reference and then Refresh the AutoComplete this way: private async Task Search ( string searchTerm ) { try { // Simulate a delay due to a long running search that updates the data await Task.Delay( 2000 );
ActiveDataSet.Add( "new entry" );
ActiveDataSet=new List<string>(ActiveDataSet);
} finally {
IsLoading=false;
StateHasChanged();
AutoCompleteControl.Refresh();
}
} Let me know if further questions arise. Kind Regards, Georgi Progress Telerik
