# TileLayoutItem - Override background-color using bootstrap css class

## Question

**Mar** asked on 15 Aug 2022

Hi, I'm using Telerik UI for Blazor and I want to use the "alert-danger" bootstrap css class to change the color of a tile item. I put the css class in the TileLayoutItem (@_cssClass) : Html result : But the color is overrided by the k-card class. I know I could create my custom css class and put !important in it, but I would just copy the same code as in alert-danger class. I also tried to set the class in the html element I built, but the background color is not "expanding" to all the tiles : If I put the css class in the div k-tilelayout-item-header and in the div k-tilelayout-item-body, I can have the desired result too, but I didn't find a way to set those in the code. Is there another way I could acheive the result I want without having to create my own css class ? Thank you.

### Response

**Joana** commented on 18 Aug 2022

You might use the built-in styles of the card component for a state. Thus, setting class `k-card-error` is sufficient to put the card into a `danger/error` state. I have created a REPL example to illustrate the usage: [https://blazorrepl.telerik.com/cmOilCky52XI46eu05](https://blazorrepl.telerik.com/cmOilCky52XI46eu05) You might explore the capabilities of the themes we integrate in our Telerik UI for Blazor suite below: [https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/_variables.scss#L208](https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/_variables.scss#L208) [https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/card/_theme.scss#L62](https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/card/_theme.scss#L62)

### Response

**Marie-Pier** commented on 18 Aug 2022

great !.k-card- #{ $name } that exists in the theme is exactly what I need. Thank you !

## Answer

**Marie-Pier** answered on 18 Aug 2022

Thanks to @Joana, using the built in class .k-card-error for coloring the card is the way to go !
