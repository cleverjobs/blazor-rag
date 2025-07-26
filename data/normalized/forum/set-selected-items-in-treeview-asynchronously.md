# Set selected items in Treeview asynchronously

## Question

**Ray** asked on 22 May 2023

Hi, I'd like to set the selected items of a treeview from an async method. The values to set come from an web api. So it's an async call. I tested the case with the provided Telerik sample. With version 2.25 it works. With the latest version selected items are not set within the treeview. What do I miss? @page "/" <TelerikTreeView Data="@FlatData" CheckBoxMode="@TreeViewCheckBoxMode.Multiple" CheckParents="@true" CheckChildren="@true" CheckOnClick="@false" @bind-CheckedItems="@SelectedItems"> </TelerikTreeView> @code {
List <TreeItem> FlatData { get; set; }
IEnumerable <object> SelectedItems { get; set; }=new List <object> ();
protected override async Task OnInitializedAsync()
{
await GenerateData();
await SelectDefault();
}

async Task SelectDefault()
{
await Task.Delay(100);
SelectedItems=FlatData.Where(data=> data.Id==2);
}

async Task GenerateData()
{
FlatData=new List <TreeItem> ();

FlatData.Add(new TreeItem()
{
Id=1,
Text="Project",
ParentId=null,
HasChildren=true,
Icon="folder",
Expanded=true
});

FlatData.Add(new TreeItem()
{
Id=2,
Text="Design",
ParentId=1,
HasChildren=true,
Icon="brush",
Expanded=true
});
FlatData.Add(new TreeItem()
{
Id=3,
Text="Implementation",
ParentId=1,
HasChildren=true,
Icon="folder",
Expanded=true
});
}

public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentId { get; set; }
public bool HasChildren { get; set; }
public string Icon { get; set; }
public bool Expanded { get; set; }
}
}

## Answer

**Yanislav** answered on 25 May 2023

Hello Rayko, I reviewed your code snippet and it looks OK. I created a REPL example with the latest version in which I've used the same TreeView configuration as the one you shared. On my side, the item is checked correctly. Could you please check if there is anything different in your scenario? Also, could you provide an example or modify the REPL sample so that the problem can be reproduced? Please send it back to me for further review. By reproducing the problem locally, I will be able to investigate it and try to find a possible solution. Thank you for your cooperation in advance! Regards, Yanislav Progress Telerik

### Response

**Rayko** commented on 26 May 2023

Hi Yanislav, where can I find your REPL sample? Best regards, Rayko

### Response

**Yanislav** commented on 26 May 2023

Hello Rayko, Here is a link to the REPL example: [https://blazorrepl.telerik.com/wRYTcUFl41nKC1tu47](https://blazorrepl.telerik.com/wRYTcUFl41nKC1tu47) I apologize for neglecting to include it in my previous response.

### Response

**Rayko** answered on 26 May 2023

Thank you for the sample! Within REPL everything works fine, even it's the same code. That's quite strange. I'll attach my zipped code (which is taken origininally from the Telerik samples). Furthermore I'll attach a video to show the issue on my side. My common problem with missing JS is also included.

### Response

**Yanislav** commented on 31 May 2023

Hello Rayko, Thank you for the provided example! I was able to reproduce the problem. After further investigation, it turned out that the behavior is a problem on our side. Therefore I have logged a bug report on your behalf: [https://feedback.telerik.com/blazor/1610826-when-the-checkeditems-are-updated-within-an-async-method-sometimes-the-treeview-items-are-not-updated](https://feedback.telerik.com/blazor/1610826-when-the-checkeditems-are-updated-within-an-async-method-sometimes-the-treeview-items-are-not-updated) As a creator, you are automatically subscribed to receive email notifications about status changes. In the meantime, as the issue seems to be timing-related what I can recommend is to try to add an additional delay before loading the data. On my side this seems to resolve the issue: async Task GenerateData ( ) { await Task.Delay( 100 ); As a token of gratitude for helping us identify this issue, I have updated your Telerik points. Please accept our apologies for the inconvenience caused by this issue. Thank you for your understanding!

### Response

**Rayko** commented on 05 Jun 2023

Thank you Yanislav! The delay works for now. Regarding the JS error popping up in the video... do you have any suggestion? I've already tried the solutions suggested on [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors,](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors,) but without any success.

### Response

**Yanislav** commented on 08 Jun 2023

Hello Rayko, You're welcome! I'm glad to hear that my suggestion was helpful. About the JS error - In general, " TelerikBlazor was undefined " means that the ` telerik-blazor.js ` file does not load or does not load on time. However, you've said that you've tried everything from the troubleshooting article but may I ask you to confirm if you tried this approach? - [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#blazor-autostart](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#blazor-autostart) When you disable the automatic client-side initialization of Blazor, you can ensure that the scripts are loaded after the Blazor framework has fully loaded its assets. <script src="_framework/blazor.server.js" autostart="false" defer> </script> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"> </script> <script> document.addEventListener( "DOMContentLoaded", function () { Blazor.start(); }); </script> I have actually tried the approach in the project you sent me, and it appears to effectively solve the problem. However, please ensure that you have followed the steps correctly, and kindly inform me if this successfully resolves the issue.
