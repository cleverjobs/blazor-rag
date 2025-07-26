# TelerikWindow retains state if reopened

## Question

**Ste** asked on 10 Apr 2025

Hi, I'm developing a Blazor web app with: - .NET9, - rendering @rendermode="new InteractiveWebAssemblyRenderMode(prerender: true) I would like to show data starting from the selected record in a grid in a telerik window, where starting from this data I would populate various fields in a chain. This data could be modified inside the telerik window and saved using a button. This use is possible but there is a problem to solve: if I modify the data in the telerik window and then close it, the modified data is maintained if I reopen the telerik window. I'll give an example: This is the code available in the telerik Blazor guides: <TelerikButton OnClick="@OpenWindow">Open Window</TelerikButton>

<TelerikWindow @ref="WindowRef" @bind-Visible="@WindowVisible">
<WindowTitle>
Window Title
</WindowTitle>
<WindowActions>
<WindowAction Name="Close" />
</WindowActions>
<WindowContent>
<p role="status">Current count: @CurrentCount</p>
<TelerikButton OnClick="IncrementCount">Increment Count</TelerikButton>
</WindowContent>
</TelerikWindow>

@code { private TelerikWindow? WindowRef { get; set; } private bool WindowVisible { get; set; } private int CurrentCount { get; set; } private void IncrementCount () {
CurrentCount++;

WindowRef?.Refresh();
} private void OpenWindow () {
WindowVisible=true;
}
} If - I open the telerik window and increase the counter to 5 - I close the window - I click on the button again, the window does not show me the count at 0 but at 5. I would like to know if there is a simple way to recreate from scratch the telerik window every time it is called, without keeping the previous state. P.S. I would not want to worry about manually resetting the fields every time I open the telerik window Thanks

## Answer

**Dimo** answered on 14 Apr 2025

Hello Stefano, You can place everything inside <WindowContent> in a separate Razor component. In this way, this child component will re-initialize from scratch on each Window opening. This approach represents general Blazor programming and is independent from the Telerik components and API. Thus, all Microsoft Blazor documentation applies. Regards, Dimo

### Response

**Stefano** answered on 16 Apr 2025

Hi Dimo, Thanks
