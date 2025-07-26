# How to show a pre-selected item in FileManager Blazor when the page loads

## Question

**Tas** asked on 08 Apr 2025

Hi Team, How to show a pre-selected item in FileManager Blazor when the page loads I have tried using two-way selection but it does not work.

## Answer

**Anislav** answered on 09 Apr 2025

I got the selection example in the Telerik documentation and modified it slightly to preselect the first item: protected override async Task OnInitializedAsync () {
FileManagerData=await GetFlatFileEntries();

SelectedItems=new List<FlatFileEntry> { FileManagerData.First() };
} This works as expected. You can see the working example here: [https://blazorrepl.telerik.com/wJuyOXYs16IkHPua03](https://blazorrepl.telerik.com/wJuyOXYs16IkHPua03) Regards, Anislav Atanasov
