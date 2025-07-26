# Override "no records available" message while loading page

## Question

**Hae** asked on 12 Aug 2024

Hello. Is there a way to override "No Records Available" message while the page is loading, for TalerikLoaderContainer for Blazor? F ound this [https://docs.telerik.com/blazor-ui/components/grid/templates/no-data-template,](https://docs.telerik.com/blazor-ui/components/grid/templates/no-data-template,) but I was hoping to find something that's specific for loading.

### Response

**Hristian Stefanov** commented on 13 Aug 2024

Hi Haewon, If you want to change the default text of the TelerikLoaderContainer component itself, you can set its Text parameter: <p> Data Count: @Data?.Count </p> <TelerikLoaderContainer Visible="@( Data==null )" Text="Please wait...CUSTOM TEXT HERE" /> @code {
private List <string> Data { get; set; }

protected override async Task OnInitializedAsync()
{
await Task.Delay(3000); // simulate slow loading of data

Data=Enumerable.Range(1, 10).Select(x=> $"data item {x}").ToList();
}
} Let me know if this is what you are looking for. Kind Regards, Hristian
