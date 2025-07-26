# Component inside tab with @ref results in null

## Question

**kk** asked on 24 Apr 2020

I have a child component that I would like to access from parent so i put @ref="myChild", when this control is inside a tab strip, the reference to myChild is always null, however if i move the component outside of tabstrip then everthing works as expected. I am using 2.10 trial

## Answer

**Svetoslav Dimitrov** answered on 24 Apr 2020

Hello, The variable you are storing the reference to your myChild will be only populated after the component is rendered and its output includes the myChild element. Until that point, there's nothing to reference. To manipulate components references after the component has finished rendering, use the OnAfterRenderAsync or OnAfterRender methods. More information on the lifecycle methods can be found in the Microsoft documentation here: [https://docs.microsoft.com/en-us/aspnet/core/blazor/lifecycle?view=aspnetcore-3.1#after-component-render.](https://docs.microsoft.com/en-us/aspnet/core/blazor/lifecycle?view=aspnetcore-3.1#after-component-render.) Below you can see a simple code snippet to illustrate how to get the reference of a TextBox nested in TabStrip. What I did is to use the ActiveTabChanged event (more information you can find here: [https://docs.telerik.com/blazor-ui/components/tabstrip/events#activetabindexchanged](https://docs.telerik.com/blazor-ui/components/tabstrip/events#activetabindexchanged) ) to be notified when the user wants to see the nested component (in this case TextBox) and added Task.Delay(20) so the TextBox has time to render and populate the reference. <TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Left" ActiveTabIndexChanged="@ActiveTabChangedHandler"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second" Disabled="true"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> <TelerikTextBox @bind-Value="@UserInput" @ref="TextBoxRef" /> </TabStripTab> </TelerikTabStrip> @(TextBoxRef==null ? "null" : "populated")

@code {
async Task ActiveTabChangedHandler()
{
await Task.Delay(20);
}

TelerikTextBox TextBoxRef { get; set; }

public string UserInput { get; set; }
} Regards, Svetoslav Dimitrov
