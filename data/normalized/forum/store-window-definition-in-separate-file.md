# Store window definition in separate file?

## Question

**EdEd** asked on 20 Jan 2020

Hi, I am using the window as a popup in my grid. Right now the markup is embedded in my grid's razor page. Is there a way to separate this out so that the window markup and/or code is in a separate file? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 20 Jan 2020

Hello Ed, You can put it in a component and expose a method or parameters from it that will do what's needed. You may also find useful these sample projects another customer of ours made: [https://github.com/telerik/blazor-ui/tree/master/common/message-box](https://github.com/telerik/blazor-ui/tree/master/common/message-box) Regards, Marin Bratanov

### Response

**Dean** answered on 28 Nov 2020

Do you have a clear example of this working? I haven't been able to get this to work at all and the examples you linked literally have hundreds of lines of code to do something that *should* be simple. I have a component with window defined as <TelerikWindow @bind-Visible="@bindPatientWindowIsVisible" Centered="true" Modal="true">. It is in it's own component file named ManagePatient. I added public bool bindPatientWindowIsVisible { get; set; } and also tried public void ShowWindow(bool localShowWindowValue) { bindPatientWindowIsVisible=localShowWindowValue; } The parent has the following definition: <ManagePatient @ref="@myManagePatientWindow"></ManagePatient> A button on the parent calls the following. void SelectPatientHandler() { myManagePatientWindow.ShowWindow(true); } This didn't work and also a direct call to the visible property myManagePatientWindow.bindPatientWindowIsVisible=true also failed to display the window. Not sure what else to try. This should have worked I think and it doesn't. I really feel like these window components just need a visible property. I should be able to just do myManagePatientWindow.Visible=true; All this extra code is rather burdensome and seemingly unnecessary. 3rd party controls written by individuals are much more user friendly than your stuff. (Blazored Window library for one). Lastly, you can put in a break point and see that the visible property is true but the window never displays.

### Response

**Dean** answered on 28 Nov 2020

I actually was able to get this to work by added StateHasChanged(); to the public void ShowWindow(bool localShowWindowValue) { bindPatientWindowIsVisible=localShowWindowValue; StateHasChanged(); } So it ended up being pretty easy to do (if you do it right) :-) Sorry for the rant above. It was my mistake.

### Response

**Svetoslav Dimitrov** answered on 02 Dec 2020

Hello Dean, I am glad to read that you managed to make this work with a method. I would like to offer another solution that includes two-way data binding of the Visible parameter so you can take advantage of that. In ManagePatient component <TelerikWindow Width="500px" Height="300px" Centered="true" Visible="@bindPatientWindowIsVisible" VisibleChanged="@VisibleChangedHandler" Modal="true">
<WindowTitle>
Title
</WindowTitle>
<WindowActions>
<WindowAction Name="Close" />
</WindowActions>
<WindowContent>
Content
</WindowContent>
</TelerikWindow>

@code {
[ Parameter ] public bool bindPatientWindowIsVisible { get; set; }

[ Parameter ] public EventCallback<bool> bindPatientWindowIsVisibleChanged { get; set; } protected override void OnParametersSet ( ) { base.OnParametersSet();
} void VisibleChangedHandler ( bool v ) {
bindPatientWindowIsVisible=v; if (bindPatientWindowIsVisibleChanged.HasDelegate)
{
bindPatientWindowIsVisibleChanged.InvokeAsync(bindPatientWindowIsVisible);
}
}
} Usage: <ManagePatient @bind-bindPatientWindowIsVisible="@isVisible"></ManagePatient>

<TelerikButton OnClick="@( _=> isVisible=true)">Show Window</TelerikButton>

@code { public bool isVisible { get; set; }
} Regards, Svetoslav Dimitrov
