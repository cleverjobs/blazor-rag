# Using GUID as a key

## Question

**Nic** asked on 31 May 2019

Hi, I'm trying to use the latest version (V1.1.0) of DropDownList with a GUID key, the original conversation is in this thread: [https://www.telerik.com/forums/dropdownlist---run-code-when-select-item-changes.](https://www.telerik.com/forums/dropdownlist---run-code-when-select-item-changes.) My understanding is this should now work, but I'm having problems binding the current value. My code looks like this: <TelerikDropDownList Data="@_viewItems" TValue="Guid" TextField="Name" ValueField="Id" bind-Value="@CurrentViewId" PopupHeight="120" /> private List<NameAndId> _viewItems; public class NameAndId { public string Name { get; } public Guid Id { get; } public NameAndId(string name, Guid id) { Name=name; Id=id; } public override string ToString() { return Name; } } private Guid CurrentViewId { get=> _currentViewId; set=> _currentViewId=value; } This gives me the following compiler error: Severity Code Description Project File Line Suppression State Error The attribute names could not be inferred from bind attribute 'bind-Value'. Bind attributes should be of the form'bind', 'bind-value' or 'bind-value-change' TestApp C:\Source\TestApp.Blazor\TestApp.Blazor\Pages\View.razor 17 Error RZ9991 The attribute names could not be inferred from bind attribute 'bind-Value'. Bind attributes should be of the form'bind', 'bind-value' or 'bind-value-change' TestApp C:\Source\TestApp.Blazor\TestApp.Blazor\Pages\View.razor 17 Thanks, Nick.

## Answer

**Nick** answered on 31 May 2019

Ignore that - I figured it out. It was missing the using statement: @using Telerik.Blazor.Components.DropDownList Unfortunately resharper shows it as redundant so I must have deleted it accidentally.
