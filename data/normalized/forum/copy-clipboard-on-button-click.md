# Copy Clipboard on Button click

## Question

**Vis** asked on 29 Jul 2021

Hi Team, Could you please suggest to do Copy Clipboard on Button click in blazor? Thanks, Vishnu

### Response

**Peter** commented on 28 Nov 2022

Added a new answer.

## Answer

**Matthias** answered on 01 Aug 2021

Here is a step-by-step guide to this very question. Build a Blazor 'Copy to Clipboard' component ...

### Response

**Marin Bratanov** answered on 29 Jul 2021

Hi Vishnu, To do that, you need JavaScript (you can call that through the JSInterop the framework provides), here is an article I found online that can be a good starting point: [https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f](https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f) Regards, Marin Bratanov Progress Telerik

### Response

**Peter** answered on 28 Nov 2022

I found this, it is simpler and works great. [https://github.com/CopyText/TextCopy](https://github.com/CopyText/TextCopy) 1. First, package manager console: NuGet\Install-Package TextCopy -Version 6.2.0 2. Then add @using TextCopy to the _Imports.razor 3. In program.cs after var builder=WebApplication.CreateBuilder(args); var serviceCollection=builder.Services; # region InjectClipboard serviceCollection.InjectClipboard(); # endregion 4. Then my razor form to test: @page "/Clipboard" <div class="card">
<div class="card-body border-dark">
<input @bind="Content" />
<button type="button" class="btn btn-primary" @onclick="CopyTextToClipboard">Copy</button>
<button type="button" class="btn btn-primary" @onclick="ReadTextFromClipboard">Read</button>
</div>
</div>

@code {

[ Inject ] public IClipboard Clipboard { get; set; } public string Body { get; set; }=string.Empty; public string Content { get; set; }=string.Empty; public Task CopyTextToClipboard () { return Clipboard.SetTextAsync(Content);
} public async Task ReadTextFromClipboard () {
Content=await Clipboard.GetTextAsync( ) ;
}
} That's it. Figured I would share because I tried the other links on here and wasn't very simple like this solution. Peter
