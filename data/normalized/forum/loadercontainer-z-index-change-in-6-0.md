# LoaderContainer z-index change in 6.0

## Question

**RobRob** asked on 29 Aug 2024

Hi, I was wondering the reason for this change? I can have many LoaderContainers on my screen, and now if a dialog appears, depending on positioning it may or may not be hidden -- and sometimes even just partially hidden! Example: [https://blazorrepl.telerik.com/mSEsmjbL50qFUO1p20](https://blazorrepl.telerik.com/mSEsmjbL50qFUO1p20) Depending on your window size you may or may not be able to click OK!

## Answer

**Dimo** answered on 02 Sep 2024

Hello Rob, Please check the following page for more information about the change: LoaderContainer and Dialog z-index The Dialog has its own overlay, so it shouldn't be necessary to use a LoaderContainer and dialogs at the same time to block the UI. The app can hide the LoaderContainer before showing the Dialog and vice versa. If this is not feasible, the linked page provides possible workarounds. If your actual app scenario is similar to the REPL, you can also create a lower stacking context for the LoaderContainer: <div style="position: relative; z-index: 9999; height: 400px"> <TelerikLoaderContainer Visible="@true" ThemeColor="@ThemeConstants.Loader.ThemeColor.Success" OverlayThemeColor="light" LoaderType="@LoaderType.InfiniteSpinner"> </TelerikLoaderContainer> </div> @code {
[CascadingParameter] public DialogFactory Dialogs { get; set; }

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
await Dialogs.AlertAsync("Above or below?");
}
} In general, when two elements have a z-index style and cover the same parts of the page, different scenarios may require different overlapping. The change was effectively a bug fix to handle some common integration scenarios, for example, triggering an async operation from a popup. Regards, Dimo Progress Telerik
