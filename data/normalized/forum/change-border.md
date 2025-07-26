# Change border

## Question

**Jon** asked on 29 Mar 2020

Hi How do you change the border ? I've tried.. doesn't seem to work. How can I make outset? and change the border color.. do it 'pops'? thx in advance .k-animation-container { border-radius: 2px 2px 2px 2px; border-color: blue; border-width: 2px; position: absolute; overflow: hidden; z-index: 100 }

## Answer

**Marin Bratanov** answered on 30 Mar 2020

Hello Jonathan, I'd use my own Class and cascade trough it, something like: <style>.my-custom-popup-border {
border: 3 px solid red;
background: yellow;
}
</style>

<TelerikAnimationContainer @ref="myPopupRef" Top="300px" Width="100px" Height="100px" AnimationType="AnimationType.ZoomOut" Class="my-custom-popup-border">
My content goes here. The "k-popup" class adds some background and borders which you can define through your own styles instead.
</TelerikAnimationContainer>

<TelerikButton OnClick="@ToggleContainer">Toggle Animation Container</TelerikButton>

@code {
Telerik.Blazor.Components.TelerikAnimationContainer myPopupRef; public void ToggleContainer ( ) {
myPopupRef.ToggleAsync();
}
} Regards, Marin Bratanov
