# Is it possible to animate a Blazor AnimationContainer to that is appears to slide in from the right-hand side of the browser window?

## Question

**Adr** asked on 17 Mar 2021

The Blazor AnimationContainer has Top, Left, Width and Height properties to customise where the container will appear. I want to be able to slide in a container using the AnimationType="AnimationType.SlideLeft" so that it appears that the container has slid in from the right hand edge of the browser window. I'm not sure if I can achieve this as I'm guessing I would need to set a Right property (which doesn't exist on the component) to zero? I have attached an example of what I'm trying to achieve.

## Answer

**Nadezhda Tacheva** answered on 19 Mar 2021

Hi Adrian, There are two ways to go about implementing this. Approach One - Write the necessary logic around the AnimationContainer Indeed, the AnimationContainer does not have Right property as its value would be changed depending on the screen size. The horizontal position of the AnimationContainer is managed by the Left parameter. The Left parameter defines the left position of the AnimationContainer and in order to achieve the desired behavior you can set it to match the value of the browser width minus the AnimationContainer width (this way it will slide from the right corner). You can use JS Interop to invoke a Javascript function that returns the browser dimensions. Then you can set the size and position of the AnimationContainer as desired. To better illustrate how to achieve the described scenario, I have created the below sample including the razor file and the JavaScript function. @inject IJSRuntime JsInterop

<TelerikButton OnClick="@ShowContainer">Show Animation Container</TelerikButton>

<TelerikAnimationContainer @ref="myPopup" Top="0px" Width="@(ContainerWidth + " px ")" Height="@(ContainerHeight + " px ")" Left="@(Left + " px ")" AnimationType="@AnimationType.SlideLeft" Class="my-popup">
My content goes here.<br />
<TelerikButton OnClick="@HideContainer">Hide Animation Container</TelerikButton>
</TelerikAnimationContainer>

@code {
TelerikAnimationContainer myPopup; public int Left { get; set; } public int ContainerWidth { get; set; }=200; public int ContainerHeight { get; set; } public int Width { get; set; } public int Height { get; set; } async Task ShowContainer ( ) { await GetDimensions();

Left=Width - ContainerWidth;

ContainerHeight=Height; await myPopup.ShowAsync();
} async Task HideContainer ( ) { await myPopup.HideAsync();
} public async Task GetDimensions ( ) { var dimension=await JsInterop.InvokeAsync<BrowserDimension>( "getDimensions" );
Height=dimension.Height;
Width=dimension.Width;
} public class BrowserDimension { public int Width { get; set; } public int Height { get; set; }
}
}

<style>
.my-popup {
border: 2 px solid red;
background: #ccc; }
</style> You can include the following script in your index.html or _Host.cshtml (depending on the Blazor project type - WASM or Server). You can also place the function in a separate JavaScript file in your project. <script type="text/javascript"> window.getDimensions=function ( ) { return { width: window.innerWidth, height: window.innerHeight
};
};
</script> Approach Two - Use a ready-made component we have with very similar behavior On another hand, you might also consider using the Drawer as it implements similar behavior and you won't need much additional configuration. You can easily change its position to right to have it sliding from right (its default animation is slide). An important point to take into consideration if using the Drawer is that by default it closes when you click in it. That could be changed if you stop the propagation from the inner elements (see this knowledge base article - Prevent Drawer from collapsing on item click ). We also have an opened request for such a feature in our public feedback portal here. I've added a vote on your behalf and you can subscribe to receive email notification on status change (this is the best way to know when a feature is implemented as we announce such information in the portal). I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Regards, Nadezhda Tacheva Progress Telerik
