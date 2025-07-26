# Element reference is null for TelerikComboBox

## Question

**Pal** asked on 16 Jan 2025

I'm trying to reference a TelerikComboBox in a razor component, but it keeps returning null. (I'm using version 6.2.0) Any clues? Html: <TelerikComboBox Class="hide-combobox-buttons" Data="@AllLabels" Value="@Label" @ref="ComboBoxRef" ValueChanged="@((string newValue)=> ValueChanged(newValue))" AllowCustom="true"> </TelerikComboBox> @code{ private TelerikComboBox<string, string>? ComboBoxRef { get; set; } [Parameter] public IReadOnlyList<string>? AllLabels { get; set; } private string Label { get; set; }=string.Empty; protected override async Task OnInitializedAsync() { if (ComboBoxRef !=null) //here it's always null await ComboBoxRef.FocusAsync(); await base.OnInitializedAsync(); } }

## Answer

**Dimo** answered on 16 Jan 2025

Hello, Blazor component references are available in OnAfterRender and OnAfterRenderAsync, not earlier. Regards, Dimo Progress Telerik
