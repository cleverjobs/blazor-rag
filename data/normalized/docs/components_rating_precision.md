
# Precision

The Rating allows you to control the precision of the item selection.

To configure the precision of the selection, use either of the following settings:

* [`Full`](#full)
* [`Half`](#half)

## Full

The full precision mode is the default mode of the Rating. If not configured, the component will automatically set the `PrecisionMode` option to `Full` which enables only whole stars to be selected by click or keyboard interaction.

````RAZOR
<TelerikRating @bind-Value="@Value"
               PrecisionMode="RatingPrecisionMode.Full">
</TelerikRating>

@code {
    private double Value { get; set; } = 1;
}
````

## Half

To configure the half precision mode of the Rating, set the `PrecisionMode` option to `Half` which allows you to set decimal values. The passed value is rounded during the rendering phase to display a full or half item based on the following value specifics:

* A value which is less than or equal to `.5` displays half an item.
* A value which is greater than `.5` displays a full item.

````RAZOR
<TelerikRating @bind-Value="@Value"
               PrecisionMode="RatingPrecisionMode.Half">
</TelerikRating>

@code {
    private double Value { get; set; } = 1.5;
}
````

## See Also

* [Live Demo: Rating Precision](https://demos.telerik.com/blazor-ui/rating/precision)
* [Live Demo: Rating Keyboard Navigation](https://demos.telerik.com/blazor-ui/rating/keyboard-navigation)