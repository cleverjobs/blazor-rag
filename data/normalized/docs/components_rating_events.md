
# Events

This article explains the events available in the Telerik Rating for Blazor:

* [ValueChanged](#valuechanged) - fires when the user selects an item (icon).

## ValueChanged

The `ValueChanged` event fires when the user clicks an item or uses the keyboard to select it.

Make sure to update the currently selected item when using the event.

>caption Handle ValueChanged

````RAZOR
<TelerikRating Value="@Value"
               ValueChanged="@((double newRating) => ValueChangedHandler(newRating))">
</TelerikRating>

@code {
    private double Value { get; set; } = 1;

    private void ValueChangedHandler(double newRating)
    {
        Value = newRating;
    }
}
````

@[template](/_contentTemplates/common/general-info.md#event-callback-can-be-async)

## See Also

* [Live Demo: Rating Events](https://demos.telerik.com/blazor-ui/rating/events)