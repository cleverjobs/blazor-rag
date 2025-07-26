# DialogFactory Cascading Parameter is NULL

## Question

**Edw** asked on 18 Jun 2021

Hello, I am using Telerik Blazor components in an ASP.net Core MVC app as we are slowly migrating the application to Blazor. My component is inserted into a Razor view using the <component> tag helper. Inside the component I have the <TelerikRootComponent> surrounding the contents, etc. The component works without any issues. I needed to add a confirmation dialog to use with grid's delete command. Unfortunately, the DialogFactory cascading parameter is always null and thus confirmation dialog cannot be shown. Please advise.

## Answer

**Dimo** answered on 23 Jun 2021

Hello Edward, The DialogFactory can be used inside a component, which is nested in the TelerikRootComponent. I assume that you are trying to use it in the component, which contains the TelerikRootComponent, right? For example, the dialog alert in this scenario will NOT work: Razor component: <TelerikRootComponent> <TelerikButton OnClick="@ShowAlert"> Show Alert </TelerikButton> </TelerikRootComponent> @code {
[CascadingParameter]
public DialogFactory Dialogs { get; set; }

public string ButtonClicked="not yet";

public async Task ShowAlert(MouseEventArgs e)
{
ButtonClicked="yes";
await Dialogs.AlertAsync("my alert");
}
} On the other hand, this scenario WILL work: Parent component (razor) <TelerikRootComponent> <MyTestComponent /> </TelerikRootComponent> MyTestComponent.razor <h3> MyTestComponent </h3> <TelerikButton OnClick="@ShowAlert"> Show Alert </TelerikButton> @code {

[CascadingParameter]
public DialogFactory Dialogs { get; set; }

public async Task ShowAlert(MouseEventArgs e)
{
await Dialogs.AlertAsync("my alert");
}
} Regards, Dimo Progress Telerik
