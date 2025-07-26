# Add Tab Dynamically After Initialization?

## Question

**Por** asked on 29 Oct 2019

Is there a way to add a tab to the tabstrip dynamically after the initial rendering, without reloading/disrupting the rest of the tabstrip? I can't seem to figure it out. The only thing I can get to work is putting in a placeholder tab, then dropping the content in later, but I would like to be able to control the position, title, etc...==============================<TabStripTab Title="X1"> @DynamicX1 </TabStripTab> ... @code { Telerik.Blazor.Components.TelerikTabStrip personTabStrip; public int ActiveTabIndex { get; set; }=0; private RenderFragment DynamicX1; protected override void OnInitialized() { app.NewTabRequested +=OpenNewTab; } private void OpenNewTab(RenderFragment fragment) { DynamicX1=fragment; ActiveTabIndex=1; StateHasChanged(); } }

## Answer

**Marin Bratanov** answered on 30 Oct 2019

Hello Portia, The last example in this article shows how you can create tabs based on view model data: [https://docs.telerik.com/blazor-ui/components/tabstrip/overview.](https://docs.telerik.com/blazor-ui/components/tabstrip/overview.) The key thing is that the tab definitions need to be in the markup, and that includes the content - this is the Blazor way. That content can come in conditionally or not at all, that's up to the app. It is important to note that a change in the rendered tabs collection requires that the tabstrip component is re-rendered with new data, and this inevitably means that the tabs content will also re-initialize. If this approach does not suit your needs, I can suggest you look into these options: Implement some form of state persistence in the app so that data retrieval, for example, happens only once and not every time the components re-render. Handle the ActiveTabIndexChanged event of the tab strip (see the article above) to know when a tab is activated, so you can render data or entire components in it (e.g., with a conditional if-block in the markup of the respective tab). Regards, Marin Bratanov

### Response

**Portia** answered on 30 Oct 2019

Thank you, I will try to implement some type of workaround to emulate a new tab appearing without disrupting the entire strip. Do you know if there is any trick to hide a tab by targeting with CSS? Once attribute splatting is available I could use that but looking for something in the meantime.

### Response

**Portia** answered on 30 Oct 2019

I don't happen to need the disabled tab state for this tabstrip, so I am going to hijack the "Disabled" property and use it as hidden for my purposes. .k-tabstrip-items .k-state-disabled { display: none; } A "Hidden" property would really be helpful.

### Response

**Marin Bratanov** answered on 31 Oct 2019

Hi Portia, I am not sure if this is relevant for you, but there is a feature request to toggle the tabs visibility through CSS so content inside does not re-initialize (and all of it initializes on first load and you would easily be able to use the index changed event to alter it): [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) Would the Hidden feature do something different than this? Generally, in Blazor, when you don't want something to render you need to change the view model so it does not render, as opposed to hiding with CSS. Regards, Marin Bratanov

### Response

**Michael** answered on 06 Apr 2020

Hey Marin, I'm trying to achieve sort of the same thing here. I'm trying to have a button to add TabStrips after the Render. I'm trying to find how to refresh the component to show that added tab. Right now to show the newly added tab, i need to click on another parent tab and comeback to this very tab to see it.

### Response

**Marin Bratanov** answered on 06 Apr 2020

Hi Michael, The general way to build a tab strip dynamically is to use a loop over a collection of models that describe the tabs, a similar example is available at the end of the docs article: [https://docs.telerik.com/blazor-ui/components/tabstrip/overview.](https://docs.telerik.com/blazor-ui/components/tabstrip/overview.) If you change the collection of models, you need to repaint the components, so usually calling .StateHasChanged() is the way to go. Regards, Marin Bratanov

### Response

**Michael** answered on 06 Apr 2020

I tried this solution beforehand and calling StateHasChanged doesnt ReRender the TabStrip. Should I make a Demo and share it with you via GitHub?

### Response

**Marin Bratanov** answered on 06 Apr 2020

Hello Michael, Can you confirm the following: there are no errors you are using 2.10.0 (the latest version at the time of writing) StateHasChanged() is called on the component that holds the data and the tab strip, not in a child component If yes to all, please open a support ticket and send me a simple runnable reproducible (e.g., modify the docs sample a little). or compare it against this sample I just made for you: @result

<TelerikButton OnClick="@AddTab">Add a new tab</TelerikButton>
<TelerikButton OnClick="@RemoveTab">Remove first tab</TelerikButton>

<TelerikTabStrip ActiveTabIndexChanged="@TabChangedHandler">
@{ foreach (MyTabModel item in tabs)
{
<TabStripTab Title="@item.Title" Disabled="@item.Disabled">
Content for tab @item.Title
</TabStripTab>
}
}
</TelerikTabStrip>

<TelerikButton OnClick="@( ()=> tabs[1].Disabled=!tabs[1].Disabled )">Toggle the Disabled state of the second tab</TelerikButton>

@code { // these methods are handlers for EventCallback type of events, so the framework already calls StateHasChanged async Task AddTab ( ) {
tabs.Add( new MyTabModel { Title=$"Tab {tabs.Count + 1 } " });
} async Task RemoveTab ( ) { if (tabs.Count> 0 )
{
tabs.RemoveAt( 0 );
}
} // sample data MarkupString result { get; set; } void TabChangedHandler ( int newIndex ) { string tempResult=$"current tab {newIndex} selected on {DateTime.Now} ";
MyTabModel currTab=tabs[newIndex];
tempResult +=$"<br />the new tab has a title {currTab.Title} ";
result=new MarkupString(tempResult);
}

List<MyTabModel> tabs=new List<MyTabModel>()
{ new MyTabModel { Title="One" }, new MyTabModel { Title="Two", Disabled=true }, new MyTabModel { Title="Three" }
}; public class MyTabModel { public string Title { get; set; } public bool Disabled { get; set; }
}
} Regards, Marin Bratanov

### Response

**Michael** answered on 06 Apr 2020

I've done a demo myself. [https://github.com/michaelccote/TelerikTabSrtipDemo](https://github.com/michaelccote/TelerikTabSrtipDemo) It seems to be working. I'm going to work on finding why my case doesnt work. My initial guess would be because i have many nested components. I'll keep you posted

### Response

**Marin Bratanov** answered on 06 Apr 2020

Hi Michael, With nested components, the common pattern is to expose an event and consume it up to where the data needs to change in order to call .StateHasChanged() on the correct component. Regards, Marin Bratanov

### Response

**Michael** answered on 06 Apr 2020

Yes i didnt something similar with an EventCallback. This part is working fine now ! Thanks! I'm now working on deleting a tabstrip on the push of a button.
