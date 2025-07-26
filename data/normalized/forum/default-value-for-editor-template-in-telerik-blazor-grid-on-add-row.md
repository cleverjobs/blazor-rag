# Default value for Editor Template in Telerik Blazor Grid on Add Row

## Question

**Sar** asked on 20 May 2024

I have a Blazor grid for which I populate an option dropdown. I use the OnAdd="@AddHandler" to add a new row. There are two other columns in the grid that have calculated values based on Name grid and 2 others, but once the option is populated, the only way for the calculations to work is to select another name, then come back to the first value. Is there a way to default the value to text that says "Select name" and make the user choose something? <EditorTemplate> @{
CurrentlyEditedRecord=context as Record; <select @bind="@CurrentlyEditedRecord.Name"> @foreach (var item in Products)
{ <option value="@item"> @item </option> } </select> } </EditorTemplate>

## Answer

**Sara** answered on 20 May 2024

I figured it out, it was in the example, I set it manually in the AddHandler: async Task AddHandler(GridCommandEventArgs args)
{
//Set default values for new items
((Record)args.Item).Name="Select product";

//Cancel if needed
//args.IsCancelled=true;
}

### Response

**Hristian Stefanov** commented on 22 May 2024

Hi Sara, I'm glad to see that you have quickly resolved the matter on your own. Thank you for sharing it here, publicly, so other developers with the same scenario can benefit from it. Kind Regards, Hristian
