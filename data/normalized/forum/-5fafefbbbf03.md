# Change AnimationType Depending on Action (Open versus Close)

## Question

**RobRob** asked on 10 Mar 2021

I am simply trying to toggle an Animation Container and have it ZoomOut when it opens, but ZoomIn when it closes. Thought I could update the AnimationType using the reference, but does not work. Please see attached.

## Answer

**Marin Bratanov** answered on 11 Mar 2021

Hello Rob, You should set the parameters, not the instance properties - setting parameters lets the component react and re-render. The key thing is that you need to give the framework a bit of time to re-render with the new settings so that they can take affect, and a small Task.Delay() is the usual way to do that: <div style="position:relative; border: 1px solid red; height: 300px;">
<TelerikButton OnClick="@ToggleContainer">Toggle Animation Container</TelerikButton>

<TelerikAnimationContainer @ref="myPopupRef" Top="50px" Left="50px" Width="250px" Height="150px" AnimationType="@DesiredAnmation" Class="k-popup">
<p>
The "k-popup" class adds some background and borders which you can define through your own styles instead.
</p>
<p> My parent element has <code> position: relative </code> to control my <code> Top </code> and <code> Left </code> offset.
</p>
</TelerikAnimationContainer>
</div>

@code {
Telerik.Blazor.Components.TelerikAnimationContainer myPopupRef; bool toggledOpen=false; AnimationType DesiredAnmation=> toggledOpen ? AnimationType.ZoomIn : AnimationType.ZoomOut; async Task ToggleContainer ( ) {
toggledOpen=!toggledOpen; await Task.Delay( 30 ); // give the framework time to re-render with the new settings await myPopupRef.ToggleAsync();
}
} On another note, would you mind if I moved this thread to the public forums so other people can see this scenario and benefit from it? Regards, Marin Bratanov Progress Telerik

### Response

**Rob** answered on 12 Mar 2021

Great answer and of course share this question/answer publicly. ;)

### Response

**Marin Bratanov** answered on 12 Mar 2021

Hello Rob, Thank you for this, the thread is now public at [https://www.telerik.com/forums/change-animationtype-depending-on-action-open-versus-close](https://www.telerik.com/forums/change-animationtype-depending-on-action-open-versus-close) Regards, Marin Bratanov
